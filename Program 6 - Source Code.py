import os

def directory_menu():
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


directory_menu()