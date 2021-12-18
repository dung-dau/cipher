import unittest
from FileParser import FileParser as fp

class CipherTest(unittest.TestCase):
    def testConstructor(self):
        try:
            testCipher = Cipher("testFiles/Basic.txt", 3)
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

    def testSingleArugmentsConstructor(self):
        try:
            testCipher = Cipher("testFiles/Basic.txt")
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def testGetResult(self):
        testCipher = Cipher("testFiles/Result.txt", 0)
        result = testCipher.getResult()
        expected = "Result"
        self.assertEqual(expected, result)

    def testSingleWordEncrypt(self):
        testCipher = Cipher("testFiles/Single.txt", 3)
        testCipher.encrypt(testCipher.fileContents, 3)
        result = testCipher.getResult()
        expected = "Zrug"
        self.assertEqual(expected, result)

class Cipher:
    def encrypt(self, text, shift):
        result = ""
        for i in range(len(text)):
            char = text[i]      
            if (char.isupper()):
                result += chr((ord(char) + shift-65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift-97) % 26 + 97)
            else:
                result += char
        return result

    def __init__(self, *args):
        if len(args) != 2:
            raise ValueError
        else:
            self.parser = fp(args[0])
            self.fileContents = self.parser.getContents()
            self.result = self.encrypt(self.fileContents, args[1])

    def getResult(self):
        print("Returning: "+self.result)
        return self.result

if __name__ == '__main__':
    unittest.main() 
