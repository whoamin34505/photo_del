import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image


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
        try:
            img = Image.open(file)
            width, height = img.size
            window = Tk()
            window.title("Clean_photo")
            window.geometry(f'{width}x{height}')
            window.mainloop()
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    window = Tk()
    window.title("Clean_photo")
    window.mainloop()

if __name__ == "__main__":
    main()