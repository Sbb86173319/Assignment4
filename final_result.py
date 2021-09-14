
"""
@author: jrgen
"""



city_list = ['Oak Park（Illinois）','Paris','Milano','Toronto','Chicago','Key West','Havana',
               'Venice','Entebbe','New York','Ketchum']


def greedy_shortestdist(start_city):   
    distance_dic={}
    distance_dic[6667] = {'Oak Park（Illinois）','Paris'}
    distance_dic[7307] = {'Milano','Oak Park（Illinois）'}
    distance_dic[712] = {'Oak Park（Illinois）','Toronto'}
    distance_dic [12] ={'Oak Park（Illinois）','Chicago'}
    distance_dic[2007] = {'Oak Park（Illinois）','Key West'}
    distance_dic[2147] = {'Oak Park（Illinois）','Havana'}
    distance_dic[7505] = {'Oak Park（Illinois）','Venice'}
    distance_dic[12464] = {'Oak Park（Illinois）','Entebbe'}
    distance_dic[1158] = {'Oak Park（Illinois）','New York'}
    distance_dic[2171] = {'Oak Park（Illinois）','Ketchum'}
    
    distance_dic [640] ={'Paris','Milano'}
    distance_dic[6006] = {'Paris','Toronto'}
    distance_dic[6661] = {'Paris','Chicago'}
    distance_dic[7573] = {'Paris','Key West'}
    distance_dic [7729] ={'Paris','Havana'}
    distance_dic[845] = {'Paris','Venice'}
    distance_dic[6149] = {'Paris','Entebbe'}
    distance_dic[5844] = {'Paris','New York'}
    distance_dic[8034] = {'Paris','Ketchum'}
    
    distance_dic [6644] ={'Milano','Toronto'}
    distance_dic[7301] = {'Milano','Chicago'}
    distance_dic[8173] = {'Milano','Key West'}
    distance_dic[8326] ={'Milano','Havana'}
    distance_dic [245] ={'Milano','Venice'}
    distance_dic[5546] = {'Milano','Entebbe'}
    distance_dic[6471] = {'Milano','New York'}
    distance_dic[8657] = {'Milano','Ketchum'}
    
    distance_dic [703] ={'Toronto','Chicago'}
    distance_dic [2142] ={'Toronto','Key West'}
    distance_dic [2306] ={'Toronto','Havana',}
    distance_dic [6849] ={'Toronto','Venice'}
    distance_dic [11752] ={'Toronto','Entebbe'}
    distance_dic [556] ={'Toronto','New York'}
    distance_dic [2792] ={'Toronto','Ketchum'}
    
    distance_dic [2000] ={'Chicago','Key West'}
    distance_dic [2140] ={'Chicago','Havana'}
    distance_dic [7499] ={'Chicago','Venice'}
    distance_dic [12455] ={'Chicago','Entebbe'}
    distance_dic [1147] ={'Chicago','New York'}
    distance_dic [2183] ={'Chicago','Ketchum'}
    
    distance_dic [170] ={'Key West','Havana'}
    distance_dic [8405] ={'Key West','Venice'}
    distance_dic [12455] ={'Key West','Entebbe'}
    distance_dic [1939] ={'Key West','New York'}
    distance_dic [3643] ={'Key West','Ketchum'}
    
    distance_dic [8559] ={'Havana','Venice'}
    distance_dic [12544] ={'Havana','Entebbe'}
    distance_dic [2109] ={'Havana','New York'}
    distance_dic [3711] ={'Havana','Ketchum'}
    
    
    distance_dic [5424] ={'Venice','Entebbe'}
    distance_dic [6688] ={'Venice','New York'}
    distance_dic [8807] ={'Venice','Ketchum'}
    
    distance_dic [11394] ={'Entebbe','New York'}
    distance_dic [14159] ={'Entebbe','Ketchum'}
    
    distance_dic [3312] ={'New York','Ketchum'}
       
    #Define a list to store  the route
    route = []
    #Define a list to store the distance (shortest) in each step.
    route_dist = []
    #Use use greedy algorithm by find the shortest distance in every step.
    for _ in range(len(city_list)-1):
        distance_list = []
        for distance, cities in distance_dic.items():
            if start_city in cities:
                distance_list.append(distance)
       
                
        shortest_dist = min(distance_list)
        route_dist.append(shortest_dist)
        nearest_cities = list(distance_dic[shortest_dist])
        
        nearest_cities. remove(start_city)
        arrive_city = nearest_cities[0]
        route.append([start_city,arrive_city])
        start_city = arrive_city
        for i in distance_list:
            del(distance_dic[i])
    
    
    #Calculate the total distance.
    total_distance = sum (route_dist)
 
    return total_distance 

startcities_shortestdict = {}
for name in city_list:
    startcities_shortestdict[name] = greedy_shortestdist(name)

for n,dist in startcities_shortestdict.items():
    if dist == min(startcities_shortestdict.values()):
        print(f'{n} as a start city is the best solution and the shortest distance is {dist}km.')



