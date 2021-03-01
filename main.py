import sys
import json


data = list(map(str.strip, sys.stdin))
for i in range(len(data)):
    data[i] = data[i].split('#')
    for j in range(len(data[i])):
        data[i][j] = data[i][j].strip()
orbit = dict()
con = dict()
var = dict()
for element in data:
    if 15 < int(element[1]) < 100:
        con[element[0]] = element[1]
    else:
        var[element[0]] = element[1]
orbit['constant'] = con
orbit['varying'] = var
with open('orbit.json', 'w') as orbit_file:
    json.dump(orbit, orbit_file)
