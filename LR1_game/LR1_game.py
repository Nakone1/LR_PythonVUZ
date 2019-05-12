    
import random
print("Введи n")
n=int(input())
print("Я загадал число в диапазоне от 0 до", n)
print("Угадай это число!")
b= random.randint(0, n)
a=int(input())
while a != b:
    print("Не угадал")
    a=int(input())
print("Молодец,угадал")