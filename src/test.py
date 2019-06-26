import argparse
import os
import csv
import AnalyticsHelper


if __name__=="__main__":
    """

    """
    parser = argparse.ArgumentParser(description='Purchase Analytics')
    parser.add_argument('OrdProdIn', metavar='in', help='Input containing ordered products')
    parser.add_argument('ProdIn', metavar='in', help='Input containing information about products')
    parser.add_argument('output', metavar='out', help='Output containing processed info deprtments and their statistics')
    args = parser.parse_args()

    
    try:
        with open(args.ProdIn, 'r') as ProdInFile:
            reader = csv.reader(ProdInFile, delimiter=',')
            next(reader)
            prod_dict = {}
            for i, record in enumerate(reader):
                AnalyticsHelper.ProdRecord(record, prod_dict)
        

        with open(args.OrdProdIn, 'r') as OrdProdInFile:
            reader = csv.reader(OrdProdInFile, delimiter=',')
            next(reader)
            dept_dict = {}
            for i, record in enumerate(reader):
                dept_id = int(prod_dict[record[1]])
                AnalyticsHelper.DeptRecord(record, dept_id, dept_dict)
    except IOError:
        print('Input file does not exist')

    dept_prod_pair = zip(dept_dict.keys(), dept_dict.values())
    dept_prod_pair = list(dept_prod_pair)
    #print (dept_prod_pair)
    dept_prod_pair = sorted(dept_prod_pair, key=lambda row: (row[0]))
    
    with open(args.output, 'w', newline='\n') as analytics_outfile:
        fieldnames = ['department_id','number_of_orders','number_of_first_orders','percentage']
        writer = csv.DictWriter(analytics_outfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in dept_prod_pair:
            writer.writerow(
                {'department_id': record[0],
                 'number_of_orders': record[1]['number_of_orders'],
                 'number_of_first_orders': record[1]['number_of_first_orders'],
                 'percentage': record[1]['percentage']}
            )
        analytics_outfile.truncate(analytics_outfile.tell() - len(os.linesep))
