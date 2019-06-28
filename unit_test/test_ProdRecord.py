import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import ProdRecord
import math

class TestProdRecord(unittest.TestCase):

    def setUp(self):
        self.prod_dict = {}
        self.dept_dict = {}
        self.ProdValid = ['9327','Garlic Powder','104','13']
        self.ProdInvalid1 = ['9327','Garlic Powder','104','-13']
        self.ProdInvalid2 = ['-9327','Garlic Powder','104','13']
        self.ProdInvalid3 = ['fadsf','Garlic Powder','104','13']
        self.ProdInvalid4 = ['9327','Garlic Powder','104','adfadf']
        self.ProdInvalid5 = ['9327','Garlic Powder','104','13.03']
        self.ProdInvalid6 = ['9327.09','Garlic Powder','104','13']
        self.ProdInvalid7 = ['9327','Garlic Powder','104'] #Product information length less than 4
        self.ProdInvalid8 = ['9327','Garlic Powder','104','13', 'jasdfdf'] #length more than 4
    
    def test_FuncCall(self):
        self.assertTrue(ProdRecord(self.ProdValid, self.prod_dict))
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid1, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid2, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid3, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid4, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid5, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid6, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid7, self.prod_dict)
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid8, self.prod_dict)
    
    def test_ProdRecord(self):
        ProdRecord(self.ProdValid, self.prod_dict)
        test_dict = {'9327': 13}
        self.assertEqual(self.prod_dict,test_dict)

        ProdRecord(self.ProdValid, self.prod_dict) #If the same entry shows up again, see that it doesnt change prod dictionary.
        self.assertEqual(self.prod_dict, test_dict)  #prod dictionary shouldnt change
        
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid1, self.prod_dict) #try to add an invalid entry
        
        self.assertEqual(self.prod_dict, test_dict) #see if it hasnt added anything

        self.prod_dict = {} #clear this dictionary
        self.assertRaises(ValueError, ProdRecord, self.ProdInvalid2, self.prod_dict) #see if it doesnt add anything to the dictionary
        self.assertEqual(self.prod_dict, {})

if __name__=="__main__":
    unittest.main()