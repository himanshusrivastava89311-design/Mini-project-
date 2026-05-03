open_Count=0
closed_Count=0
while True:
     user=input("Allow access? (yes/no):")
     if user=="yes":
        print("open the lock")
        open_Count +=1;
     elif user=="no":
         print("not open the lock")
         closed_Count +=1;
     elif user=="exit":
         break
     else:
         print("Invalid input")    
class Camera:
     def __init__(self, name, quality):
         self.name=name
         self.quality=quality
         print("quality",quality)
    
cam1=Camera("FrontCam","1080p")
print("total open_Count",open_Count)
print("total close_Count",closed_Count)


    



                