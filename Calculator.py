# Python program to create a simple GUI-based calculator

from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from math import *

expression = ""                                                 #Used to display the mathematical expression in the entry box
total = ""                                                      #Used to display the value after having simplified the expression
e = exp(1)                                                      #Initialising the value of Euler's number to the variable "e"

layout = {                                                      #Layout of buttons 
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': 'black',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#6b7070"
}


def ftan(n):
    return tan(n*(pi)/180)


def fsin(n):
    return sin(n*(pi)/180)


def fcos(n):
    return cos(n*(pi)/180)


def arctan(n):
    return atan(n)*(180/pi)


def arcsin(n):
    return asin(n)*(180/pi)


def arccos(n):
    return acos(n)*(180/pi)


def Log(n):
    return log(n, 10)


def ln(n):
    return log(n)


def abs(n):
    return fabs(n)


def press(num):
    global expression
    global length

    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    
    try:

        global expression
        global length
        
        if "×" in expression:
            
                    expression = expression.replace("×", "*")   #Used to change mathematical operators so as to make it evaluable
                    
        if "÷" in expression:
            
                    expression = expression.replace("÷", "/")
                    
        if "!" in expression:
            
                    expression = expression.replace("!", "")
                    expression = str(factorial(int(expression)))


        if "²" in expression:
            
                    expression = expression.replace("²", "**2")

        if "^" in expression:
            
                    expression = expression.replace("^", "**")                    

        if "%" in expression:
            
                    expression = expression.replace("%", "/100")
                    
        if "√" in expression:
            
                    expression = expression.replace("√", "**0.5")

        if "π" in expression:
            
                    expression = expression.replace("π", "pi")


        print(expression)
        total = str(eval(expression))
        print(total)


        equation.set(total)
        expression = total



    except ZeroDivisionError:
        
        messagebox.showinfo('Division by zero is a bit surreal','Infinity is a concept. It is bigger than any number you can imagine!')
        
    except ValueError as v:
        
        messagebox.showinfo('Invalid format!', str(v).title())
        
    except SyntaxError as S:
        
        messagebox.showinfo('Invalid format!', str(S).title())
        
    except TypeError as T:
        
        messagebox.showinfo('Invalid format!', str(T).title())
        


def clear():
    global expression
    expression = ""
    equation.set("")


def percent():
    press("%")
    equalpress()


def radical():
    press("√")
    equalpress()


def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def wholesquare():
    press("²")
    equalpress()



