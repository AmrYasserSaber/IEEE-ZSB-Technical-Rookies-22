import sys
def solution():
    result1 = 0
    counter1 = 0
    for ind in range(len(topic)-1):
        for jnd in range(ind+1, len(topic)):
            tmp = bin(int(topic[ind], 2) | (int(topic[jnd], 2))).count("1")
            if tmp > result1:
                result1 = tmp
                counter1 = 1
            elif tmp == result1:
                counter1 += 1

    return (result1, counter1)


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

print("\n".join(map(str, solution())))