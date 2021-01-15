import re
import json

# set pause length
PAUSE_WHITESPACE = 0.1
PAUSE_NEWLINE = 0.2
PAUSE_PERIOD = 0.8
PAUSE_COMMA = 0.2
# PAUSE_PARAGRAPH = 1.0


CHANNEL_NAME = "わんぽけ"
MAX_CHARS = 800

# check if string contains only hiragana & space
def is_hiragana_sentence(str):
    if " " not in str:
        return False
    re_hiragana = re.compile(r'^[あ-ん 。]+$')
    return re_hiragana.fullmatch(str)

def markup(txt):
    # wrap with tags
    txt = "<speak>" + txt + "</speak>"

    # wrap hiragana-only sentence lines
    # lines = txt.split('\n')
    # lines = map(lambda x: f'<s>{x}</s>' if is_hiragana_sentence(x) else x, lines)
    # txt = ('\n').join(lines)

    # add break tags
    txt = txt.replace(" ", f'<break time="{PAUSE_WHITESPACE}s" />')
    txt = txt.replace("\n", f'<break time="{PAUSE_NEWLINE}s" />')
    # txt = txt.replace("。", f'<break time="{PAUSE_PERIOD}s" />')
    # txt = txt.replace("、", f'<break time="{PAUSE_COMMA}s" />')
    # txt = txt.replace("\n\n", f'<break time="{PAUSE_PARAGRAPH}s" />')

    # load lexicon by x-amazon-pron-kana
    f = open('lexicon-kana.json')
    data = json.load(f)
    f.close()
    for lexeme in data:
        g = lexeme['grapheme']
        p = lexeme['phoneme']
        txt = txt.replace(g, f'<phoneme alphabet="x-amazon-pron-kana" ph="{p}">{g}</phoneme>')
    
    # txt = txt.replace("フシギバナ", '<phoneme alphabet="x-amazon-pron-kana" ph="フ\'シギバナ">フシギバナ</phoneme>')

    # other rules
    txt = txt.replace("DX", f'<w>DX</w>')
    # replace space with commas for titles
    titles = re.findall(r'『.+?』', txt)
    for t in titles:
        t2 = t.replace(" ", "、")
        txt = txt.replace(t, t2)
    return txt


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
    if not line.startswith(('#', '＃')):
        txt = txt + line + '\n'

lines = txt.splitlines()

file_index = 1
line_index = 0
while line_index < len(lines):
    txt_out = ""
    while(len(txt_out) < MAX_CHARS and line_index < len(lines)):
        txt_out += lines[line_index] + '\n'
        line_index += 1

    # markup
    txt_out = markup(txt_out)

    # write to file
    f = open(f'ssml-{file_index}.txt', "w")
    f.write(txt_out)
    f.close()

    # update indices
    file_index += 1
    
print('DONE!')