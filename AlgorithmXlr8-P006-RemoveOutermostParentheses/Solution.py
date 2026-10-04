def main(s):
    depth=0
    res=""
    for i in s:
        if i == "(":
            if depth >0 :
                res+=i 
            depth+=1 
        else:
            depth-=1
            if depth > 0:
                res+=i
    return res 
    


if __name__ == "__main__":
    s = input().strip()
    result = main(s)

    if result == "":
        print("(empty)")
    else:
        print(result)
    
