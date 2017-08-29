#集合を作るときはset()を使う
empty_set = set()
print(type(empty_set))

#もしくは、カンマで区切った{}を使う
even_numbers = {0,2,4,6,8}
print(even_numbers)

odd_numbers = {1,3,5,7,9}
print(odd_numbers)

#集合型にするにはset()を使う
print(set('letters')) #重複文字は取り除かれる

print(set(['Dasher','Dancer','Prancer','Mason-Dixon'])) #リストから集合を作る
print(set(('Ummaguma','Echoes','Atom Heart Mother'))) #タプルから集合を作る
print(set({'apple':'red','orange':'orange','cherry':'red'})) #辞書から集合を作るとキーのみ

#要素の確認はinを使う
drinks = {
    'martini': {'vodka','vermouth'},
    'black russian' : {'vodka','kahlua'},
    'white russian' : {'cream','kahlua','vodka'},
    'manhatten' : {'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
}
print("vodkaが入っている飲み物")
for name, contens in drinks.items():
    if 'vodka' in contens:
        print(name)
print("")
print("vodkaが入っていて、ベルモットとクリームが無いもの")
for name,contens in drinks.items():
    if 'vodka' in contens and not ('vermouth' in contens or 'cream' in contens):
        print(name)

print("")
print("簡潔に書き直す")
for name, contens in drinks.items():
    if contens & {'vermouth','orange juice'}:
        print(name)

print("")
for name, contens in drinks.items():
    if 'vodka' in contens and not contens & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1,2}
b = {2,3}

print(a & b) #積集合
print(a.intersection(b)) #積集合

print(bruss & wruss)

print(a | b) #和集合
print(a.union(b)) #和集合
print(bruss | wruss)

print(a - b) #差集合
print(a.difference(b)) #差集合

print(bruss - wruss) #差集合
print(wruss - bruss) #差集合

print(a ^ b) #排他的OR(どちらかにはあるが、両方には含まれていない)
print(a.symmetric_difference(b))

print(bruss ^ wruss)

print("")
print("部分集合")
print(a <= b) #aがbの部分集合か？
print(a.issubset(b))

print(bruss <= wruss)
print(a <= a) #自身は必ず部分集合
print(b.issubset(b))

print("")
print("真部分集合")
print(a < b) #真部分集合か？
print(a < a)
print(bruss < wruss)

print("")
print("上位集合")
print(a >= b) #上位集合か?
print(a.issuperset(b))

print(wruss >= bruss)
print(a >= a) #自身は上位集合
print(a.issubset(a))

print("")
print("真上位集合")
print(a > b) #真上位集合か？
print(wruss > bruss)

print("データ構造の比較")
marx_list = ['Groucho','Chico','Harpo']
marx_tuple = 'Groucho','Chico','Harpo'
marx_dict = {'Groucho':'banjo','Chico':'piano','Harpo':'harp'}
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])

marxes = ['Groucho','Chico','Harpo']
pythons = ['Chapman','Cleese','Gilliam','Jones','Palin']
stooges = ['Moe','Curly','Larry']

tuple_of_lists = marxes,pythons,stooges
print(tuple_of_lists)

list_of_lists = [marxes,pythons,stooges]
print(list_of_lists)

dict_of_lists = {'Marxes':marxes, 'Pythons':pythons, 'Stooges':stooges}
print(dict_of_lists)

#制限はデータ型
#辞書のキーはイミュータブル
#タプルなら辞書のキーになれる
houses = {
    (44.79, -93.14,285) : 'My house',
    (38.89,-77.03,13):'The White House'
}