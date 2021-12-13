import unittest

class FileParser:
    def __init__(self, *args):

        if len(args) != 1:
            raise ValueError
        else:
            file = open(args[0], "r")
            self.fileIsEmpty(file)
            file.readLines()
            file.close()

    def fileIsEmpty(self, file):
        firstChar = file.read(1)
        if not firstChar:
            return True
        return False



class FileParserTest(unittest.TestCase):
    def testBasicFile(self):
        try:
            testParser = FileParser("testFiles/Basic.txt")
        except:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def testNonExistantFile(self):
        try:
            testParser = FileParser("testFiles/NonExistant.txt")
        except FileNotFoundError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def testEmptyFile(self):
        testParser = FileParser("testFiles/Empty.txt")
        file = open("testFiles/Empty.txt")
        expected = True;
        result = testParser.fileIsEmpty(file)
        file.close()
        self.assertEqual(expected, result)

    def testEmptyConstructor(self):
        try:
            testParser = FileParser()
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def testMultipleArugmentsConstructor(self):
        try:
            testParser = FileParser("test1", "test2")
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def testExclamationMark(self):
        testParser = FileParser("testFiles/ExclamationMark.txt")
        expected = True
        result = testParser.fileContainsSpecialCharacters()
        self.assertEqual(expected, result)

    def testFileContainsNumbers(self):
        testParser = FileParser("testFiles/Number.txt")
        expected = True
        result = testParser.fileContainsNumbers()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main() 
