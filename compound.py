import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('Compound Label Demo')

snakePhoto = tk.PhotoImage(file='./python.png')
myLabel = ttk.Label(root, image=snakePhoto, text='Cute Snake', compound='top', padding=8).pack()

root.mainloop()