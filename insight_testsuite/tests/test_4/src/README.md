This folder contains the source files for the solution. The PurchaseAnalyticsMain file uses AnalyticsHelper file functions to process the data and add records into the dictionary. Read the documentation below for more information on all the functions

NAME PurchaseAnalyticsMain

FUNCTIONS

    main():
        """
        input 1: CSV Products file of [product_id,product_name,aisle_id,department_id]
        input 2: CSV product orders file of [order_id,product_id,add_to_cart_order,reordered]

        output: CSV file of [department_id,number_of_orders,number_of_first_orders,percentage] 
                where percentage is the ratio of first orders/ total orders
        method: using dict data structure to implement a hashtable, the products are read in and a 
                a dict is created with product_ID as key, and int department_ID as value. Then orders are read in
                and a dept_dict is created with department_ID as key, and a function_dict as value, where the processed
                order information is stored. Then the hash table is converted into a list of tuples, 
                and sorted in asscending order. The sorted dictionary is output as a CSV file 
                in the following format [department_id,number_of_orders,number_of_first_orders,percentage]
        """
NAME AnalyticsHelper

FUNCTIONS

    DeptRecord(record, prod_dict, dept_dict):
        """ 
        :param record: [order_id,product_id,add_to_cart_order,reordered]
        :param prod_dict: dictionary of ['Product_ID': department_ID]
        :param dept_dict: an empty or of format dept_dict = {department_ID1: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}}
        :out put {department_ID1: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}}
        :return: dict with record added or updated
        """
    ProdRecord(record, prod_dict):
        """
        Adds an entry to prod_dictionary with product ID as key and department ID as value.
        :param record: [product_id,product_name,aisle_id,department_id]
        :param prod_dict: dictionary of ['Product_ID': department_ID]
        :return: with the prod_dict updated or entry added
        """
    IsValidOrd(record, prod_dict):
        """ 
        Checks if the order entry is correct length, and then if the order entries are correct type, and if the product ID key exists in the prod_dict
        :param record: [order_id,product_id,add_to_cart_order,reordered]
        :param prod_dict: dictionary of ['Product_ID': department_ID]
        :return: True or False depending on the conditions
        """
    IsValidProd(record, prod_dict):
        """
        Checks if the products record is correct length and the values are positive integers
        :param record: [product_id,product_name,aisle_id,department_id]
        :param prod_dict: dictionary of ['Product_ID': department_ID]
        :return: True or False depending on the conditions
        """
    IsPosIntegerOrd(record):
        """
        Checks if Product ID is positive integer, and if reordered flag is 1 or 0 
        :param record: [order_id,product_id,add_to_cart_order,reordered]
        :return: True or False depending on the conditions
        """
    IsPosIntegerProd(record):
        """
        Checks if product ID and department ID are positive integers
        :param record: [product_id,product_name,aisle_id,department_id]
        :return: True or False depending on the conditions
        """