import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import IsPosIntegerProd
import math

class TestIsPosIntegerProd(unittest.TestCase):

    def setUp(self):
        self.ProdValid = ['9327','Garlic Powder','104','13']
        self.ProdInvalid1 = ['9327','Garlic Powder','104','-13']
        self.ProdInvalid2 = ['-9327','Garlic Powder','104','13']
        self.ProdInvalid3 = ['fadsf','Garlic Powder','104','13']
        self.ProdInvalid4 = ['9327','Garlic Powder','104','adfadf']
        self.ProdInvalid5 = ['9327','Garlic Powder','104','13.03']
        self.ProdInvalid6 = ['9327.09','Garlic Powder','104','13']
    
    def test_IsPosIntegerProd(self):
        self.assertTrue(IsPosIntegerProd(self.ProdValid))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid1))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid2))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid3))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid4))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid5))
        self.assertFalse(IsPosIntegerProd(self.ProdInvalid6))


if __name__=="__main__":
    unittest.main()