import GenRandTimes as a 
import Calculations as c

itterations = int(input("Itterations: "))
quantum = int(input("Quantum: "))
context_switch = int(input("Context Switch: "))

ids = a.gen_ids(itterations)
arrival_times = a.gen_arrival_times(itterations)
service_times = a.gen_service_times(itterations)
service_times_remaining = service_times.copy()
que = []

start_time = []
end_time = []
initial_wait_time = []
total_wait_time = []
turnaround_time = []

compleated_time = 0
finished = False

while finished == False:
    for i in range(len(ids)):
        # if task has arrived
        if arrival_times[i] <= compleated_time:
            # check if item has started and if not ever in que then add it
            item_found = False
            for item in range(len(start_time)):
                if start_time[item][0] == ids[i]:
                    item_found = True
            # if item is not in que add it
            if item_found == False:
                que.append([ids[i], arrival_times[i], service_times_remaining[i]])
                # add start time of process
                start_time.append([ids[i], compleated_time])
                # calculate initial wait time of process
                initial_wait_time.append([ids[i], compleated_time - arrival_times[i]])
                
    # go through que
    j = 0
    while j in range(len(que)): 
        # if service time >= quantum
        if que[j][2] >= quantum:
            compleated_time += quantum
            que[j][2] -= quantum
            if que[j][2] == 0:
                end_time.append([que[j][0], compleated_time])
                turnaround_time.append([que[j][0], compleated_time - que[j][1]])
                que.pop(j)
                j -= 1
                
            if len(que) > 0:
                compleated_time += context_switch

        # if service time is less than quantum
        elif que[j][2] < quantum:
            compleated_time += que[j][2]
            que[j][2] = 0
            end_time.append([que[j][0], compleated_time])
            turnaround_time.append([que[j][0], compleated_time - que[j][1]])
            if len(que) > 0:
                compleated_time += context_switch
            que.pop(j)
            j -= 1

        #print(que, " ", compleated_time)
        j +=1       

    # if que is empty +1 compleated time (clock)
    if not que:
        compleated_time += 1
        #print(compleated_time)
    
    # when all process have ended stop loop
    if(len(end_time) == itterations):
        finished = True

average_turnaround_time = 0
average_total_wait_time = 0

total_wait_time = c.calc_total_wait_time(ids, start_time, end_time)
average_turnaround_time = c.calc_average_time(turnaround_time)
average_total_wait_time = c.calc_average_time(total_wait_time)


print(" ")
print("ID    Start    End       Initial Wait    Total Wait    Turn Around")
for id in range(len(ids)):
    for index in ids:
        if id == index:
            print("---------------------------------------------------------------------------------------------------------------------------------")
            print(ids[id], "   ", start_time[id][1], "      ", end_time[id][1], "        ", initial_wait_time[id][1], "             ", total_wait_time[id][1], "            ", turnaround_time[id][1])

print("")
print("average_total_wait_time : ", average_total_wait_time)
print("Avg turnaround Time     : ", average_turnaround_time)
