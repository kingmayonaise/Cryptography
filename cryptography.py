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
while loop==True:
    enterletter=input("Enter e to encrypt,d to decrypt, or q to quit: ")
    if enterletter=='e':
        letters=[]
        keyChar=[]
        #message=input("Message: ")
        message="Two plus two = Five"
        #key=input("Key: ")
        key="Lorem ipsum"
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        print(key)
        for i in message:
            letters.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
        keyandChar=list(map(add, letters, keyChar))
        for x in keyandChar:
            if x>len(associations):
                x-=len(associations)
            else:
                encrypted+=associations[x]
        print(encrypted)
        #loop=False
    elif enterletter=='d':
        letters=[]
        keyChar=[]
        #message=input("Message: ")
        message="+KF;B(CH=NIZ};R\Dt "
        #key=input("Key: ")
        key="Lorem ipsum"
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        for i in message:
            letters.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
        keyandChar=list(map(sub, letters, keyChar))
        print(keyandChar)
        for x in keyandChar:
            if x<0:
                x+=len(associations)
            else:
                print(x)
                decrypted+=associations[x]
        print(decrypted)
        print('Decrypt works')
        loop=False
    elif enterletter=='q':
        print('Goodbye!')
        loop=False
    else:
        print('Did not understand command, try again.')