if __name__ == "__main__":
    
    gui = Tk()                                                  #Creates a GUI window           
    
    gui.configure(background="black")

    gui.title("Calculator")

    gui.geometry("960x630")
    
    gui.resizable(False, False)

    equation = StringVar()
    

    expression_field = Entry(gui, textvariable=equation, font = ("default", 30), fg = "white", bg = "black")

    expression_field.grid(columnspan=4, ipadx=70)

    

    button1 = Button(gui, text=' 1 ', command=lambda: press(1), **layout)
    button1.grid(row=4, column=4)

    button2 = Button(gui, text=' 2 ',command=lambda: press(2), **layout)
    button2.grid(row=4, column=5)

    button3 = Button(gui, text=' 3 ',command=lambda: press(3), **layout)
    button3.grid(row=4, column=6)

    button4 = Button(gui, text=' 4 ',command=lambda: press(4), **layout)
    button4.grid(row=3, column=4)

    button5 = Button(gui, text=' 5 ', command=lambda: press(5), **layout)
    button5.grid(row=3, column=5)

    button6 = Button(gui, text=' 6 ', command=lambda: press(6), **layout)
    button6.grid(row=3, column=6)

    button7 = Button(gui, text=' 7 ', command=lambda: press(7), **layout)
    button7.grid(row=2, column=4)

    button8 = Button(gui, text=' 8 ', command=lambda: press(8), **layout)
    button8.grid(row=2, column=5)

    button9 = Button(gui, text=' 9 ', command=lambda: press(9), **layout)
    button9.grid(row=2, column=6)

    button0 = Button(gui, text=' 0 ', command=lambda: press(0), **layout)
    button0.grid(row=5, column=5)
    
    button10 = Button(gui, text=' x² ', command=wholesquare, **layout)
    button10.grid(row=4, column=1)
    
    

    plus = Button(gui, text=' + ', command=lambda: press("+"), **layout)
    plus.grid(row=4, column=7)

    minus = Button(gui, text=' - ', command=lambda: press("-"), **layout)
    minus.grid(row=3, column=7)

    multiply = Button(gui, text=' × ', command=lambda: press("×"), **layout)
    multiply.grid(row=2, column=7)

    divide = Button(gui, text=' ÷ ', command=lambda: press("÷"), **layout)
    divide.grid(row=1, column=7)

    plusminus = Button(gui, text=' +/- ', command=lambda: press("(-"), **layout)
    plusminus.grid(row=5, column=4)
    
    equal = Button(gui, text=' = ', command=equalpress, **layout)
    equal.grid(row=5, column=7)
    equal.configure(bg = "lime green")

    clear = Button(gui, text='C', command=clear, **layout)
    clear.grid(row=1, column=4)
    clear.configure(fg = "red")

    Decimal= Button(gui, text='.', command=lambda: press('.'), **layout)
    Decimal.grid(row=5, column=6)

    coma = Button(gui, text=',', command=lambda: press(','), **layout)
    coma.grid(row=3, column=8)

    Tan= Button(gui, text='tan', command=lambda: press('ftan('), **layout)
    Tan.grid(row=1, column=2)

    Sin= Button(gui, text='sin', command=lambda: press('fsin('), **layout)
    Sin.grid(row=1, column=0)
    
    Cos= Button(gui, text='cos', command=lambda: press('fcos('), **layout)
    Cos.grid(row=1, column=1)

    Taninv= Button(gui, text='tan⁻¹', command=lambda: press('arctan('), **layout)
    Taninv.grid(row=2, column=2)

    Sininv= Button(gui, text='sin⁻¹', command=lambda: press('arcsin('), **layout)
    Sininv.grid(row=2, column=0)
    
    Cosinv= Button(gui, text='cos⁻¹', command=lambda: press('arccos('), **layout)
    Cosinv.grid(row=2, column=1)
    
    Logarithm= Button(gui, text='log', command=lambda: press('Log('), **layout)
    Logarithm.grid(row=3, column=1)

    inversenum= Button(gui, text='1/x', command=lambda: press('1÷'), **layout)
    inversenum.grid(row=3, column=2)

    exponentiation = Button(gui, text='xʸ', command=lambda: press('^('), **layout)
    exponentiation.grid(row=4, column=2)

    Ex = Button(gui, text='eˣ', command=lambda: press('e^'), **layout)
    Ex.grid(row=4, column=0)

    mod = Button(gui, text='|x|', command=lambda: press('abs('), **layout)
    mod.grid(row=5, column=0)

    Pi = Button(gui, text='π', command=lambda: press('π'), **layout)
    Pi.grid(row=5, column=1)

    E = Button(gui, text='e', command=lambda: press('e'), **layout)
    E.grid(row=5, column=2)

    Ln= Button(gui, text='ln', command=lambda: press('ln('), **layout)
    Ln.grid(row=3, column=0)

    per= Button(gui, text='%', command=percent, **layout)
    per.grid(row=1, column=6)
    per.configure(fg = "lime green", font = ("arial, 20"))

    obrac= Button(gui, text='(', command=lambda: press('('), **layout)
    obrac.grid(row=5, column=8)

    cbrac= Button(gui, text=')', command=lambda: press(')'), **layout)
    cbrac.grid(row=4, column=8)

    fact= Button(gui, text='!', command=lambda: press('!'), **layout)
    fact.grid(row=3, column=8)
    
    rad = Button(gui, text=' √ ', command=radical, **layout)
    rad.grid(row=2, column=8)

    backspace = Button(gui, text='⌫', command=backspace, **layout)
    backspace.grid(row=1, column=8)
    backspace.configure(fg = "lime green")
    # start the GUI
    gui.mainloop()
