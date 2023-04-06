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


if client.find(olca.Process,"B4"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B4").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)
    
if client.find(olca.ProductSystem,"B4"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"B4").id)
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

if not client.find(olca.Flow,"B4_flow"):    
    austausch_flow = olca.Flow()
    austausch_flow.id = str(uuid.uuid4())
    austausch_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    austausch_flow.name = "B4_flow"
    austausch_flow.description = "An awesome new building"
    austausch_flow.unit = items_unit
    austausch_flow.flow_properties = [item_factor]
    austausch_flow.olca_type = olca.schema.Flow.__name__

    client.insert(austausch_flow)

austausch_flow = client.get(olca.Flow,client.find(olca.Flow,"B4_flow").id)


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

C1_flow = client.get(olca.Flow,client.find(olca.Flow,"C1_flow").id)
C1_process = client.get(olca.Process,client.find(olca.Process,"C1").id)

C2_flow = client.get(olca.Flow,client.find(olca.Flow,"C2_flow").id)
C2_process = client.get(olca.Process,client.find(olca.Process,"C2").id)

C3_flow = client.get(olca.Flow,client.find(olca.Flow,"C3_flow").id)
C3_process = client.get(olca.Process,client.find(olca.Process,"C3").id)

C4_flow = client.get(olca.Flow,client.find(olca.Flow,"C4_flow").id)
C4_process = client.get(olca.Process,client.find(olca.Process,"C4").id)



austausch_input_A1toA3 = olca.Exchange()
austausch_input_A1toA3.input = True
austausch_input_A1toA3.flow = A1toA3_flow
austausch_input_A1toA3.amount = 1
austausch_input_A1toA3.default_provider = A1toA3_process
austausch_input_A1toA3.unit = items_unit
austausch_input_A1toA3.flow_property = item 
austausch_input_A1toA3.internal_id =ID;ID = ID + 1
austausch_input_A1toA3.avoided_product = False
exch.append(austausch_input_A1toA3)

    
austausch_input_A4 = olca.Exchange()
austausch_input_A4.input = True
austausch_input_A4.flow = A4_flow
austausch_input_A4.amount = 1
austausch_input_A4.default_provider = A4_process
austausch_input_A4.unit = items_unit
austausch_input_A4.flow_property = item 
austausch_input_A4.internal_id =ID;ID = ID + 1
austausch_input_A4.avoided_product = False
exch.append(austausch_input_A4)

   
austausch_input_A5 = olca.Exchange()
austausch_input_A5.input = True
austausch_input_A5.flow = A5_flow
austausch_input_A5.amount = 1
austausch_input_A5.default_provider = A5_process
austausch_input_A5.unit = items_unit
austausch_input_A5.flow_property = item 
austausch_input_A5.internal_id =ID;ID = ID + 1
austausch_input_A5.avoided_product = False
exch.append(austausch_input_A5)

    
austausch_input_C1 = olca.Exchange()
austausch_input_C1.input = True
austausch_input_C1.flow = C1_flow
austausch_input_C1.amount = 1
austausch_input_C1.default_provider = C1_process
austausch_input_C1.unit = items_unit
austausch_input_C1.flow_property = item 
austausch_input_C1.internal_id =ID;ID = ID + 1
austausch_input_C1.avoided_product = False
exch.append(austausch_input_C1)

    
austausch_input_C2 = olca.Exchange()
austausch_input_C2.input = True
austausch_input_C2.flow = C2_flow
austausch_input_C2.amount = 1
austausch_input_C2.default_provider = C2_process
austausch_input_C2.unit = items_unit
austausch_input_C2.flow_property = item 
austausch_input_C2.internal_id =ID;ID = ID + 1
austausch_input_C2.avoided_product = False
exch.append(austausch_input_C2)

   
austausch_input_C3 = olca.Exchange()
austausch_input_C3.input = True
austausch_input_C3.flow = C3_flow
austausch_input_C3.amount = 1
austausch_input_C3.default_provider = C3_process
austausch_input_C3.unit = items_unit
austausch_input_C3.flow_property = item 
austausch_input_C3.internal_id =ID;ID = ID + 1
austausch_input_C3.avoided_product = False
exch.append(austausch_input_C3)

    
austausch_input_C4 = olca.Exchange()
austausch_input_C4.input = True
austausch_input_C4.flow = C4_flow
austausch_input_C4.amount = 1
austausch_input_C4.default_provider = C4_process
austausch_input_C4.unit = items_unit
austausch_input_C4.flow_property = item 
austausch_input_C4.internal_id =ID;ID = ID + 1
austausch_input_C4.avoided_product = False
exch.append(austausch_input_C4)

austausch = olca.Process()
austausch.category = client.find(olca.Category,"B4")
austausch.process_type = olca.ProcessType.UNIT_PROCESS
austausch.id = str(uuid.uuid4())
austausch.name = "B4"
austausch.olca_type = olca.schema.Process.__name__



austausch_output = olca.Exchange()
austausch_output.input = False
austausch_output.flow = austausch_flow
austausch_output.flow_property = item
austausch_output.unit = items_unit
austausch_output.amount = 1
austausch_output.quantitative_reference = True
austausch_output.internal_id = ID;ID = ID + 1
austausch_output.avoided_product = False
exch.append(austausch_output)


austausch.exchanges= exch
client.insert(austausch)


