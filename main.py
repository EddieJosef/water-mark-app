from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import filedialog
window = Tk()
window.title("Add water mark")
window.geometry("600x650")

def open_img():
    global my_img
    window.filename = filedialog.askopenfilename(initialdir="C:/Users/Eid josef/OneDrive/Pictures", title="Select file", filetypes=[('PNG', '*.png'), ('All Files', '*.*')])
    # my_photo = PhotoImage(file=window.filename)
    # my_label = Label(window, image=my_photo).pack()
    my_img = ImageTk.PhotoImage(Image.open(window.filename))
    my_image_label = Label(window, image=my_img).pack()

    def add_watermark():
        global my_img
        my_img = Image.open(window.filename)
        image_width, image_height = my_img.size
        font_size = int(image_width / 8)
        text_font = ImageFont.truetype('arial.ttf', font_size)
        x, y = int(image_width / 2), int(image_height / 2)
        text_add = my_entry.get()
        edit_img = ImageDraw.Draw(my_img)
        edit_img.text((x, y), text_add, 'red', font=text_font)
        my_img.save("C:/Users/Eid josef/OneDrive/Pictures/image1.png")
        my_entry.delete(0, END)
        my_img.show()

    my_entry = Entry(window, font=("Courier", 24))
    my_entry.pack()
    add_btn = Button(window, text="add_watermark", command=add_watermark).pack()


open_btn = Button(window, text="open file", command=open_img).pack()





window.mainloop()