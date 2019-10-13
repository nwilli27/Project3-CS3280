
import unittest
from resistor import createFormattedResistanceString

class TestCreateFormattedResistanceString(unittest.TestCase):
    
    #Low multiplier/tolerance
    
    def testCreateStringLowMultiplierLowTolerance4Band(self):
        expected = createFormattedResistanceString(["brown", "red", "black", "grey"])
        self.assertEquals("12 ohms +/- 0.05%", expected)
    
    def testCreateStringLowMultiplierLowTolerance5Band(self):
        expected = createFormattedResistanceString(["brown", "red", "orange", "black", "green"])
        self.assertEquals("123 ohms +/- 0.5%", expected)
        
    #Medium multiplier/tolerance
    
    def testCreateStringMediumMultiplierMediumTolerance4Band(self):
        expected = createFormattedResistanceString(["yellow", "green", "yellow", "brown"])
        self.assertEquals("450 Kohms +/- 1%", expected)
    
    def testCreateStringMediumMultiplierMediumTolerance5Band(self):
        expected = createFormattedResistanceString(["yellow", "green", "blue", "green", "red"])
        self.assertEquals("45600 Kohms +/- 2%", expected)
        
    #High multiplier/tolerance
    
    def testCreateStringHighMultiplierHighTolerance4Band(self):
        expected = createFormattedResistanceString(["violet", "grey", "blue", "gold"])
        self.assertEquals("78 Mohms +/- 5%", expected)
        
    def testCreateStringHighMultiplierHighTolerance5Band(self):
        expected = createFormattedResistanceString(["violet", "grey", "white", "grey", "none"])
        self.assertEquals("78900 Mohms +/- 20%", expected)
        
    