import os, platform

so = platform.system()

def cls ():
     if so == 'Windows':
          os.system('cls')
     else:
          os.system('clear')
