def findEmailDomain(address):
    return(address.split('@').pop())


if __name__ == "__main__":
    print(findEmailDomain('prettyandsimple@example.com'))
