from PIL import Image, ImageDraw
print("hi")

#[red, green, brown, orange, cyan, grey, yellow, purple, blue]
colours = [(255,255,255),(255,0,0),(131,248,131), (102, 51, 0),(255, 153, 0),(102, 255, 255),(129, 129, 131),(255, 255, 0),(102, 0, 102),(0, 0, 204)]
testgrid = \
[[1, 10, 8, 8, 8, 7] ,
 [2, 2, 1, 8, 1, 7] ,
 [6, 2, 2, 4, 4, 7] ,
 [6, 1, 3, 3, 1, 7] ,
 [6, 6, 3, 3, 9, 1] ,
 [5, 5, 5, 1, 9, 9]]

im = Image.new('RGB',[160,160], (0, 0, 0))
d = ImageDraw.Draw(im)
for i in range(1, len(testgrid)+1):
    for j in range(1, len(testgrid)+1):
        d.rectangle(xy=(20*j, 20*i, 20*j+20, 20*i+20), fill=(colours[testgrid[i-1][j-1]-1]), outline=(50,50,50))
d.text(xy=(28,8),text="1       2       3       4       5       6",fill=(255,255,255),spacing=200)
d.text(xy=(8,25), text="A", fill=(255,255,255))
d.text(xy=(8,45), text="B", fill=(255,255,255))
d.text(xy=(8,65), text="C", fill=(255,255,255))
d.text(xy=(8,85), text="D", fill=(255,255,255))
d.text(xy=(8,105), text="E", fill=(255,255,255))
d.text(xy=(8,125), text="F", fill=(255,255,255))

im.show()

