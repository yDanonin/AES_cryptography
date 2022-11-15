m = [[2, 3, 1, 1],            
     [1, 2, 3, 1],
     [1, 1, 2, 3],
     [3, 1, 1, 2]]

matrix = [[0xd4, 0xe0, 0xb8, 0x1e],
          [0xbf, 0xb4, 0x41, 0x27],
          [0x5d, 0x52, 0x11, 0x98],
          [0x30, 0xae, 0xf1, 0xe5]]




# def __mix_single_column(a):
#     # please see Sec 4.1.2 in The Design of Rijndael
#     t = a[0] ^ a[1] ^ a[2] ^ a[3]
#     u = a[0]
#     a[0] ^= t ^ xtime(a[0] ^ a[1])
#     a[1] ^= t ^ xtime(a[1] ^ a[2])
#     a[2] ^= t ^ xtime(a[2] ^ a[3])
#     a[3] ^= t ^ xtime(a[3] ^ u)
#     return a

# def __mix_columns(s):
#     return [__mix_single_column(s[i]) for i in range(4)]

# newMatrix = [ [hex(c) for c in l] for l in __mix_columns(matrix) ]

# print(newMatrix)
  

# def hexToBin(valueInHex: str) -> str:
#   return bin(int(valueInHex, 16))[2:]




def hexToBin(valueInHex: str):
  return bin(int(valueInHex, 16))[2:]

# def registerPosition(byte):
#   listIndex = []
#   for i in range(len(byte)):
#     if byte[i] == '1':
#       listIndex.append(7-i)
#   return listIndex

# print(bin(0b10 * 0b10000111)[2:])

byte1 = 0b11010100
byte2 = 0b00000010

byte3 = byte1*byte2

# print(hex(byte3 ^ 0b00000010))

# xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

# opt1 = 0x02 * 0xd4 >> 1
# opt2 = 0x03 * 0xbf >> 1
# opt3 = 0x01 * 0x5d
# opt4 = 0x01 * 0x30

# opt1 = 0x02 * int(bin(((0xd4 << 1) & 0xFF))[2:].zfill(8), 2) ^ 0b00011011
# opt2 = (int(bin(((0xbf << 1) & 0xFF))[2:].zfill(8), 2) * 0b10) ^ (0b01 * int(bin(((0xbf << 1) & 0xFF))[2:].zfill(8), 2)) 
# opt3 = 0x01 * 0x5d 
# opt4 = 0x01 * 0x30 

# print("OMG ", bin(int(bin(((0xd4 << 1) & 0xFF))[2:].zfill(8), 2)))
# print("opFinal: ", hex(opt1 ^ opt2 ^ opt3 ^ opt4 ))
# opt1 = int(bin(0x02), 2) * int(bin(0x87), 2) 
# opt1 = xtime(opt1)
# opt2 = int(bin(0x03), 2) * int(bin(0x6E), 2)
# opt2 = xtime(opt2)
# opt3 = int(bin(0x01), 2) * int(bin(0x46), 2)
# opt3 = xtime(opt3)
# opt4 = int(bin(0x01), 2) * int(bin(0xA6), 2)
# opt4 = xtime(opt4)


# opt1 = 0x01 * 0x87
# opt2 = 0x02 * 0x6E
# opt3 = 0x03 * 0x46
# opt4 = 0x01 * 0xA6

# print("opt1: ", bin(opt1))
# print("opt2: ", bin(opt2))
# print("opt3: ", bin(opt3))
# print("opt4: ", bin(opt4))

# print("bin: ", bin(opt1 ^ opt2 ^ opt3 ^ opt4))


# op1 = int(bin(2), 2) * int(hexToBin(matrix[0][0]), 2)
# op2 = int(bin(3), 2) * int(hexToBin(matrix[1][0]), 2)
# op3 = int(hexToBin(matrix[2][0]), 2)
# op4 = int(hexToBin(matrix[3][0]), 2)
# op5 = op1 ^ op2 ^ op3 ^ op4

# print(hex(op5))

  # return [(lambda a: 7-i if (a == '1'))(byte[i]) for i in range(len(byte))]

# def toDoXorOnPosition(firstList, secondList):
#   newPositionList

def mul_by_02(num):
  """The function multiplies by 2 in Galua space"""

  if num < 0x80:
    res = (num << 1)
  else:
    res = (num << 1) ^ 0x1b

  return res % 0x100

def mul_by_03(num):
  """The function multiplies by 3 in Galua space
  example: 0x03*num = (0x02 + 0x01)num = num*0x02 + num
  Addition in Galua field is oparetion XOR
  """
  return (mul_by_02(num) ^ num)


def mixColumn(): 
  R = [[0x00 for k in range(4)] for i in range(4)]
  for c in range(4):
    
    R[0][c] = mul_by_02(matrix[0][c]) ^ mul_by_03(matrix[1][c]) ^ matrix[2][c] ^ matrix[3][c]
    R[1][c] = matrix[0][c] ^ mul_by_02(matrix[1][c]) ^ mul_by_03(matrix[2][c]) ^ matrix[3][c]
    R[2][c] = matrix[0][c] ^ matrix[1][c] ^ mul_by_02(matrix[2][c]) ^ mul_by_03(matrix[3][c])
    R[3][c] = mul_by_03(matrix[0][c]) ^ matrix[1][c] ^ matrix[2][c] ^ mul_by_02(matrix[3][c])

  return R

r = mixColumn()

mix = [[hex(k) for k in i] for i in r]

print(mix)









# def listIndexOfBinary(galoisField, byteInHex):
#   byte = hexToBin(byteInHex)
#   listOfIndexes = []
#   for i in range(len(byte)):
#     if (byte[i] == '1'):
#       listOfIndexes.append(7-i)
#   if(galoisField == 1):
#     return listOfIndexes
  
#   galoisByte = bin(galoisField)[2:].zfill(8)
#   listOfGaloiIndexes = []
  
#   for k in range(len(galoisByte)):
#     if (galoisByte[i] == '1'):
#       listOfGaloiIndexes.append(7-k)

#   return [i+j for j in listOfIndexes for i in listOfGaloiIndexes]


  

