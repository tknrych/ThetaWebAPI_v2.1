#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

cmdURL = "http://192.168.1.1/osc/info"
res = requests.get(cmdURL)
json_dict = json.loads(res.text)

# Manufacturer name
print("Manufacturer name : " + json_dict["manufacturer"])

# Model
print("Model : " + json_dict["model"])

# Serial number
print("Serial number : " + json_dict["serialNumber"])

# MAC address of wireless LAN
print("MAC address of wireless LAN : " + json_dict["_wlanMacAddress"])

# MAC address of Bluetooth
print("MAC address of Bluetooth : " + json_dict["_bluetoothMacAddress"])

# Firmware version
print("Firmware version : " + json_dict["firmwareVersion"])

# URL of the support page
print("URL of the support page : " + json_dict["supportUrl"])

# Presence of GPS
print("Presence of GPS : " + json_dict["gps"])

# endpoints
print("endpoints :")
print("    httpPort : " + str(json_dict["endpoints"]["httpPort"]))
print("    httpUpdatesPort : " + str(json_dict["endpoints"]["httpUpdatesPort"]))

# api
NumberOfElements = len(json_dict["api"])
print("api :")
for i in range(NumberOfElements):
    print(json_dict["api"][i])