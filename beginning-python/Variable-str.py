# シングル/ダブル どちらでもどちらでも
print("hello-world")
print('hello-world')

# トリプル
print('''There was a Yound Lady of Norway,
who casulally sat in doorway;''')

# 改行する場合は、トリプル
poem = '''There was a Yound Lady of Norway,
who casulally sat in doorway;'''

print(poem)

# print関数は、複数指定可能
# スペースで連結する
print(99,'bottels','world be enough')

bottels = 99
base = ''
base += 'current inventory:'
base += str(bottels)
print(base)

# 文字列変換はstr
print(str(98.6))
print(str(1.0e4))
print(str(True))

# 改行コードは \n
print('hoge \nfoo \npiyo')
# タブ文字は \t
print('hoge\tfoo\tpiyo')

# エスケープ文字は\
print('hoge\'foo\"piyo')

# 連結は+
a = 'hoge'
b = 'foo'
c = 'piyo'
print(a + b + c)
print(a, b, c)

# 繰り返しは*
start = 'Na ' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'

print(start + start + middle , end)

# 文字列は[]で抽出可
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])

# 文字列はイミュータブル
name = 'Henny'
# name[0] = 'P' #この行はエラーになる

name = 'Henny'
name.replace('H','P')
print(name)
print('P' + name[1:])


# [start:end:step]
print(letters[:])
print(letters[20:])
print(letters[10:])

print(letters[-3:])
print(letters[18:-3])

print(letters[-6:-2])

print("7文字おき")
print(letters[::7])

print(letters[4:20:3])
print(letters[19::4])

print(letters[:20:5])

print(letters[-1::-1])
print(letters[::-1])

print(letters[-26:])
print(letters[-27:-26])

# 長さはlen
print(len(letters))

# 分割はsplit
todos = 'get gloves,get mask,get cat vitamins,call ambulance'
print(todos.split(','))

print('split()に指定しない場合は、スペース分割')
print(todos.split())

# 結合はjoin
crypto_list = ['Yeti','Bigfoot','Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print('Found and singing book deals:',crypto_string)

# その他の文字列関数
poem = '''All that doth flow we cannnot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.startswith('all'))
print(poem.endswith('no doubt.'))

word = 'the'
print(poem.find(word))
print(poem.rfind(word))

print(poem.count(word))
print(poem.isalnum())

# 大文字/小文字
setup = 'a duck goes into a bar...'
print(setup.strip('.'))


print(setup.capitalize()) # 先頭の単語だけタイトルケース
print(setup.title()) # 全単語タイトルケース
print(setup.upper()) # すべて大文字
print(setup.lower()) # すべて小文字
print(setup.swapcase()) # 大文字/小文字反転

print(setup.center(30)) #30文字分の真ん中配置
print(setup.ljust(30)) #30文字分の左配置
print(setup.rjust(30)) #30文字分の右配置

print(setup.replace('duck','marmoset')) # 最初の１回だけ置換
print(setup.replace('a','a famouse ', 100)) # 100回置換

# http://bit.ly/py-docs-strings