from .cipher import Cipher

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
