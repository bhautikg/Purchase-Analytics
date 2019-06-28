import unittest
import sys
sys.path.insert(0, 'C:/Users/bhaut/Documents/GitHub/Purchase-Analytics')
from src.AnalyticsHelper import IsPosIntegerOrd

import math

class TestIsPosIntegerOrd(unittest.TestCase):

    def setUp(self):

        self.OrdValid = ['2','9327','3','0']
        self.OrdValid2 = ['2','45918','4','1']
        self.OrdValid3 = ['3','32665','3','1']

        self.OrdInvalid1 = ['2','-9327','3','0']
        self.OrdInvalid2 = ['2','9327','3','-10']
        self.OrdInvalid3 = ['2','9327.098','3','0']
        self.OrdInvalid4 = ['2','9327','3','0.908']
        self.OrdInvalid5 = ['2','9327','3','2'] #reorded flag is not 0 or 1
    
    def test_IsPosIntegerOrd(self):
        self.assertTrue(IsPosIntegerOrd(self.OrdValid))
        self.assertTrue(IsPosIntegerOrd(self.OrdValid2))
        self.assertFalse(IsPosIntegerOrd(self.OrdInvalid1))
        self.assertFalse(IsPosIntegerOrd(self.OrdInvalid2))
        self.assertFalse(IsPosIntegerOrd(self.OrdInvalid3))
        self.assertFalse(IsPosIntegerOrd(self.OrdInvalid4))
        self.assertFalse(IsPosIntegerOrd(self.OrdInvalid5))

if __name__=="__main__":
    unittest.main()