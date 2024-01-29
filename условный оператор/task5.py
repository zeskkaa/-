#задание 1
num = int(input())
if (1000 <= num <= 9999) and (num % 7 == 0 or num % 17 == 0):
   print("красивое") 
else:
   print('страшное')

    