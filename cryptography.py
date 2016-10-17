"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
loop=True
while loop==True:
    enterletter=input("Enter e to encrypt,d to decrypt, or q to quit: ")
    if enterletter=='e':
        message=input("Message: ")
        key=input("Key: ")
        for i in message:
            for 
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