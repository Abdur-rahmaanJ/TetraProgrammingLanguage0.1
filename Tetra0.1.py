remove_quotes = lambda x: x

OPERATORS = ['+', '-', '/', '%', '*', '(', ')']

from random import randint

ARBITRARY_LARGE_NUM = 2 ** 32

def perform_eval(command):
    try:
        print integerize(str(eval(command.replace("pow", "**").replace("0.0.0", "0").replace("1.0.0", "1"))))
    except ZeroDivisionError:
        x = eval(command.replace("0.0", "0.01"))
        if x < 0:
            print "-infinity"
        else:
            print "infinity"

def is_evalable(code_line):
    code_line = remove_quotes(code_line)
    code_line = code_line.replace("pow", "")
    for char in code_line:
        if ord(char) in range(ord('a'), ord('z')) or ord(char) in range(ord('A'), ord('Z')):
            return False
    return not("=" in code_line or "if" in code_line)

def safe_to_float(number_str):
    try:
        return float(number_str)
    except ValueError:
        return number_str

def integerize(number_str):
    num_str2 = number_str[:-2] if number_str.endswith(".0") else number_str
    return "0" if float(num_str2) == 0.0 else num_str2

def infinify(x):
    return "(1.0 / 0.0)" if x == "infinity" else safe_to_float(x)

def read_eval_print_loop():
    while True:
        print "(Tetra 0.1)",
        command = raw_input()
        command = command.replace("\t", " ")
        command = command.replace("**", " pow ")
        for op in OPERATORS:
            command = command.replace(op, " " + op + " ")
        for _ in range(12):
            command = command.replace("  ", " ")
        # print "COM", command
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
        if is_evalable(command):
            perform_eval(command)
        else:
            perform_eval(command)

read_eval_print_loop()
