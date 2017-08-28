emtpy_dic = {} #単純な辞書（キー/値ペアを持たないから辞書）
print(type(emtpy_dic))

#キーはイミュータブル型なら良い

bierce = {
    "day" : "A period of twenty-four hours, mostly misspent",
    "positive":"Mistaken at the top of one's voice",
    "misfortune":"The Kind of fortune that never misses",
}
print(bierce)

#2要素のリストのリスト
lol = [['a','b'],['c','d'],['e','f']]
print(dict(lol)) #dict()を使うと、キー/値ペアのシーケンスを辞書型に変換できる

#2要素のタプルのリスト
lot = [('a','b'),('c','d'),('e','f')]
print(dict(lot))

#2要素のリストのタプル
tol = (['a','b'],['c','d'],['e','f'])
print(dict(tol))

#2字の文字列のリスト
los = ['ab','cd','ef']
print(dict(los))

#2文字の文字列のタプル
tos = ('ab','cd','ef')
print(dict(tos))

#キーを使って要素を参照
#キーがあれば既存の値の書き換え
#キーが無い場合は値ともども追加される
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Idel':'Eric',
    'Jones':'Terry',
    'Falin':'Michel'
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

#同じキーを指定すると後勝ち
some_pythons = {
    'Graham' :'Chapman',
    'John':'Cleese',
    'Eric':'Idle',
    'Terry':'Gilliam',
    'Michael':'Palin',
    'Terry':'Johnes' #Terryキーに対して、この行の値が優先される
}
print(some_pythons) 

#update()で辞書のキーと値をコピーする
pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Gilliam' : 'Terry',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael'
}
print(pythons)

others = {'Marx' : 'Groucho', 'Howard' : 'Moe'}
pythons.update(others)
print(pythons)

first = {'a':1,'b':2}
second = {'b':'platpus'}
first.update(second) #第1辞書と第2辞書に同じキーがあると、第2辞書の値が残る
print(first)

#要素の削除はdelを使う
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

#すべてのキーと値を削除するにはclear()を使う
#もしくはから辞書を設定する
pythons.clear()
print(pythons)
pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Gilliam' : 'Terry',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael'
}
pythons = {}
print(pythons)

#キーが含まれいるかはinを使う
pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Gilliam' : 'Terry',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael'
}
print('Chapman' in pythons)
print('Marx' in pythons)

#値を取得するにはキーを指定する
print(pythons['Cleese'])
#print(pythons['Marx']) #キーが無いとエラーになる
#エラーを回避するには、inを使う
print('Marx' in pythons)
#もしくはget()を使う
print(pythons.get('Cleese'))
print(pythons.get('Marx')) #Noneが返却される
print(pythons.get('Marx','Not a Python')) #オプションを指定することも可能

#全てのキーを取得するにはkeys()を使う
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
print(signals.keys())
print(type(signals.keys()))
#dict_keys型をリスト型にするときはlist()を使う
print(list(signals.keys()))
print(type(list(signals.keys())))

#全ての値を取得するにはvalues()を使う
print(signals.values())
print(type(signals.values())) #dict_values型

#全てのキー/値を取得するにはitems()を使う
print(signals.items())
print(type(signals.items()))#dict_items型

#=はポインタの参照
#copy()はオブジェクトのコピー
#この辺はリストと同じ
save_signals = signals
signals['blue'] = 'confuse everypne'
print(save_signals.items())
del signals['blue']
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals.items())
print(original_signals.items())