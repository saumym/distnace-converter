import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Distance converter")

root.columnconfigure(0,weight=1)

main=ttk.Frame(root,padding=(30,15))
main.grid()

meters_value=tk.StringVar()
feets_value=tk.StringVar(value="")
def converter(*arg):
  try:
    meter=float(meters_value.get())
    feet=meter * 3.28084
    feets_value.set(f"{feet:.3f}")
  except ValueError:
    pass

meter_label=ttk.Label(main,text='Meter :',font=('Segoe UI',15))
meter_input=ttk.Entry(main,width=10,textvariable=meters_value,font=('Segoe UI',15))
meter_input.focus()

feet_label=ttk.Label(main,text='Feet :',font=('Segoe UI',15))
feet_display=ttk.Label(main,textvariable=feets_value,font=('Segoe UI',15))

meter_label.grid(row=0,column=0,sticky='w')
meter_input.grid(row=0,column=1,sticky='we')
feet_label.grid(row=1,column=0,sticky='w')
feet_display.grid(row=1,column=1,sticky="we")

button=ttk.Button(main,text="Calculate",command=converter)
button.grid(row=2,column=0,columnspan=2,sticky='we')

for child in main.winfo_children():
  child.grid_configure(ipadx=10,ipady=10)
meter_input.bind('<Return>',converter)
root.bind('<KP_Enter>',converter)


root.mainloop()