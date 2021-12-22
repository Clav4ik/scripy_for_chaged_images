
from random import randrange
import os
from time import time
from tkinter import *
from tkinter import filedialog



root = Tk()
root.geometry('600x400+200+100')

label_result = Label(root, bg='black', fg='white', width=50)
label_info_how_work = Label(root, width=70,text='Вставте путь к фалу такого типа\nC:\\Users\\Пользователь\\PycharmProjects\\pythonProjectformom' )
test_way= f""

entry_first = Entry(root, width=100)

button_start = Button(root, text="Начать дела")
def process():
    start_time=time()
    way = entry_first.get()
    dir = os.path.join(way,"ChaNged_Foto")
    if not os.path.exists(dir):
        os.mkdir(dir)
    for filename in os.listdir(way):
        try:
            from PIL import Image, ImageEnhance
            first_factor = randrange(9000, 11000)
            factor = first_factor / 10000
            im = Image.open(way+'\\'+filename)
            enhancer = ImageEnhance.Contrast(im)
            im_output = enhancer.enhance(factor)
            im_output.save(way+'\\ChaNged_Foto\\'+'ChaNgeD'+filename)
        except Exception as ex:
            print(ex)
    label_result['text'] = 'Закончил работать'
    label_result['bg'] = 'red'
    print(time()-start_time)


entry_first.pack()

label_result.pack()
button_start.pack()
label_info_how_work.pack()
def find_path():
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    entry_first.delete(0, "end")
    entry_first.insert(0, folder_selected)



button_start.config(command = process)


root.mainloop()

#C:\Users\Пользователь\PycharmProjects\pythonProjectformom\mom_office\test
#D:\физра\21 год зима
#C:\Users\Пользователь\PycharmProjects\pythonProjectformom
#D:\Python
