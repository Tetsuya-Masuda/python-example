rabbits = ['Flopsy','Mopsy','Cottontail','Peter']

# この反復処理はよろしくない
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# この書き方がpythonらしい処理
for rabbit in rabbits:
    print(rabbit)

# イテラブルオブジェクトなら利用可能
word = 'cat'
for letter in word:
    print(letter)

# 辞書をforで処理するとキーが返される
accusation = {'room':'ballroom','weapon':'lead pipe','person':'Col.Mustard'}
for card in accusation:
    print(card)

# 値を処理するならvalues()を使う
for value in accusation.values():
    print(value)

# キーと値ならitems()を使う
for item in accusation.items():
    print(item)

for card,contents in accusation.items():
    print('Card',card, 'has the contents',contents)

cheese = []
for cheese in cheese:
    print('Tthis shop has some lovely',cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

# zip()を使うと、複数のシーケンスを並列的に反復処理可能
days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']
for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# zip()便利
english = 'Monday','Tuesday','Wednesday'
french = 'Lundi','Mardi','Mercredi'
print(list(zip(english,french)))
print(dict(zip(english,french)))

# range()を使うと指定した範囲の数値のストリームを返すことが可能
for x in range(0,3):
    print(x)
print(list(range(0,3)))

for x in range(2,-1,-1):
    print(x)
print(list(range(2,-1,-1)))
print(list(range(0,11,2)))