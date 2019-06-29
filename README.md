# Purchase-Analytics

## Table of Contents
1. [Problem](README.md#problem)
1. [Solution](README.md#summary-of-key-achievements-and-solution)
1. [Installation and Running](README.md#installation-and-running)
1. [Testing](README.md#testing)
1. [Repo directory structure](README.md#repo-directory-structure)

## Problem

This Insight coding challenge was to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers. The solution must be well tested, scalable, and documented. Any choice of programming language was allowed, but you are limited to only the built-in data types and libaries.

The dataset can be found on Instacart (a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders. )


## Summary of Key Achievements and Solution
* Achieved a runtime of ~2 mins on test data of 3.2 million
* A dictionary of dictionaries was used to create a hash table, in order achieve O(1) time for search and insert. As these would be the most operations executed.
* Robust error handling for I/O and type cast for inputs.

### Full Solution
The main objective of the solution was to process large data set quickly. Since parsing the full dataset cannot be avoided, it was only done once. This was done in python using the argparse, os, csv and decimal built-in libraries as part of the problem specifications. I assumed that the total number of unique of products and departments will be much smaller than the number of orders, meaning storing products and departments was not an issue for memory. The main goal then was to process all the orders quickly, by achieving a O(1) time for search and insert.

To do this I first created a dictionary using "Product_ID" as key, and "Department_ID" as value read from the "products" database.

```
prod_dict = {
             'Product1': department_ID,
	     'product2': department_ID
	    }
```

Next, I create a `dept_dict`, and for each order being read from the "order_products" database, I find the associated department ID for the product being orderd, which will be the key for dept_dict. Each department in `dept_dict` had a value of `function_dict`, created and updated as the orders are read.


The final data structure looks like this

```
dept_dict = {
             department_ID1: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z} ,
	     department_ID2: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}
	    }
```
`function_dict` for department_ID1 is {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}

The records were read in using the CSV library, and before adding the record to the Hash table, they were validated in the following way.

For the Product Record dictionary, in this order:

1. Length of the record must be 4
2. The relevant enteries (`Product_Id` and `Department_ID`, ) are all positive integers
3. `Product_Id` key is not already in `prod_dict` (i.e a duplicate entry)

If these are not met, then the record is not added, otherwise the record is added to the `prod_dict`.

For the Department Record dictionary, the Product Orders were validated in the following order, and order is important for this:

1. Lenght of the record must be 4
2. The `Product_Id` is positive integers
3. The `reordered` flag is either 0 or 1
4. The `Product_Id` key must be in the `prod_dict`

If these conditions are not met, a statement is printed in the terminal showing which record is invalid, and the record is not added in the `dept_dict` (this was done so that a valid report would still be generated with all the valid records)

If those conditions are satisfied then record is added to `dept_dict` as following

1. If the department_ID key is not already in the `dept_dict`, then create a `function_dict` for that department ID:
    
    i. Set the `function_dict['number_of_orders']= 1`
    
    ii. Check the reordered flag, and if its '0' set `function_dict['number_of_first_orders']= 1` else set it as 0
    
    iii. Calculate the ratio and set `function_dict['percentage']` as that and round it to two decimal places.
2. If the department_ID key is already in the `dept_dict` then:

    i. Get the `function_dict` for that deptartment_ID from `dept_dict`
    
    ii. Add 1 to the `function_dict['number_of_orders']` field. 
    
    iii. Check the reordered flag in the record, and if its '0' add 1 to `function_dict['number_of_first_orders']` field
    
    IV. Calculate the ratio and set `function_dict['percentage']` as that and round it to two decimal places

After reading and entering all the records, the `dept_dict` dictionary is converted into a list to be sorted in ascending order of department_ID (for this, the department_ID must be integers). Finally, the sorted list is output as a CSV file in the following format {department_id,number_of_orders,number_of_first_orders,percentage}



## Installation and Running
Run the program using run.sh in the Purchase-Analytics directory. The bash file runs the PurchaseAnalyticsMain.py and gives order_products.csv and products.csv as input files and report.csv as output file.


## Testing

The two sample inputs are given with `order_products.csv` as
```
order_id,product_id,add_to_cart_order,reordered
2,33120,1,1
2,28985,2,1
2,9327,3,0
2,45918,4,1
3,17668,1,1
3,46667,2,1
3,17461,4,1
3,32665,3,1
4,46842,1,0
```

where

* `order_id`: unique identifier of order
* `product_id`: unique identifier of product
* `add_to_cart_order`: sequence order in which each product was added to shopping cart
* `reordered`: flag indicating if the product has been ordered by this user at some point in the past. The field is `1` if the user has ordered it in the past and `0` if the user has not. While data engineers should validate their data, for the purposes of this challenge, you can take the `reordered` flag at face value and assume it accurately reflects whether the product has been ordered by the user before.

The 2nd input file `products.csv` holds data on every product, and looks something like this:

```
product_id,product_name,aisle_id,department_id
9327,Garlic Powder,104,13
17461,Air Chilled Organic Boneless Skinless Chicken Breasts,35,12
17668,Unsweetened Chocolate Almond Breeze Almond Milk,91,16
28985,Michigan Organic Kale,83,4
32665,Organic Ezekiel 49 Bread Cinnamon Raisin,112,3
33120,Organic Egg Whites,86,16
45918,Coconut Butter,19,13
46667,Organic Ginger Root,83,4
46842,Plain Pre-Sliced Bagels,93,3
```
where

* `product_id`: unique identifier of the product
* `product_name`: name of the product
* `aisle_id`: identifier of aisle in which product is located
* `department_id`: identifier of department

The output sample file `report.csv` looks like this:

```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```
`number_of_orders`. How many times was a product requested from this department? (If the same product was ordered multiple times, we count it as multiple requests)

`number_of_first_orders`. How many of those requests contain products ordered for the first time?

`percentage`. What is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department? (e.g., `number_of_first_orders` divided by `number_of_orders`)



### Unit Testing

Run the unittest_run.sh script unit test all the functions in AnalyticsHelper.py. The results are in unit_test/results.txt

* ProdRecord(record, prod_dict): Checks if the entries are added to the prod_dict, if the record is valid.
* DeptRecord(record, prod_dict, dept_dict): Checks if the entries are added or not added depending on the validity of the record, and prod_dict 
* IsPosIntegerProd(record): Checks if the Product ID and and the Department ID in the record are positive integers
* IsPosIntegerOrd(record): Checks if the Product ID is positive integer, and the reorder flag is 0 or 1. 
* IsValidProd(record): Checks the length to be 4, and if the entries are positive integer
* IsValidOrd(record, prod_dict): Checks the length to be 4, whether the entries are positive integer, and whether the department ID key is in prod_dict

### Test Suite

The testsuite tests are run using run_tests.sh file to run the following tests:

* test_1: runs the provided sample test with all valid entries to see if a valid output is seen
* test_2: tests the result when one of the department_id entry in products.csv is invalid.
* test_3: tests the result when one of the reordered flag entry in products_order.csv is invalid.
* test_4: tests the result when an extra value is added to one of the orders. 
* test_5: tests the result when a product_ID has two records in products.csv file, it only takes the first one.


## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md
    ├── run.sh
    ├── unittest_run.sh
    ├── src
    │   └── PurchaseAnalyticsMain.py
    │   └── AnalyticsHelper.py
    │   └── __init__.py   
    ├── input
    │   └── products.csv
    |   └── order_products.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
    |   └── run_tests.sh
    |   └── tests
    |       └── test_1
    |       |   ├── input
    |       |   │   └── products.csv
    |       |   │   └── order_products.csv
    |       |   |__ output
    |       |   │   └── report.csv
    |       . . . 
    |       . . .
    |       . . .
    |       ├── test_5
    |           ├── input
    |           │   └── products.csv
    |           |   └── order_products.csv
    |           |── output
    |               └── report.csv
    |──unit_tests
       └──test_DeptRecord.py
       └──test_ProdRecord.py
       └──test_IsValidProd.py
       └──test_IsValidOrd.py
       └──test_IsPosIntegerProd.py
       └──test_IsPosIntegerOrd.py
       └──__init__.py

