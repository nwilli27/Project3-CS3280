
import unittest
from resistor import validateColorsList

class TestValidateColorsList(unittest.TestCase):
    
    #VALID # of Bands and correct tolerance, multiplier, and digit values
    
    def test4ValidColorsBands(self):
        listOfColors = ["brown", "red", "blue", "violet"]
        validateColorsList(listOfColors)
        
    def test5ValidColorBands(self):
        listOfColors = ["brown", "red", "blue", "violet", "green"]
        validateColorsList(listOfColors)    
    
    #INVALID # of Bands
            
    def test3ColorBands(self):
        listOfColors = ["brown", "red", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("There should only be 4 or 5 bands" in str(error.exception))     
            
    def test6ColorBands(self):
        listOfColors = ["brown", "red", "black", "blue", "orange", "red"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("There should only be 4 or 5 bands" in str(error.exception))
            
    #INVALID color band
    
    def testInvalidColorLimegreen(self):
        listOfColors = ["brown", "red", "black", "limegreen"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("limegreen is not a valid resistor color band" in str(error.exception))      
            
    #INVALID significant digit bands
    
    def testBandWithNoSignificantDigitGold(self):
        listOfColors = ["gold", "red", "green", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("gold does not contain a significant figure digit" in str(error.exception))   
        
    def testBandWithNoSignificantDigitSilver(self):
        listOfColors = ["silver", "red", "green", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("silver does not contain a significant figure digit" in str(error.exception))        
        
    def testBandWithNoSignificantDigitNone(self):
        listOfColors = ["none", "red", "green", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("none does not contain a significant figure digit" in str(error.exception))
    
    #INVALID multiplier band
    
    def testInvalidMultiplierBandNone(self):
        listOfColors = ["brown", "red", "none", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("none does not contain a multiplier" in str(error.exception))
        
    #INVALID tolerance bands
    
    def testInvalidToleranceBandBlack(self):
        listOfColors = ["brown", "red", "orange", "black"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("black does not contain a tolerance value" in str(error.exception))
    
    def testInvalidToleranceBandOrange(self):
        listOfColors = ["brown", "red", "orange", "orange"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("orange does not contain a tolerance value" in str(error.exception))
    
    def testInvalidToleranceBandYellow(self):
        listOfColors = ["brown", "red", "orange", "yellow"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("yellow does not contain a tolerance value" in str(error.exception))
    
    def testInvalidToleranceBandWhite(self):
        listOfColors = ["brown", "red", "orange", "white"]
        with self.assertRaises(ValueError) as error: validateColorsList(listOfColors)
        self.assertTrue("white does not contain a tolerance value" in str(error.exception))
        
    