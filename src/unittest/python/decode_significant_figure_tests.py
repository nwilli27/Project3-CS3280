
import unittest
from resistor import decodeSignificantFigures

class TestDecodeSignificantFigures(unittest.TestCase):
    
    def testGetDigitsInOrderOf5BandResistor(self):
        self.assertEquals("123", decodeSignificantFigures(["brown", "red", "orange", "green", "violet"]))
    
    def testGetDigitsInReverseOrderOf5BandResistor(self):
        self.assertEquals("321", decodeSignificantFigures(["orange", "red", "brown", "green", "violet"]))
        
    def testGetDigitsInOrderOf4BandResistor(self):
        self.assertEquals("56", decodeSignificantFigures(["green", "blue", "green", "violet"]))
    
    def testGetDigitsInReverseOrderOf4BandResistor(self):
        self.assertEquals("65", decodeSignificantFigures(["blue", "green", "green", "violet"]))     
    