matrixHex = [[0x04, 0xe0, 0x48, 0x28],
             [0x66, 0xcb, 0xf8, 0x06],
             [0x81, 0x19, 0xd3, 0x26],
             [0xe5, 0x9a, 0x7a, 0x4c]]   
    
exampleRoundKey = [[0xa0, 0x88, 0x23, 0x2a],
              [0xfa, 0x54, 0xa3, 0x6c],
              [0xfe, 0x2c, 0x39, 0x76],
              [0x17, 0xb1, 0x39, 0x05]]
              
roundedMatrixHex = [[],[],[],[]]

for i in range(4):
    for j in range(4):
        roundedMatrixHex[i].append(hex(matrixHex[i][j] ^ exampleRoundKey[i][j]))
print(roundedMatrixHex)