import datetime as dt
from shortest_path import get_shortest_path_dist_from_stat

def main():
    station_list = {'CS25', 'CS26', 'COSO2', 'CS44', 'CS43'}
    permutations = permute(station_list)
    for stations in permutations:
        res = add_visit_timestamp(stations)
        print("Departure and arrival time of each station")
        print(res)


''' Find all permutations of a station list.
'''
def permute(station_list):
    permutations = list()
    tmp_list = list()
    backtrack(permutations, tmp_list, station_list)
    return permutations


''' Helper function for permutation.
'''
def backtrack(permutations, tmp_list, station_list):
    if len(tmp_list) == len(station_list):
        permutations.append(list(tmp_list))
        return
    for station in station_list:
        if station in tmp_list:
            continue
        tmp_list.append(station)
        backtrack(permutations, tmp_list, station_list)
        del tmp_list[len(tmp_list) - 1]


''' Add time for each station in the list.
    All times are measured in secondes.
'''
def add_visit_timestamp(stations):
    last_station = None
    res = list()

    for station in stations:

        if last_station == None:
            arrival_time = 0
        else:
            # 15m/s i.e. 54km/h Will be speed between actual station
            speed = 15
            distance =  get_shortest_path_dist_from_stat(last_station, station)
            road_time = distance / speed    # intra-station time (secs)
            arrival_time = departure_time + road_time

        measure_time = 150                  # inner-station time (secs)
        departure_time = arrival_time + measure_time
        last_station = station

        entry = station + ", " + str(dt.timedelta(seconds = arrival_time)) \
                + ", " + str(dt.timedelta(seconds = departure_time))
        res.append(entry)

    return res


if __name__ == '__main__':
    main()