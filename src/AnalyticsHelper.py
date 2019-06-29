from decimal import Decimal

def IsPosIntegerProd(record):
    """
    Checks if product ID and department ID are positive integers
    :param record: [product_id,product_name,aisle_id,department_id]
    :return: True or False depending on the conditions
    """
    try:
        #Check if product_id is positive int, and department ID is positive integer
        if int(record[0])>=0 and int(record[3])>=0:
            return True
    except TypeError:
        return False
    except ValueError:
        return False

def IsPosIntegerOrd(record):
    """
    Checks if Product ID is positive integer, and if reordered flag is 1 or 0 
    :param record: [order_id,product_id,add_to_cart_order,reordered]
    :return: True or False depending on the conditions
    """
    try:

        if int(record[1])>=0 and (int(record[3]) == 0 or int(record[3])== 1):
            return True
    except TypeError:
        return False
    except ValueError:
        return False

def IsValidProd(record, prod_dict):
    """
    Checks if the products record is correct length and the values are positive integers and not duplicate
    :param record: [product_id,product_name,aisle_id,department_id]
    :param prod_dict: dictionary of ['Product_ID': department_ID]
    :return: True or False depending on the conditions
    """
    # Must check in this order! if length is not correct, IsPos will throw error
    if (len(record) == 4) and IsPosIntegerProd(record) and (record[0] not in prod_dict): 
        return True
    else:
        return False

def ProdRecord(record, prod_dict):
    """
    Adds an entry to prod_dictionary with product ID as key and department ID as value.
    :param record: [product_id,product_name,aisle_id,department_id]
    :param prod_dict: dictionary of ['Product_ID': department_ID]
    :return: with the prod_dict updated or entry added
    """
    if IsValidProd(record, prod_dict):
        try:
            prod_dict[record[0]] = int(record[3])
        except TypeError:
            return False
        return True
    else:
        print('This product information is invalid or duplicated %s' % record)
        return False

def IsValidOrd(record, prod_dict):
    """ 
    Checks if the order entry is correct length, and then if the order entries are correct type, and if the product ID key exists in the prod_dict
    :param record: [order_id,product_id,add_to_cart_order,reordered]
    :param prod_dict: dictionary of ['Product_ID': department_ID]
    :return: True or False depending on the conditions
    """
    # Must check in this order! if length is not correct, IsPos will throw error
    if (len(record) == 4) and IsPosIntegerOrd(record) and (record[1] in prod_dict): 
        return True
    else:
        return False

def DeptRecord(record, prod_dict, dept_dict):
    """
    Processes and adds the order(record) to dept_dict, using department_ID as key, and function_dict as value.
    :param record: [order_id,product_id,add_to_cart_order,reordered]
    :param prod_dict: dictionary of ['Product_ID': department_ID]
    :param dept_dict: an empty or of format dept_dict = {department_ID1: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}}
    :out put {department_ID1: {'number_of_orders': x, 'number_of_first_orders': y, 'percentage': z}}
    :return: dict with record added or updated
    """
    if IsValidOrd(record, prod_dict):
        #Get the valid dept_ID from the prod_dict
        dept_id = prod_dict[record[1]]
        function_dict = {}
        
        if dept_id in dept_dict:
            
            #If its already in dept_dict, get the function_dict associated with it, and update it with current order
            function_dict = dept_dict[dept_id]
            function_dict['number_of_orders'] = function_dict['number_of_orders'] + 1

            #Check the reordered flag, if 0, add 1 to number of first orders
            if record[3] == '0':
                function_dict['number_of_first_orders'] = function_dict['number_of_first_orders'] + 1
            
            ratio = function_dict['number_of_first_orders']/ function_dict['number_of_orders']
            function_dict['percentage'] = round(ratio,2)
        
        else:
            #If department_ID is not already in dept_dict, create the entry, and populate it as such. 
            dept_dict[dept_id] = function_dict
            function_dict['number_of_orders'] = 1
            
            if record[3] =='0':
                function_dict['number_of_first_orders'] = 1
            else:
                function_dict['number_of_first_orders'] = 0
            
            ratio = function_dict['number_of_first_orders']/ function_dict['number_of_orders']
            function_dict['percentage'] = round(ratio,2)
    else:
        print('This product order is invalid or product information missing %s' % record)
        return False
    return True