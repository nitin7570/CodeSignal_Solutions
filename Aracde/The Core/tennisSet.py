def tennisSet(score1, score2):
    mins, maxs = (min(score1, score2), max(score1, score2))
    return (maxs == 6 and mins < 5) or (maxs == 7 and mins in (5,6))


if __name__ == "__main__":
    print(tennisSet(3, 6))
