class Map:
    def __init__(self):
        self.data = []
        self.length = 0

    def add_data(self, key, value):
        for item in self.data:
            if item[0] == key:
                item[1].append(value)
                return
        self.length += 1
        self.data.append([key, [value]])

    def get_data(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        print("No data found")
        return None

    def remove_key(self, key):
        for item in self.data:
            if item[0] == key:
                self.data.remove(item)
                self.length -= 1
                return
        print("Key is not found")

    def show_map(self):
        for item in self.data:
            print(f"{item[0]}: {item[1]}")


