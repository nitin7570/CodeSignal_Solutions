def validTime(time):
    hours, minutes = time.split(':')
    if int(hours) in range(0, 24) and int(minutes) in range(0, 60):
        return True
    else:
        return False


if __name__ == "__main__":
    print(validTime('13:58'))
