def reachNextLevel(experience, threshold, reward):
    return (experience + reward) >= threshold


if __name__ == "__main__":
    print(reachNextLevel(10, 15, 5))
