import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("190x140") 

label = 0
number = 0
op = None
def CE():
  global label,number,op
  label = 0
  output["text"] = label
def choice(number):
  global label
  if label > 0:
    label = str(label)+str(number)
    label = int(label)
  else:
    label = number
  output["text"]=label
def defCalc(cal):
  global number,label,op
  number = label
  op = cal
  print(f"{label}{cal}")
  label = 0
  output["text"]=label
def equal():
  global number,label,op
  print(f"{number}{op}{label}")
  if op == "+":
    total = number + label
    label = total
  elif op == "-":
    total = number - label
    label = total
  elif op == "*":
    total = number * label
    label = total
  elif op == "/":
    total = number / label
    label = total
  output["text"]=label
  
  

  


output = tk.Label(text = label)
output.grid(row = 0, column = 4)
button9 = tk.Button(text = "9", command = lambda: choice(9))
button9.grid(row = 1, column = 0)
button8 = tk.Button(text = "8", command = lambda: choice(8))
button8.grid(row = 1, column = 1)
button7 = tk.Button(text = "7", command = lambda: choice(7))
button7.grid(row = 1, column = 2)
button6 = tk.Button(text = "6", command = lambda: choice(6))
button6.grid(row = 2, column = 0)
button5 = tk.Button(text = "5", command = lambda: choice(5))
button5.grid(row = 2, column = 1)
button4 = tk.Button(text = "4", command = lambda: choice(4))
button4.grid(row = 2, column = 2)
button3 = tk.Button(text = "3", command = lambda: choice(3))
button3.grid(row = 3, column = 0)
button2 = tk.Button(text = "2", command = lambda: choice(2))
button2.grid(row = 3, column = 1)
button1 = tk.Button(text = "1", command = lambda: choice(1))
button1.grid(row = 3, column = 2)
button0 = tk.Button(text = "0", command = lambda: choice(0))
button0.grid(row = 4, column = 1)
buttonPlus = tk.Button(text = "+", command = lambda: defCalc("+"))
buttonPlus.grid(row = 1, column = 3)
buttonMinus = tk.Button(text = "-", command = lambda: defCalc("-"))
buttonMinus.grid(row = 1, column =4)
buttonMult = tk.Button(text = "*", command = lambda: defCalc("*"))
buttonMult.grid(row = 2, column =3)
buttonDiv = tk.Button(text = "/", command = lambda: defCalc("/"))
buttonDiv.grid(row = 2, column =4)
buttonEq = tk.Button(text = "=", command = equal)
buttonEq.grid(row = 4, column =3)
buttonCE = tk.Button(text = "CE", command = CE)
buttonCE.grid(row = 4, column =4)
