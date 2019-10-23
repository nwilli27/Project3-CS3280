
import unittest
from resistor import decodeSignificantFigures

class TestDecodeSignificantFigures(unittest.TestCase):
    
    def testGetDigitsInOrderOf5BandResistor(self):
        self.assertEquals(123, decodeSignificantFigures(["brown", "red", "orange", "green", "violet"]))
    
    def testGetDigitsInReverseOrderOf5BandResistor(self):
        self.assertEquals(321, decodeSignificantFigures(["orange", "red", "brown", "green", "violet"]))
        
    def testGetDigitsInOrderOf4BandResistor(self):
        self.assertEquals(56, decodeSignificantFigures(["green", "blue", "green", "violet"]))
    
    def testGetDigitsInReverseOrderOf4BandResistor(self):
        self.assertEquals(65, decodeSignificantFigures(["blue", "green", "green", "violet"]))

    def testGetDigitsWithLeadingBlackBand5Bands(self):
        self.assertEquals(23, decodeSignificantFigures(["black", "red", "orange", "green", "violet"]))

    def testGetDigitsWithLeadingBlackBand4Bands(self):
        self.assertEquals(2, decodeSignificantFigures(["black", "red", "green", "violet"]))

    def testGetDigitsWithBlackBand4Bands(self):
        self.assertEquals(20, decodeSignificantFigures(["red", "black", "green", "violet"]))

    def testGetDigitsWithBlackBand5Bands(self):
        self.assertEquals(200, decodeSignificantFigures(["red", "black", "black", "green", "violet"]))
    
