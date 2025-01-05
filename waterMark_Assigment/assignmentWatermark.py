
from tkinter import *

from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Assignment Watermark")
window.config(bg="#d9d9d9", padx=20, pady=20)

def get_img():
    img_path = img_path_entry.get()
    watermark_text = watermark_text_entry.get()
    img = Image.open(img_path)
    return add_watermark(img , watermark_text)

def add_watermark(image, watermark_text):
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    # ("font type",font size)
    w, h = image.size
    print(w, h)
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("Arial", int(font_size / 10))
    y_w= 0
    for i in range(1,h,int(h/10)):
        y_w += i
        x_w = 0
        for j in range(1,w,int(w/10)):
            x_w += j
            draw.text((x_w,y_w),text= watermark_text, fill=(0, 0, 0), font=font, stroke_fill="white", embedded_color=True, anchor="ms")
    return watermark_image.show()

upload_button = Button(text= "Upload",highlightthickness=0,background="#d9d9d9", command=get_img)
upload_button.grid(row=0, column=1)
path_label = Label(text="Enter the file path")
path_label.grid(row=1, column=1)
img_path_entry = Entry(width=40)
img_path_entry.grid(row=1, column=3, columnspan=2)
img_path_entry.focus()
watermark_label = Label(text="Enter watermark text")
watermark_label.grid(row=2, column=1)
watermark_text_entry = Entry(width=40)
watermark_text_entry.grid(row=2, column=3, columnspan=2)





window.mainloop()

