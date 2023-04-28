import random
import time

alp_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_low = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_symbols = "!~`!@#$%^&?/-_=+|"
data = alp_up+alp_low+numbers+special_symbols
length = int(input("Ну что, нарисуем пароль? Введите введите вашу хотелку по длинне: "))
password = "".join(random.sample(data,length))
print("Придумываю пароль, обождите ... ")
time.sleep(2)
print("Ииии, вы молодец, ваш пароль - ")
time.sleep(1)
print(password)
print("Спасибо, и... Good Luck!")
time.sleep(10)
