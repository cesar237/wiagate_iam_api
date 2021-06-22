import csv

data_bulk = []

with open('equipment_list_db.csv') as db:
    dbreader = csv.reader(db, delimiter=';')
    for row in dbreader:
        data = {}
        data['device_type'] = row[0]
        data['brand'] = row[1]
        data['model'] = row[2]
        data['version'] = row[3]
        data['cpu'] = row[4]
        data['cpu_core'] = row[5]
        data['cpu_clock_mhz'] = row[6]
        data['flash_mb'] = row[7]
        data['ram_mb'] = row[8]
        data['ethernet_100MB_ports'] = row[9]
        data['ethernet_gbit_ports'] = row[10]
        data['wlan_24ghz'] = row[11]
        data['wlan_50ghz'] = row[12]
        data['bluetooth_support'] = row[13]
        data['usb_ports'] = row[14]
        data['serial'] = row[15]
        data['power_supply'] = row[16]
        data_bulk.append(data)

print(data_bulk)
