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


def cashbox_dict(some_file):
    cashbox = {}
    with open(some_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            cashbox[int(row[0])] = int(row[1])
    return cashbox


products = products_dict('products.csv')
cashbox = cashbox_dict('cashbox.csv')


def rewrite_products():
    with open('products_temp.csv', 'w') as csvfile:
        fieldnames = ['id', 'name', 'price', 'stock']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for key in products.keys():
            writer.writerow({'id': key,
                             'name': products[key]['name'],
                             'price': products[key]['price'],
                             'stock': products[key]['stock']})
        csvfile.close()


def rewrite_rename_cashbox():
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


def rename_products():
    os.rename(r'products_temp.csv', r'products.csv')
