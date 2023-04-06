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


if client.find(olca.Process,"verb_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"verb_primaer").id)
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

if not client.find(olca.Flow,"verb_primaer"):
    verb_flow = olca.Flow()
    verb_flow.id = str(uuid.uuid4())
    verb_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    verb_flow.name = "verb_primaer"
    verb_flow.description = "Verbindungen des Holzhybrides"
    verb_flow.unit = kg
    verb_flow.olca_type = olca.schema.Flow.__name__

    client.insert(verb_flow)

verb_flow = client.get(olca.Flow,client.find(olca.Flow,"verb_primaer").id)


steel_flow = client.get(olca.Flow,"c33b5236-001e-49b5-aa3d-810c0214f9ce") #steel, chromium steel 18/8

########################
###     Processes  #####
########################
steel_process = client.get(olca.Process,"192c5ce4-1742-4106-861a-20d466037af7") #market for steel, chromium steel 18/8 | steel, chromium steel 18/8 | EN15804, U

exch = []
ID=1



verb_input_steel = olca.Exchange()
verb_input_steel.input = True
verb_input_steel.flow = steel_flow
verb_input_steel.default_provider = steel_process
verb_input_steel.amount =  1 # in kg
verb_input_steel.unit = kg  
verb_input_steel.flow_property = mass
verb_input_steel.internal_id =ID;ID = ID + 1 
verb_input_steel.avoided_product = False
verb_input_steel.quantitative_reference = False
exch.append(verb_input_steel)


verb_process = olca.Process()
verb_process.category = client.find(olca.Category,"A1-A3")
verb_process.process_type = olca.ProcessType.UNIT_PROCESS
verb_process.id = str(uuid.uuid4())
verb_process.name = "verb_primaer"
verb_process.olca_type = olca.schema.Process.__name__


verb_output_verb = olca.Exchange()
verb_output_verb.input = False
verb_output_verb.flow = verb_flow
verb_output_verb.flow_property = mass
verb_output_verb.unit = kg
verb_output_verb.amount = 1
verb_output_verb.quantitative_reference = True
verb_output_verb.internal_id =ID;ID = ID + 1 
verb_output_verb.avoided_product = False
exch.append(verb_output_verb)


verb_process.exchanges= exch
client.insert(verb_process)
