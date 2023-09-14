import time
import sys
import os

massage = "Welcome To A Simple Console Calculator By JinxScripts"

for char in massage:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

print('.')
time.sleep(1)
print('Please enter the First Number Calculation')
a = float(input())
time.sleep(1)
print('Please enter the Second Number Calculation')
b = float(input())
time.sleep(1)
print('Which operation do you want to perform?')
time.sleep(1)
print('Press 1 for + ,Press 2 for - ,Press 3 for x, Press 4 for /')
time.sleep(1)
c = int(input())
print('your answer is ')
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
else: 
    print('Operation value is invalid')
