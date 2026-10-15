def coaster(n, riders):
    can_ride = 0 
    for i in riders:
        if i[0]> 120 and i[1] > 12 or i[2] =="Y":
            can_ride +=1
            print(can_ride)
    return can_ride