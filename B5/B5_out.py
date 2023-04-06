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


if client.find(olca.Process,"B5_out"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B5_out").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)
    
if client.find(olca.ProductSystem,"B5_out"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"B5_out").id)
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


C1_flow = client.get(olca.Flow,client.find(olca.Flow,"C1_flow").id)
C1_process = client.get(olca.Process,client.find(olca.Process,"C1").id)

C2_flow = client.get(olca.Flow,client.find(olca.Flow,"C2_flow").id)
C2_process = client.get(olca.Process,client.find(olca.Process,"C2").id)

C3_flow = client.get(olca.Flow,client.find(olca.Flow,"C3_flow").id)
C3_process = client.get(olca.Process,client.find(olca.Process,"C3").id)

C4_flow = client.get(olca.Flow,client.find(olca.Flow,"C4_flow").id)
C4_process = client.get(olca.Process,client.find(olca.Process,"C4").id)



    
umbau_input_C1 = olca.Exchange()
umbau_input_C1.input = True
umbau_input_C1.flow = C1_flow
umbau_input_C1.amount = 1
umbau_input_C1.default_provider = C1_process
umbau_input_C1.unit = items_unit
umbau_input_C1.flow_property = item 
umbau_input_C1.internal_id =ID;ID = ID + 1
umbau_input_C1.avoided_product = False
exch.append(umbau_input_C1)

    
umbau_input_C2 = olca.Exchange()
umbau_input_C2.input = True
umbau_input_C2.flow = C2_flow
umbau_input_C2.amount = 1
umbau_input_C2.default_provider = C2_process
umbau_input_C2.unit = items_unit
umbau_input_C2.flow_property = item 
umbau_input_C2.internal_id =ID;ID = ID + 1
umbau_input_C2.avoided_product = False
exch.append(umbau_input_C2)

   
umbau_input_C3 = olca.Exchange()
umbau_input_C3.input = True
umbau_input_C3.flow = C3_flow
umbau_input_C3.amount = 1
umbau_input_C3.default_provider = C3_process
umbau_input_C3.unit = items_unit
umbau_input_C3.flow_property = item 
umbau_input_C3.internal_id =ID;ID = ID + 1
umbau_input_C3.avoided_product = False
exch.append(umbau_input_C3)

    
umbau_input_C4 = olca.Exchange()
umbau_input_C4.input = True
umbau_input_C4.flow = C4_flow
umbau_input_C4.amount = 1
umbau_input_C4.default_provider = C4_process
umbau_input_C4.unit = items_unit
umbau_input_C4.flow_property = item 
umbau_input_C4.internal_id =ID;ID = ID + 1
umbau_input_C4.avoided_product = False
exch.append(umbau_input_C4)

umbau = olca.Process()
umbau.category = client.find(olca.Category,"B5")
umbau.process_type = olca.ProcessType.UNIT_PROCESS
umbau.id = str(uuid.uuid4())
umbau.name = "B5_out"
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


