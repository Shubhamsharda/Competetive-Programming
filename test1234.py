import heapq


def sortbydeadline(ls):
    return ls[-1]  # returns deadline for a job


def func():
    t = int(input())
    res_for_test_cases = []
    for i in range(t):
        n = int(input())
        jobs = []
        for j in range(n):
            jobtemp = input().split()
            jobs.append([int(i) for i in jobtemp])
        totrunningtime = 0
        totalmoney = 0
        jobs = jobs.sorted(key=sortbydeadline)
        priorityq = []
        heapq.heapify(priorityq)
        for job in jobs:
            # heapq.push((job[-1],job[0],job[1]))
            totrunningtime += jobs[1]
            if totrunningtime < job[-1]:
                heapq.push(priorityq, (job[-1], job[0], job[1]))
            else:
                highest_a_job = heapq.pop(priorityq)
                if totrunningtime - highest_a_job[2] < job[-1]:
                    time_to_dec = totrunningtime - job[-1]
                    amount = (highest_a_job[-1] - time_to_dec) / highest_a_job[1]
                    totalmoney += amount
                    heapq.push(priorityq, (highest_a_job[1], highest_a_job[0], highest_a_job[1] - time_to_dec))
                    print('totalmoney: ', totalmoney)
                    for i in range(t):
                        print(res_for_test_cases[i])

                    func()