def build_str(char_list: list[str], multiplier: int) -> str:
    char_list.reverse()
    return "".join(char_list) * multiplier


def processing(stack: list) -> str:
    char_list = []  # empty list
    while len(stack):
        value = stack.pop()
        if isinstance(value, int):  # this is multiplier
            return build_str(char_list, value)
        else:
            char_list.append(value)


def solution(expression: str) -> str:

    # init
    multiplier_default = 1
    stack = [multiplier_default]  # built-in list uses like a stack

    for char in expression:
        if char == "[":
            peek = stack[-1]
            if len(stack) and isinstance(peek, str) and peek.isdigit():
                stack.append(int(stack.pop()))
            else:
                stack.append(multiplier_default)
            continue
        elif char == "]":
            stack.append(processing(stack))
        else:
            stack.append(char)

    return processing(stack)
