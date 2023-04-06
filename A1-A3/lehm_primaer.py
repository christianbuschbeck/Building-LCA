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


if client.find(olca.Process,"lehm_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"lehm_primaer").id)
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

if not client.find(olca.Flow,"lehm_primaer"):
    lehm_flow = olca.Flow()
    lehm_flow.id = str(uuid.uuid4())
    lehm_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    lehm_flow.name = "lehm_primaer"
    lehm_flow.description = "lehmindungen des Holzhybrides"
    lehm_flow.unit = kg
    #lehm_flow.flow_properties = [mass_factor]
    lehm_flow.olca_type = olca.schema.Flow.__name__

    client.insert(lehm_flow)

lehm_flow = client.get(olca.Flow,client.find(olca.Flow,"lehm_primaer").id)



########################
###     Processes  #####
########################
exch = []
ID=1

clay_flow     = client.get(olca.Flow,"e89b4064-afcc-4f08-9481-651b7eaa90a1") #clay
clay_process  = client.get(olca.Process,"0eb789ee-cf05-4340-a3a1-ffbb5227e4e3") #clay pit operation | clay | EN15804, U




lehm_input_clay = olca.Exchange()
lehm_input_clay.input = True
lehm_input_clay.flow = clay_flow
lehm_input_clay.default_provider = clay_process
lehm_input_clay.amount =  1 # in kg
lehm_input_clay.unit = kg  
lehm_input_clay.flow_property = mass
lehm_input_clay.internal_id =ID;ID = ID + 1 
lehm_input_clay.avoided_product = False
lehm_input_clay.quantitative_reference = False
exch.append(lehm_input_clay)


lehm_process = olca.Process()
lehm_process.category = client.find(olca.Category,"A1-A3")
lehm_process.process_type = olca.ProcessType.UNIT_PROCESS
lehm_process.id = str(uuid.uuid4())
lehm_process.name = "lehm_primaer"
lehm_process.olca_type = olca.schema.Process.__name__


lehm_output_lehm = olca.Exchange()
lehm_output_lehm.input = False
lehm_output_lehm.flow = lehm_flow
lehm_output_lehm.flow_property = mass
lehm_output_lehm.unit = kg
lehm_output_lehm.amount = 1
lehm_output_lehm.quantitative_reference = True
lehm_output_lehm.internal_id =ID;ID = ID + 1 
lehm_output_lehm.avoided_product = False
exch.append(lehm_output_lehm)


lehm_process.exchanges= exch
client.insert(lehm_process)
