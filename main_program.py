from csv_handler import CSVHandler
from basic import BasicStringFunctions
from basic import BasicListFunctions
from cluster import Cluster
from map import Map
import os


#Getting path of current working dir
code_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(code_directory, 'locations.csv')


#Reading CSV File
csv_reader = CSVHandler(csv_file_path)
all_locations_list = csv_reader.read_csv()
length_csv_locations_list = BasicListFunctions.length_of_list(all_locations_list)

clusters = []
#Traversing each location
for location_csv_index in range(1,length_csv_locations_list):
    
    location_name = all_locations_list[location_csv_index][0]
    location_latitude = all_locations_list[location_csv_index][1]
    location_longitude = all_locations_list[location_csv_index][2]

    latitude_degree = int(BasicStringFunctions.substring_extractor_till_delimeter(all_locations_list[location_csv_index][1], '°'))
    cluster_index = Cluster.cluster_finder(clusters, latitude_degree)
    
    if(cluster_index == -1):  #No cluster found for latitude
        clusters.append(Cluster())
        cluster_index = BasicListFunctions.length_of_list(clusters)-1  #getting the index of recently created cluster
        
    clusters[cluster_index].add_location(location_name, location_latitude, location_longitude, int(latitude_degree))

    

        
length_of_cluster_list = BasicListFunctions.length_of_list(clusters)
for cluster_index in range(length_of_cluster_list):
    print(f"\nCluster {cluster_index+1} : ")
    clusters[cluster_index].show_formatted_location()