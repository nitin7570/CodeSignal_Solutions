def depositProfit(deposit, rate, threshold):
    count = 0
    while(deposit < threshold):
        deposit += deposit * (rate/100)
        count += 1
    return count


if __name__ == "__main__":
    print(depositProfit(100, 20, 170))
