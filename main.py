import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Distance converter")

meter_label=ttk.Label(main,text='Meter :',font=('Segoe UI',15))
meter_input=ttk.Entry(main,width=10,textvariable=meters_value,font=('Segoe UI',15))
meter_input.focus()

feet_label=ttk.Label(main,text='Feet :',font=('Segoe UI',15))
feet_display=ttk.Label(main,textvariable=feets_value,font=('Segoe UI',15))

meter_label.grid(row=0,column=0,sticky='w')
meter_input.grid(row=0,column=1,sticky='we')
feet_label.grid(row=1,column=0,sticky='w')
feet_display.grid(row=1,column=1,sticky="we")

root.mainloop()