from basic import BasicListFunctions

class Cluster:

    def __init__(self):
        self.locations = []
        self.cluster_range = [0,0]

    def add_location(self, location_name, latitude, longitude, latitude_degree):
        if(BasicListFunctions.length_of_list(self.locations) == 0):
                range_start = latitude_degree//10
                if(range_start%2==0):
                     range_start = range_start*10
                else:
                     range_start = (range_start-1)*10
                self.cluster_range[0] = range_start
                self.cluster_range[1] = range_start+20
        
        self.locations.append((location_name, latitude, longitude))

    def get_locations(self):
        return self.locations
    
    def show_formatted_location(self):
        for location in self.locations:
            print(location)

    @staticmethod
    def cluster_finder(clusters, latitude):
        for index in range(BasicListFunctions.length_of_list(clusters)):
            cluster = clusters[index]
            if cluster.cluster_range[1] > latitude and cluster.cluster_range[0] <= latitude:
                return index
        return -1