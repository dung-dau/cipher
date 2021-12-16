import unittest

class FileParserTest(unittest.TestCase):
	def testBasicFile(self):
		testParser = FileParser("testFiles/Basic.txt")
		expected = not None
		self.assertEqual(expected, testParser)

	def testNonExistantFile(self):
		testParser = FileParser("testFiles/NonExistant.txt")
		expected = None
		self.assertEqual(expected, testParser)

	def testEmptyFile(self):
		testParser = FileParser("testFiles/Empty.txt")
		expected = True;
		result = testParser.fileIsEmpty()
		self.assertEqual(expected, result)

	def testEmptyConstructor(self):
		testParser = FileParser()
		expected = None
		self.assertEqual(expected, testParser)

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
