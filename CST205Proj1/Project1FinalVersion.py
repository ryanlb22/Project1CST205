
import statistics
from PIL import Image
#myImagelist=[10];
#sorted([myImagelist])
im  = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\1.png")
im2 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\2.png")
im3 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\3.png")
im4 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\4.png")
im5 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\5.png")
im6 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\6.png")
im7 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\7.png")
im8 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\8.png")
im9 = Image.open("C:\\Users\\Ryan\\Desktop\\CST205Proj1\\Project1Images\\9.png")

print("Working...")

#creates 3 pixels and sets values of pixels to 0
redmpixel=0
greenmpixel=0
bluempixel=0

#create new lists to store each different pixel
redpixellist=[]
greenpixellist=[]
bluepixellist=[]




#size of picture 495x557
pictureWidth = 495
pictureHeight = 557

#putting all of the images into an imagelist
imagelist=[im,im2,im3,im4,im5,im6,im7,im8,im9]
print("The sizes of all images is: ", im.size)
print("Still working...")

#CREATES A NEW IMAGE
newImage = Image.new("RGB",(495,557),"white")
counter=0;
counter2=0;
#for loop to go through each image and takes the pixels and puts them into a new image
for x in range(0,pictureWidth):
    for y in range(0,pictureHeight):
        for Image in imagelist:
            #creates red green and blue pixel
            r,g,b=Image.getpixel((x,y))
            #adds r,g,b to several pixel lists
            redpixellist.append(r)
            greenpixellist.append(g)
            bluepixellist.append(b)
            counter=counter+1
        #GETS THE RED PIXEL LIST,GETS THE MEDIAN AND PUTS INTO REDMPIXEL
        redmpixel=statistics.median(redpixellist)
        #GETS THE GREEN PIXEL LIST, GETS THE MEDIAN AND PUTS INTO GREENMPIXEL
        greenmpixel=statistics.median(greenpixellist)
        #GETS THE BLUE PIXEL LIST,GETS THE MEDIAN AND PUTS INTO BLUEMPIXEL
        bluempixel=statistics.median(bluepixellist)
        #DELETES THE OLD PIXEL LIST EACH TIME IT LOOPS
        bluepixellist=[]
        greenpixellist=[]
        redpixellist=[]
        #puts the pixels RGB into the new images
        newImage.putpixel((x,y),(redmpixel,greenmpixel,bluempixel))
        counter2=counter2+1
        
    
#shows how many time image in imagelist loops
print("Counter 1 loops:",counter,"times")
#shows how many times the x and y 
print("Counter 2 loops:",counter2,"times")


print("Showing the image...")
#SHOWS THE NEW IMAGE
newImage.show()
print("DONE")
