def maximumMeetings(n, start, end):
    activity = []
    for i in range(n):
        activity.append([start[i], end[i]])

    activity.sort(key = lambda x: x[1])
    count = 1
    i = 0
    for j in range(1, n):
        if activity[j][0] > activity[i][1]:
            count += 1
            i = j

    return count



s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 0 , 7 , 3 , 9]
print(maximumMeetings(len(s), s, f))