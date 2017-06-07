from time import strftime, localtime

import requests


class StationPos:

    def __init__(self, latitude, longitude, timestamp):
        self.latitude = latitude.strip('-')
        self.longitude = longitude.strip('-')
        self.meridian = 'N' if float(latitude) > 0 else 'S'
        self.parallel = 'E' if float(longitude) > 0 else 'W'
        self.time = strftime('%T', localtime(timestamp))

    def __str__(self):
        return (f'Latitude: {self.latitude}° {self.meridian} | '
                f'Longitude: {self.longitude}° {self.parallel} | '
                f'Local time: {self.time}')

    __repr__ = __str__

    def print_data(self):
        print('International Space Station position')
        print(f'Local time: \t{self.time}')
        print(f'Latitude: \t{self.latitude}° {self.meridian}')
        print(f'Longitude: \t{self.longitude}° {self.parallel}')


def _get_data():
    session = requests.Session()
    response = session.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    return response.json()


def station_position():
    data = _get_data()
    station_latitude = data['iss_position']['latitude']
    station_longitude = data['iss_position']['longitude']
    local_time = data['timestamp']
    return StationPos(station_latitude, station_longitude, local_time)
