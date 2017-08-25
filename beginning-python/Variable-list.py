print("---------------------------")
print("listの宣言")
print("---------------------------")
emtpy_list = []
another_empty_list = list()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']

print(type(emtpy_list))
print(type(another_empty_list))
print(type(weekdays))

big_birds = ['emu','ostrich','cassowary']
first_names = ['Graham','John','Terry','Terry','Michael']

print("")
print("---------------------------")
print("list()関数を使った型変換")
print("---------------------------")

cat_list = list('cat')
print(cat_list)

a_tuple = ('ready','fire','aim')
print(a_tuple)

birthday = '1/6/1952'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

print("")
print("---------------------------")
print("[offset]を使った要素の取り出し")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo']
print(marxex[0])
print(marxex[1])
print(marxex[2])

print(marxex[-1])
print(marxex[-2])
print(marxex[-3])


print("")
print("---------------------------")
print("リストのリスト")
print("---------------------------")

small_birds = ['humingbird','finch']
extinct_birds = ['dodo','passenger pigeon','Norwegian Blue']
carol_birds = [3,'French hens',2,'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw',carol_birds]

print(all_birds)
print(all_birds[0])
print(all_birds[1][0])

print("")
print("---------------------------")
print("[offset]による要素の書き換え")
print("---------------------------")

print(marxex)
marxex[2] = 'Wanda'
print(marxex)

print("")
print("---------------------------")
print("オフセットの範囲を指定したスライスによるサブシーケンスの取り出し")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo']
print(marxex[0:2])
print(marxex[::2])
print(marxex[::-2])
print(marxex[::-1])

print("")
print("---------------------------")
print("append()による末尾への要素の追加")
print("---------------------------")
marxex.append('Zeppo')
print(marxex)

print("")
print("---------------------------")
print("extend()または+=を使ったリストの結合")
print("---------------------------")
others = ['Gummo','Karl']
marxex.extend(others)
print(marxex)

marxex = ['Groucho','Chico','Harpo','Zeppo']
marxex += others
print(marxex)

marxex = ['Groucho','Chico','Harpo','Zeppo']
marxex.append(others)
print(marxex)

marxex = ['Groucho','Chico','Harpo','Zeppo']

print("")
print("---------------------------")
print("insert()によるオフセットを指定した要素の追加")
print("---------------------------")
marxex.insert(3, 'Gummo')
print(marxex)
marxex.insert(10, 'Karl')
print(marxex)

print("")
print("---------------------------")
print("delによる指定したオフセットの要素の削除")
print("---------------------------")
del marxex[-1]
print(marxex)

marxex = ['Groucho','Chico','Harpo','Gummo','Zeppo']
print(marxex[2])

del marxex[2]
print(marxex)
print(marxex[2])

print("")
print("---------------------------")
print("remover()による値に基づく要素の削除")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Gummo','Zeppo']
marxex.remove("Gummo")
print(marxex)

print("")
print("---------------------------")
print("pop()でオフセットを指定して要素を取り出し、削除する")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Zeppo']
marxex.pop()  #末尾の要素が取り出される
print(marxex)

marxex.pop(1) #offset=1の要素が取り出される
print(marxex)

print("")
print("---------------------------")
print("index()で要素の値からオフセットを知る")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Zeppo']
print(marxex.index('Chico'))

print("")
print("---------------------------")
print("inを使った値の有無")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Zeppo']
print('Groucho' in marxex)
print('Bob' in marxex)

print("")
print("---------------------------")
print("count()を使った値の個数の計算")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Zeppo']
print(marxex.count('Zeppo'))
print(marxex.count('Bob'))

snl_skit = ['cheeseburger','cheeseburger','cheeseburger']
print(snl_skit.count('cheeseburger'))


print("")
print("---------------------------")
print("join()による文字列への変換")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo','Zeppo']
print(','.join(marxex))

friends = ['Harry','Hermione','Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)

separated = joined.split(separator)
print(separated)

print(separated == friends)

print("")
print("---------------------------")
print("sort()による要素の並び替え")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo']
sorted_marxex = sorted(marxex) #ソートしたオブジェクトのコピー
print(sorted_marxex)

print(marxex) #オブジェクト自体をソート
marxex.sort()
print(marxex)

numbers = [2,1,4.0,3]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

print("")
print("---------------------------")
print("len()による長さの取得")
print("---------------------------")
marxex = ['Groucho','Chico','Harpo']
print(len(marxex))

print("")
print("---------------------------")
print("=による代入とcopy()によるコピー")
print("---------------------------")
a = [1,2,3]
print(a)

b = a #オブジェクトをコピーしている（ポインタアドレスのコピー？）
print(b)

a[0] = 'surprise'
print(a)
print(b)

a = [1,2,3]
b = a.copy() # 新しいオブジェクトを作成する
c = list(a) # 新しいオブジェクトを作成する
d = a[:] # 新しいオブジェクトを作成する

a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)