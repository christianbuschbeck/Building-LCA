# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:29:12 2020

@author: cbuschbeck
"""

import sys

home_dir = "C:/Users/cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid

#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"pv"):
    todelete = client.get(olca.Process,client.find(olca.Process,"pv").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.Process,"solar"):
    todelete = client.get(olca.Process,client.find(olca.Process,"solar").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import area,m2


########################
###     Flows      #####
########################


if not client.find(olca.Flow,"pv"):
    pv_flow = olca.Flow()
    pv_flow.id = str(uuid.uuid4())
    pv_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    pv_flow.name = "pv"
    pv_flow.description = "Furnierschichtholz aus der Oekobaudat"
    pv_flow.unit = m2
    pv_flow.olca_type = olca.schema.Flow.__name__

    client.insert(pv_flow)

pv_flow = client.get(olca.Flow,client.find(olca.Flow,"pv").id)





solar_flow = client.get(olca.Flow,"98556c18-39ab-4d83-b9b9-cf9ae41566a9") #photovoltaic panel, single-Si wafer

########################
###     Processes  #####
########################
solar_process = client.get(olca.Process,"1905592d-3e6e-4d28-90f6-8c137fdaab4a") #photovoltaic panel production, single-Si wafer | photovoltaic panel, single-Si wafer | EN15804, U

for i in range(1,5):

    for ex in solar_process.exchanges:
        if ex.input==False:
            if ex.quantitative_reference != True:
                solar_process.exchanges.remove(ex)
  

solar_process.name = "solar"
solar_process.id = str(uuid.uuid4())
solar_process.olca_type = olca.schema.Process.__name__
client.insert(solar_process)    

solar_process = client.get(olca.Process,client.find(olca.Process,"solar").id) #eigen





exch = []
ID = 1


pv_input_solar = olca.Exchange()
pv_input_solar.input = True
pv_input_solar.flow = solar_flow
pv_input_solar.default_provider = solar_process
pv_input_solar.flow_property = area
pv_input_solar.unit = m2
pv_input_solar.amount = 1
pv_input_solar.quantitative_reference = False
pv_input_solar.internal_id =ID;ID = ID + 1 
pv_input_solar.avoided_product = False
exch.append(pv_input_solar)

pv_process = olca.Process()
pv_process.category = client.find(olca.Category,"A1-A3")
pv_process.process_type = olca.ProcessType.UNIT_PROCESS
pv_process.id = str(uuid.uuid4())
pv_process.name = "pv"
pv_process.olca_type = olca.schema.Process.__name__


pv_output_pv = olca.Exchange()
pv_output_pv.input = False
pv_output_pv.flow = pv_flow
pv_output_pv.flow_property = area
pv_output_pv.unit = m2
pv_output_pv.amount = 1
pv_output_pv.quantitative_reference = True
pv_output_pv.internal_id =ID;ID = ID + 1 
pv_output_pv.avoided_product = False
exch.append(pv_output_pv)



pv_process.exchanges= exch
client.insert(pv_process)
