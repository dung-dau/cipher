import unittest
from FileParser import FileParser as fp

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

    def testGetResult(self):
        testCipher = Cipher("testFiles/Result.txt", 0)
        result = testCipher.getResult()
        expected = "Result"
        self.assertEqual(expected, result)

    def testSingleWordEncrypt(self):
        testCipher = Cipher("testFiles/Single.txt", 3)
        result = testCipher.getResult()
        expected = "Zrug"
        self.assertEqual(expected, result)

    def testMultipleWordEncrypt(self):
        testCipher = Cipher("testFiles/Multiple.txt", 4)
        result = testCipher.getResult()
        expected = "Qypxmtpi asvh irgvctxmsr"
        self.assertEqual(expected, result)

    def testSingleNewLine(self):
        testCipher = Cipher("testFiles/SingleNewLine.txt", 9)
        result = testCipher.getResult()
        expected = "\n"
        self.assertEqual(expected, result)

    def testMultipleNewLines(self):
        testCipher = Cipher("testFiles/MultipleNewLines.txt", 7)
        result = testCipher.getResult()
        expected = "\n\n\n\n"
        self.assertEqual(expected, result)

    def testMultipleLinesWithWords(self):
        testCipher = Cipher("testFiles/MultipleLines.txt", 1)
        result = testCipher.getResult()
        expected = "Uijt jt uif gjstu mjof\nUifsf jt bopuifs mjof\nUijt jt uif gjobm mjof"
        self.assertEqual(expected, result)

    def testSingleSpecialCharacters(self):
        testCipher = Cipher("testFiles/Exclamation.txt", 5)
        result = testCipher.getResult()
        expected = "Ymnx nx fs jchqfrfynts knqj!"
        self.assertEqual(expected, result)
        
    def testMultipleLinesSpecialCharacters(self):
        testCipher = Cipher("testFiles/MultipleLinesCharacters.txt", 2)
        result = testCipher.getResult()
        expected = "Yjgp urgcmkpi cnqwf,\naqw rwpevwcvg\neqpuvcpvna-ykvj dqfa\nncpiwcig.\n"
        self.assertEqual(expected, result)

    def testZeroShift(self):
        testCipher = Cipher("testFiles/Basic.txt", 0)
        result = testCipher.getResult()
        expected = "This is a basic file"
        self.assertEqual(expected, result)

    def testNumbers(self):
        testCipher = Cipher("testFiles/Number.txt", 11)
        result = testCipher.getResult()
        expected = "2.03% zq dzwlc pypcrj qczx esp Dlslcl td pyzfrs ez azhpc esp hszwp zq Pfczap\n"
        self.assertEqual(expected, result)

    # def testMultipleLinesWithNumbers(self):
    #     testCipher = Cipher("testFiles/MultipleLinesWithNumbers.txt", 6)
    #     result = testCipher.getResult()
    #     expected = "Znk Atozkj Yzgzky ul Gskxoig, oy g iuatzxe ruigzkj ot Tuxzn Gskxoig.\n"
    #     expected += "Oz iutyoyzy ul 50 yzgzky, g lkjkxgr joyzxoiz, lobk sgpux atotiuxvuxgzkj\n"
    #     expected += "zkxxozuxoky, 326 Otjogt xkykxbgzouty, gtj yusk sotux vuyykyyouty.\n"
    #     expected += "Gz 3.8 sorrout ywagxk sorky (9.8 sorrout ywagxk qoruskzkxy), oz oy znk\n"
    #     expected += "cuxrj'y znoxj- ux luaxzn-rgxmkyz iuatzxe he zuzgr gxkg."
    #     self.assertEqual(expected, result)

    # def testNegativeShift(self):
    #     try:
    #         testCipher = Cipher("testFiles/Basic.txt", -1)
    #     except ValueError:
    #         self.assertEqual(True, True)
    #     else:
    #         self.assertEqual(False, True)


    # def testVariousCapitalization(self):

    #def testIncorrectFileFormat(self)




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
        return self.result

if __name__ == '__main__':
    unittest.main() 
