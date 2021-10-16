#
from tkinter import *
import math

class TotalDelayCalculation:

    def __init__(self):
        window = Tk()
        window.title("Total Delay Calculation")
        window.geometry("500x250")

        Label(window, text="Packet Size: ").grid(row=1, column=1, sticky=W)
        Label(window, text="Bit Rate: ").grid(row=2, column=1, sticky=W)
        Label(window, text="Propagation delay").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1)  # space between inputs and outputs
        Label(window, text="The Total Delay is:").grid(row=6, column=1, sticky=W)
        Label(window, text="t1:").grid(row=7, column=3, sticky=W)
        Label(window, text="t2:").grid(row=7, column=4, sticky=W)
        Label(window, text="The Total bits are:").grid(row=9, column=1, sticky=W)


        # vars to store inputs
        self.packet_size = StringVar()
        self.bit_rate = StringVar()
        self.propagation_delay = StringVar()
        self.t1 = StringVar()
        self.t2 = StringVar()
        # vars for outputs
        self.total_delay = StringVar()
        self.total_bits = StringVar()

        # text boxes to hold inputs and outputs
        Entry(window, textvariable=self.packet_size,
              justify=RIGHT).grid(row=1, column=2, padx=(0, 5))
        Entry(window, textvariable=self.bit_rate,
              justify=RIGHT).grid(row=2, column=2, padx=(0, 5))
        Entry(window, textvariable=self.propagation_delay,
              justify=RIGHT).grid(row=3, column=2, padx=(0, 5))
        Entry(window, textvariable=self.t1,
              justify=RIGHT).grid(row=8, column=3, padx=(0, 2))
        Entry(window, textvariable=self.t2,
              justify=RIGHT).grid(row=8, column=4, padx=(0, 2))
        Label(window, textvariable=self.total_delay,
              font="Helvetica 12 bold",
              justify=RIGHT).grid(row=6, column=2)
        Label(window, textvariable=self.total_bits,
              font="Helvetica 12 bold",
              justify=RIGHT).grid(row=9, column=2)


        Label(window, text="Bytes").grid(row=1, column=3, sticky=W)
        Label(window, text="bits/sec").grid(row=2, column=3, sticky=W)
        Label(window, text="sec").grid(row=3, column=3, sticky=W)



        Button(window, text="Calculate Delay", command=self.calcDelay).grid(row=5, column=2)
        Button(window, text="Calculate Bits", command=self.calcBits).grid(row=8, column=2)


        window.mainloop()

    def calcDelay(self):
       
        packet_size = float(self.packet_size.get())*8
        bit_rate = float(self.bit_rate.get())
        propagation_delay = float(self.propagation_delay.get())
        total_delay = round((float(packet_size) / float(bit_rate)) + float(propagation_delay),5)
        self.total_delay.set(format(total_delay)+" sec")

    def calcBits(self):
        packet_size = float(self.packet_size.get()) * 8
        bit_rate = float(self.bit_rate.get())
        propagation_delay = float(self.propagation_delay.get())
        total_delay = round((float(packet_size) / float(bit_rate)) + float(propagation_delay), 5)
        total_time = abs(float(self.t2.get()) - float(self.t1.get()))
        if(total_time>total_delay):
            total_time = total_time - float(total_delay)
        else:
            total_time = 0
        self.total_bits.set(format(math.floor(bit_rate * total_time)) + " bits")

TotalDelayCalculation()
