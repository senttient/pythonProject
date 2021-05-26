import os
import shutil
# home = os.getcwd()
# print(home)


target = os.path.expanduser('~/Downloads/')
# print(target)
books = os.path.expanduser('~/Desktop/Books/')
# print(books)
images_svg = os.path.expanduser('~/Desktop/Images/svg/')
# print(images_svg)
images_jpg = os.path.expanduser('~/Desktop/Images/jpg/')
# print(images_jpg)
images_png = os.path.expanduser('~/Desktop/Images/png/')
# print(images_png)
images_gif = os.path.expanduser('~/Desktop/Images/gif/')
# print(images_gif)
images_ai = os.path.expanduser('~/Desktop/Images/ai/')
# print(images_ai)
images_bmp = os.path.expanduser('~/Desktop/Images/bmp/')
# print(images_bmp)

all_images = [images_ai, images_bmp, images_gif, images_jpg, images_png, images_svg, books
              ]

for i in all_images:
    if os.path.isdir(i):
        print('Directory '+ i + ' exists.')
        continue       
    
    else:
        print("Making Directory" + i)
        os.makedirs(i)

'''Code looks at files in the target directory searches for the specified ext i.e. 
(.pdf) once it finds it moves it to the appropriate directory. using try blocks for the error handling capabilities.'''

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.pdf'):
                shutil.copy(os.path.join(target, x), books)
except:
    pass

# noinspection PyBroadException
try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.svg'):
                shutil.copy(os.path.join(target, x), images_svg)
except:
    pass

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.jpg'):
                shutil.copy(os.path.join(target, x), images_jpg)
            elif x.endswith('.jpeg'):
                shutil.copy(os.path.join(target, x), images_jpg)
except:
    pass

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.png'):
                shutil.copy(os.path.join(target, x), images_png)
except:
    pass

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.ai'):
                shutil.copy(os.path.join(target, x), images_ai)
except:
    pass

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.gif'):
                shutil.copy(os.path.join(target, x), images_gif)
except:
    pass

try:
    for root, dirname, files in os.walk(target):
        for x in files:
            if x.endswith('.bmp'):
                shutil.copy(os.path.join(target, x), images_bmp)
except:
    pass
