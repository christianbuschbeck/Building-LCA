# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:38 2020

@author: cbuschbeck
"""

import sys
import pandas as pd
import os

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)

if client.find(olca.Process,"sorting and chipping"):
    client.delete(client.get(olca.Process,client.find(olca.Process,"sorting and chipping").id))


########################
###   Processes      ###
########################

wood_chips_proc = client.get(olca.Process,"27dc1893-1e28-3864-99e6-f2dec1fc3791") #treatment of waste wood, untreated, municipal incineration | waste wood, untreated | Cutoff, U

for ex in wood_chips_proc.exchanges:
    if ex.flow.name == "waste wood, post-consumer":
        wood_chips_proc.exchanges.remove(ex)
    if ex.flow.name == "Carbon dioxide":
        wood_chips_proc.exchanges.remove(ex)


wood_chips_proc.name = "sorting and chipping"
wood_chips_proc.id = str(uuid.uuid4())
wood_chips_proc.category = client.find(olca.Category,"C3")

client.insert(wood_chips_proc)