import random

def gen_arrival_times(itterations):
    
    inter_arrival_times = []
    rand_arrival_times = []

    for i in range(itterations - 1):
        arrival_time = random.randrange(4, 10, 1)
        inter_arrival_times.append(arrival_time)
        
    for i in range(itterations):
        if i == 0:
            rand_arrival_times.append(0)
        else:
            arrival_time = (rand_arrival_times[i-1] + inter_arrival_times[i-1])
            rand_arrival_times.append(arrival_time)
           
    return rand_arrival_times

def gen_service_times(itterations):
    rand_service_times = []

    for i in range(itterations):
        service_time = random.randrange(2, 6, 1)
        rand_service_times.append(service_time)
    
    return rand_service_times

def gen_ids(itterations):
    ids = []
    for i in range(itterations):
        ids.append(i)

    return ids
