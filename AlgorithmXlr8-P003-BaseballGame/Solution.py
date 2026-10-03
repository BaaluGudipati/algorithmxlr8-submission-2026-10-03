def main(ops):
    stack = []

    for i in ops:

        if i == "C":
            stack.pop()

        elif i == "D":
            stack.append(stack[-1] * 2)

        elif i == "+":
            stack.append(stack[-1] + stack[-2])

        else:
            stack.append(int(i))

    return sum(stack)


if __name__ == "__main__":
    n = int(input())
    ops = [input().strip() for _ in range(n)]

    print(main(ops))