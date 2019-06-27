def ProdRecord(record, dict):
    """
    :param record: [product_id,product_name,aisle_id,department_id]
    :param dict: dictionary of entries
    :return: dict with record added or updated
    """
    dict[record[0]] = record[3]
    return True

def DeptRecord(record, dept_id, dept_dict):
    """ 
    :param Order record: [order_id,product_id,add_to_cart_order,reordered]
    :param dict: dictionary of entries 
    :out put [department_id,number_of_orders,number_of_first_orders,percentage]
    :return: dict with record added or updated
    """
    function_dict = {}
    if dept_id in dept_dict:
        function_dict = dept_dict[dept_id]
        function_dict['number_of_orders'] = function_dict['number_of_orders'] + 1

        #print (record[3])
        #print(function_dict['number_of_orders'])
        if record[3] == '0':
            function_dict['number_of_first_orders'] = function_dict['number_of_first_orders'] + 1
        function_dict['percentage'] = function_dict['number_of_first_orders']/ function_dict['number_of_orders']
    else:
        dept_dict[dept_id] = function_dict
        function_dict['number_of_orders'] = 1
        if record[3] =='0':
            function_dict['number_of_first_orders'] = 1
        else:
            function_dict['number_of_first_orders'] = 0
        function_dict['percentage'] = function_dict['number_of_first_orders']/ function_dict['number_of_orders']

    return True