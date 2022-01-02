# https://leetcode.com/problems/evaluate-reverse-polish-notation/
OPERATOR = ("+", "-", "*", "/")


def calculate(postfix_notation: str) -> int:
    stack = []
    for s in postfix_notation.split():
        value = None
        if not is_operator(s):
            value = int(s)
        else:
            r_value = stack.pop()
            l_value = stack.pop()
            expression = f"{l_value}{s}{r_value}"
            value = int(eval(expression))
        stack.append(value)

    return stack[0]


def is_operator(s: str) -> bool:
    return s in OPERATOR


# keep this function call here
print(calculate(input()))
