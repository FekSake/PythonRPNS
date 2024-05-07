import os

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        value = self.stack[-1]
        self.stack.pop(-1)

        return value

    def isEmpty(self):
        return len(self.stack) == 0

    def isFinished(self):
        return isinstance(self.stack[0], (int, float)) and len(self.stack) == 1


def solverpn(rpn):
    def isNum(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    s = Stack()
    if isinstance(rpn, str):
        rpn = rpn.split()
    elif isinstance(rpn, list):
        ...
    else:
        TypeError("Invalid rpn type")
    inBracket = 0
    for value in rpn:
        value = str(value)
        if isNum(value):
            s.push(float(value))
        elif value in "+-*/^" and inBracket == 0:
            operand2 = s.pop()
            operand1 = s.pop()
            if value == '+':
                s.push(operand1 + operand2)
            elif value == '-':
                s.push(operand1 - operand2)
            elif value == '*':
                s.push(operand1 * operand2)
            elif value == '/':
                s.push(operand1 / operand2)
            elif value == "^":
                s.push(operand1 ** operand2)

        elif value in "+-*/^" and inBracket != 0:
            s.push(value)

        elif value == '(':
            s.push(value)
            inBracket += 1

        elif value == ')':
            def findAllStartingBrackets(stack):
                brackets = []
                for n in range(len(stack)):
                    s = stack[n]
                    if s == "(":
                        brackets.append(n)
                return brackets
            
            newrpn = s.stack[findAllStartingBrackets(s.stack)[inBracket-1]+1:rpn.index(")")]
            result = solverpn(newrpn)

            while s.stack[-1] != "(":
                s.pop()
            s.pop()
            s.push(result)
            inBracket -= inBracket

        else:
            raise ValueError("Invalid value: " + value)

    return s.pop()

os.system("cls|title RPNS // Made by FekSake" if os.name == "nt" else "clear")

def gradient_text(text, start_color, end_color):
    gradient_text = ""
    color_step = len(text) / (len(text) - 1)
    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / (len(text) - 1)))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / (len(text) - 1)))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / (len(text) - 1)))
        gradient_text += f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"
    return gradient_text

text = """
 ____   ____   _   _  ____  
|  _ \ |  _ \ | \ | |/ ___| 
| |_) || |_) ||  \| |\___ \ 
|  _ < |  __/ | |\  | ___) |
|_| \_\|_|    |_| \_||____/ 
    
"""
start_color = (255, 0, 0)  # Red
end_color = (0, 0, 255)    # Blue

gradient_colored_text = gradient_text(text, start_color, end_color)
print(gradient_colored_text)

print(f"Reverse Polish Notation Solver")
print(f"https://github.com/FekSake/PythonRPNS")
print(f"Avalible operations...\n+ for adding\n- for subtracting\n/ for dividing\n* for multiplication\n^ for powers\nAnd brackets ()")
print(f"USAGE : Enter your reverse polish notation string, for example \" -> 5 2 / 1 + 2 ^\" and get the answer!")
print(f"{' '*len('USAGE : Enter your reverse polish notation string, for example ')}\"Result : 12.5    \"")
rpn = input(f"Input a reverse polish notation string...\nNOTICE : Make sure all numbers, operaters and brackets are seperated by a space...\n\n -> ")

print(f"Calculating {rpn}")
result = solverpn(rpn)
print(f"Result : {result}")
