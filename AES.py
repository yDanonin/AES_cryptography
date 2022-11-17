import random
import re

subBox = [
  [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
  [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
  [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
  [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
  [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
  [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
  [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
  [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
  [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
  [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
  [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
  [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
  [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
  [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
  [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
  [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],
]

invSubBox = [
  [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
  [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
  [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
  [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
  [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
  [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
  [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
  [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
  [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
  [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
  [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
  [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
  [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
  [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
  [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
  [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D],
]

Rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]


def encrypt(matrix, key):
  state = addRoundKey(matrix, key)
  keySchedule = keyExpansion(key)

  # print(keySchedule)
  for i in range(9):
    state = subBytes(state)
    state = shiftRows(state)
    state = mixColumns(state)
    state = addRoundKey(state, keySchedule[i])

  state = subBytes(state)
  state = shiftRows(state)
  state = addRoundKey(state, keySchedule[9])
  return state

def decrypt(matrix, key):
  keySchedule = keyExpansion(key)

  state = addRoundKey(matrix, keySchedule[9])

  for i in range(9):
    state = invShiftRows(state)
    state = invSubBytes(state)
    state = addRoundKey(state, keySchedule[8-i])
    state = invMixColumn(state)
  
  state = invShiftRows(state)
  state = invSubBytes(state)
  state = addRoundKey(state, key)

  return state

def addRoundKey(m, n):
  return [[hex(int(m[i][j], 16) ^ int(n[i][j], 16)) for j in range(4)] for i in range(4)]

def keyExpansion(key):
  keySchedule = []
  for k in range(10):
    keyLastColumn = [key[0][3], key[1][3], key[2][3], key[3][3]]
    x = keyLastColumn.pop(0)
    keyLastColumn.append(x)
    newKeyLastColumn = subBytes([keyLastColumn])
    newKeyLastColumn = newKeyLastColumn[0]

    newFirstColumn = [hex(int(key[0][0], 16) ^ int(newKeyLastColumn[0], 16) ^ Rcon[0][k]),
                      hex(int(key[1][0], 16) ^ int(newKeyLastColumn[1], 16) ^ Rcon[1][k]),
                      hex(int(key[2][0], 16) ^ int(newKeyLastColumn[2], 16) ^ Rcon[2][k]),
                      hex(int(key[3][0], 16) ^ int(newKeyLastColumn[3], 16) ^ Rcon[3][k])]


    newKey = [[newFirstColumn[0], 0x00, 0x00, 0x00], [newFirstColumn[1], 0x00, 0x00, 0x00], [newFirstColumn[2], 0x00, 0x00, 0x00], [newFirstColumn[3], 0x00, 0x00, 0x00]]

    for i in range(1, 4):
      newKey[0][i] = hex(int(newKey[0][i-1], 16) ^ int(key[0][i], 16))
      newKey[1][i] = hex(int(newKey[1][i-1], 16) ^ int(key[1][i], 16))
      newKey[2][i] = hex(int(newKey[2][i-1], 16) ^ int(key[2][i], 16))
      newKey[3][i] = hex(int(newKey[3][i-1], 16) ^ int(key[3][i], 16))

    key = newKey
    keySchedule.append(key)

  return keySchedule

# conversions HexTo
def hexToDecimal(valueInHex: str) -> int: 
  return int(valueInHex, 16)

def hexToBin(valueInHex: str) -> str:
  return bin(int(valueInHex, 16))[2:]

# conversions binTo
def binToHex(valueInBin: int) -> str:
  return hex(int(valueInBin, 2))

# conversions strTo
# This function return an array of bytes
def strToBin(text: str) -> list:
  l = [ord(i) for i in text]
  return [str(bin(k)[2:]).zfill(8) for k in l]

def genKey():
  return [[hex(random.randrange(0, 255)) for c in range(4)] for i in range(4)]

def createMatrix(hexList):
  matrix = []
  for i in range(16):
    byte = hexList[i]
    if i % 4 == 0:
      matrix.append([byte])
    else:
      matrix[i // 4].append(byte)
  return matrix


def prepareAListOfMatrices(listOfHex):
  while len(listOfHex) % 16 != 0:
    listOfHex.append("0x00") 
  listOfMatrix = []
  ini = 0
  # print(len(listOfHex) // 16)
  for i in range(1, (len(listOfHex) // 16)+1):
    listOfMatrix.append(createMatrix(listOfHex[ini:16*i+1]))
    ini = 16*i
  
  return listOfMatrix


# TODO: review this function 
def mulBy02(num):
  if num < 0x80:
    res = (num << 1)
  else:
    res = (num << 1) ^ 0x1b

  return res % 0x100

# TODO: review this function 
def mulBy03(num):
  
  return (mulBy02(num) ^ num)

# TODO: review this function 
def mulBy09(num):
    return mulBy02(mulBy02(mulBy02(num))) ^ num

# TODO: review this function 
def mulBy0b(num):
    return mulBy02(mulBy02(mulBy02(num))) ^ mulBy02(num) ^ num

# TODO: review this function 
def mulBy0d(num):
    return mulBy02(mulBy02(mulBy02(num))) ^ mulBy02(mulBy02(num)) ^ num

# TODO: review this function 
def mulBy0e(num):
    return mulBy02(mulBy02(mulBy02(num))) ^ mulBy02(mulBy02(num)) ^ mulBy02(num)



def subBytes(hexadecimal: list) -> list:
  for i in range(len(hexadecimal)):
    for j in range(len(hexadecimal[i])):
      v = hexadecimal[i][j][2:]
      if(len(v) == 1):
        v = "0"+v
      hexadecimal[i][j] = hex(subBox[hexToDecimal(v[0])][hexToDecimal(v[1])])

  return hexadecimal


def shiftRows(m):
  x = m[1].pop(0)
  m[1].append(x)

  x = m[2].pop(0)
  m[2].append(x)
  y = m[2].pop(0)
  m[2].append(y)

  x = m[3].pop(0)
  m[3].append(x)
  y= m[3].pop(0)
  m[3].append(y)
  z= m[3].pop(0)
  m[3].append(z)

  return m


def mixColumns(matrix):
  R = [[0x00 for k in range(4)] for i in range(4)]
  for c in range(4):
    R[0][c] = hex(mulBy02(int(matrix[0][c], 16)) ^ mulBy03(int(matrix[1][c], 16)) ^ int(matrix[2][c], 16) ^ int(matrix[3][c], 16))
    R[1][c] = hex(int(matrix[0][c], 16) ^ mulBy02(int(matrix[1][c], 16)) ^ mulBy03(int(matrix[2][c], 16)) ^ int(matrix[3][c], 16))
    R[2][c] = hex(int(matrix[0][c], 16) ^ int(matrix[1][c], 16) ^ mulBy02(int(matrix[2][c], 16)) ^ mulBy03(int(matrix[3][c], 16)))
    R[3][c] = hex(mulBy03(int(matrix[0][c], 16)) ^ int(matrix[1][c], 16) ^ int(matrix[2][c], 16) ^ mulBy02(int(matrix[3][c], 16)))

  return R


def invSubBytes(hexadecimal):
  for i in range(len(hexadecimal)):
    for j in range(len(hexadecimal[i])):
      v = hexadecimal[i][j][2:]
      if(len(v) == 1):
        v = "0"+v
      hexadecimal[i][j] = hex(invSubBox[hexToDecimal(v[0])][hexToDecimal(v[1])])

  return hexadecimal


def invShiftRows(m):
  x = m[1].pop(3)
  m[1].insert(0, x)

  x = m[2].pop(3)
  m[2].insert(0, x)
  y = m[2].pop(3)
  m[2].insert(0, y)

  x = m[3].pop(3)
  m[3].insert(0, x)
  y= m[3].pop(3)
  m[3].insert(0, y)
  z= m[3].pop(3)
  m[3].insert(0, z)

  return m


def invMixColumn(matrix):
  R = [[0x00 for k in range(4)] for i in range(4)]

  for i in range(4):
    R[0][i] = hex(mulBy0e(int(matrix[0][i], 16)) ^ mulBy0b(int(matrix[1][i], 16)) ^ mulBy0d(int(matrix[2][i], 16)) ^ mulBy09(int(matrix[3][i], 16)))
    R[1][i] = hex(mulBy09(int(matrix[0][i], 16)) ^ mulBy0e(int(matrix[1][i], 16)) ^ mulBy0b(int(matrix[2][i], 16)) ^ mulBy0d(int(matrix[3][i], 16)))
    R[2][i] = hex(mulBy0d(int(matrix[0][i], 16)) ^ mulBy09(int(matrix[1][i], 16)) ^ mulBy0e(int(matrix[2][i], 16)) ^ mulBy0b(int(matrix[3][i], 16)))
    R[3][i] = hex(mulBy0b(int(matrix[0][i], 16)) ^ mulBy0d(int(matrix[1][i], 16)) ^ mulBy09(int(matrix[2][i], 16)) ^ mulBy0e(int(matrix[3][i], 16)))

  return R
  


'''
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  from now on they are just functions for a test system =)
'''


def options():
  print("Você deseja criptografar ou descriptografar uma mensagem?")
  print("Digite 1 para criptografar, 2 para descriptografar ou 0 para encerrar o programa")
  choice = input()
  if (not (choice in ['0', '1', '2'])):
    print("Você precisa escolher uma função válida digitanto 0, 1 ou 2")
    return options()
  else:
    return choice

def keyRules(key):
  if len(key) > 16:
    print("Entre com uma chave menor:")
    key = input()
    return keyRules(key)
  else:
    for char in key:
      if ord(char) > 0xff:
        print("Cada caracter tem que ter no máximo 1 byte!")
        print("Entre com uma nova chave:")
        key = input()
        return keyRules(key)
    arrayKey = [binToHex(i) for i in strToBin(key)]
    while len(arrayKey) % 16 != 0:
      arrayKey.append("0x00")
    #print(arrayKey)
    return key

def textRules(text):
  for char in text:
    if ord(char) > 0xff:
      print("Cada caracter tem que ter no máximo 1 byte")
      print("Escolha uma nova mensagem a ser criptografada:")
      text = input()
      return textRules(text)
  return text

def tryToCreateAFile(fileName):
  try:
    f = open(fileName+".bin", "x")
    return f
  except Exception as e:
    print("Ocorreu um erro ao tentar criar um arquivo com esse nome.")
    print("O erro é:", e)
    print("\nTente criar um arquivo com um nome diferente!")
    newFileName = input("Digite o nome do arquivo: ")
    return tryToCreateAFile(newFileName)

def tryToOpenAFile(fileName):
  try:
    f = open(fileName+".bin", "rb")
    return f
  except Exception as e:
    print("Ocorreu um erro ao tentar ler um arquivo com esse nome.")
    print("Lembre-se que não precisa da extensão do arquivo, só são lidos arquivos .bin")
    print("O erro é:", e)
    print("\nTente criar um arquivo com um nome diferente")
    newFileName = input("Digite o nome do arquivo: ")
    return tryToOpenAFile(newFileName)

def infoAboutTheKey(info):
  if info not in ['1', '2']:
    print("Você tentou uma opção inválida, tente novamente com um dos valores válidos:")
    info = input()
    return infoAboutTheKey(info)
  return info
# to test
def main():
  #hexList = [binToHex(i) for i in strToBin("Testando AES AQUI NA SALA AO VIVO")]

  while True:
    choice = options()
    if (choice == '0'):
      break
    elif (choice == '1'):
      print("Você deseja que nós geremos a sua key? [Sim - Nao]")
      inp = input().lower()
      if(inp == 's' or inp == "sim" or inp == 'y' or inp == "yes"):
        key = genKey()
        keyValue = ""
        for i in key:
          for j in i:
            keyValue += j
        print("\nA sua key é: {}\n".format(keyValue))
      else:
        print("Digite a sua key:")
        value = input()
        key = createMatrix(keyRules(value))
      print("Digite aqui o texto que deseja criptografar:")
      inputValue = input()
      text = textRules(inputValue)
      hexList = [binToHex(i) for i in strToBin(text)]
      listOfBytesArray = prepareAListOfMatrices(hexList)
      encryptedText = [encrypt(matrix, key) for matrix in listOfBytesArray]
      cipher = ""
      for i in range(len(encryptedText)):
        for l in range(len(encryptedText[i])):
          cipher += bin(int(encryptedText[i][l][0], 16))+" "
          cipher += bin(int(encryptedText[i][l][1], 16))+" "
          cipher += bin(int(encryptedText[i][l][2], 16))+" "
          cipher += bin(int(encryptedText[i][l][3], 16))+" "
      print("\nAgora nessa estapa você deve informar o nome do arquivo que salvará o texto criptografado.")
      print("\nO nome não deverá conter a extensão do arquivo, pois por padrão será .bin")
      fileName = input("Digite o nome do arquivo: ")
      f = tryToCreateAFile(fileName)
      f.write(cipher)
      f.close()

      print("\nTexto criptografado com sucesso =)\n")

    else: 
      print("\nJá que deseja descriptografar a mensagem, é necessário antes se certificar de alguns passos.\n")
      print("Passo 1: se certifique que o texto criptografado está em formato .bin na mesma pasta do programa")
      print("Passo 2: Você deve saber a chave criptográfica\n")
      print("Tendo esses dois passos certo podemos começar o programa.\n")
      print("...")
      print("\nAntes de tudo precisamos saber se a chave que vai ser informada foi gerada por nós.")
      print("Precisamos dessa informação pois se a resposta for afirmativa, então trataremos a entrada da key já em hexadecimal.\n")
      print("Digite 1 para SIM ou 2 para NÃO")
      value = input()
      info = infoAboutTheKey(value)
      print()
      if info == '1':
        key = input("Digite a sua chave: ")
        key = key.split("0x")
        keyInList = [hex(int(key[i], 16)) for i in range(1, len(key))]
        #print(keyInList)
        key = createMatrix(keyInList)
      else:
        print("Digite a sua chave:")
        value = input()
        key = createMatrix(keyRules(value))

      print("Agora digite o nome do arquivo em que está o texto criptografado:")
      fileName = input()
      f = tryToOpenAFile(fileName)
      data = f.read().split()
      # print(data)
      hexList = [hex(int(i, 2)) for i in data]
      # print(hexList)
      listOfMatrices = prepareAListOfMatrices(hexList)
      result = []
      # print(listOfMatrices)
      for matrix in listOfMatrices:
        result.append(decrypt(matrix, key))
      #print(result)
      message = ""
      for i in range(len(result)):
        for l in range(len(result[i])):
          message += chr(int(result[i][l][0], 16))
          message += chr(int(result[i][l][1], 16))
          message += chr(int(result[i][l][2], 16))
          message += chr(int(result[i][l][3], 16))

      print("\nA sua mensagem descriptografada é: {}\n".format(message))

main()