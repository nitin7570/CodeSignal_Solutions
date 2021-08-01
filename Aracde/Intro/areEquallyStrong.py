def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft + yourRight) == (friendsLeft + friendsRight) and (yourLeft == friendsLeft or yourLeft == friendsRight)


if __name__ == "__main__":
    print(areEquallyStrong(10,15,15,10))
