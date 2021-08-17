from PIL import Image
im = Image.open(r"sampleImage.png")
width, height = im.size
left = 0
top = 0
right = 200
bottom = height/4

numRows = 4
numCols = 4

for row in range (numRows):
    for col in range (numCols):
        left = col*width/4
        right = (col+1)*width/4
        top = row*width/4
        bottom = (row+1)*width/4
        img = im.crop((left, top, right, bottom))
        imageName = "img"+str(row+1)+","+str(col+1)
        img = img.save(imageName+".PNG")