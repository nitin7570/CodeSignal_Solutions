def electionsWinners(votes, k):
    count_winner = 0
    max_votes = max(votes)
    
    if k == 0 and votes.count(max_votes) == 1:
        return 1
    
    for vote in votes:
        if (vote + k) > max_votes:
            count_winner += 1
            
    return count_winner 


if __name__ == "__main__":
    print(electionsWinners([2, 3, 5, 2], 3))
