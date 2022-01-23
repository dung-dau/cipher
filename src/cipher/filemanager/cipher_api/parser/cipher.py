class Cipher:
    encryptedText=""
    def __init__(self, *args):
        self.encryptedText = self.encrypt(args[0], args[1])

    def encrypt(self, text, shift):
        res = ""
        for i in range(0,len(text)):
            char = text[i]      
            if (char.isupper()):
                res += chr((ord(char) + shift-65) % 26 + 65)
            elif char.islower():
                res += chr((ord(char) + shift-97) % 26 + 97)
            else:
                res += char
        return res

    def getEncryptedText(self):
        return self.encryptedText