# ISS Position Python API Wrapper for Open Notify API

This is a basic Python 3.6 wrapper for the Open Notify API, speficically the one that provides current location of the International Space Station.

[Open Notify website](http://open-notify.org/)

### Dependencies
* [Python 3.6](https://www.python.org/downloads/release/python-361/)
* [requests library](http://docs.python-requests.org/en/master/)

### Example

The `station_position` function calls the `_get_data` function, which gets the data from the API. The data is passed into the `StationPos` class and the function returns its instance.

To display the station's position the `station_position` function can be assigned to a variable. Use the `print_data()` method to print the data to shell.

```
>>> position = station_position()
>>> position.print_info()
International Space Station position
Local time:   16:06:42
Latitude:     51.0431° S
Longitude:    138.4967° W
```

Calling the assigned variable directly will display the string representation of the `StationPos` instance.
```
>>> position = station_position()
>>> position
Latitude: 51.0431° S | Longitude: 138.4967° W | Local time: 16:06:42
```
