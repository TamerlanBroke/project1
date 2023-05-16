from PIL import Image, ImageFilter

def lab7n1():

    filename = "3.jpg"
    with Image.open(filename)as  img:
        img.load()

    img.show()
    widht,height = img.size

    format = img.format


    mode = img.mode

    print('Ширина: ', widht)
    print('Высота: ',height)
    print('Формат: ',format)
    print('цветовая модель: ',mode)


def lab7n2():
    filename = "2.jpg"
    with Image.open(filename)as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save('resized_2.jpg')

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img .save('image_flip_top.jpg')
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save('image_flip.jpg')

def lab7n3():
    spisok = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]
    for i in spisok:
        filename = Image.open(i)
        filename = image.filter(ImageFilter.CONTOUR)
        filename.show()

lab7n1()
lab7n2()
lab7n3()