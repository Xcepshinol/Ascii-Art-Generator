from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageTk

def draw(input_im,text_file=False):
    lett = "@#$%&*+-.  " #character corresponding to brightness
    s=''

    im_b = input_im.convert("L") #convert to grayscale
    w1,l1 = im_b.size #pixel width and length of image
    aspect = l1/w1

    w = 100 #resized width constant
    l = int(aspect*w*0.55) #corresponding length

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
def open_im():
    file = filedialog.askopenfilename(title='select and image', filetypes=[("Image files","*.png *.jpg *.jpeg *.bmp")])

    if file:
        img = Image.open(file)
        img.thumbnail((300,300))

        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

        draw(img)

root = Tk()
root.title("ASCII Art Generator")

Button(root, text="Upload Image", command=open_im).pack(pady=10)
label = Label(root)
label.pack()

root.mainloop()
    



