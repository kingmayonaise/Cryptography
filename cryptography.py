"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
from operator import add
loop=True
char=[]
keyChar=[]
while loop==True:
    enterletter=input("Enter e to encrypt,d to decrypt, or q to quit: ")
    if enterletter=='e':
        #message=input("Message: ")
        message="Two plus two = Five"
        #key=input("Key: ")
        key="Lorem ipsum"
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        print (key)
        exit
        for i in message:
            char.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
        keyandChar=list(map(add, char, keyChar))
        for x in 
        print(char)
        print(keyChar)
        print('It works')
        loop=False
    elif enterletter=='d':
        print('Decrypt')
        loop=False
    elif enterletter=='q':
        print('Goodbye')
        loop=False
    else:
        print('Did not understand command, try again.')