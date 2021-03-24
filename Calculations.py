def calc_total_wait_time(ids, start_time, end_time):
    total_wait_time = []
    for i in range(len(start_time)):
        total_wait_time.append([ids[i], end_time[i][1] - start_time[i][1]])
    
    return total_wait_time

def calc_average_time(turnaround_time):
    average_turnaround_time = 0
    for i in range(len(turnaround_time)): 
        average_turnaround_time += turnaround_time[i][1]

    average_turnaround_time /= len(turnaround_time)

    return average_turnaround_time
