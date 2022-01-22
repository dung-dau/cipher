import unittest
from cipher import Cipher

class CipherTest(unittest.TestCase):
    maxDiff = None
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

    def testGettext(self):
        testCipher = Cipher("testFiles/text.txt", 0)
        text = testCipher.gettext()
        expected = "text"
        self.assertEqual(expected, text)

    def testSingleWordEncrypt(self):
        testCipher = Cipher("testFiles/Single.txt", 3)
        text = testCipher.gettext()
        expected = "Zrug"
        self.assertEqual(expected, text)

    def testMultipleWordEncrypt(self):
        testCipher = Cipher("testFiles/Multiple.txt", 4)
        text = testCipher.gettext()
        expected = "Qypxmtpi asvh irgvctxmsr"
        self.assertEqual(expected, text)

    def testSingleNewLine(self):
        testCipher = Cipher("testFiles/SingleNewLine.txt", 9)
        text = testCipher.gettext()
        expected = "\n"
        self.assertEqual(expected, text)

    def testMultipleNewLines(self):
        testCipher = Cipher("testFiles/MultipleNewLines.txt", 7)
        text = testCipher.gettext()
        expected = "\n\n\n\n"
        self.assertEqual(expected, text)

    def testMultipleLinesWithWords(self):
        testCipher = Cipher("testFiles/MultipleLines.txt", 1)
        text = testCipher.gettext()
        expected = "Uijt jt uif gjstu mjof\nUifsf jt bopuifs mjof\nUijt jt uif gjobm mjof"
        self.assertEqual(expected, text)

    def testSingleSpecialCharacters(self):
        testCipher = Cipher("testFiles/Exclamation.txt", 5)
        text = testCipher.gettext()
        expected = "Ymnx nx fs jchqfrfynts knqj!"
        self.assertEqual(expected, text)
        
    def testMultipleLinesSpecialCharacters(self):
        testCipher = Cipher("testFiles/MultipleLinesCharacters.txt", 2)
        text = testCipher.gettext()
        expected = "Yjgp urgcmkpi cnqwf,\naqw rwpevwcvg\neqpuvcpvna-ykvj dqfa\nncpiwcig.\n"
        self.assertEqual(expected, text)

    def testZeroShift(self):
        testCipher = Cipher("testFiles/Basic.txt", 0)
        text = testCipher.gettext()
        expected = "This is a basic file"
        self.assertEqual(expected, text)

    def testNumbers(self):
        testCipher = Cipher("testFiles/Number.txt", 11)
        text = testCipher.gettext()
        expected = "2.03% zq dzwlc pypcrj qczx esp Dlslcl td pyzfrs ez azhpc esp hszwp zq Pfczap\n"
        self.assertEqual(expected, text)

    def testMultipleLinesWithNumbers(self):
        testCipher = Cipher("testFiles/MultipleLinesWithNumbers.txt", 6)
        text = testCipher.gettext()
        expected = "Znk Atozkj Yzgzky ul Gskxoig, oy g iuatzxe ruigzkj ot Tuxzn Gskxoig.\n"
        expected += "Oz iutyoyzy ul 50 yzgzky, g lkjkxgr joyzxoiz, lobk sgpux atotiuxvuxgzkj\n"
        expected += "zkxxozuxoky, 326 Otjogt xkykxbgzouty, gtj yusk sotux vuyykyyouty.\n"
        expected += "Gz 3.8 sorrout ywagxk sorky (9.8 sorrout ywagxk qoruskzkxy), oz oy znk\n"
        expected += "cuxrj'y znoxj- ux luaxzn-rgxmkyz iuatzxe he zuzgr gxkg."
        self.assertEqual(expected, text)

    def testNegativeShift(self):
        try:
            testCipher = Cipher("testFiles/Basic.txt", -1)
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)


    # def testVariousCapitalization(self):

    # def testIncorrectFileFormat(self)

if __name__ == '__main__':
    unittest.main() 