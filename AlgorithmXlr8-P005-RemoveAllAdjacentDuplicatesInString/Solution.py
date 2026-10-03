def main(s):
    stk=[]
    for i in s:
        if stk and stk[-1]==i:
            stk.pop()
        else:
            stk.append(i)
        
        
    return "".join(stk)    


if __name__ == "__main__":
    s=input().strip()
    print(main(s))
