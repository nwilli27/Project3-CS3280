
import unittest
from resistor import decodeResistance

class TestDecodeResistance(unittest.TestCase):
    
    #Low multiplier/tolerance
    
    def testDecodeReistanceLowMultiplerAndTolerance4Band(self):
        expected = decodeResistance(["brown", "red", "black", "grey"])
        self.assertEquals(12, expected['value'])
        self.assertEquals("ohms", expected['units'])
        self.assertEquals(0.05, expected['tolerance'])
        self.assertEquals("12 ohms +/- 0.05%", expected['formatted'])
        
    def testDecodeReistanceLowMultiplerAndTolerance5Band(self):
        expected = decodeResistance(["brown", "red", "orange", "black", "green"])
        self.assertEquals(123, expected['value'])
        self.assertEquals("ohms", expected['units'])
        self.assertEquals(0.5, expected['tolerance'])
        self.assertEquals("123 ohms +/- 0.5%", expected['formatted'])
        
    #Medium multiplier/tolerance
    
    def testDecodeReistanceMediumMultiplerAndTolerance4Band(self):
        expected = decodeResistance(["yellow", "green", "yellow", "brown"])
        self.assertEquals(450, expected['value'])
        self.assertEquals("Kohms", expected['units'])
        self.assertEquals(1, expected['tolerance'])
        self.assertEquals("450 Kohms +/- 1%", expected['formatted'])
        
    def testDecodeReistanceMediumMultiplerAndTolerance5Band(self):
        expected = decodeResistance(["yellow", "green", "blue", "green", "red"])
        self.assertEquals(45600, expected['value'])
        self.assertEquals("Kohms", expected['units'])
        self.assertEquals(2, expected['tolerance'])
        self.assertEquals("45600 Kohms +/- 2%", expected['formatted'])
        
    #High multiplier/tolerance
    
    def testDecodeReistanceHighMultiplerAndTolerance4Band(self):
        expected = decodeResistance(["violet", "grey", "blue", "gold"])
        self.assertEquals(78, expected['value'])
        self.assertEquals("Mohms", expected['units'])
        self.assertEquals(5, expected['tolerance'])
        self.assertEquals("78 Mohms +/- 5%", expected['formatted'])
        
    def testDecodeReistanceHighMultiplerAndTolerance5Band(self):
        expected = decodeResistance(["violet", "grey", "white", "grey", "none"])
        self.assertEquals(78900, expected['value'])
        self.assertEquals("Mohms", expected['units'])
        self.assertEquals(20, expected['tolerance'])
        self.assertEquals("78900 Mohms +/- 20%", expected['formatted'])