numbers_of_players=input()
players=list(set(list(map(int,(input().split())))))
players.sort()
numbers_of_games=int(input())
scores=list(map(int,(input().split())))
l=len(players)
i=0
for score in scores:
    while i<l and players[i]<=score:
        i+=1
    print(l-i+1)