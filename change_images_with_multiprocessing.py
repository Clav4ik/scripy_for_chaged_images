
from random import randrange
import os
from multiprocessing import Pool
from time import time


def process_images(data):
    try:
        from PIL import Image, ImageEnhance
        first_factor = randrange(9000, 11000)
        factor = first_factor / 10000
        im = Image.open(data.get('path') + '\\' + data.get('filename'))
        enhancer = ImageEnhance.Contrast(im)
        im_output = enhancer.enhance(factor)
        im_output.save(data.get('path') + '\\ChaNged_Foto\\' + 'ChaNgeD' + data.get('filename'))
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    while True:
        way = input('Ввести путь к папке\n')
        start_time = time()
        dir = os.path.join(way, "ChaNged_Foto")
        if not os.path.exists(dir):
            os.mkdir(dir)
        data = []
        for filename in os.listdir(way):
            data.append({
                "path": way,
                'filename': filename
            })
        p = Pool()  # process 5 images simultaneously
        p.map(process_images, data)
        print(time() - start_time)

# C:\Users\User\PycharmProjects\pythonProjectformom\mom_office\test

