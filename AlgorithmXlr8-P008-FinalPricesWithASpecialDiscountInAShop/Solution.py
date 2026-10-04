def main(n):
    stk=[]
    for i in range(n):
        while stk and prices[stk[-1]] >= prices[i]:
            prices[stk.pop()]-=prices[i]
        stk.append(i)
    return " ".join(map(str,prices))
   
        


   


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    print(main(n))
