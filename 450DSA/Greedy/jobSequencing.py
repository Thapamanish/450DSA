class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def maxProfit(jobs, t):
    profit = 0
    slot = [-1] * t
    jobs.sort(key = lambda x: x.profit, reverse = True)

    count = 0
    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j <= t and slot[j - 1] == -1:
                slot[j - 1] = job.id
                profit += job.profit
                count += 1
                break


    return profit, count

# jobs = [
#     Job(1, 9, 25), Job(2, 2, 2),
#     Job(3, 5, 18), Job(4, 7, 1),
#     Job(5, 4, 15), Job(6, 2, 20),
#     Job(7, 5, 8), Job(8, 7, 10),
#     Job(9, 4, 12), Job(10, 3, 5)
# ]

jobs = [Job(1,4,20),
        Job(2,1,10),
        Job(3,1,40),
        Job(4,1,30)]

t = float('-INF')
for job in jobs:
    if job.deadline > t:
        t = job.deadline


print(*maxProfit(jobs, t))