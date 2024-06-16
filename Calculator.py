import os 
import sys 
import time

os.system("clear")
os.system("termux-tts-speak welcome to JackuXFlameBoy Calculator")
os.system("figlet Calculator | lolcat")
print("   ")
print("\033[0;36m    Welcome to JackuXFlameBoy Calculator ")
print("    ")
print("\033[0;37m1. Addition +")
print("   ")
print("2. Subtraction -")
print("   ")
print("3. Multiplication ×")
print("   ")
print("4. Deviation ÷")
print("   ")
num1 = int(input("\033[0;33m Add first value  here : "))
print("   ")
op = input(" Select What to do + - × ÷ : ")
print("   ")
num2 = int(input(" Add second value  here : \33m"))

if op == "+" :
   answer = num1 + num2

elif op == "-" :
  answer = num1 - num2

elif op == "×" :
  answer = num1 * num2

elif op == "÷" :
  answer = num1 / num2
print("   ")
print("   ")
print("   ")
print("\033[0;32m your Answer is" , str(answer))
print("       ")
print("   ")
print("   ")
print("\033[0;31m Start Again  with  just typing Calculator")
