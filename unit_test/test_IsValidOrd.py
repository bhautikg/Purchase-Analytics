import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import IsValidOrd

import math

class TestIsValidOrd(unittest.TestCase):

    def setUp(self):
        
        self.prod_dict = {'9327': 13, '45918':13, '32665':3}

        self.OrdValid = ['2','9327','3','0']
        self.OrdValid2 = ['2','45918','4','1']
        self.OrdValid3 = ['3','32665','3','1']

        self.OrdInvalid1 = ['2','-9327','3','0']
        self.OrdInvalid2 = ['2','9327','3','-10']
        self.OrdInvalid3 = ['2','9327.098','3','0']
        self.OrdInvalid4 = ['2','9327','3','0.908']
        self.OrdInvalid5 = ['2','1234','3','0']  # Product ID not in Prod_dict
        self.OrdInvalid6 = ['2','9327','3'] #record lenght less than 4
        self.OrdInvalid7 = ['2','9327','3', '0', 'fadfadf'] #record lenght more than 4
        self.OrdInvalid8 = ['2','9327','3','2'] #reorded flag is not 0 or 1
    
    def test_IsValidOrd(self):
        self.assertTrue(IsValidOrd(self.OrdValid, self.prod_dict))
        self.assertTrue(IsValidOrd(self.OrdValid2, self.prod_dict))
        self.assertFalse(IsValidOrd(self.OrdInvalid1, self.prod_dict))
        self.assertFalse(IsValidOrd(self.OrdInvalid2, self.prod_dict))
        self.assertFalse(IsValidOrd(self.OrdInvalid3, self.prod_dict))
        self.assertFalse(IsValidOrd(self.OrdInvalid4, self.prod_dict))
        self.assertFalse(IsValidOrd(self.OrdInvalid5, self.prod_dict))

if __name__=="__main__":
    unittest.main()