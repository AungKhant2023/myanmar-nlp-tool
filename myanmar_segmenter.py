import re

def load_wordlist(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f.readlines())

def rmm_segment(text, dictionary, max_len=10):
    result = []
    i = len(text)
    while i > 0:
        matched = False
        for l in range(max_len, 0, -1):
            if i - l < 0:
                continue
            chunk = text[i - l:i]
            if chunk in dictionary:
                result.append(chunk)
                i -= l
                matched = True
                break
        if not matched:
            result.append(text[i-1])
            i -= 1
    return list(reversed(result))

# Function to check if a character is Myanmar (Burma) Unicode
def is_myanmar(char):
    return '\u1000' <= char <= '\u109F' or '\uAA60' <= char <= '\uAA7F'