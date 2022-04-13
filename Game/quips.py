text = """fuck you, fuck me yourself coward
politics, I'd rather die
war, peace
sex, war
peace, piece
win, lol
finish, nice try
test, looks like it's working?
xkcd, https://xkcd.com/
easter egg, https://venture-games.netlify.app/
hello, hi
hi, hello"""
text = text.split('\n')
quips = {}
for line in text:
    line = line.split(', ')
    key = line[0]
    value = line[1]
    quips[key] = value