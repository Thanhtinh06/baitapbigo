def solve(N, start, finish, Ticket_cost):
    # Write your code here
    out_ = 0
    i = start - 1
    costClockWise = 0
    costAntiClockWise = 0
    j = start - 1
    while i < finish:
        costClockWise += Ticket_cost[i]
        i += 1

    while j > - (finish - j):
        costAntiClockWise += Ticket_cost[j]
        j -= 1

    if costAntiClockWise > costClockWise:
        out_ = costClockWise
        return out_
    out_ = costAntiClockWise
    return out_


N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print(out_)
