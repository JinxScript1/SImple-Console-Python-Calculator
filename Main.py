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
print('addition, substraction, multiplication or division')
time.sleep(1)
c = str(input())
print('your answer is ')
if c == 'addition':
    print(a+b)
elif c == 'substraction':
    print(a-b)
elif c == 'multiplication':
    print(a*b)
elif c == 'division':
    print(a/b)
else: 
    print('Operation value is invalid')
print('do you want to close or start again?')
d = str(input())
if d == 'close':
    sys.exit()
elif d == 'start':
    os.execl(sys.executable, sys.executable, *sys.argv)
