name = input('What is your name')
days = int(input('How many days you want to calculate?'))
sum = 0

for day in range(days):
    answer = int(input('how many cups taken on day ' + str(day + 1)))
    sum = sum + answer


average = sum/ days



if average < 5:
    print('Drink More')
elif average == 5:
    print('Good')
else:
    print("You drank too much")