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
encrypted=""
decrypted=""
while True:
    enterletter=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if enterletter in ('e','d'):
        message=input('Message:')
        key=input('Key:')
        letters=[]
        keyChar=[]
        if key=='':
            continue
        while len(key)<len(message):
            key+=key[:min(len(key),len(message)-len(key))]
        for i in message:
            letters.append(associations.find(i))
        for n in key:
            keyChar.append(associations.find(n))
    elif enterletter=='q':
        print('Goodbye!')
        break
    else:
        print('Did not understand command, try again.')
    
    if enterletter=='e':
        #key="Lorem ipsum"
        keyandChar=list(map(add, letters, keyChar))
        for x in keyandChar:
            if x>len(associations):
                x-=len(associations)
            encrypted+=associations[x]
        print(encrypted)
    elif enterletter=='d':
        #message="+KF;B(CH=NIZ}m;R\Dt"
        #key="Lorem ipsum"
        keyandChar=list(map(sub, letters, keyChar))
        for x in keyandChar:
            if x<0:
                x+=len(associations)
            decrypted+=associations[x]
        print(decrypted)
