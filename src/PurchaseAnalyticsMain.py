import argparse
import os
import csv
import AnalyticsHelper


def main():
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
    parser = argparse.ArgumentParser(description='Purchase Analytics')
    parser.add_argument('OrdProdIn', metavar='orders file address', help='Input containing ordered products')
    parser.add_argument('ProdIn', metavar='products file address', help='Input containing information about products')
    parser.add_argument('output', metavar='output file addres', help='Output containing processed info deprtments and their statistics')
    args = parser.parse_args()

    
    try:
        with open(args.ProdIn, 'r', encoding="utf8") as ProdInFile:
            infile = csv.reader(ProdInFile, delimiter=',')
            next(infile)
            prod_dict = {}
            for i, record in enumerate(infile):
                AnalyticsHelper.ProdRecord(record, prod_dict)
        

        with open(args.OrdProdIn, 'r', encoding="utf8") as OrdProdInFile:
            infile = csv.reader(OrdProdInFile, delimiter=',')
            next(infile)
            dept_dict = {}
            for i, record in enumerate(infile):
                AnalyticsHelper.DeptRecord(record, prod_dict, dept_dict)
    except IOError:
        print('One or both of the input files not found')
        return
    except ValueError:
        return

    dept_prod_pair = zip(dept_dict.keys(), dept_dict.values())
    dept_prod_pair = list(dept_prod_pair)
    dept_prod_pair = sorted(dept_prod_pair, key=lambda row: (row[0]))
    
    with open(args.output, 'w', newline='\n') as analytics_outfile:
        headers = ['department_id','number_of_orders','number_of_first_orders','percentage']
        outfile = csv.DictWriter(analytics_outfile, fieldnames=headers)
        outfile.writeheader()
        for record in dept_prod_pair:
            outfile.writerow(
                {'department_id': record[0],
                 'number_of_orders': record[1]['number_of_orders'],
                 'number_of_first_orders': record[1]['number_of_first_orders'],
                 'percentage': record[1]['percentage']}
            )

if __name__=="__main__":
    main()
