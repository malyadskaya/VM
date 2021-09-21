# Basic vending machine in Python

In the repository you will find 2 csv and py files used to run the program (given in Python 3.8).

- [Specification](#specification)
- [Usage](#usage)
- [Example](#example)

--------------------------------------------------------------------------------

## Specification

We have 2 csv files,

The first represents cashbox inside the vending mashine with the same name 'cashbox.csv' and 2 columns: denomination and number of bills;

**`cashbox.csv`**
----- | -----
100   | 2  |
50    | 50 |
20    | 50 |
10    | 50 |
5     | 50 |
1     | 100|

The second one represents products inside the vending mashine, 'products.csv' has 4 columns: product id, product name, price and stock amount.

**`products.csv`**

| :---| :--------------------- | --
| 1   | Croissant         | 5  | 20
| 2   | Mini Hummus       | 4  | 20
| 3   | Licorice Candy    | 4  | 20
| 4   | Non-alcoholic Rum | 10 | 20
| 5   | Soda              | 1  | 20

| Attempt | #1  | #2  |
| :-----: | :-: | :-: |
| Seconds | 301 | 283 |


--------------------------------------------------------------------------------

## Usage

To make sure it works:

1. Check the `cashbox.csv` and `products.csv` files for their contents
2. Run the program


By running `run_vending_machine.py` you will see the table of products with its prices and will be asked to choose one,
If the choice is correct and the product exists in the stock you'll be asked to pay its price by inputing banknotes/coins (numbers separated by space),
Here we also have few options: either the input wasn't correct or the amount of inputed banknote/coin wasn't correct or the amount wasn't enough then you'll get an error message accordingly, 
If you've inputted banknotes/coins correctly but there is no change in cashbox you'll get your money back and the excuses from the vending mashine,
If the amount was the exact as price or there were change then you'll finally get the product and the change if needed =)

In case everything went well and you've got the product, 2 csv files will be changed (new temps created and renamed) accordingly: the amount of stock will be reduced in products.csv, in cashbox.csv the amount of banknotes/coins will be increased by inputted and descreased by given change. 


--------------------------------------------------------------------------------

## Example

**Input files**

**`cashbox.csv`**

----- | -----
100   | 2
50    | 50
20    | 50
10    | 50
5     | 50
1     | 100

--------------------------------------------------------------------

**`products.csv`**
:-: | :---------------: | :-: | :-: |
| 1 | Croissant         | 5   | 20  |
| 2 | Mini Hummus       | 4   | 20  |
| 3 | Licorice Candy    | 4   | 20  |
| 4 | Non-alcoholic Rum | 10  | 20  |
| 5 | Soda              | 1   | 20  |

--------------------------------------------------------------------

Running the program:

----------------------------------------------
1 - Croissant - $5
2 - Mini Hummus - $12
3 - Licorice Candy - $4
4 - Non-alcoholic Rum - $10
5 - Soda - $1

Now tell me what is it that you truly desire? 
(Please choose the product)

----------------------------------------------
2

----------------------------------------------

Mini Hummus is a perfect choice! The price is $12. Please enter banknotes (numbers separated by space)

----------------------------------------------
10 10

----------------------------------------------

Enjoy and do not forget your change [5, 1, 1, 1]

----------------------------------------------


--------------------------------------------------------------------------------

**Output files**


**`cashbox.csv`**
----- | -----
100   | 2
50    | 50
20    | 50
10    | 50
5     | 50
1     | 100

--------------------------------------------------------------------

**`products.csv`**
----| ---------------------- | -----
1   | Croissant         | 5  | 20
2   | Mini Hummus       | 4  | 19
3   | Licorice Candy    | 4  | 20
4   | Non-alcoholic Rum | 10 | 20
5   | Soda              | 1  | 20

--------------------------------------------------------------------
