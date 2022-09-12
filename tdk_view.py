import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('TDK LAMBDA')

#row 0 port
tk.Button(root, text='Rescan port').grid(row=0, column=0)

port_name = tk.StringVar()
port_name_cb = ttk.Combobox(root, values = '', textvar=port_name, width=12)
port_name_cb.grid(row=0, column=1)

tk.Button(root, text='Stop').grid(row=0, column=2)

#row 1 constant current label
tk.Label(root, text='Current').grid(row=1, column=1)
#row 2 constant current
tk.Label(root, text='CC').grid(row=2, column=0)
tk.Entry(root).grid(row=2, column=1)
tk.Button(root, text='Start').grid(row=2, column=2)

#row 3 ramp up label
tk.Label(root, text='min').grid(row=3, column=1)
tk.Label(root, text='max').grid(row=3, column=2)
#row 4 ramp up
tk.Label(root, text='Ramp up').grid(row=4, column=0)
tk.Entry(root).grid(row=4, column=1)
tk.Entry(root).grid(row=4, column=2)
tk.Button(root, text='Start').grid(row=4, column=3)

#row 5 ramp down label
tk.Label(root, text='max').grid(row=5, column=1)
tk.Label(root, text='min').grid(row=5, column=2)
#row 6 ramp down
tk.Label(root, text='Ramp down').grid(row=6, column=0)
tk.Entry(root).grid(row=6, column=1)
tk.Entry(root).grid(row=6, column=2)
tk.Button(root, text='Start').grid(row=6, column=3)

#row 7 last label
tk.Label(root, text='max').grid(row=7, column=1)
tk.Label(root, text='t1').grid(row=7, column=2)
tk.Label(root, text='t2').grid(row=7, column=3)
#row 8 last
tk.Label(root, text='Last').grid(row=8, column=0)
tk.Entry(root).grid(row=8, column=1)
tk.Entry(root).grid(row=8, column=2)
tk.Entry(root).grid(row=8, column=3)
tk.Button(root, text='Start').grid(row=8, column=5)

#row 9 cycle label
tk.Label(root, text='min').grid(row=9, column=1)
tk.Label(root, text='max').grid(row=9, column=2)
tk.Label(root, text='t1').grid(row=9, column=3)
tk.Label(root, text='t2').grid(row=9, column=4)
#row 10 cycle
tk.Label(root, text='Cycle').grid(row=10, column=0)
tk.Entry(root).grid(row=10, column=1)
tk.Entry(root).grid(row=10, column=2)
tk.Entry(root).grid(row=10, column=3)
tk.Entry(root).grid(row=10, column=4)
tk.Button(root, text='Start').grid(row=10, column=5)

#row 11 voltage current
tk.Label(root, text='Current').grid(row=11, column=0)
tk.Label(root, text='I').grid(row=11, column=1)
tk.Label(root, text='Voltage').grid(row=11, column=2)
tk.Label(root, text='V').grid(row=11, column=3)


root.mainloop()
