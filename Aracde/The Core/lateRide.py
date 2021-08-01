def lateRide(n):
    
    hours = n // 60

    minutes = n % 60
    
    if hours < 10:
        hours = '0' + str(hours)
    
    if minutes < 10:
        minutes = '0' + str(minutes)

    time_string = "{}{}".format(hours, minutes)

    return(sum(list(map(int, time_string))))


if __name__ == "__main__":
    print(lateRide(240))
