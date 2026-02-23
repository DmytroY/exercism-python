def is_paired(input_string) -> bool:
    stack = []
    for c in input_string:
        if(c in {"{", "[", "("}):
            stack.append(c)
        if(c in {"}", "]", ")"}):
            if not stack:
               return False
            s = stack.pop()
            if(c == "}" and s != "{"):
                return False
            if(c == "]" and s != "["):
                return False
            if(c == ")" and s != "("):
                return False
    if len(stack):
        return False
    return True
