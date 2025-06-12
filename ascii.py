from PIL import Image

def draw(input_im,text_file=False):
    lett = "@#$%&*+-.  " #character corresponding to brightness
    s=''

    im_b = Image.open(input_im).convert("L") #convert to grayscale
    w1,l1 = im_b.size #pixel width and length of image
    aspect = l1/w1

    w = 250 #resized width constant
    l = int(aspect*250*0.55) #corresponding length

    im = im_b.resize((w,l)) #resized image

    for i in range(l):
        s+='\n'
        for j in range(w):
            x = (255-(im.getpixel((j,i))))//25 #find the character corresponding brightness
            s+=lett[x]

    try:
        with open(text_file,'w') as imat: #write to txt file
            imat.write(s)
    except:    
        print(s)

    return

#global variables
input_im = "test.jpg"
text_file = "test_output.txt"

draw(input_im, text_file)
    



