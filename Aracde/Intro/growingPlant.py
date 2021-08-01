def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 1
    height += upSpeed
    while height < desiredHeight:
        days += 1
        height -= downSpeed
        height += upSpeed
    return days


if __name__ == "__main__":
    print(growingPlant(100, 10, 910))
