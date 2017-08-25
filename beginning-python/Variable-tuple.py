print("---------------------------")
print("タプルオブジェクトの作成")
print("---------------------------")
empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

marx_tuple = 'Groucho','Chico','Harpo'
print(marx_tuple)


marx_tuple = ('Groucho','Chico','Harpo') # tupleは","で作成されるが、()を使うことで分かりやすくなる
print(marx_tuple)

marx_tuple = ('Groucho','Chico','Harpo')
a, b, c = marx_tuple # tupleのアンパック
print(a)
print(b)
print(c)

# tupleのアンパックを使うと、一時変数を使わなくても 値を交換可能
password = 'swordfish'
icecream = 'tuttifrutti'
password,icecream = icecream, password
print(password)
print(icecream)