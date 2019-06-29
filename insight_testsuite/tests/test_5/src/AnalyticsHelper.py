from decimal import Decimal

def IsPosIntegerProd(record):
    try:

        if int(record[0])>=0 and int(record[3])>=0:
            return True
    except TypeError:
        return False
    except ValueError:
        return False

def IsPosIntegerOrd(record):
    try:

        if int(record[1])>=0 and (int(record[3]) == 0 or int(record[3])== 1):
            return True
    except TypeError:
        return False
    except ValueError:
        return False

def IsValidProd(record):
    if (len(record) == 4) and IsPosIntegerProd(record): # Must check in this order! if length is not correct, IsPos will throw error
        return True
    else:
        return False

def ProdRecord(record, prod_dict):
    """
    :param record: [product_id,product_name,aisle_id,department_id]
    :param dict: dictionary of entries
    :return: dict with record added or updated
    """
    if IsValidProd(record): #Must check in this order! Or else IsPosInt will throw error
        try:
            prod_dict[record[0]] = int(record[3])
        except TypeError:
            return False
        return True
    else:
        raise ValueError('This record is invalid %s' % record)

def IsValidOrd(record, prod_dict):
    if (len(record) == 4) and IsPosIntegerOrd(record) and (record[1] in prod_dict): # Must check in this order! if length is not correct, IsPos will throw error
        return True
    else:
        return False

def DeptRecord(record, prod_dict, dept_dict):
    """ 
    :param Order record: [order_id,product_id,add_to_cart_order,reordered]
    :param dict: dictionary of entries 
    :out put [department_id,number_of_orders,number_of_first_orders,percentage]
    :return: dict with record added or updated
    """
    if IsValidOrd(record, prod_dict):
        dept_id = prod_dict[record[1]]
        function_dict = {}
        
        if dept_id in dept_dict:
            
            function_dict = dept_dict[dept_id]
            function_dict['number_of_orders'] = function_dict['number_of_orders'] + 1

            if record[3] == '0':
                function_dict['number_of_first_orders'] = function_dict['number_of_first_orders'] + 1
            
            ratio = function_dict['number_of_first_orders']/ function_dict['number_of_orders']
            function_dict['percentage'] = round(ratio,2)
        
        else:
            dept_dict[dept_id] = function_dict
            function_dict['number_of_orders'] = 1
            
            if record[3] =='0':
                function_dict['number_of_first_orders'] = 1
            else:
                function_dict['number_of_first_orders'] = 0
            
            ratio = function_dict['number_of_first_orders']/ function_dict['number_of_orders']
            function_dict['percentage'] = round(ratio,2)
    else:
        raise ValueError('This record is invalid or product information missing %s' % record)
    return True