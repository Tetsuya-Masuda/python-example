# 加算
print("加算")
print(10 + 5)

a = 10 + 5
print(a)

a = a + 5
print(a)

a += 5
print(a)

# 減算
print("減算")
print(10 - 5)

b = 10 - 5
print(b)

b = b - 5
print(b)

b -= 5
print(b)

# 乗算
print("乗算")
print(10 * 5)

c = 10 * 5
print(c)

c = c * 10
print(c)

c *= 10
print(c)

# 減算
print("減算")

d = 10 / 5
print(d)

d = 1000 / 10
print(d)

d = d / 10
print(d)

d = 1000
d /= 10
print(d)

d = 100
d /= 3
print(d)

d = 100
d //= 3
print(d)

# 剰余
print("剰余")

e = 10 % 3
print(e)

e = 10
e %= 3
print(e)

e = 10
f = divmod(10,3)
print(f)
print(type(f))

# 基数
print("基数")

print(10)
print(0b10)
print(0o10)
print(0x10)

# 型変換
print(int(True))
print(int(False))

print(int(98.6)) #整数型にすると切り捨てられる
print(int(1.0e4))

print(int('99'))
print(int('-1'))

# 型が異なる加算
print(4 + 7.0)
print(True + 2)
print(False - 3)

# long型はない
googol = 10 ** 100
print(googol)
print(googol * googol)

# float
print(float(1))
print(float('-1.5'))
