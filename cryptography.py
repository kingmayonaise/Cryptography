"""
cryptography.py
Author: Daniel Melnikov
Credit: Dad, StackOverflow.com, Internet

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
from operator import add, sub
loop=True
encrypted=""
decrypted=""
print(len(associations))
while loop==True:
    enterletter=input("Enter e to encrypt,d to decrypt, or q to quit: ")
    if enterletter=='e':
        char=[]
        keyChar=[]
        #message=input("Message: ")
        message="Two plus two = Five"
        #key=input("Key: ")
        key="Lorem ipsum"
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        print(key)
        for i in message:
            char.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
        keyandChar=list(map(add, char, keyChar))
        for x in keyandChar:
            if x>len(associations):
                x-=len(associations)
            else:
                encrypted+=associations[x]
        print(encrypted)
        #loop=False
    elif enterletter=='d':
        char=[]
        keyChar=[]
        #message=input("Message: ")
        message="+KF;B(CH=NIZ};R\Dt "
        #key=input("Key: ")
        key="Lorem ipsum"
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        print(key)
        for i in message:
            char.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
        keyandChar=list(map(sub, char, keyChar))
        print(len(char))
        print(len(keyChar))
        print(keyandChar)
        for x in keyandChar:
            if x<len(associations):
                x+=len(associations)
            else:
                decrypted+=associations[x]
        print(decrypted)
        print('Decrypt works')
        loop=False
    elif enterletter=='q':
        print('Goodbye!')
        loop=False
    else:
        print('Did not understand command, try again.')