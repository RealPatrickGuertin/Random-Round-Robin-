def calc_total_wait_time(ids, arrival_times, service_times, end_time):
    total_wait_time = []
    for i in range(len(ids)):
        total_wait_time.append([ids[i], end_time[i][1] - service_times[i] - arrival_times[i]])
    
    return total_wait_time

def calc_average_time(turnaround_time):
    average_turnaround_time = 0
    for i in range(len(turnaround_time)): 
        average_turnaround_time += turnaround_time[i][1]

    average_turnaround_time /= len(turnaround_time)

    return average_turnaround_time

def calc_average_time_d(arr):
    item = 0
    for i in range(len(arr)): 
        item += arr[i]

    item /= len(arr)

    return item