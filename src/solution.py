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

    multiplier = 1  # default
    stack = [multiplier]  # built-in list uses like a stack

    for char in expression:
        if char.isdigit():
            multiplier = int(char)
            continue
        elif char == "[":
            stack.append(multiplier)
            multiplier = 1  # drop to default
            continue
        elif char == "]":
            stack.append(processing(stack))
        else:
            stack.append(char)

    return processing(stack)
