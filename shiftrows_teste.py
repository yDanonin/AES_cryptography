# assumindo que as matrizes já vão ser dividas em 4x4 (16 bytes)

m = [['20', '4d', '8f', '92'],
    ['ef', '9f', '43', 'a8'],
    ['b7', 'ef', 'b7', 'fb'],
    ['40', 'f9', '51', '92']]

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

print(m)
