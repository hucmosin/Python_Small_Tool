"""
    处理图片变成-文字的一个转变,需要PIL
    pip install PIL
    from PIL import Image
"""

from PIL import Image
import glob
import os


folder_input = raw_input("Enter the directory of the image :")
folder_output = raw_input("Enter the directory of the text:")


def left(image):
    fn = open(image)
    (filepath, filename) = os.path.split(fn.name)
    fn_o = os.path.splitext(filename)
    text = open(folder_output + fn_o[0] + '.txt', 'w')
    im = Image.open(image)
    im = im.convert('L')
    for y in range(1, 480 * 2,5):
        y /= 2
        for x in range(1, 480 * 2 , 3):
            x /= 2
            pixel = im.getpixel((x,y))
            if pixel < 120:
                text.write(' ')
            else:
                text.write('M')
        text.wite('\n')
    text.flush()
    print image + ' ' + 'successful!'
    text.close()
    fn.close()


for img in glob.glob(folder_input + '*_*'):
    left(img)

print 'Done....'
