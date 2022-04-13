variables = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0,
    "Z":0
}
registry  = [0]*2048

master_program_pointer = 0
subroutine_pointers = []


def solve(x):# this just might be the least elegant code I've ever written
    assert type(x)==(str or int)
    print()
    print(f"solving {x}")
    # evaluates the result of stuff
    # pemdas
    # ()
    # !
    # * / %
    # + -
    # < <= > >=
    # == !=
    # = += -= *= /= %= &bitwise
    if x.isdigit():
        print(f'{x}  is a digit')
        return int(x)
    if "!" in x:
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if b!=0: return 0
        elif b==0: return 1
        else: print("hooray for boobies")

    elif ("*" in x) or ("/" in x) or ("%" in x):# if this level is present, evaluate it
        print("* or / or % is in the problem")
        first = 0
        token = None
        if "*" in x:
            first = x.index("*")
            token = "*"
        if "/" in x:
            first = x.index("/")
            token = "/"
        if "%" in x:
            first = x.index("%")
            token = "%"
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if token=="*": return a*b
        if token=="/": return a/b
        if token=="&": return a%b

    elif ("+" in x) or ("-" in x):# if this level is present, evaluate it
        print("+ or - is present in the problem")
        first = 0
        token = None
        if "+" in x:
            first = x.index("+")
            token = "+"
        if "-" in x:
            first = x.index("-")
            token = "-"
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if token=="+": return a+b
        if token=="-": return a-b

    elif ("<" in x) or ("<=" in x) or (">" in x) or (">=" in x):# if this level is present, evaluate it
        first = 0
        token = None
        if "<=" in x:# this will  read <= before <
            first = x.index("<=")
            token = "<="
        elif "<" in x:
            first = x.index("<")
            token = "<"
        if ">=" in x:
            first = x.index(">=")
            token = ">="
        elif ">" in x:
            first = x.index(">")
            token = ">"
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if token=="<=":
            if a<=b: return 1
            else: return 0
        if token=="<":
            if a<b: return 1
            else: return 0
        if token==">=":
            if a>=b: return 1
            else: return 0
        if token==">":
            if a>b: return 1
            else: return 0
    
    else: return x

def REM(x):# comment command, REMARK
    return None
def LET(x):# variable assignment
    solve(x)

def PRINT(x):# prints to console
    print('printing')
    x = ''.join(x)
    return solve(x)
def INPUT(x):# takes user input
    pass
def IF(x):# conditional
    pass
def GOTO(x):# sends program execution line specified
    pass
def GOSUB(x):# equivalent of a function call, temporarily sends execution to a separate section
    pass
def RETURN(x):# returns from a GOSUB call
    pass
def FOR(x):
    pass
def NEXT(x):
    pass
def STOP(x):
    pass
def RUN(x):
    pass

functions = {
    "REM":REM,
    "LET":LET,
    "PRINT":PRINT,
    "INPUT":INPUT,
    "IF":IF,
    "GOTO":GOTO,
    "GOSUB":GOSUB,
    "RETURN":RETURN,
    "FOR":FOR,
    "NEXT":NEXT,
    "STOP":STOP,
    "RUN":RUN,

}


def intepret(command):
    print('intepreting')
    command = command.upper()
    command = command.strip()
    command = command.split(" ")
    funct, *body = command
    if funct in functions.keys():
        output =  functions[funct](body)
        if output != None: return output
        else: return None
    
    command = ''.join(command)
    print(f"the command is {command}")
    return solve(command)