def isValid(s):
    stack = []

    for ch in s:

        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)

        else:
        
            if ch == ")" and stack[-1] == "(":
                stack.pop()
            elif ch == "]" and stack[-1] == "[":
                stack.pop()
            elif ch == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    s = input()
    print(str(isValid(s)).lower())