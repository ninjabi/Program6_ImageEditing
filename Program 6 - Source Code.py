import os

def input_directory():
    global working_directory
    while True:
        try:
            working_directory = int(input("Would you like to:"
                           "\n 1. Open your files from the directory you are in?"
                           "\n 2. Open your files from another directory?"))
            while working_directory not in [1,2]:
                working_directory = int(input("Please enter a valid input [1/2] =>"))
            break
        except ValueError:
            print("Please enter a valid input [1/2]")
            continue
    if working_directory ==1:
        Files = os.listdir(os.getcwd())
    if working_directory == 2:
        while True:
            try:
                global input_directory
                input_directory = input("Enter the directory of the source images: ")
                os.chdir(input_directory) #changes working directory to users input
            except FileNotFoundError:
                print("The directory {} is not found.".format(input_directory))
                continue
            Files = os.listdir(os.getcwd())
            files_indir = [f for f in Files]
            print("\nYour directory was valid. \n"
                  "\nYou have", len(files_indir), "item(s) within the working directory: ")


            break
def output_directory():
    while True:
        try:
            output_directory = int(input("\nDo you want the output file to:"
                                     "\n 1. Output to the working directory?"
                                     "\n 2. Output to a different directory?\n"))
            while output_directory not in [1,2]:
                output_directory = int(input("Please enter a valid input [1/2] =>"))
            break
        except ValueError:
            print("Please enter a valid input [1/2]")
            continue
    if output_directory == 2:
        while True:
            try:
                global file_output_dir
                file_output_dir = input("Enter the directory that the output file will be saved to: ")
                os.chdir(file_output_dir)
            except FileNotFoundError:
                print("The directory {} is not found.".format(file_output_dir))
                continue
            print("Your directory was valid. "
                  "\nYour output file will be saved to " + file_output_dir + ".")
            break
    os.chdir(input_directory)
def new_file():
    global output_file
    output_file_name = input("\nWhat do you want to name your output file? (excluding extension).")
    while output_file_name == "" or output_file_name == " ":
        output_file_name = input("You cannot enter blank as a file name. Please try again: ")
    output_file = open(output_file_name, "a")
def iterate_files():
    global Files, file_list, PPMS, num_lines
    Files = os.listdir(os.getcwd())
    PPMS = [open(f, "r") for f in Files if f.lower().endswith('.ppm')] #opens all files that end with .ppm
    print("\nBeginning to iterate through the files...")
    for file in PPMS:
        num_lines = (sum(1 for x in file))
        print(num_lines)
        break

def median_filter():
    for file in PPMS:   #iterate over files in PPMS (the list of the files)
        for line in file:    #iterate over line within each file
            for j in range(1, num_lines):
                CurrentLine = line[1]
                print(CurrentLine)
                #line = int(line) #convert each line to an integer
            #print(CurrentLine)


input_directory()
new_file()
iterate_files()
median_filter()