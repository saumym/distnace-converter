import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Distance converter")

meter_label=ttk.Label(main,text='Meter :',font=('Segoe UI',15))
meter_input=ttk.Entry(main,width=10,textvariable=meters_value,font=('Segoe UI',15))
meter_input.focus()

feet_label=ttk.Label(main,text='Feet :',font=('Segoe UI',15))
feet_display=ttk.Label(main,textvariable=feets_value,font=('Segoe UI',15))


root.mainloop()