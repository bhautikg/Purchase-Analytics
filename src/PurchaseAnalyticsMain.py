import argparse
import os
import csv
import AnalyticsHelper


def main():
    """

    """
    parser = argparse.ArgumentParser(description='Purchase Analytics')
    parser.add_argument('OrdProdIn', metavar='orders file address', help='Input containing ordered products')
    parser.add_argument('ProdIn', metavar='products file address', help='Input containing information about products')
    parser.add_argument('output', metavar='output file addres', help='Output containing processed info deprtments and their statistics')
    args = parser.parse_args()

    
    try:
        with open(args.ProdIn, 'r') as ProdInFile:
            infile = csv.reader(ProdInFile, delimiter=',')
            next(infile)
            prod_dict = {}
            for i, record in enumerate(infile):
                flag = AnalyticsHelper.ProdRecord(record, prod_dict)
                if flag != True:
                    break
        

        with open(args.OrdProdIn, 'r') as OrdProdInFile:
            infile = csv.reader(OrdProdInFile, delimiter=',')
            next(infile)
            dept_dict = {}
            for i, record in enumerate(infile):
                AnalyticsHelper.DeptRecord(record, prod_dict, dept_dict)
    except IOError:
        print('One or both of the input files not found')
        return
    except ValueError as e:
        print (str(e))
        return
    print (dept_dict)
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
        #analytics_outfile.truncate(analytics_outfile.tell() - len(os.linesep))

if __name__=="__main__":
    main()
