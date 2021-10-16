from tkinter import *


class Dimensioning:

    def __init__(self):
        window = Tk()
        window.title("Bit Rate calculation")
        window.geometry("320x200")

        Label(window, text="Metrhtes: ").grid(row=1, column=1, sticky=W)
        Label(window, text="Arithmos Parametrwn: ").grid(row=2, column=1, sticky=W)
        Label(window, text="Stathmes Kvadopoihshs: ").grid(row=3, column=1)  # space between inputs and outputs
        Label(window, text=None).grid(row=4, column=1)  # space between inputs and outputs
        Label(window, text="The total Bit Rate is:").grid(row=7, column=1, sticky=W)
        Label(window, text="")

        # vars to store inputs
        self.N = StringVar()
        self.X = StringVar()
        self.Q = StringVar()
        # vars for outputs
        self.bit_rate = StringVar()

        # text boxes to hold inputs and outputs
        Entry(window, textvariable=self.N, justify=RIGHT).grid(row=1, column=2)
        Entry(window, textvariable=self.X, justify=RIGHT).grid(row=2, column=2)
        Entry(window, textvariable=self.Q, justify=RIGHT).grid(row=3, column=2)
        Label(window, textvariable=self.bit_rate, font="Helvetica 12 bold", justify=RIGHT).grid(row=7, column=2)

     

        self.selected = StringVar()
        
        Button(window, text="Calculation", command=self.calcTotalBitRate).grid(row=6, column=2, padx=(10, 5), pady=5)

        window.mainloop()


    def calcTotalBitRate(self):

        N = float(self.N.get())
        X = float(self.X.get())
        Q = float(self.Q.get())
        
        bit_rate = N * X * Q
        self.bit_rate.set(format(bit_rate))


Dimensioning()
