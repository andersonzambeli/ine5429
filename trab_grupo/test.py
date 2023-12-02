a = 1
b = 1
b2 = 1
k = 0
print(a)
k = k + a
k = k + (b << 3)
k = k + (b2 << 3)
print(bin(k))
bt = k >> 3
print(bt)
print (k - (bt << 3))
