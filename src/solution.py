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
    stack = [1]  # built-in list uses like a stack

    prev = None
    for char in expression:
        if char == "[":
            if prev and prev.isdigit():
                stack.pop()
                stack.append(int(prev))
                prev = char
            else:
                stack.append(1)
            continue
        elif char == "]":
            stack.append(processing(stack))
        else:
            stack.append(char)
            prev = char

    return processing(stack)
