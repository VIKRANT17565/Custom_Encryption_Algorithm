
class customEncryption:
    # mores code
    __moresCode = {
        'a': '01', 'b': '1000', 'c': '1010', 'd': '100', 'e': '0',
        'f': '0010', 'g': '110', 'h': '0000', 'i': '00', 'j': '0111',
        'k': '101', 'l': '0100', 'm': '11', 'n': '10', 'o': '111',
        'p': '0110', 'q': '1101', 'r': '010', 's': '000', 't': '1',
        'u': '001', 'v': '0001', 'w': '011', 'x': '1001', 'y': '1011',
        'z': '1100', '1': '01111', '2': '00111', '3': '00011', '4': '00001',
        '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110',
        '0': '11111', 
        ' ' : '000000', '_' : '111111','':''
    }

    def encryptBlockDvision(self, message, key=5):
        blockList = []
        for i in range(0, len(message), key):
            mes = '1' + message[i:i+key]
            blockList.append(mes)
        return blockList

    def padWith2(self, message, key=5):
        if len(message) % key != 0:
            message += '2' * (key - len(message) % key)
        return message

    def padWith0(self, message, key=5):
        # #print(message)
        if len(message) % key != 0:
            message = '0' * (key - len(message) % key) + message
        # #print(message)
        return message

    def ternaryToDecimal(self, ternary):
        decimal = 0
        power = len(ternary) - 1

        for digit in ternary:
            decimal += int(digit) * (3 ** power)
            power -= 1

        return str(decimal)

    def encrypt(self, message, key=5):
        # message to equevalent binary mores code
        encryptedMessage = ''
        for i in message:
            if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9') or i == ' ' or i == '_':
                encryptedMessage += str(self.__moresCode[i]) + '2'

        #print(encryptedMessage)
        paddedMessage = self.padWith2(encryptedMessage, key)
        #print(paddedMessage)
        blockList = self.encryptBlockDvision(paddedMessage, key)
        #print(blockList)

        decimalList = []
        for i in blockList:
            mes = self.ternaryToDecimal(i)
            decimalList.append(self.padWith0(mes, key))

        #print(decimalList)

        encryptedMessage = ''
        for i in decimalList:
            encryptedMessage += i

        return encryptedMessage

#######################################################################################################################

    def decimalToTernary(self, decimal):
        decimal = int(decimal)
        ternary = ""

        while decimal > 0:
            remainder = decimal % 3
            decimal //= 3
            ternary = str(remainder) + ternary

        return ternary if ternary != "" else "0"

    def decrypt(self, message, key=5):
        # message to list of block of decimal number
        blockList = []
        for i in range(0, len(message), key):
            blockList.append(message[i:i+key])

        # print(blockList)

        # convert list of block of decimal number to list of block of trinary number
        trinaryList = []
        for i in blockList:
            trinaryList.append(self.decimalToTernary(i))

        # print(trinaryList)

        # concatinate all block of trinary number to one string
        trinaryMessage = ''
        for i in trinaryList:
            trinaryMessage += i[1:]

        # print(trinaryMessage)

        # split the string when 2 is found
        trinaryMessage = trinaryMessage.split('2')

        # print(trinaryMessage)

        # refer morse code to get the original message
        decryptedMessage = ''
        for i in trinaryMessage:
            # print(i)
            decryptedMessage += list(self.__moresCode.keys()
                                     )[list(self.__moresCode.values()).index(i)]

        return decryptedMessage


obj = customEncryption()
m = input('Enter message: ')
k = int(input('Enter key: '))

encryptedText = obj.encrypt(m.lower(), k)
print("Encrypted text: ", encryptedText)

decryptedText = obj.decrypt(encryptedText, k)
print("Decrypted text: ", decryptedText)
