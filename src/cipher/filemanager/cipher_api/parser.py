# import unittest
from cipher import Cipher

class Parser:
    def __init__(self, *args):
        self.NonEncryptedText = args[0]
        self.shift = args[1]
        self.parseText(self.NonEncryptedText)
        self.cipher = Cipher(self.NonEncryptedText, self.shift)
        self.EncryptedText = self.cipher.getEncryptedText()

    def parseText(self, text):
        print("parsing text...")
            
    def fileIsEmpty(self, file):
        firstChar = file.read(1)
        if not firstChar:
            return True
        return False

    def fileContainsNumbers(self):
        return False

    def fileContainsSpecialCharacters(self):
        return False

    def getNonEncryptedText(self):
        return self.text

    def getEncryptedText(self):
        return self.EncryptedText

# class ParserTest(unittest.TestCase):
#     def testBasicFile(self):
#         try:
#             testParser = Parser("testFiles/Basic.txt")
#         except:
#             self.assertEqual(True, False)
#         else:
#             self.assertEqual(True, True)

#     def testNonExistantFile(self):
#         try:
#             testParser = Parser("testFiles/NonExistant.txt")
#         except FileNotFoundError:
#             self.assertEqual(True, True)
#         else:
#             self.assertEqual(False, True)

#     def testEmptyFile(self):
#         testParser = Parser("testFiles/Empty.txt")
#         file = open("testFiles/Empty.txt")
#         expected = True
#         result = testParser.fileIsEmpty(file)
#         file.close()
#         self.assertEqual(expected, result)

#     def testEmptyConstructor(self):
#         try:
#             testParser = Parser()
#         except ValueError:
#             self.assertEqual(True, True)
#         else:
#             self.assertEqual(False, True)

#     def testMultipleArugmentsConstructor(self):
#         try:
#             testParser = Parser("test1", "test2")
#         except ValueError:
#             self.assertEqual(True, True)
#         else:
#             self.assertEqual(False, True)

#     def testExclamationMark(self):
#         testParser = Parser("testFiles/Exclamation.txt")
#         expected = True
#         result = testParser.fileContainsSpecialCharacters()
#         self.assertEqual(expected, result)

#     def testFileContainsNumbers(self):
#         testParser = Parser("testFiles/Number.txt")
#         expected = True
#         result = testParser.fileContainsNumbers()
#         self.assertEqual(expected, result)

#     def testGetContents(self):
#         testParser = Parser("testFiles/Basic.txt")
#         expected = "This is a basic file"
#         result = testParser.getContents()
#         self.assertEqual(expected, result)

#     def testMultipleLineFile(self):
#         testParser = Parser("testFiles/MultipleLines.txt")
#         expected = "This is the first line.\n", "There is another line!\n", "This is the final line...."
#         result = testParser.getContents()
#         self.assertEqual(expected, result)

# if __name__ == '__main__':
#     unittest.main() 
