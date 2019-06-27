import unittest
import sys
from src.AnalyticsHelper import DeptRecord

import math

class TestDeptRecord(unittest.TestCase):

    def setUp(self):
        self.prod_dict = {'9327': 13, '45918':13, '32665':3}
        self.dept_dict = {}

        self.OrdValid = ['2','9327','3','0']
        self.OrdValid2 = ['2','45918','4','1']
        self.OrdValid3 = ['3','32665','3','1']

        self.OrdInvalid1 = ['2','-9327','3','0']
        self.OrdInvalid2 = ['2','9327','3','-10']
        self.OrdInvalid3 = ['2','9327.098','3','0']
        self.OrdInvalid4 = ['2','9327','3','0.908']
    
    def test_FuncCall(self):
        self.assertTrue(DeptRecord(self.OrdValid, self.prod_dict, self.dept_dict))
        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid1, self.prod_dict, self.dept_dict)
        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid2, self.prod_dict, self.dept_dict)
        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid3, self.prod_dict, self.dept_dict)
        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid4, self.prod_dict, self.dept_dict)

    
    def test_DeptRecord(self):
        DeptRecord(self.OrdValid, self.prod_dict, self.dept_dict)
        test_dict = {13:{'number_of_orders': 1, 'number_of_first_orders': 1, 'percentage': 1}}
        self.assertEqual(self.dept_dict, test_dict)
        
        DeptRecord(self.OrdValid2, self.prod_dict, self.dept_dict) #add another item to department 13, a reorder
        test_dict = {13:{'number_of_orders': 2, 'number_of_first_orders': 1, 'percentage': 0.50},}
        self.assertEqual(self.dept_dict, test_dict)

        DeptRecord(self.OrdValid3, self.prod_dict, self.dept_dict) #Add an order from department 3, instead of 13
        test_dict = {13:{'number_of_orders': 2, 'number_of_first_orders': 1, 'percentage': 0.50},
                    3: {'number_of_orders': 1, 'number_of_first_orders': 0, 'percentage': 0} }
        self.assertEqual(self.dept_dict, test_dict)  #Dept dictionary shouldnt change

        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid1, self.prod_dict, self.dept_dict) #try to add an invalid entry
        self.assertEqual(self.dept_dict, test_dict) #see if it hasnt added anything

        self.dept_dict = {} #clear this dictionary
        self.assertRaises(ValueError, DeptRecord, self.OrdInvalid1, self.prod_dict, self.dept_dict) #see if it doesnt add anything to the dictionary
        self.assertEqual(self.dept_dict, {})

if __name__=="__main__":
    unittest.main()