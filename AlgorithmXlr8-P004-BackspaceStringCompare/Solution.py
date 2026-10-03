def main(s,t):
    stk1=[]
    stk2=[]
    for i in s:
        if i == "#":
            stk1.pop()
        else:
            stk1.append(i)
    for j in t:
        if j =="#":
            stk2.pop()
        else:
            stk2.append(j)
    return stk1 == stk2

    

   


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(str(main(s,t)).lower())
