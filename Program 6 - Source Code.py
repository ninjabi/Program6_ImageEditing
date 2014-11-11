import os

def directory_menu():
    global choice
    while True:
        try:
            choice = int(input("Would you like to:"
                           "\n 1. Open your files from the directory you are in?"
                           "\n 2. Open your files from another directory?"))
            while choice not in [1,2]:
                choice = int(input("Please enter a valid input [1/2] =>"))
            break
        except ValueError:
            print("Please enter a valid input [1/2]")
            continue
        break

def open_files():
    if choice == 1:
        print("Hello")
    elif choice ==2:
        while True:
            try:
                global directory
                directory = input("Enter the directory of the source images: ")
                os.chdir(directory)
            except FileNotFoundError:
                print("The directory {} is not found.".format(directory))
                continue
            break
directory_menu()
open_files()