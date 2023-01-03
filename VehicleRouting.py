
######## Vehicle Routing  #########
######## Jose Mancilla #############
######## Independet Study ##########

import math
from collections import namedtuple
import sys

#Get the coordinate difference between points
def coor_dif(coor1, coor2):
    return math.sqrt((coor1.x - coor2.x)**2 + (coor1.y - coor2.y)**2)


#Set up dictonary tupple
Customer = namedtuple("Customer", ['id', 'dem', 'x', 'y'])


def vrp(file):

#divide the file by jump line
    text = file.split('\n')
    line = text[0].split()

#divide the lines by cust,vehicle and cap.
    cust_num = int(line[0])
    vehcl_num = int(line[1])
    vehcl_cap = int(line[2])


#All custumers start
    all_customers = []
    for c in range(1, cust_num+1):
        line = text[c]
        line = line.split()
        #send each of the cust num, vech num and vech num
        all_customers.append(Customer(c-1, int(line[0]), float(line[1]), float(line[2])))


#first custmer in all custmers
    first = all_customers[0]

#greedy solution assign cust to the vech
#by the largest demand

    visited = []
    #set all the custmers tuple
    cust_left = set(all_customers)
    #Remove cust
    cust_left.remove(first)

#loop from 0 thorugh vehcl_num send viisted and how much cap left
    for vehc in range(0, vehcl_num):
#append to visited
        visited.append([])
        cap_left = vehcl_cap

#while we still have cap_left
        while sum([cap_left >= cust.dem for cust in cust_left]) > 0:
            done = set()
            #funtion sorted tupple by cust demand
            sorted_dem = sorted(cust_left, key=lambda customer: -customer.dem)

#loop thorugh the sorted dema
            for cust in sorted_dem:
                if cap_left >= cust.dem:
                    cap_left -= cust.dem #rest the demand
                    visited[vehc].append(cust) #vech has all of vehcl_num
                    done.add(cust)
            cust_left -= done #rest


#cost of the vehc using the funciton coor_dif between each coordinate
    result = 0
#Loop through vehcl_num
    for n in range(0, vehcl_num):
        vehcl_vis = visited[n]
        if len(vehcl_vis) > 0:
            result += coor_dif(first,vehcl_vis[0])
            #Loop through vehcl_vis
            for vis in range(0, len(vehcl_vis)-1):
                result += coor_dif(vehcl_vis[vis],vehcl_vis[vis+1])
            result += coor_dif(vehcl_vis[-1],first) #the biggest demand

#final length
    final = str(result)+ '\n'
#vehicle routes
    for veh in range(0, vehcl_num):
        final += str(first.id) + ' ' + ' '.join([str(cust.id)
        for cust in visited[veh]]) + ' ' + str(first.id) + '\n'
#return the final
    return final



##########main

if __name__ == '__main__':
    #Open input file
    with open('vrp_484_19_1', 'r') as vhr_file:

        file = vhr_file.read()
        sys.stdout=open("vrp_484_19_1_output.txt",'w')
        print(vrp(file))
        sys.stdout.close()
