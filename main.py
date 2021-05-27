import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Distance converter")

root.columnconfigure(0,weight=1)

# ------------Frames-------------------

inp=ttk.Frame(root,padding=(30,15))
inp.grid()

out=ttk.Frame(root,padding=(30,15))
out.grid()

but=ttk.Frame(root,padding=(30,15))
but.grid()

# ------------ Calculate Function -------------

input_value=tk.StringVar()
kilometers_value=tk.StringVar(value="")
meters_value=tk.StringVar(value="")
feets_value=tk.StringVar(value="")
yards_value=tk.StringVar(value="")
inches_value=tk.StringVar(value="")
centimeters_value=tk.StringVar(value="")
millimeters_value=tk.StringVar(value="")

def converter(*arg):
  try:
    option=selected_option.get()
    inputvalue=float(input_value.get())

    # --------------Kilometer--------------------
    if option=="Kilometer":
      kilometers_value.set(f"{inputvalue :.3f}")
      meters_value.set(f"{inputvalue * 1000:.3f}")
      feets_value.set(f"{inputvalue * 3280.84:.3f}")
      yards_value.set(f"{inputvalue * 1093.61:.3f}")
      inches_value.set(f"{inputvalue * 39370.07:.3f}")
      centimeters_value.set(f"{inputvalue * 100000:.3f}")
      millimeters_value.set(f"{inputvalue * 1e+6:.3f}")

    # --------------Meter--------------------
    elif option=="Meter":
      kilometers_value.set(f"{inputvalue / 1000:.3f}")
      meters_value.set(f"{inputvalue :.3f}")
      feets_value.set(f"{inputvalue * 3.28084:.3f}")
      yards_value.set(f"{inputvalue * 1.094:.3f}")
      inches_value.set(f"{inputvalue * 39.27:.3f}")
      centimeters_value.set(f"{inputvalue * 100:.3f}")
      millimeters_value.set(f"{inputvalue * 1000:.3f}")

    # --------------Feet--------------------
    elif option=="Feet":
      kilometers_value.set(f"{inputvalue / 3280.84:.4f}")
      meters_value.set(f"{inputvalue * 0.3048:.3f}")
      feets_value.set(f"{inputvalue :.3f}")
      yards_value.set(f"{inputvalue * 0.33333:.3f}")
      inches_value.set(f"{inputvalue * 12:.3f}")
      centimeters_value.set(f"{inputvalue * 30.48:.3f}")
      millimeters_value.set(f"{inputvalue * 304.8:.3f}")

    # --------------Yard--------------------
    elif option=="Yard":
      kilometers_value.set(f"{inputvalue / 1000:.3f}")
      meters_value.set(f"{inputvalue :.3f}")
      feets_value.set(f"{inputvalue * 3.28084:.3f}")
      yards_value.set(f"{inputvalue * 1.094:.3f}")
      inches_value.set(f"{inputvalue * 39.27:.3f}")
      centimeters_value.set(f"{inputvalue * 100:.3f}")
      millimeters_value.set(f"{inputvalue * 1000:.3f}")

    # --------------Inch--------------------
    elif option=="Inch":
      kilometers_value.set(f"{inputvalue / 39370.1:.3f}")
      meters_value.set(f"{inputvalue * 0.0254:.3f}")
      feets_value.set(f"{inputvalue / 12:.3f}")
      yards_value.set(f"{inputvalue * 0.0277777778:.3f}")
      inches_value.set(f"{inputvalue :.3f}")
      centimeters_value.set(f"{inputvalue * 2.54:.3f}")
      millimeters_value.set(f"{inputvalue * 25.4:.3f}")

    # --------------centimeter--------------------
    elif option=="Centimeter":
      kilometers_value.set(f"{inputvalue / 100000:.3f}")
      meters_value.set(f"{inputvalue / 100:.3f}")
      feets_value.set(f"{inputvalue / 30.48:.3f}")
      yards_value.set(f"{inputvalue / 91.44:.3f}")
      inches_value.set(f"{inputvalue / 2.54:.3f}")
      centimeters_value.set(f"{inputvalue :.3f}")
      millimeters_value.set(f"{inputvalue * 10:.3f}")

    # --------------Millimeter--------------------
    elif option=="Millimeter":
      kilometers_value.set(f"{inputvalue / 1000000:.3f}")
      meters_value.set(f"{inputvalue / 1000:.3f}")
      feets_value.set(f"{inputvalue / 304.8:.3f}")
      yards_value.set(f"{inputvalue / 914:.3f}")
      inches_value.set(f"{inputvalue / 25.4:.3f}")
      centimeters_value.set(f"{inputvalue / 10:.3f}")
      millimeters_value.set(f"{inputvalue :.3f}")

    else:
      raise ValueError
    

  except ValueError:
    print("unknown input")



