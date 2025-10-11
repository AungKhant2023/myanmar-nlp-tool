import os
import unicodedata
import re

def normalize(text):
    return unicodedata.normalize("NFC", text)

def load_dictionary(file_path="dict-output-v1-18-6-2025.txt"):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return sorted([normalize(line.strip()) for line in f if line.strip()], key=len, reverse=True)

def is_myanmar_word(text):
    return all('\u1000' <= char <= '\u109F' or char in "ါ-ှ" for char in text if char.strip())

def is_number(text):
    # English numbers or Myanmar numbers
    return re.fullmatch(r"[0-9၀-၉]+([.,][0-9၀-၉]+)?", text) is not None

def segment_myanmar_text(text, dictionary):
    output = ""
    i = 0
    while i < len(text):
        matched = False
        for word in dictionary:
            if text[i:].startswith(word):
                output += word + " "
                i += len(word)
                matched = True
                break
        if not matched:
            output += text[i] + " "
            i += 1
    return output

# def syllable_tokenization(input_text: str) -> str:
#     input_text = normalize(input_text.strip())
#     dictionary = load_dictionary()

#     pattern = r'[\u1000-\u109F\uAA60-\uAA7F\uA9E0-\uA9FF]+|[a-zA-Z]+|[0-9၀-၉]+(?:[.,][0-9၀-၉]+)?|[^\s\w]'

#     parts = re.findall(pattern, input_text)

#     result = ""
#     for part in parts:
#         part = normalize(part)
#         if is_number(part):
#             result += part + " "
#         elif is_myanmar_word(part):
#             result += segment_myanmar_text(part, dictionary)
#         else:
#             result += part + " "

#     return result.strip()

def syllable_tokenization(input_text: str) -> str:
    input_text = normalize(input_text.strip())
    dictionary = load_dictionary()

    pattern = r'[\u1000-\u109F\uAA60-\uAA7F\uA9E0-\uA9FF]+|[a-zA-Z]+|[0-9၀-၉]+(?:[.,][0-9၀-၉]+)?|[^\s\w]'

    # Split input into lines to preserve sentence structure
    lines = input_text.splitlines()
    tokenized_lines = []

    for line in lines:
        line = normalize(line.strip())
        parts = re.findall(pattern, line)

        result_line = ""
        for part in parts:
            part = normalize(part)
            if is_number(part):
                result_line += part + " "
            elif is_myanmar_word(part):
                result_line += segment_myanmar_text(part, dictionary)
            else:
                result_line += part + " "
        tokenized_lines.append(result_line.strip())

    return '\n'.join(tokenized_lines)
