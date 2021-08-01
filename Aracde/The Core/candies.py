def candies(n, m):
    if m < n: return 0
    
    count = 0
    
    while(m >= n):
        m = m - n
        print(m)
        count += 1
        
    return count*n


if __name__ == "__main__":
    print(candies(3, 10))
