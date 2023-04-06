# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:36:33 2020

@author: cbuschbeck
"""
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


if client.find(olca.Process,"bew_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"bew_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,mass

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"bew_sekundaer"):
    bew_flow = olca.Flow()
    bew_flow.id = str(uuid.uuid4())
    bew_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    bew_flow.name = "bew_sekundaer"
    bew_flow.description = "bewindungen des Holzhybrides"
    bew_flow.unit = kg
    bew_flow.olca_type = olca.schema.Flow.__name__

    client.insert(bew_flow)

bew_flow = client.get(olca.Flow,client.find(olca.Flow,"bew_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)

########################
###     Processes  #####
########################
exch = []
ID=1


bew_input_SM = olca.Exchange()
bew_input_SM.input = True
bew_input_SM.flow = SM_flow
bew_input_SM.amount =  1 # in kg
bew_input_SM.unit = kg  
bew_input_SM.flow_property = mass
bew_input_SM.internal_id =ID;ID = ID + 1 
bew_input_SM.avoided_product = False
bew_input_SM.quantitative_reference = False
exch.append(bew_input_SM)


bew_process = olca.Process()
bew_process.category = client.find(olca.Category,"A1-A3")
bew_process.process_type = olca.ProcessType.UNIT_PROCESS
bew_process.id = str(uuid.uuid4())
bew_process.name = "bew_sekundaer"
bew_process.olca_type = olca.schema.Process.__name__


bew_output_bew = olca.Exchange()
bew_output_bew.input = False
bew_output_bew.flow = bew_flow
bew_output_bew.flow_property = mass
bew_output_bew.unit = kg
bew_output_bew.amount = 1
bew_output_bew.quantitative_reference = True
bew_output_bew.internal_id =ID;ID = ID + 1 
bew_output_bew.avoided_product = False
exch.append(bew_output_bew)


bew_process.exchanges= exch
client.insert(bew_process)
