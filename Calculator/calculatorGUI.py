#!/usr/bin/python
"""This module contains a class called <CalculatorGUI> and
    It's the GUI representation or desktop app calculator
"""

import tkinter as tk
from tkinter import messagebox
from Arithemetic import calc


class CalculatorGUI():
    """A class which is a desktop GUI for calculator"""
    def __init__(self):
        """initializing the instance field attribute"""
        self.root = tk.Tk()
        self.root.title("CALCULATOR")
        self.root.geometry("500x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # adding the textbox where the user can perform various operations
        self.textbox = tk.Text(self.root, fg="white", bg="black", font=("Arial", 20), height=4, wrap="none")
        self.textbox.bind("<Enter>", self.on_text_hover)
        self.textbox.bind("<Leave>", self.on_text_leave)
        self.textbox.pack(padx=10, pady=10)

        # creating a button frame to accomadate the button
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)
        self.buttonFrame.columnconfigure(3, weight=1)

        # buttons on row 0
        self.clearAllbtn = tk.Button(self.buttonFrame, command=self.clearAll, fg="white", bg="red", text="AC", font=("Arial", 14))
        self.clearAllbtn.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.clearOnebtn = tk.Button(self.buttonFrame, command=self.clearOne, text="C", font=("Arial", 14))
        self.clearOnebtn.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.modulobtn = tk.Button(self.buttonFrame, command=lambda: self.writeOperand(self.modulobtn["text"]), bg="lightblue", text="%", font=("Arial", 14))
        self.modulobtn.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.dividebtn = tk.Button(self.buttonFrame, command=lambda: self.writeOperand(self.dividebtn["text"]), bg="lightblue", text="/", font=("Arial", 14))
        self.dividebtn.grid(row=0, column=3, sticky=tk.W+tk.E)
        
        # buttons on row 1
        self.sevenbtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.sevenbtn["text"]), text="7", font=("Arial", 14))
        self.sevenbtn.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.eightbtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.eightbtn["text"]), text="8", font=("Arial", 14))
        self.eightbtn.grid(row=1, column=1, sticky=tk.W+tk.E)
        self.ninebtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.ninebtn["text"]), text="9", font=("Arial", 14))
        self.ninebtn.grid(row=1, column=2, sticky=tk.W+tk.E)
        self.multiplybtn = tk.Button(self.buttonFrame, command=lambda: self.writeOperand(self.multiplybtn["text"]), bg="lightblue", text="X", font=("Arial", 14))
        self.multiplybtn.grid(row=1, column=3, sticky=tk.W+tk.E)
        
        # buttons on row 2
        self.fourbtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.fourbtn["text"]), text="4", font=("Arial", 14))
        self.fourbtn.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.fivebtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.fivebtn["text"]), text="5", font=("Arial", 14))
        self.fivebtn.grid(row=2, column=1, sticky=tk.W+tk.E)
        self.sixbtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.sixbtn["text"]), text="6", font=("Arial", 14))
        self.sixbtn.grid(row=2, column=2, sticky=tk.W+tk.E)
        self.minusbtn = tk.Button(self.buttonFrame, command=lambda: self.writeOperand(self.minusbtn["text"]), bg="lightblue", text="-", font=("Arial", 14))
        self.minusbtn.grid(row=2, column=3, sticky=tk.W+tk.E)
        
        # buttons on row 3
        self.onebtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.onebtn["text"]), text="1", font=("Arial", 14))
        self.onebtn.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.twobtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.twobtn["text"]), text="2", font=("Arial", 14))
        self.twobtn.grid(row=3, column=1, sticky=tk.W+tk.E)
        self.threebtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.threebtn["text"]), text="3", font=("Arial", 14))
        self.threebtn.grid(row=3, column=2, sticky=tk.W+tk.E)
        self.plusbtn = tk.Button(self.buttonFrame, bg="lightblue", command=lambda: self.writeOperand(self.plusbtn["text"]), text="+", font=("Arial", 14))
        self.plusbtn.grid(row=3, column=3, sticky=tk.W+tk.E)
        
        # buttons on row 4
        self.dzerobtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.dzerobtn["text"]), text="00", font=("Arial", 14))
        self.dzerobtn.grid(row=4, column=0, sticky=tk.W+tk.E)
        self.zerobtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.zerobtn["text"]), text="0", font=("Arial", 14))
        self.zerobtn.grid(row=4, column=1, sticky=tk.W+tk.E)
        self.dotbtn = tk.Button(self.buttonFrame, command=lambda: self.write(self.dotbtn["text"]), text=".", font=("Arial", 14))
        self.dotbtn.grid(row=4, column=2, sticky=tk.W+tk.E)
        self.equalbtn = tk.Button(self.buttonFrame, command=self.equalTo, bg="lightblue", text="=", font=("Arial", 14))
        self.equalbtn.grid(row=4, column=3, sticky=tk.W+tk.E)


        self.buttonFrame.pack(fill="both", pady=20)
    

        
        
        self.root.mainloop()

    def write(self, btnText):
        """Enter a number into the textbox"""
        self.textbox.insert(tk.END, btnText)

    def writeOperand(self, btnText):
        """Enter operand into the textbox"""
        addSpace = f' {btnText} '
        self.textbox.insert(tk.END, addSpace)

    def clearAll(self):
        """clear everything in the textbox"""
        self.textbox.delete("1.0", tk.END)

    def clearOne(self):
        """clear one at a time from the textbox"""
        self.textbox.delete("end-2c", tk.END)
        # self.textbox.delete("end-2c", tk.END)
    
    def on_text_hover(self, event):
        """disable the textbox when the mouse is on it"""
        self.textbox.config(state=tk.DISABLED)
    
    def on_text_leave(self, event):
        """undisable the textbox when the mouse a away"""
        self.textbox.config(state=tk.NORMAL)

    def equalTo(self):
        """Get the content of the textbox and process it and show the result"""
        userInput = self.textbox.get("1.0", tk.END)
        if len(userInput) >= 5:
            userInput = calc(userInput)
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, userInput)
            
        # text_widget.mark_set("insert", "end")
        # print("\n" + userInput)

    def on_closing(self):
        """what to do when user press the close button"""
        if messagebox.askyesno(title="Quit Calculator?", message="Are you sure?"):
            self.root.destroy()



if __name__ == "__main__":
    CalculatorGUI()