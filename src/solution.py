
def build_str(char_list: list[str], multiplier: int) -> str:
    char_list.reverse()
    return "".join(char_list) * multiplier


def stack_processing(stack: list) -> str:
    temporary_list = []  # empty list
    while True:
        stack_value = stack.pop()
        if isinstance(stack_value, int):
            return build_str(temporary_list, stack_value)
        else:
            temporary_list.append(stack_value)


def solution(source_sequence: str) -> str:

    multiplier = 1  # default
    stack = [multiplier]

    for ch in source_sequence:
        if ch.isdigit():
            multiplier = int(ch)
            continue
        elif ch == "[":
            stack.append(multiplier)
            multiplier = 1
            continue
        elif ch == "]":
            stack.append(stack_processing(stack))
        else:
            stack.append(ch)
    return stack_processing(stack)
