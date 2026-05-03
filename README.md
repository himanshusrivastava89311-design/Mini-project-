# Mini-project-
Overview
This program does two main things:
Takes user input (yes/no/exit) in a loop and counts how many times access is allowed or denied.
Defines a Camera class and creates an object.
🔹 Part 1: Access Control System
Python
open_Count=0
closed_Count=0

while True:
    user=input("Allow access? (yes/no):")
✅ Logic:
Infinite loop (while True)
User input is taken repeatedly
🔹 Conditions:
✔ If user enters "yes"
Python
print("open the lock")
open_Count +=1
Lock opens
open_Count increases
❌ If user enters "no"
Python
print("not open the lock")
closed_Count +=1
Lock stays closed
closed_Count increases
🚪 If user enters "exit"
Python
break
Loop stops
⚠ Invalid input
Python
print("Invalid input")
Any other input is rejected
🔹 Part 2: Camera Class
Python
class Camera:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        print("quality", quality)
📌 What it does:
Defines a class Camera
Constructor (__init__) runs when object is created
Stores:
name
quality
Prints the camera quality
🔹 Object Creation
Python
cam1 = Camera("FrontCam", "1080p")
👉 Output:

quality 1080p
🔹 Final Output
Python
print("total open_Count",open_Count)
print("total close_Count",closed_Count)
📊 Displays:
Total number of times lock opened
Total number of times lock denied
<img width="1080" height="1245" alt="17777858875217392097370847764493" src="https://github.com/user-attachments/assets/4dacdd79-94fa-48ef-ae1b-7dc0c9399ce3" />
