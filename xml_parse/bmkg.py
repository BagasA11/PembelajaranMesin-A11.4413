import xml.etree.ElementTree as ET
import pandas as pd
data_path = "DigitalForecast-JawaTengah.xml"

tree = ET.parse(data_path)
root = tree.getroot()

print("root element: ", root.tag) # </data>
# data > forecast > area
print("len of area tag: ", len(root[0].findall("area")))

forecast = root[0]
print("forecast: ", forecast.tag)

# demak, semarang, kendal, kudus, ungaran, salatiga
demak = {}
semarang = {}
kendal = {}
kudus = {}
ungaran = {}
salatiga = {}

for area in forecast.findall("area"):
    
    if area.get("description") == "Semarang":
        semarang = area
        print("kota: ", semarang.find("name").text)
    elif area.get("description") == "Kendal":
        kendal = area
        print("kota: ", kendal.find("name").text)
    elif area.get("description") == "Demak":
        demak = area
        print("kota: ", demak.find("name").text)
    elif area.get("description") == "Kudus":
        kudus = area
        print("kota: ", kudus.find("name").text)
    elif area.get("description") == "Ungaran":
        ungaran = area
        print("kota: ", ungaran.find("name").text)
    elif area.get("description") == "Salatiga":
        salatiga = area
        print("kota: ", salatiga.find("name").text)

# semarang {time:[], humax:[], tmin:[]}


print("\n\t=== semarang ===\t")
semarang_dict = dict()
for parameter in semarang:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        
        
        semarang_dict.update({"datetime":ts})
        semarang_dict[key] = vs
        
        print(key, ": ", len(semarang_dict[key]))

print("\n\t=== Kendal ===\t")
kendal_dict = dict()
for parameter in kendal:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        kendal_dict.update({"datetime":ts})
        kendal_dict[key] = vs
        
        print(key, ": ", len(kendal_dict[key]))

demak_dict = dict()
print("\n\t=== Demak ===\t")
for parameter in demak:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        demak_dict.update({"datetime":ts})
        demak_dict[key] = vs
        
        print(key, ": ", len(demak_dict[key]))

kudus_dict = dict()
print("\n\t=== Kudus ===\t")
for parameter in kudus:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        kudus_dict.update({"datetime":ts})
        kudus_dict[key] = vs
        
        print(key, ": ", len(kudus_dict[key]))

salatiga_dict = dict()
print("\n\t=== Salatiga ===\t")
for parameter in salatiga:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        salatiga_dict.update({"datetime":ts})
        salatiga_dict[key] = vs
        
        print(key, ": ", len(salatiga_dict[key]))

ungaran_dict = dict()
print("\n\t=== Ungaran ===\t")
for parameter in ungaran:

    if parameter.get("type") == "hourly":
        key = parameter.get("id")
        if key == "wd" or key == "ws":
            # if key == wd or ws, to nextline
            continue
        vs = []
        ts = []
        for timerange in parameter:
            vs.append( float(timerange[0].text) )
            ts.append(timerange.get("datetime"))

        ungaran_dict.update({"datetime":ts})
        ungaran_dict[key] = vs
        
        print(key, ": ", len(ungaran_dict[key]))

print(f"semarang: \n{semarang_dict}")

# flush unused var
demak = {}
semarang = {}
kendal = {}
kudus = {}
ungaran = {}
salatiga = {}

# semarang -> kendal -> demak -> salatiga -> ungaran -> kudus
print(f"before len: {len(kendal_dict['t'])} \n====\n")
print(f"\n{kendal_dict['t']}\n")

# push semarang_dict to kendal_dict
for x in semarang_dict:
    # access key
    # key: x
    print("key: ", x)
    
    for y in semarang_dict[x]:
        # acess x: element
        print(x, ": ", y, "\n")
        kendal_dict[x].append(y)

# remove semarang_dict val
semarang_dict = {}

print(f"\n after len: {len(kendal_dict['t'])} \n====\n")
print(f"\n{kendal_dict['t']}\n")

print(f"before len: {len(demak_dict['t'])} \n====\n")
print(f"\n{demak_dict['t']}\n")

for x in kendal_dict:
    # access key
    # key: x
    print("key: ", x)
    
    for y in kendal_dict[x]:
        # acess x: element
        print(x, ": ", y, "\n")
        demak_dict[x].append(y)

kendal_dict = {}

print(f"\n after len: {len(demak_dict['t'])} \n====\n")
print(f"\n{demak_dict['t']}\n")