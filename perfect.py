import PIL
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
color_num=[0.1,0.5,0.9]
x=y=0

#black background
#black=PIL.Image.new(image.mode, (image.width,int(image.height*1.1)))
#black.paste(image, (x, y) )
#black = black.resize((int(black.width/2),int(black.height/2) ))
#display(black)

font=ImageFont.truetype('readonly/fanwood-webfont.ttf',50)

blacks=[]
for i in range(3):
    for j in color_num:     
        black=PIL.Image.new(image.mode, (image.width,int(image.height*1.1)))
        black.paste(image, (x, y) )
        draw = ImageDraw.Draw(black) 
        draw.text((0,image.height),"channel "+ str(i) + " intensity "+ str(j), font=font, fill=(255,255,255))
        black=black.convert('RGB')
        r,g,b=black.split()
        if i==0:
            r = r.point(lambda z: z*j)            
        if i==1:
            g = g.point(lambda z: z*j)
        if i==2:
            b = b.point(lambda z: z*j)
        out_black = Image.merge("RGB", (r, g, b))
        blacks.append(out_black)        

#check    
#display(blacks[0],blacks[1],blacks[2])


first_image=blacks[0]
contact_sheet=PIL.Image.new(image.mode, (first_image.width*3,first_image.height*3))

for img in blacks:
    contact_sheet.paste(img, (x, y) )
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