# -------------------------------------------
# -------------input parameters--------------
# -------------------------------------------

# meter_label=ttk.Label(inp,text='Meter :',)
selected_option = tk.StringVar()
options = ttk.Combobox(inp, textvariable=selected_option,font=('Segoe UI',15),width=8)
options["values"] = ["Kilometer", "Meter", "Feet", "Yard", "Inch", "Centimeter", "Millimeter"]
options["state"] = "readonly"  

meter_input=ttk.Entry(inp,width=10,textvariable=input_value,font=('Segoe UI',15))
meter_input.focus()


# ----------input parameters grid ----------

# meter_label.grid(row=0,column=0,sticky='w')
options.grid(row=0,column=0,sticky="w")
meter_input.grid(row=0,column=1,sticky='we')



# --------------------------------------------
# ---------output parameters -----------------
# --------------------------------------------



kilometer_label=ttk.Label(out,text='Kilometer :',font=('Segoe UI',13))
kilometer_display=ttk.Label(out,textvariable=kilometers_value,font=('Segoe UI',15))

meter_label=ttk.Label(out,text='Meter :',font=('Segoe UI',13))
meter_display=ttk.Label(out,textvariable=meters_value,font=('Segoe UI',15))

feet_label=ttk.Label(out,text='Feet :',font=('Segoe UI',13))
feet_display=ttk.Label(out,textvariable=feets_value,font=('Segoe UI',15))

centimeter_label=ttk.Label(out,text='Centimeter :',font=('Segoe UI',13))
centimeter_display=ttk.Label(out,textvariable=centimeters_value,font=('Segoe UI',15))

inch_label=ttk.Label(out,text='Inch :',font=('Segoe UI',13))
inch_display=ttk.Label(out,textvariable=inches_value,font=('Segoe UI',15))

yard_label=ttk.Label(out,text='Yard :',font=('Segoe UI',12))
yard_display=ttk.Label(out,textvariable=yards_value,font=('Segoe UI',15))

millimeter_label=ttk.Label(out,text='Millimeter :',font=('Segoe UI',12))
millimeter_display=ttk.Label(out,textvariable=millimeters_value,font=('Segoe UI',15))


# --------output parameters grid--------------


kilometer_label.grid(row=0,column=0,sticky='w')
kilometer_display.grid(row=0,column=1,sticky="we")

meter_label.grid(row=0,column=2,sticky='w')
meter_display.grid(row=0,column=3,sticky="we")

yard_label.grid(row=1,column=0,sticky='w')
yard_display.grid(row=1,column=1,sticky="we")

feet_label.grid(row=1,column=2,sticky='w')
feet_display.grid(row=1,column=3,sticky="we")

inch_label.grid(row=3,column=0,sticky='w')
inch_display.grid(row=3,column=1,sticky="we")

centimeter_label.grid(row=3,column=2,sticky='w')
centimeter_display.grid(row=3,column=3,sticky="we")

millimeter_label.grid(row=4,column=0,sticky='w')
millimeter_display.grid(row=4,column=1,sticky="we")


# -------------------Button---------------------

button=ttk.Button(but,text="Calculate",command=converter)

button.grid(row=4,column=0,columnspan=2,sticky='we')

# ---------All component configuration----------

for child in inp.winfo_children():
  child.grid_configure(ipadx=10,ipady=10)

for child in out.winfo_children():
  child.grid_configure(ipadx=10,ipady=10)

meter_input.bind('<Return>',converter)
root.bind('<KP_Enter>',converter)


root.mainloop()