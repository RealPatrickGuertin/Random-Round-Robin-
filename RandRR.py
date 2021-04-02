import GenRandTimes as a 
import Calculations as c

# q =1, service
# q = 3 service
# Service =2,4
# service 3,5
# Service 4.8


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
first_to_finish = None
last_to_finish = None

compleated_time = 0
finished = False

while finished == False:
    # go through tasks and add to que if arrived
    for i in range(len(ids)):
        # if task has arrived
        if arrival_times[i] <= compleated_time:
            # check if task has started and if not ever started then add it
            item_found = False
            for item in range(len(start_time)):
                if start_time[item][0] == ids[i]:
                    item_found = True
            # if task is not in que add it
            if item_found == False:
                que.append([ids[i], arrival_times[i], service_times_remaining[i]])
                start_time.append([ids[i], compleated_time])
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
                if first_to_finish is None:
                    first_to_finish = que[j][0]
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

        j +=1       

    # if que is empty +1 compleated time (clock)
    if not que:
        compleated_time += 1
        #print(compleated_time)
    
    # when all process have ended stop loop
    if(len(end_time) == itterations):
        finished = True

last_to_finish = ids[len(end_time) - 1]
total_wait_time = c.calc_total_wait_time(ids, arrival_times, service_times, end_time)
average_turnaround_time = c.calc_average_time(turnaround_time)
average_total_wait_time = c.calc_average_time(total_wait_time)
average_service_time = c.calc_average_time_d(service_times)

# print first and last 10
print(" ")
print("ID    Start    End       Initial Wait    Total Wait    Turn Around       Arrival Time      Service Time")
for id in range(len(ids)):
    for index in ids:
        if id == index and (id < 10 or id >89 ):
            print("---------------------------------------------------------------------------------------------------------------------------------")
            print(ids[id], "   ", start_time[id][1], "      ", end_time[id][1], "        ", initial_wait_time[id][1], "             ", total_wait_time[id][1], "            ", turnaround_time[id][1], "                   ", arrival_times[id], "            ", service_times[id])

print("")
print("First Job to Finish: ", first_to_finish)
print("Last Job to Finish: ", last_to_finish)
print("average_total_wait_time : ", average_total_wait_time)
print("Avg turnaround Time     : ", average_turnaround_time)
print("Avg service time: ", average_service_time)
