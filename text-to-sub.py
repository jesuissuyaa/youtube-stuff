
CHANNEL_NAME = "わんぽけ"

# open file
f = open("text.txt", "r")
txt = f.read()
f.close()

lines = txt.splitlines()
txt = ""

# move to beginning of speech i.e. channel name
i = 0
for line in lines:
    if CHANNEL_NAME in line:
       break
    i = i + 1

# remove comment lines
for line in lines[i:]:   
    if not line.startswith('#'):
        txt = txt + line + '\n'

# write to file
f = open(f'sub.txt', "w")
f.write(txt)
f.close()