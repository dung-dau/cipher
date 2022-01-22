class Cipher:
    def __init__(self, *args):
        self.encryptedText = self.encrypt(args[0], args[1])

    def encrypt(self, text, shift):
        text = ""
        for i in range(len(text)):
            char = text[i]      
            if (char.isupper()):
                text += chr((ord(char) + shift-65) % 26 + 65)
            elif char.islower():
                text += chr((ord(char) + shift-97) % 26 + 97)
            else:
                text += char
        return text

    def getEncryptedText(self):
        return self.text