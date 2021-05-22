#FUNCTION TO FIND THE DENSITY OF TRAFFIC IN EACH LANE
#RETURNS A DICTIONARY
def Find_density():
    density = {}
    sorted_values = sorted(density.values()) # Sort the values
    sorted_density = {}

    for i in sorted_values:
       for k in density.keys():
            if density[k] == i:
                sorted_density[k] = dict1[k]
                break
    return sorted_density        


#FUNCTION TO SEND GREEN SIGNAL ACCORDING TO PRIORITY
def Check_density():
    sorted_density=Find_density()
    max=7
    for i in sorted_density.values():
        #find key
        lane=#
        if i==0:
            Traffic_Light(lane,11)
        elif i>max:
            Traffic_light(lane,36)
        else:
            Traffic_light(lane,26)
            

#FUNCTION TO DISPLAY THE STATE OF EACH TRAFFIC LIGHT IN A CYCLE 
def Traffic_light():
    if lane==lane1:
       print() 
