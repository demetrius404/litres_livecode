
def build_str(char_list: list[str], multiplier: int) -> str:
    char_list.reverse()
    return "".join(char_list) * multiplier


def stack_processing(stack: list) -> str:
    char_list = []  # empty list
    while len(stack):
        stack_value = stack.pop()
        if isinstance(stack_value, int):
            return build_str(char_list, stack_value)
        else:
            char_list.append(stack_value)


def solution(expression: str) -> str:

    multiplier = 1  # default
    stack = [multiplier]  # init

    for char in expression:
        if char.isdigit():
            multiplier = int(char)
            continue
        elif char == "[":
            stack.append(multiplier)
            multiplier = 1  # drop to default
            continue
        elif char == "]":
            stack.append(stack_processing(stack))
        else:
            stack.append(char)
    return stack_processing(stack)
