import csv
import os


def products_dict(some_file):
    products = {}
    with open(some_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            value = {}
            value['name'] = str(row[1])
            value['price'] = int(row[2])
            value['stock'] = int(row[3])
            products[int(row[0])] = value
    return products


products = products_dict('products.csv')


def cashbox_dict(some_file):
    cashbox = {}
    with open(some_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            cashbox[int(row[0])] = int(row[1])
    return cashbox


cashbox = cashbox_dict('cashbox.csv')


def change(product_chosen, input_amount, cashbox, products):
    if not all(item in cashbox.keys() for item in input_amount):
        msg = 'Nice try =) please use other currency'
        pass
    else:
        price = products[product_chosen]['price']
        if sum(input_amount) < price:
            msg = 'Not enough coins given, {} more needed, please take back your amount {}'.format(
                price - sum(input_amount), input_amount)
            pass
        elif sum(input_amount) == price:
            products[product_chosen]['stock'] -= 1
            for i in input_amount:
                cashbox[i] += 1
            msg = 'Enjoy!'
        else:
            ch = sum(input_amount) - price
            given_change = []
            products[product_chosen]['stock'] -= 1
            for i in input_amount:
                cashbox[i] += 1
            while ch > 0:
                max_change_given = max(cashbox.keys(), key=lambda x: x <= ch and cashbox[x] > 0)
                if cashbox[max_change_given] > 0 and max_change_given != max(cashbox.keys()):
                    cashbox[max_change_given] -= 1
                    ch -= max_change_given
                    given_change.append(max_change_given)
                else:
                    msg = 'Sorry hun, we have no change for you, please take back your money {}'.format(input_amount)
                    for i in input_amount:
                        cashbox[i] -= 1
                    products[product_chosen]['stock'] += 1
                    break
                msg = 'Enjoy and do not forget your change {}'.format(given_change)
    return msg


def choose_product(product_chosen):
    if product_chosen not in products.keys():
        ans = 'Please choose some of existing products'
    elif products[product_chosen]['stock'] == 0:
        ans = 'Sorry dear we are empty here, please choose another product'
    else:
        c = str(input('{} is a perfect choice! The price is ${}. Please enter banknotes (numbers separated by space)\n'.format(
            products[product_chosen]['name'], products[product_chosen]['price'])))
        lst = c.split()
        input_amount = []
        for num in lst:
            input_amount.append(int(num))
        ans = change(product_chosen, input_amount, cashbox, products)
    return ans


for key in products.keys():
    print('{} - {} - ${}'.format(key, products[key]['name'], products[key]['price']))
n = int(input('\nNow tell me what is it that you truly desire? \n(Please choose the product)\n'))
print(choose_product(n))


with open('products_temp.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'price', 'stock']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for key in products.keys():
        writer.writerow({'id': key,
                         'name': products[key]['name'],
                         'price': products[key]['price'],
                         'stock': products[key]['stock']})
    csvfile.close()


if products_dict('products.csv') == products_dict('products_temp.csv'):
    pass
else:
    with open('cashbox_temp.csv', 'w') as csvfile:
        fieldnames = ['denom', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for key in cashbox.keys():
            writer.writerow({'denom': key,
                             'count': cashbox[key]})
        csvfile.close()
    os.rename(r'cashbox_temp.csv', r'cashbox.csv')

os.rename(r'products_temp.csv', r'products.csv')
