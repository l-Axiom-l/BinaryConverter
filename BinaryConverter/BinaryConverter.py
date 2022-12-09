from ctypes import windll
from tkinter import *
import tkinter

class MainWindow:

    window = Tk()
    sv = StringVar()
    Output = Label()
    ChangeModeButton = Button()
    binaryMode = True
    windll.shcore.SetProcessDpiAwareness(1)

    def __init__(self):
        self.window.geometry("400x150+500+200")
        self.window.title("BC")
        label = Label(text = "Binary Converter", fg='Orange', font=("Arial", 22))
        label.pack()
        Input = Entry(textvariable=self.sv ,width=30, justify=CENTER, font=("Arial", 16))
        Input.pack()
        self.sv.trace_add("write", self.EntryModifiedCallback)
        self.Output = Label(text = "Placeholder", font = ("Arial", 16))
        self.Output.pack()
        self.ChangeModeButton = Button(text="Converting to Binary", command=self.ChangeMode, font = ("Arial", 14))
        self.ChangeModeButton.pack()
        self.EntryModifiedCallback()
        self.window.mainloop()

    def EntryModifiedCallback(self, *args):
        if(not self.sv.get().isdecimal()):
            self.Output["text"] = "Only numbers allowed"
            return

        if(self.binaryMode):
            if(not self.IsBinary(self.sv.get())):
                self.Output["text"] = "Input not a binary"
                return
            else:
                self.Output["text"] = str(self.ConvertBinary(self.sv.get()))
        else:
            self.Output["text"] = self.ConvertDecimal(int(self.sv.get()))
        #self.Output["text"] = "IsBinary:" + str(self.IsBinary(self.sv.get()))

    def ConvertBinary(self, Input):
        Ergebnis = 0
        print(Input)
        for i in range(0, len(Input)):
            Ergebnis = Ergebnis * 2
            temp = int(Input[i])
            Ergebnis = Ergebnis + temp

        return Ergebnis

    def ConvertDecimal(self, input):
        temp = input
        Rest = 0
        Ergebnis = ""

        while True:

            Rest = temp % 2 
            temp = temp / 2
            temp = int(str(temp).split(".")[0])
            Ergebnis += str(Rest)

            print("T: " + str(temp))
            print("R: " + str(Rest))

            if(temp == 0):
                break

        Ergebnis = Ergebnis[::-1]
        return Ergebnis

    def IsBinary(self, string):
        isBinary = True
        for i in range(0, len(string)):
            try:
                temp = int(string[i])

                if(temp > 1 or temp < 0):
                    isBinary = False
                    
            except:
                isBinary = False
                print("Error")

        return isBinary

    def ChangeMode(self):
        match self.binaryMode:
            case True:
                self.binaryMode = False
                self.ChangeModeButton["text"] = "Converting to binary"
            case False:
                self.binaryMode = True
                self.ChangeModeButton["text"] = "Converting to decimal"

        self.EntryModifiedCallback()


        

window = MainWindow()