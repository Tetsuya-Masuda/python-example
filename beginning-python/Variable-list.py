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