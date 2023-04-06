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


if client.find(olca.Process,"wool_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"wool_primaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,m3,mass,vol_factor,area,m2


########################
###     Flows      #####
########################


if not client.find(olca.Flow,"wool_primaer"):
    wool_flow = olca.Flow()
    wool_flow.id = str(uuid.uuid4())
    wool_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    wool_flow.name = "wool_primaer"
    wool_flow.description = "Furnierschichtholz aus der Oekobaudat"
    wool_flow.unit = m3
    wool_flow.flow_properties = [vol_factor]
    wool_flow.olca_type = olca.schema.Flow.__name__

    client.insert(wool_flow)

wool_flow = client.get(olca.Flow,client.find(olca.Flow,"wool_primaer").id)

steinwolle_flow = client.get(olca.Flow,"9e0e1511-492a-4ea4-a88a-50564b29805b") #stone wool

########################
###     Processes  #####
########################
steinwolle_process = client.get(olca.Process,"d24ca5e8-ea62-4fbd-b628-57d3609b435d") #stone wool production | stone wool | EN15804, U

exch = []
ID = 1


wool_input_woolsheet = olca.Exchange()
wool_input_woolsheet.input = True
wool_input_woolsheet.flow = steinwolle_flow
wool_input_woolsheet.default_provider = steinwolle_process
wool_input_woolsheet.amount = 1 
wool_input_woolsheet.unit = kg 
wool_input_woolsheet.flow_property = mass
wool_input_woolsheet.internal_id =ID;ID = ID + 1 
wool_input_woolsheet.avoided_product = False
exch.append(wool_input_woolsheet)

wool_process = olca.Process()
wool_process.category = client.find(olca.Category,"A1-A3")
wool_process.process_type = olca.ProcessType.UNIT_PROCESS
wool_process.id = str(uuid.uuid4())
wool_process.name = "wool_primaer"
wool_process.olca_type = olca.schema.Process.__name__

wool_output_wool = olca.Exchange()
wool_output_wool.input = False
wool_output_wool.flow = wool_flow
wool_output_wool.flow_property = mass
wool_output_wool.unit = kg
wool_output_wool.amount = 1
wool_output_wool.quantitative_reference = True
wool_output_wool.internal_id =ID;ID = ID + 1 
wool_output_wool.avoided_product = False
exch.append(wool_output_wool)

wool_process.exchanges= exch
client.insert(wool_process)
