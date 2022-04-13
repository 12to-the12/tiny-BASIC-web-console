

from browser import document
#from browser.html import DIV, BR
print('arrived at web main')
#header = """Greetings stranger!"""
rendered_lines = 5 # not including console
readout = document["readout"] # this refers to the readout div
console_lines = [' ']*rendered_lines# running list of every line printed to the console

def pprint(new_text=" ", command=False):

    # this parts prepares the command, then adds the new text to the console list
    new_text = str(new_text)
    new_text = new_text.split('\n')
    if command: new_text[0] = ">> " + new_text[0]
    console_lines.extend(new_text)

    # this parts prepares a part of the console to be written
    #print(f"full console_lines:{console_lines}")
    console_out = console_lines[-rendered_lines:]
    #print(f"curated console_lines:{console_out}")
    console_out = "\n".join(console_out)
    #print(f"formed:{console_out}")
    

    readout.clear()
    #readout <= header
    #readout <= '\n'
    readout <= console_out
    readout <= ' '

pprint()



def keypress(ev):# every time the enter key is pressed, pprint the console contents, execute it, then clear it
    if ev.code == "Enter":
        pprint(console.value, command=True)
        execute(console.value)
        console.value = ""

def scroll(ev):
    if ev.code == "KeyUp":
        pprint("upKey")



console = document["console"] # this refers to the console input field
console.bind("keyup", keypress)
console.bind("keypress", scroll)

from  intepreter import interpret

def execute(command):

    try: response = interpret(command)
    except Exception as ex: response = ex
    if response!=None:
        pprint(response)