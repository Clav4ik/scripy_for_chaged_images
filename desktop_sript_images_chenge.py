from random import randrange
import os
from time import time
from tkinter import *
from tkinter import filedialog



root = Tk()
root.geometry('600x400+200+100')

label_result = Label(root, fg='black', width=50)
label_info_how_work = Label(root, width=70,text='Вставте путь к фалу такого типа\nC:\\Users\\Пользователь\\PycharmProjects\\pythonProjectformom' )

entry_first = Entry(root, width=100)

button_start = Button(root, text="Начать дела")
button_path_folder = Button(root, text="Найти дела")
def process():
    start_time=time()
    way = entry_first.get().strip().split('/')
    way = '\\'.join(way)
    dir = os.path.join(way,"ChaNged_Foto").split('/')
    directory = '\\'.join(dir)
    if not os.path.exists(directory):
        os.mkdir(directory)
    for filename in os.listdir(way):
        try:
            from PIL import Image, ImageEnhance
            first_factor = randrange(9000, 11000)
            factor = first_factor / 10000
            if factor == 1:
                factor = 1.05
            #factor = 0.01
            im = Image.open(way+'\\'+filename)
            enhancer = ImageEnhance.Contrast(im)
            im_output = enhancer.enhance(factor)
            im_output.save(way+'\\ChaNged_Foto\\'+'ChaNgeD'+filename)
        except Exception as ex:
            print(ex)
    label_result['text'] = 'Закончил работать'
    label_result['bg'] = 'green'
    print(time()-start_time)


entry_first.pack()

label_result.pack()
button_start.pack()
label_info_how_work.pack()
button_path_folder.pack()
def find_path():
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    entry_first.delete(0, "end")
    entry_first.insert(0, folder_selected)



button_start.config(command = process)
button_path_folder.config(command = find_path)

root.mainloop()
