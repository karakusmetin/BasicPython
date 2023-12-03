import string
import time
from termcolor import colored
import random

s =""
arr = list(string.ascii_letters)
x="Hello World"
for  i in range(len(x)):
    random.shuffle(arr)
    if x[i] == " ":
        s+=x[i]
    else:
        for j in range(len(arr)):
            print(colored(s, 'green') + colored(arr[j], 'red'))
            time.sleep(0.07)
            if arr[j] == x[i]:
                s+=x[i]
                if s == x:
                    print(colored(x,'green')+"\n")
                break

