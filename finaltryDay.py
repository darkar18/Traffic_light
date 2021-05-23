##[Team cuatro]
#[Smart-Traffic management]

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

#FUNCTION TO FIND THE DENSITY OF TRAFFIC IN EACH LANE
#RETURNS A DICTIONARY
def Find_density():
    im1 = cv2.imread('day1.png')
    assert not isinstance(im1,type(None)), 'image not found'
    dict_lane ={'lane-1':0,'lane-2':0,'lane-3':0,'lane-4':0}

    bbox, label, conf = cv.detect_common_objects(im1)
    output_image1 = draw_bbox(im1, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-1 in the image is ', total)
    dict_lane['lane-1'] =total

    #2nd image
    im2 = cv2.imread('day2.png')
    assert not isinstance(im2,type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(im2)
    output_image2 = draw_bbox(im2, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-2 in the image is ', total)
    dict_lane['lane-2'] =total

    #3rd image
    im3 = cv2.imread('day3.png')
    assert not isinstance(im3,type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(im3)
    output_image3 = draw_bbox(im3, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-3 in the image is ', total)
    dict_lane['lane-3'] =total

    #4th image
    im4 = cv2.imread('day4.png')
    assert not isinstance(im4,type(None)), 'image not found'

    bbox, label, conf = cv.detect_common_objects(im4)
    output_image4 = draw_bbox(im4, bbox, label, conf)
    total = label.count('person')+label.count('car')+label.count('motorcycle')+label.count('truck')
    #print('Number of vehicles in cam-4 in the image is ', total)
    dict_lane['lane-4'] =total
   # print(dict_lane)
       
    sorted_density = sorted(dict_lane.items(), key=lambda x: x[1], reverse=True)
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
    print("TRAFFIC - LIGHT STATUS")
    if lane=='lane-1':
       print("LANE-1")
       print('turns yellow for 3 sec!')
       print(f'turns green for {time} sec!')
       print("turns yellow for 3 sec!")
       print("Back to red")
       print("-------------------------------")
       print("LANE-2")
       print("Remains red")
       print("-------------------------------")
       print("LANE-3")
       print("Remains red")
       print("-------------------------------")
       print("LANE-4")
       print("Remains red")
       print("-------------------------------")
       

    elif lane=='lane-2':
       print("LANE-1")
       print("Remains red")
       print("-------------------------------")
       print("LANE-2")
       print('turns yellow for 3 sec!')
       print(f'turns green for {time} sec!')
       print("turns yellow for 3 sec!")
       print("Back to red")
       print("-------------------------------")
       print("LANE-3")
       print("Remains red")
       print("-------------------------------")
       print("LANE-4")
       print("Remains red")
       print("-------------------------------")

    elif  lane=='lane-3':
       print("LANE-1")
       print("Remains red")
       print("-------------------------------")
       print("LANE-2")
       print("Remains red")
       print("-------------------------------")
       print("LANE-3")
       print('turns yellow for 3 sec!')
       print(f'turns green for {time} sec!')
       print("turns yellow for 3 sec!")
       print("Back to red")
       print("-------------------------------")
       print("LANE-4")
       print("Remains red")
       print("-------------------------------")

    else:
       print("LANE-1")
       print("Remains red")
       print("-------------------------------")
       print("LANE-2")
       print("Remains red")
       print("-------------------------------")
       print("LANE-3")
       print("Remains red")
       print("-------------------------------")
       print("LANE-4")
       print('turns yellow for 3 sec!')
       print(f'turns green for {time} sec!')
       print("turns yellow for 3 sec!")
       print("Back to red")
       print("-------------------------------")
    print("===============================")    
 
       
Check_density()






