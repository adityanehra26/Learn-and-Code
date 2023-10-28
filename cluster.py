
class Cluster:
    def __init__(self):
        self.locations = []
        self.center_latitude = 0.0

    def get_locations(self):
        return self.locations

    def add_location(self, location):
        self.locations.append(location)

    def show_locations(self):
        number = 1
        for location in self.locations:
            print(f"{number}: {location}")
            number += 1

    @staticmethod
    def haversine_distance(lat1, lat2):
        # Radius of the Earth in degrees of latitude (approximately 111.32 km per degree)
        earth_radius_deg = 111.32

        # Calculate the distance in degrees of latitude
        distance = abs(lat1 - lat2)
        return distance * earth_radius_deg

    @staticmethod
    def cluster_creator(locations, max_distance_deg):
        clusters = []

        for location in locations:
            nearest_cluster = False # False means no nearest cluster found

            for cluster in clusters:
                distance = Cluster.haversine_distance(location['Latitude'], cluster.center_latitude)

                if distance <= max_distance_deg:
                    nearest_cluster = cluster

            if nearest_cluster:
                nearest_cluster.add_location(location)
            else:
                new_cluster = Cluster()
                new_cluster.center_latitude = location['Latitude']
                new_cluster.add_location(location)
                clusters.append(new_cluster)

        return clusters

# Example usage
if __name__ == "__main__":
    locations = [
        {'City Name': 'Vatican City', 'Latitude': 41.9, 'Longitude': 12.45},
        {'City Name': 'Same coordinate City', 'Latitude': 41.9, 'Longitude': 12.45},
        {'City Name': 'Tegucigalpa', 'Latitude': 14.1, 'Longitude': -87.216667},
        {'City Name': 'Kabul2', 'Latitude': 14.1, 'Longitude': -87.2183333},
        {'City Name': 'Kabul', 'Latitude': 84.5166666666666, 'Longitude': 69.183333}
    ]

    max_distance_deg = 10.0
    clusters = Cluster.cluster_creator(locations, max_distance_deg)
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}:")
        cluster.show_locations()
