count = 1
while count <= 5:
    print(count)
    count += 1

#while True:
#    stuff = input("String to capitalize [type q to quit]:")
#    if stuff == "q":
#        break
#    print(stuff.capitalize())

#whileループばbreakで完了しない場合にelseブロックのコードが実行される
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')