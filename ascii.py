from PIL import Image, ImageDraw, ImageFont

def draw(input_im,text_file=False):
    lett = "@#$%&*+-. " #character corresponding to brightness

    oa = []

    im_b = Image.open(input_im).convert("L") #convert to grayscale
    w1,l1 = im_b.size #pixel width and length of image
    aspect = l1/w1

    w = 100 #resized width constant
    l = int(aspect*w*0.55) #corresponding length

    im = im_b.resize((w,l)) #resized image

    try:
        for i in range(l):
            oa.append([]) #initialize character matrix
            for j in range(w):
                x = (255-(im.getpixel((j,i))))//25 #find the character corresponding brightness
                oa[i].append(lett[x-1]) #add character to character matrix

        with open(text_file,'w') as imat: #write to txt file
            for k in range(len(oa)):
                for p in range(len(oa[k])):
                    imat.write(oa[k][p])
                imat.write("\n") #space for each line in character matrix
    except:
        for i in range(l):
            s =''
            for j in range(w):
                x = (255-(im.getpixel((j,i))))//25 #find the character corresponding brightness
                s+=lett[x-1]
            print(s)
    return

#local variables
input_im = "test.jpg"

draw(input_im)
    



