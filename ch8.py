
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

##a set is like an array but each item can only show up oct
##arr = [1,2,3,4,5,5,5,5,2]
##print(set(arr))


def findStations(stationSet): 

  stations = {}

  stations["kone"] = set(["id", "nv", "ut",])
  stations["ktwo"] = set(["wa", "id", "mt"])
  stations['kthree'] = set(["or", "nv", "ca"])
  stations["kfour"] = set(["nv", "ut"])
  stations["kfive"] = set(["ca", "az"])


  final_stations = set()

  while stationSet: 
    best_station = None
    states_covered = set()
    for station, states in stations.items():
      covered = stationSet & states ##with sets you can apply operators to show union, intersection and difference of set values
      if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
    stationSet -= states_covered
    final_stations.add(best_station)
  return final_stations

print(findStations(states_needed))
