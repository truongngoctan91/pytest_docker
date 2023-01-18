class Point():
    def __init__(self, name, longitude, latitude):

        self._name = name
        self._logitude = longitude
        self._latitude = latitude

    def get_lon_lat(self):
        return (self._logitude, self._latitude)
