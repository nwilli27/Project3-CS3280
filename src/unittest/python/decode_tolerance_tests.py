
import unittest
from resistor import decodeTolerance

class TestDecodeTolerance(unittest.TestCase):
    
    def testGetToleranceBrownBand(self):
        self.assertEquals(1, decodeTolerance(["brown", "red", "blue", "brown"]))
        
    def testGetToleranceRedBand(self):
        self.assertEquals(2, decodeTolerance(["brown", "red", "blue", "red"]))
        
    def testGetToleranceGreenBand(self):
        self.assertEquals(0.5, decodeTolerance(["brown", "red", "blue", "green"]))
    
    def testGetToleranceBlueBand(self):
        self.assertEquals(0.25, decodeTolerance(["brown", "red", "blue", "blue"]))
    
    def testGetToleranceVioletBand(self):
        self.assertEquals(0.1, decodeTolerance(["brown", "red", "blue", "violet"]))
        
    def testGetToleranceGreyBand(self):
        self.assertEquals(0.05, decodeTolerance(["brown", "red", "blue", "grey"]))
    
    def testGetToleranceGoldBand(self):
        self.assertEquals(5, decodeTolerance(["brown", "red", "blue", "gold"]))
    
    def testGetToleranceSilverBand(self):
        self.assertEquals(10, decodeTolerance(["brown", "red", "blue", "silver"]))
    
    def testGetToleranceNoneBand(self):
        self.assertEquals(20, decodeTolerance(["brown", "red", "blue", "none"]))
   