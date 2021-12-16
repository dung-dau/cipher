import unittest
from FileParser import FileParser as fp
from Encryptable import Encryptable

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

    def testSingleWordEncrypt(self):
        testCipher = Cipher("testFiles/Single.txt")
        testCipher.encrypt()
        file = open("testFiles", "r")
        result = file.readLines()
        expected = [Yrug]
        assertEqual(expected, result)

class Cipher:
    def __init__(self, *args):
        if len(args) != 2:
            raise ValueError
        else:
            parser = fp(args[0])
            fileContents = parser.getContents()
            for i in range(0, len(contents)):
                encrypt(fileContents[i], args[1])

    def encrypt(text, shift):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
        # Encrypt uppercase characters in plain text
      
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char.islower():
            result += chr((ord(char) + shift-97) % 26 + 97)
        else:
            result += char
        return result



if __name__ == '__main__':
    unittest.main() 
