#FUNCTION TO FIND THE DENSITY OF TRAFFIC IN EACH LANE
#RETURNS A DICTIONARY
def Find_density():
    density = {'lane-1': 13, 'lane-2': 17, 'lane-3': 10, 'lane-4': 13}
    sorted_density = sorted(density.items(), key=lambda x: x[1], reverse=True)


    return sorted_density        


#FUNCTION TO SEND GREEN SIGNAL ACCORDING TO PRIORITY
def Check_density():
    sorted_density=Find_density()
    max=10
    for i in sorted_density:
        lane =i[0]
        if i[1]==0:
            Traffic_Light(lane,11)
        elif i[1]>max:
            Traffic_light(lane,36)
        else:
            Traffic_light(lane,26)
            

#FUNCTION TO DISPLAY THE STATE OF EACH TRAFFIC LIGHT IN A CYCLE 
def Traffic_light(lane,time):
    if lane==lane-1:
       print("Lane-1")

