
import unittest
from resistor import validateColorsList

class TestValidateColorsList(unittest.TestCase):
    
    #VALID # of Bands
    
    def test4ColorsBands(self):
        listOfColors = ["brown", "red", "blue", "violet"]
        validateColorsList(listOfColors)
        
    def test5ColorBands(self):
        listOfColors = ["brown", "red", "blue", "violet"]
        validateColorsList(listOfColors)    
    
    #INVALID # of Bands
            
    def test3ColorBands(self):
        listOfColors = ["brown", "red", "black"]
        with self.assertRaises(ValueError):
            validateColorsList(listOfColors)
            
    def test6ColorBands(self):
        listOfColors = ["brown", "red", "black"]
        with self.assertRaises(ValueError):
            validateColorsList(listOfColors)
            
    #VALID color bands
    
    def test5ValidColors(self):
        listOfColors = ["black", "brown", "red", "orange", "yellow"]
        validateColorsList(listOfColors)
        
    #INVALID color bands
    
    def testInvalidColorLimegreen(self):
        listOfColors = ["brown", "red", "black", "limegreen"]
        with self.assertRaises(ValueError):
            validateColorsList(listOfColors)
    