'''
programer: Sandy Yang
Data:2023-09-28
Discribe: 
This program for takes the story from "henryTheSquareEaredCat.txt" file  , 
find all the words “square,” and replace them with the word “pentagon”,
create a new file   “henryThePentagonEaredCat.txt” file to save the replace story,
ask the user if keep the new file “henryThePentagonEaredCat.txt” ,
if choose y: keep the new file
if choose n: delete the new file

''' 

import os
# read the story from "henryTheSquareEaredCat.txt" file
file = open("henryTheSquareEaredCat.txt", mode = 'r')
#creat a list newLines to store the new story
newLines = []
for line in file:
    # replace Square to Pentagon and replece square to pentagon, and store to the newLines list
    if "Square" in line:
        newLines.append(line.replace("Square", "Pentagon"))
    elif "square" in line:
        newLines.append(line.replace("square", "pentagon"))
    else:
        newLines.append(line)
# close file "henryTheSquareEaredCat.txt"
file.close()

# create a new file "henryThePentagonEaredCat.txt", write the file using newLines list's content
with open("henryThePentagonEaredCat.txt", mode = 'w') as newFile:
    for newLine in newLines:
        newFile.write(newLine)
#close file "henryThePentagonEaredCat.txt"
newFile.close()

userChoose = input("Do you want to keep the newly generated file henryThePentagonEaredCat.txt? (Y/N): ")
#  Delete henryThePentagonEaredCat.txt file if the user input  "N"  of "n"; 
if userChoose.upper() == "N":
    os.remove("henryThePentagonEaredCat.txt")
    print("henryThePentagonEaredCat.txt file was deleted.")
#  Keep the file if user input "Y" or "y"
elif userChoose.upper() == "Y":
    print("henryThePentagonEaredCat.txt file was kept.")
else:
    print("Please enter 'y' or 'Y' or 'n' or 'N' to choose if you want to keep the file.")

