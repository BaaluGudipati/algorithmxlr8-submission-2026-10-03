def main(n):
    res=0
    depth=0
    for i in logs:
        if i == "../":
            if depth >0:
                depth-=1 
            else:
                return depth
        elif i == "./":
            return depth 
        else:
            depth+=1 
    return depth
        
            
   

    
   


if __name__ == "__main__":
    n = int(input())
    logs = [input().strip() for _ in range(n)]

    print(main(n))
