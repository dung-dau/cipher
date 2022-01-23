import unittest
from parser.cipher import Cipher

class CipherTest(unittest.TestCase):
    def testGetEncryptedText(self):
        testFile = open("testFiles/Basic.txt")
        testCipher = Cipher(testFile.read(), 0)
        result = testCipher.getEncryptedText()
        expected = "This is a basic file"
        testFile.close()
        self.assertEqual(expected, result)

    def testSingleWordEncrypt(self):
        testFile = open("testFiles/Single.txt")
        testCipher = Cipher(testFile.read(), 3)
        result = testCipher.getEncryptedText()
        expected = "Zrug"
        self.assertEqual(expected, result)
        testFile.close()

    def testMultipleWordEncrypt(self):
        testFile = open("testFiles/Multiple.txt")
        testCipher = Cipher(testFile.read(), 4)
        result = testCipher.getEncryptedText()
        expected = "Qypxmtpi asvh irgvctxmsr"
        self.assertEqual(expected, result)
        testFile.close()

    def testSingleNewLine(self):
        testFile = open("testFiles/SingleNewLine.txt")
        testCipher = Cipher(testFile.read(), 9)
        result = testCipher.getEncryptedText()
        expected = "\n"
        self.assertEqual(expected, result)
        testFile.close()

    def testMultipleNewLines(self):
        testFile = open("testFiles/MultipleNewLines.txt")
        testCipher = Cipher(testFile.read(), 7)
        result = testCipher.getEncryptedText()
        expected = "\n\n\n\n"
        self.assertEqual(expected, result)
        testFile.close()

    def testMultipleLinesWithWords(self):
        testFile = open("testFiles/MultipleLines.txt")
        testCipher = Cipher(testFile.read(), 1)
        result = testCipher.getEncryptedText()
        expected = "Uijt jt uif gjstu mjof\nUifsf jt bopuifs mjof\nUijt jt uif gjobm mjof"
        self.assertEqual(expected, result)
        testFile.close()

    def testSingleSpecialCharacters(self):
        testFile = open("testFiles/Exclamation.txt")
        testCipher = Cipher(testFile.read(), 5)
        result = testCipher.getEncryptedText()
        expected = "Ymnx nx fs jchqfrfynts knqj!"
        self.assertEqual(expected, result)
        testFile.close()

    def testMultipleLinesSpecialCharacters(self):
        testFile = open("testFiles/MultipleLinesCharacters.txt")
        testCipher = Cipher(testFile.read(), 2)
        result = testCipher.getEncryptedText()
        expected = "Yjgp urgcmkpi cnqwf,\naqw rwpevwcvg\neqpuvcpvna-ykvj dqfa\nncpiwcig.\n"
        self.assertEqual(expected, result)
        testFile.close()

    def testNumbers(self):
        testFile = open("testFiles/Number.txt")
        testCipher = Cipher(testFile.read(), 11)
        result = testCipher.getEncryptedText()
        expected = "2.03% zq dzwlc pypcrj qczx esp Dlslcl td pyzfrs ez azhpc esp hszwp zq Pfczap\n"
        self.assertEqual(expected, result)
        testFile.close()

    # def testMultipleLinesWithNumbers(self):
    #     testCipher = Cipher("testFiles/MultipleLinesWithNumbers.txt", 6)
    #     text = testCipher.gettext()
    #     expected = "Znk Atozkj Yzgzky ul Gskxoig, oy g iuatzxe ruigzkj ot Tuxzn Gskxoig.\n"
    #     expected += "Oz iutyoyzy ul 50 yzgzky, g lkjkxgr joyzxoiz, lobk sgpux atotiuxvuxgzkj\n"
    #     expected += "zkxxozuxoky, 326 Otjogt xkykxbgzouty, gtj yusk sotux vuyykyyouty.\n"
    #     expected += "Gz 3.8 sorrout ywagxk sorky (9.8 sorrout ywagxk qoruskzkxy), oz oy znk\n"
    #     expected += "cuxrj'y znoxj- ux luaxzn-rgxmkyz iuatzxe he zuzgr gxkg."
    #     self.assertEqual(expected, text)

    # def testNegativeShift(self):
    #     try:
    #         testCipher = Cipher("testFiles/Basic.txt", -1)
    #     except ValueError:
    #         self.assertEqual(True, True)
    #     else:
    #         self.assertEqual(False, True)


    # def testVariousCapitalization(self):

    # def testIncorrectFileFormat(self)
