
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
    # the first things executed first becuase it cascades down last
    print()
    print(f"solving {x}")
    assert type(x)==(str or int)
    
    
    # evaluates the result of stuff
    # pemdas
    # ()
    # !
    # * / %
    # + -
    # < <= > >=
    # == !=
    # = += -= *= /= %= &bitwise
    # (2+2)*8

    count = 0
    dummy = []
    for char in x:# this generates a list of tokens not in parenthesis
        if char is "(": count+=1

        if count==0: dummy.append(char)
        else: dummy.append("#")
        
        if char is ")": count-=1
        
        
    print(f"dummy list: {dummy}")
    
            
    if ("<" in dummy) or ("<=" in dummy) or (">" in dummy) or (">=" in dummy):# if this level is present, evaluate it
        first = 0
        token = None
        if "<=" in dummy:# this will  read <= before <
            first = dummy.index("<=")
            token = "<="
        elif "<" in dummy:
            first = dummy.index("<")
            token = "<"
        if ">=" in dummy:
            first = dummy.index(">=")
            token = ">="
        elif ">" in x:
            first = dummy.index(">")
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

    elif ("+" in dummy) or ("-" in dummy):# if this level is present, evaluate it
        print("+ or - is present in the problem")
        first = 0
        token = None
        if "+" in dummy:
            first = dummy.index("+")
            token = "+"
        if "-" in dummy:
            first = dummy.index("-")
            token = "-"
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if token=="+": return a+b
        if token=="-": return a-b
    
    elif ("*" in dummy) or ("/" in dummy) or ("%" in dummy):# if this level is present, evaluate it
        print("* or / or % is in the problem")
        first = 0
        token = None
        if "*" in dummy:
            first = dummy.index("*")
            token = "*"
        if "/" in dummy:
            first = dummy.index("/")
            token = "/"
        if "%" in dummy:
            first = dummy.index("%")
            token = "%"
        print(f"the token is {token}")
        a = x[0:first]
        print(f"solving {a}")
        a = solve(a)
        print(f"a solved to {a}")
        b = x[first+1:]
        print(f"solving {b}")
        b = solve(b)
        print(f"b solved to {b}")
        if token=="*": return a*b
        if token=="/": return a/b
        if token=="&": return a%b
    
    elif "!" in dummy:
        first = dummy.index("!")
        a = x[0:first]
        a = solve(a)
        b = x[first+1:]
        b = solve(b)
        if b!=0: return 0
        elif b==0: return 1
        else: print("hooray for boobies")
    
    if ("(" in x) or (")" in x):
        print(f'{x}  contains parenthesis')
        x = list(x)
        print(x)
        if x.count("(") != x.count(")"): raise Exception('unclosed parenthesis')
        first = x.index("(")
        open = 1
        end = None
        sample = x[first+1:]# everything after the first parenthesis
        print(f"the sample is {sample}")
        for position, char in enumerate(sample):
            print(f"the char is {char}")
            print(f"the position is {position}")
            if char=="(": open+=1
            if char==")": open-=1
            if open==0:
                contents =  sample[:position]
                end = position
                break
        print(f"the contents are {contents}")

        contents = ''.join(contents)
        contents = solve(contents)
        contents = str(contents)
        print(f"returning the contents as {contents}")
        a = ''.join( x[:first] )
        b = ''.join( sample[end+1:] )
        out = solve(a + contents + b)
        return  out# each item needs to be a string

    elif x.isdigit():
        print(f'{x}  is a digit')
        return int(x)
    
    elif x in variables.keys():
        return variables[x]

    else: raise Exception("no contents")

def REM(x):# comment command, REMARK
    return None
def LET(x):# variable assignment
    statements = x.split(",")
    for assignment in statements:
        var, value = assignment.split("=")
        value = solve(value)
        print(f"the value is {value}")
        if var in variables.keys():# if assigning to one of the 26 variables
            variables[var] = value
            print(f"set {var} to the value {value}")
        elif "@" in var:# assigning to the list
            if type(value) is str: value = list(value)
            if type(value): value = [value]
            print(f"the value is {value}")
            start = var.index("(")
            end = var.index(")")
            length = len(value)
            argument  = var[start+1:end]
            argument = solve(argument)# evaluates the position expression
            registry[argument:argument+length+1] = value
        else: raise Exception("that is not a valid assignment statement")
        

def PRINT(x):# prints to console
    x = ''.join(x)
    return solve(x)
def INPUT(x):# takes user input
    pass
def IF(x):# conditional
    pass
    """
    condition, body = x.split(":")
    condition = solve(condition)
    if condition==0: return "hi"
    if condition>0: return body
    """
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


def interpret(command):
    command = command.upper()
    command = command.strip()
    command = command.split(" ")
    funct, *body = command
    body = ''.join(body)
    if funct in functions.keys():
        output =  functions[funct](body)
        if output != None: return output
        else: return None
    
    command = ''.join(command)
    print(f"the command is {command}")
    return solve(command)