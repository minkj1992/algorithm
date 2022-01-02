"""
Arith geo

Have the function arithGeo(arr) take the array of numbers stored in arr and
return the string "Arithmetic" if the sequence follows an arithmetic pattern
or return "Geometric" if it follows a geometric pattern. If the sequence
doesn't follow either pattern return -1. An arithmetic sequence is one where
the difference between each of the numbers is consistent, where as in a
geometric sequence, each term after the first is multiplied by some constant
or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2,
6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be
entered, and no array will contain all the same elements.

 @param  {array} arr
 @return {string} (if negative string should add "negative")
"""

from typing import Optional


NUMBERS = list(range(10))
WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
OPERATORS = {"minus": "-", "plus": "+"}
N2W = {n: w for n, w in zip(NUMBERS, WORDS)}
W2N = {w: n for w, n in zip(WORDS, NUMBERS)}


def string_challenge(raw_input: str) -> str:
    n = len(raw_input)
    start = 0
    count = 0
    word_len = (3, 4, 5)
    expr = ""
    for i in range(n + 1):
        if count in word_len:
            word = decode(raw_input[start:i])
            if word:
                expr += word
                count = 0
                start = i
        count += 1
    num = eval(expr)
    return encode(num)


def decode(string: str) -> Optional[str]:
    if string in OPERATORS:
        return OPERATORS[string]
    if string in W2N:
        return str(W2N[string])
    return None


def encode(num: int):
    string_num = ""
    for n in str(num):
        if n == "-":
            string_num += "negative"
            continue
        string_num += N2W[int(n)]
    return string_num


# keep this function call here
print(string_challenge(input()))
