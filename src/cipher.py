import unittest
from FileParser import FileParser as fp
import Encryptable

class CipherTest(unittest.TestCase):
    def testConstructor(self):
        try:
            testParser = fp("testFiles/Basic.txt")
            testCipher = Cipher(testParser)
        except:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def testEmptyConstructor(self):
        try:
            testCipher = Cipher()
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def testMultipleArugmentsConstructor(self):
        try:
            testCipher = Cipher("test1", "test2")
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

class Cipher:
    def __init__(self, *args):
        if len(args) != 1:
            raise ValueError

if __name__ == '__main__':
    unittest.main() 
