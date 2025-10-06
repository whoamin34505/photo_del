import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk


def main():
    print("Select a folder with photos.")
    os.system("PAUSE")

    dir_path = filedialog.askdirectory()
    if not dir_path:
        print("No folder selected. Exiting.")
        return
    
    dir_path = os.path.normpath(dir_path).replace("\\", "/")
    
    for file in os.listdir(dir_path):
        r = os.path.splitext(file)[1]
        if (r=='.jpg' or r=='.png'):
            print(r)
            print(file)
        try:
            root = Tk()
            root.title("file")
            img = Image.open(file)
            width, height = img.size
            root.geometry(f'{width}x{height}')
 
            canvas = Canvas(bg="white", width=width, height=height)
            canvas.pack(anchor=CENTER, expand=1)
 
            python_image = PhotoImage(file=file)
 
            canvas.create_image(0, 0, anchor=NW, image=python_image)
 
            root.mainloop()
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    tk.mainloop()

if __name__ == "__main__":
    main()