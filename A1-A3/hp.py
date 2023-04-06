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


if client.find(olca.Process,"hp"):
    todelete = client.get(olca.Process,client.find(olca.Process,"hp").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import item,items_unit

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"hp"):
    hp_flow = olca.Flow()
    hp_flow.id = str(uuid.uuid4())
    hp_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    hp_flow.name = "hp"
    hp_flow.description = "hpindungen des Holzhybrides"
    hp_flow.unit = items_unit
    hp_flow.olca_type = olca.schema.Flow.__name__

    client.insert(hp_flow)

hp_flow = client.get(olca.Flow,client.find(olca.Flow,"hp").id)




heat_pump_flow = client.get(olca.Flow,"30f4a0f3-cd30-4c2d-81dc-b50105c320cf") # heat pump, brine-water, 10kW
heat_pump_process = client.get(olca.Process,"f42e04d0-65f7-4bfe-accb-d0315efba4bf") # market for heat pump, brine-water, 10kW | heat pump, brine-water, 10kW | EN15804, U


########################
###     Processes  #####
########################
exch = []
ID=1

hp_input_hp = olca.Exchange()
hp_input_hp.input = True
hp_input_hp.flow = heat_pump_flow
hp_input_hp.amount = 1.6  # scaling damit es für air-water heat pump passt. siehe ecoinvent Wärmepumpen.pdf
hp_input_hp.unit = items_unit
hp_input_hp.flow_property = item 
hp_input_hp.internal_id =ID;ID = ID + 1 
hp_input_hp.default_provider = heat_pump_process
hp_input_hp.avoided_product = False
exch.append(hp_input_hp)





hp_process = olca.Process()
hp_process.category = client.find(olca.Category,"A1-A3")
hp_process.process_type = olca.ProcessType.UNIT_PROCESS
hp_process.id = str(uuid.uuid4())
hp_process.name = "hp"
hp_process.olca_type = olca.schema.Process.__name__


hp_output_hp = olca.Exchange()
hp_output_hp.input = False
hp_output_hp.flow = hp_flow
hp_output_hp.flow_property = item
hp_output_hp.unit = items_unit
hp_output_hp.amount = 1
hp_output_hp.quantitative_reference = True
hp_output_hp.internal_id =ID;ID = ID + 1 
hp_output_hp.avoided_product = False
exch.append(hp_output_hp)


hp_process.exchanges= exch
client.insert(hp_process)
