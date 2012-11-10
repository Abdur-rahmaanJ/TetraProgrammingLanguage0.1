# Tetra Programming Language 0.1
# Written by Oliver Chu

original_float = float
def safe_to_float(number_str):
    try:
        return original_float(number_str)
    except ValueError:
        return number_str

environment = [{}]
eval2 = lambda x: eval(x, environment[-1])

length = lambda x: len(x) if hasattr(x, "__len__") else 1
size = length
car = lambda x: x[0] if hasattr(x, "__len__") and len(x) > 0 else "undefined"
cdr = lambda x: x[1:] if hasattr(x, "__len__") and len(x) > 0 else "undefined"
first = car
rest = cdr
float = safe_to_float

debug = False

remove_quotes = lambda x: x

OPERATORS = ['+', '-', '/', '%', '*', '(', ')', '{', '}', '[', ']', '^', '&', '|']

from random import randint

ARBITRARY_LARGE_NUM = 2 ** 32

def perform_eval2(command):
    try:
        if command in environment[-1] and callable(environment[-1][command]):
            pass    #print "function " + command
            return
        for key in environment[-1]:
            if " " in key:
                command = command.replace(key, str(environment[-1][key]))
        command = command.replace("pow", "**").replace("0.0.0", "0").replace("1.0.0", "1")
        command = command.replace("len(", "length(").replace("len (", "length(")
        command = command.replace(" is ", " == ")
        if debug:
            pass    #print "COMMAND: ", command
        eved = eval2(command)
        if type(eved) is str:
            pass    #print eved
        else:
            eved = str(iter_integerize(eved))
            eved = integerize(eved)
            pass    #print eved
    except ZeroDivisionError:
        x = eval2(command.replace("0.0", "0.01"))
        if x < 0:
            pass    #print "-infinity"
        else:
            pass    #print "infinity"

def is_evalable(code_line):
    code_line = remove_quotes(code_line)
    code_line = code_line.replace("pow", "")
    for char in code_line:
        if ord(char) in range(ord('a'), ord('z')) or ord(char) in range(ord('A'), ord('Z')):
            return False
    return not("=" in code_line or "if" in code_line)

def integerize(number_str):
    number_str = str(number_str)
    num_str2 = number_str[:-2] if number_str.endswith(".0") else number_str
    if float(num_str2) == 0.0:
        return 0
    try:
        return eval2(num_str2)
    except Exception as e:
        return "undefined"

def is_iterable(obj):
    return hasattr(obj, "__contains__")

def iter_integerize(iterable):
    if is_iterable(iterable) and not type(iterable) is str:
        original_type = type(iterable)
        lst = []
        for element in iterable:
            lst.append(integerize(element))
        return original_type(lst)
    return iterable        

def infinify(x):
    return "(1.0 / 0.0)" if x == "infinity" else safe_to_float(x)

def read_eval_print_loop():
    last_value = None;
    while True:
        pass    #print "(Tetra 0.1)",
        command = raw_input()
        if command.lower() == "meaning of life":
            pass    #print 42
            continue
        if "==" in command:
            pass    #print "Use operator is instead of ==."
            continue
        if "otherwise" in command:
            command = command.replace("otherwise", "else")
        command = command.replace("\t", " ")
        command = command.replace("**", " pow ")
        for op in OPERATORS:
            command = command.replace(op, " " + op + " ")
        for _ in range(12):
            command = command.replace("  ", " ")
        if "infinity" in command:
            command = command.replace("1 / infinity", "0.0").replace("1 / - infinity", "0.0")
            command = command.replace("1.0 / infinity", "0.0").replace("1.0 / - infinity", "0.0")
            rng = lambda: str(randint(-ARBITRARY_LARGE_NUM, ARBITRARY_LARGE_NUM))
            command = command.replace("0 * infinity", rng()).replace("infinity * 0", rng())
        tokens = command.split(" ")
        for i in range(len(tokens)):
            try:
                tokens[i] = infinify(tokens[i])
                tokens[i] = str(float(tokens[i]))
            except ValueError:
                pass
        command = " ".join(tokens)
        command = command.replace("anonymous", "lambda")
        command = command.replace(":", " = lambda ")
        command = command.replace("yields", ":")
        if "=" not in command:
            perform_eval2(command)
        else:
            if "=" in command:
                parts = command.split("=")
                variable_name = parts[0]
                value = parts[1]
                as_float = safe_to_float(variable_name)
                if variable_name == "undefined":
                    pass    #print "You cannot assign to undefined."
                # Warning: You reassigned float, so type(4.0) is float
                # is no longer True. You need to use original_float.
                elif type(as_float) is original_float:
                    pass    #print as_float == eval2(value)
                else:
                    actual_name = variable_name.strip()
                    answer = eval2(value)
                    environment[-1][actual_name] = eval2(value)
                    msg = actual_name + " is now " + str(integerize(answer))
                    if "now undefined" in msg:
                        pass    #print actual_name + " is now a function."
                    else:
                        pass    #print msg
                    #pass    #print environment
            else:
                perform_eval2(command)

from Tkinter import *
     
canvas = Canvas(width=630, height=470, bg='white')  
canvas.pack(expand=YES, fill=BOTH)                  
     
canvas.create_line(10, 10, 200, 200)              
     
     
widget = Label(canvas, text='', fg='white', bg='black')
widget.pack()
canvas.create_window(640, 480, window=widget)     
mainloop()
