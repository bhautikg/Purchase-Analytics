import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import IsValidProd
import math

class TestIsValidProd(unittest.TestCase):

    def setUp(self):
        self.ProdValid = ['9327','Garlic Powder','104','13']
        self.ProdInvalid1 = ['9327','Garlic Powder','104','-13']
        self.ProdInvalid2 = ['-9327','Garlic Powder','104','13']
        self.ProdInvalid3 = ['fadsf','Garlic Powder','104','13']
        self.ProdInvalid4 = ['9327','Garlic Powder','104','adfadf']
        self.ProdInvalid5 = ['9327','Garlic Powder','104','13.03']
        self.ProdInvalid6 = ['9327.09','Garlic Powder','104','13']
        self.ProdInvalid7 = ['9327','Garlic Powder','104'] #Product information length less than 4
        self.ProdInvalid8 = ['9327','Garlic Powder','104','13', 'jasdfdf'] #length more than 4
    
    def test_IsValidProd(self):
        self.assertTrue(IsValidProd(self.ProdValid))
        self.assertFalse(IsValidProd(self.ProdInvalid1))
        self.assertFalse(IsValidProd(self.ProdInvalid2))
        self.assertFalse(IsValidProd(self.ProdInvalid3))
        self.assertFalse(IsValidProd(self.ProdInvalid4))
        self.assertFalse(IsValidProd(self.ProdInvalid5))
        self.assertFalse(IsValidProd(self.ProdInvalid6))
        self.assertFalse(IsValidProd(self.ProdInvalid7))
        self.assertFalse(IsValidProd(self.ProdInvalid8))


if __name__=="__main__":
    unittest.main()