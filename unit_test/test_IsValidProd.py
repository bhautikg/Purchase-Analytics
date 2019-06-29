import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import IsValidProd
import math

class TestIsValidProd(unittest.TestCase):

    def setUp(self):
        self.prod_dict = {'9327': 13, '32665':3}
        self.ProdValid = ['45918','mangoes','205','13'] #a valid entry not in prod_dict
        self.ProdValidDuplicate = ['9327','Garlic Powder','104','9'] #duplicate product ID entry with different department ID
        self.ProdInvalid1 = ['9327','Garlic Powder','104','-13']
        self.ProdInvalid2 = ['-9327','Garlic Powder','104','13']
        self.ProdInvalid3 = ['fadsf','Garlic Powder','104','13']
        self.ProdInvalid4 = ['9327','Garlic Powder','104','adfadf']
        self.ProdInvalid5 = ['9327','Garlic Powder','104','13.03']
        self.ProdInvalid6 = ['9327.09','Garlic Powder','104','13']
        self.ProdInvalid7 = ['9327','Garlic Powder','104'] #Product information length less than 4
        self.ProdInvalid8 = ['9327','Garlic Powder','104','13', 'jasdfdf'] #length more than 4
    
    def test_IsValidProd(self):
        self.assertTrue(IsValidProd(self.ProdValid, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdValidDuplicate, self.prod_dict)) #checks that if product ID already exists in prod_dict, that it is not changed
        self.assertFalse(IsValidProd(self.ProdInvalid1, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid2, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid3, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid4, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid5, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid6, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid7, self.prod_dict))
        self.assertFalse(IsValidProd(self.ProdInvalid8, self.prod_dict))


if __name__=="__main__":
    unittest.main()