from PIL import Image
import os
import random
import time

cdir = os.path.dirname(os.path.realpath(__file__))

def show_image(image):
    try:
        ydir = os.path.join(cdir, "yuri/")
        to_show = ydir + str(image)
        img = Image.open(to_show)
        img.show()
    except:
        print("Failed to show yuri :c")

def get_random_image():
       yuril = list()
       t_tried = 0
       try:
            files = os.listdir(os.path.join(cdir,"yuri"))
            numv = len([f for f in files if os.path.isfile(os.path.join(os.path.join(cdir,"yuri"), f))])
            for x in os.listdir(os.path.join(cdir, "yuri")):
                    t_tried += 1
                    apd = str(x)
                    yuril.append(apd)
                    if t_tried == numv:
                        give = random.choice(yuril)
                        return give
       except:
        print("Failed to get random image bwaaaa")


while True:
    time.sleep(random.randint(60,240))
    show_image(get_random_image())
