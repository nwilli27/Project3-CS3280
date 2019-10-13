
import unittest
from resistor import decodeMultiplier

class TestDecodeMultiplier(unittest.TestCase):
    
    def testGetMultiplierBlackBand(self):
        multiplier = decodeMultiplier(["brown", "red", "black", "brown"])
        self.assertEquals(1, multiplier[0])
        
    def testGetMultiplierBrownBand(self):
        multiplier = decodeMultiplier(["brown", "red", "brown", "brown"])
        self.assertEquals(10, multiplier[0])
    
    def testGetMultiplierRedBand(self):
        multiplier = decodeMultiplier(["brown", "red", "red", "brown"])
        self.assertEquals(100, multiplier[0])
        
    def testGetMultiplierOrangeBand(self):
        multiplier = decodeMultiplier(["brown", "red", "orange", "brown"])
        self.assertEquals(1, multiplier[0])
        self.assertEquals("K", multiplier[1])
        
    def testGetMultiplierYellowBand(self):
        multiplier = decodeMultiplier(["brown", "red", "yellow", "brown"])
        self.assertEquals(10, multiplier[0])
        self.assertEquals("K", multiplier[1])
        
    def testGetMultiplierGreenBand(self):
        multiplier = decodeMultiplier(["brown", "red", "green", "brown"])
        self.assertEquals(100, multiplier[0])
        self.assertEquals("K", multiplier[1])
        
    def testGetMultiplierBlueBand(self):
        multiplier = decodeMultiplier(["brown", "red", "blue", "brown"])
        self.assertEquals(1, multiplier[0])
        self.assertEquals("M", multiplier[1])
        
    def testGetMultiplierVioletBand(self):
        multiplier = decodeMultiplier(["brown", "red", "violet", "brown"])
        self.assertEquals(10, multiplier[0])
        self.assertEquals("M", multiplier[1])
        
    def testGetMultiplierGreyBand(self):
        multiplier = decodeMultiplier(["brown", "red", "grey", "brown"])
        self.assertEquals(100, multiplier[0])
        self.assertEquals("M", multiplier[1])
        
    def testGetMultiplierWhiteBand(self):
        multiplier = decodeMultiplier(["brown", "red", "white", "brown"])
        self.assertEquals(1, multiplier[0])
        self.assertEquals("G", multiplier[1])
        
    def testGetMultiplierGoldBand(self):
        multiplier = decodeMultiplier(["brown", "red", "gold", "brown"])
        self.assertEquals(0.1, multiplier[0])
        
    def testGetMultiplierSilverBand(self):
        multiplier = decodeMultiplier(["brown", "red", "silver", "brown"])
        self.assertEquals(0.01, multiplier[0])
                          
        
  