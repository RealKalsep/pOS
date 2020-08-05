from os import system, name
import sys
def clear(): 
    if name == 'nt': 
        _ = system('cls')
        
    else: 
        _ = system('clear')

def welcome():
    print('Welcome to pOS 0.01 - a custom Python operating system')
    print('Type "help" for help\n')

welcome()

def awaiting():
    command = input('> ')
    if command == "help":
        print('help, about, shutdown, restart, cls\n')
        awaiting()
        
    elif command == "about":
        print('You are using pOS 0.01, made in Python.\n')
        awaiting()
        
    elif command == "shutdown":
        yesno = input('Are you sure? y/n ')

        if yesno == "y":
            print('Shutting down...')
            sys.exit()
            
        if yesno == "n":
            print('Okay.\n')
            awaiting()

    elif command == "restart":
        yesno = input('Are you sure? y/n ')

        if yesno == "y":
            clear()
            welcome()
            awaiting()

        if yesno == "n":
            print('Okay.\n')
            awaiting()
        
    elif command == "cls":
        clear()
        awaiting()
        
    else:
        print('Command does not exist!\n')
        awaiting()

awaiting()
