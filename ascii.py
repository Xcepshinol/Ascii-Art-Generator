from PIL import Image

def draw(input_im,text_file):
    lett = "@#$%&*+-. " #character corresponding to brightness

    oa = []

    im = Image.open(input_im).convert("L") #convert to grayscale
    w,l = im.size #pixel width and length of image

    for i in range(l):
        oa.append([]) #initialize character matrix
        for j in range(w):
            x = (255-(im.getpixel((j,i))))//25 #find the character corresponding brightness
            oa[i].append(lett[x-1]) #add character to character matrix

    with open(text_file,'w') as imat: #write to txt file
        for k in range(len(oa)):
            for p in oa[k]:
                imat.write(p)
            imat.write("\n") #space for each line in character matrix

    return

#local variables
input_im = "im4.jpg"
text_file = "text12.txt"

draw(input_im, text_file)
    



