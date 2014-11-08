"""
Fatima Mohamed
COMP - SCI 101
Algorithm #6
Due: 11/09/14

Problem:
    - Creating a program that compares multiple images and replaces portions that are not similar to other parts. Useful
    when removing pesky tourists that just don't know how to get out of an image!

Notes:
    - All error handling using try except blocks.

Algorithm:
    1. Ask user what directory they want to load the image files from and open them:
        import os
        file_path = input("What directory are your pictures in?")
        change directory to file_path assignment
        open_files = if file name ends with .ppm, open.
            - if directory contains less than 3 images, print([Warning that there are less than 3 images])
    2. Ask user the name of the file they want to output to.
        If file format is not proper, use try except block to catch exception and
        until the user inputs a file format that is correct.
    3. Now that the files are open, create for loop to iterate through each file,
       line by line, comparing the the median values to see if one is
       out of the ordinary.
    4. For each rgb values that is present in the majority of the pictures,
       copy and write it on the new file to be exported.
    5. Once the iteration has completed through all the files, the final bits of code
       are added to the file to be exported.
    6. Once that is complete, ask user if they would like to export file as
       jpeg or ppm.
    7. If jpeg is chosen, import the pillow module and work code in
       to export the file as a jpeg.
    8. If the ppm is chosen, export file with ending .ppm.
    9. Once this is completed, save editing image file to chosen directory and print
       message letting the user know that the file editing is complete.
    10. Close the files.
"""