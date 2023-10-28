from excel_handler import ExcelHandler
from basic import BasicStringFunctions
from basic import BasicListFunctions
from cluster import Cluster
from map import Map
import os


#Getting path of current working dir
code_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(code_directory, 'cities.xlsx')


#Reading excel file File
excel_reader = ExcelHandler(csv_file_path)
all_locations_list = excel_reader.get_data_as_list()
length_locations_list = BasicListFunctions.length_of_list(all_locations_list)
clusters = Cluster.cluster_creator(all_locations_list, 10)


cluster_number = 1
for cluster in clusters:
    print(f"Cluster {cluster_number}")
    print(cluster.get_locations())
    cluster_number += 1
