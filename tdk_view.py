import tkinter as tk
from tkinter import ttk


class TDK_View:
    def __init__(self, root, ctrl=None):
        self.root = root
        self.ctrl = ctrl

        self.add_ctrl()
        self.add_monitor()

    def add_ctrl(self):
        self.frm_ctrl = tk.Frame(self.root)
        self.frm_ctrl.pack(fill='x', padx=3, pady=3)

        #row 0 port
        self.btn_serial_ports = tk.Button(self.frm_ctrl, text='Serial ports').grid(row=0, column=0)

        self.port_name = tk.StringVar()
        self.port_name_cb = ttk.Combobox(self.frm_ctrl, values = '', textvar=self.port_name, width=12)
        self.port_name_cb.grid(row=0, column=1)

        self.stop = tk.Button(self.frm_ctrl, text='Stop').grid(row=0, column=2)

        #row 1 constant current label
        tk.Label(self.frm_ctrl, text='Current').grid(row=1, column=1)
        #row 2 constant current
        tk.Label(self.frm_ctrl, text='CC').grid(row=2, column=0)
        tk.Entry(self.frm_ctrl).grid(row=2, column=1)
        tk.Button(self.frm_ctrl, text='Start').grid(row=2, column=2)

        #row 3 ramp up label
        tk.Label(self.frm_ctrl, text='min').grid(row=3, column=1)
        tk.Label(self.frm_ctrl, text='max').grid(row=3, column=2)
        #row 4 ramp up
        tk.Label(self.frm_ctrl, text='Ramp up').grid(row=4, column=0)
        tk.Entry(self.frm_ctrl).grid(row=4, column=1)
        tk.Entry(self.frm_ctrl).grid(row=4, column=2)
        tk.Button(self.frm_ctrl, text='Start').grid(row=4, column=3)

        #row 5 ramp down label
        tk.Label(self.frm_ctrl, text='max').grid(row=5, column=1)
        tk.Label(self.frm_ctrl, text='min').grid(row=5, column=2)
        #row 6 ramp down
        tk.Label(self.frm_ctrl, text='Ramp down').grid(row=6, column=0)
        tk.Entry(self.frm_ctrl).grid(row=6, column=1)
        tk.Entry(self.frm_ctrl).grid(row=6, column=2)
        tk.Button(self.frm_ctrl, text='Start').grid(row=6, column=3)

        #row 7 last label
        tk.Label(self.frm_ctrl, text='max').grid(row=7, column=1)
        tk.Label(self.frm_ctrl, text='t1').grid(row=7, column=2)
        tk.Label(self.frm_ctrl, text='t2').grid(row=7, column=3)
        #row 8 last
        tk.Label(self.frm_ctrl, text='Last').grid(row=8, column=0)
        tk.Entry(self.frm_ctrl).grid(row=8, column=1)
        tk.Entry(self.frm_ctrl).grid(row=8, column=2)
        tk.Entry(self.frm_ctrl).grid(row=8, column=3)
        tk.Button(self.frm_ctrl, text='Start').grid(row=8, column=5)

        #row 9 cycle label
        tk.Label(self.frm_ctrl, text='min').grid(row=9, column=1)
        tk.Label(self.frm_ctrl, text='max').grid(row=9, column=2)
        tk.Label(self.frm_ctrl, text='t1').grid(row=9, column=3)
        tk.Label(self.frm_ctrl, text='t2').grid(row=9, column=4)
        #row 10 cycle
        tk.Label(self.frm_ctrl, text='Cycle').grid(row=10, column=0)
        tk.Entry(self.frm_ctrl).grid(row=10, column=1)
        tk.Entry(self.frm_ctrl).grid(row=10, column=2)
        tk.Entry(self.frm_ctrl).grid(row=10, column=3)
        tk.Entry(self.frm_ctrl).grid(row=10, column=4)
        tk.Button(self.frm_ctrl, text='Start').grid(row=10, column=5)

    def add_monitor(self):
        self.frm_monitor = tk.Frame(self.root)
        self.frm_monitor.pack(fill='x', padx=3, pady=3)

        #row 0 voltage current
        tk.Label(self.frm_monitor, text='Current').grid(row=0, column=0)
        tk.Label(self.frm_monitor, text='I').grid(row=0, column=1)
        tk.Label(self.frm_monitor, text='Voltage').grid(row=0, column=2)
        tk.Label(self.frm_monitor, text='V').grid(row=0, column=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('TDK LAMBDA')
    tdk_view = TDK_View(root)
    root.mainloop()
