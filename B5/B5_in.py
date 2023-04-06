# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:29:52 2020

@author: cbuschbeck
"""


import sys

home_dir = "C:/Users/cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"B5_in"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B5_in").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)
    
if client.find(olca.ProductSystem,"B5_in"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"B5_in").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)



########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
from units import items_unit,item_factor,item

########################
###   Amounts        ###
########################

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"B5_flow"):    
    umbau_flow = olca.Flow()
    umbau_flow.id = str(uuid.uuid4())
    umbau_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    umbau_flow.name = "B5_flow"
    umbau_flow.description = "An awesome new building"
    umbau_flow.unit = items_unit
    umbau_flow.flow_properties = [item_factor]
    umbau_flow.olca_type = olca.schema.Flow.__name__

    client.insert(umbau_flow)

umbau_flow = client.get(olca.Flow,client.find(olca.Flow,"B5_flow").id)


########################
###   Processes      ###
########################
exch =[]
ID = 1

A1toA3_flow = client.get(olca.Flow,client.find(olca.Flow,"A1-A3_flow").id)
A1toA3_process = client.get(olca.Process,client.find(olca.Process,"A1-A3").id)

A4_flow = client.get(olca.Flow,client.find(olca.Flow,"A4_flow").id)
A4_process = client.get(olca.Process,client.find(olca.Process,"A4").id)

A5_flow = client.get(olca.Flow,client.find(olca.Flow,"A5_flow").id)
A5_process = client.get(olca.Process,client.find(olca.Process,"A5").id)




umbau_input_A1toA3 = olca.Exchange()
umbau_input_A1toA3.input = True
umbau_input_A1toA3.flow = A1toA3_flow
umbau_input_A1toA3.amount = 1
umbau_input_A1toA3.default_provider = A1toA3_process
umbau_input_A1toA3.unit = items_unit
umbau_input_A1toA3.flow_property = item 
umbau_input_A1toA3.internal_id =ID;ID = ID + 1
umbau_input_A1toA3.avoided_product = False
exch.append(umbau_input_A1toA3)

    
umbau_input_A4 = olca.Exchange()
umbau_input_A4.input = True
umbau_input_A4.flow = A4_flow
umbau_input_A4.amount = 1
umbau_input_A4.default_provider = A4_process
umbau_input_A4.unit = items_unit
umbau_input_A4.flow_property = item 
umbau_input_A4.internal_id =ID;ID = ID + 1
umbau_input_A4.avoided_product = False
exch.append(umbau_input_A4)

umbau_input_A5 = olca.Exchange()
umbau_input_A5.input = True
umbau_input_A5.flow = A5_flow
umbau_input_A5.amount = 1
umbau_input_A5.default_provider = A5_process
umbau_input_A5.unit = items_unit
umbau_input_A5.flow_property = item 
umbau_input_A5.internal_id =ID;ID = ID + 1
umbau_input_A5.avoided_product = False
exch.append(umbau_input_A5)
    

umbau = olca.Process()
umbau.category = client.find(olca.Category,"B5")
umbau.process_type = olca.ProcessType.UNIT_PROCESS
umbau.id = str(uuid.uuid4())
umbau.name = "B5_in"
umbau.olca_type = olca.schema.Process.__name__



umbau_output = olca.Exchange()
umbau_output.input = False
umbau_output.flow = umbau_flow
umbau_output.flow_property = item
umbau_output.unit = items_unit
umbau_output.amount = 1
umbau_output.quantitative_reference = True
umbau_output.internal_id = ID;ID = ID + 1
umbau_output.avoided_product = False
exch.append(umbau_output)


umbau.exchanges= exch
client.insert(umbau)


