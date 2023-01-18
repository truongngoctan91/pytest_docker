
class Point():
    def __init__(self, name, latitude, longitude):
        self.name = name
        if (type(self.name) != str):
            raise TypeError("wrong type")
        self.latitude = latitude
        self.longitude = longitude
        if not (-90 <= longitude <= 90) or not (-90 <= latitude <= 90):
            raise ValueError("wrong input")

    def get_lat_long(self):
        return (self.latitude, self.longitude)
