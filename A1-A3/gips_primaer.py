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


if client.find(olca.Process,"gips_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"gips_primaer").id)
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


if not client.find(olca.Flow,"gips_primaer"):
    gips_flow = olca.Flow()
    gips_flow.id = str(uuid.uuid4())
    gips_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    gips_flow.name = "gips_primaer"
    gips_flow.description = "Furnierschichtholz aus der Oekobaudat"
    gips_flow.unit = m3
    gips_flow.flow_properties = [vol_factor]
    gips_flow.olca_type = olca.schema.Flow.__name__

    client.insert(gips_flow)

gips_flow = client.get(olca.Flow,client.find(olca.Flow,"gips_primaer").id)

plasterboard_flow = client.get(olca.Flow,"38dfe915-58e3-4ca4-921f-e6dfcf82c84f") #gypsum plasterboard

########################
###     Processes  #####
########################
plasterboard_process = client.get(olca.Process,"2fa3dcf2-e930-4884-b399-fae8915a1eac") #gypsum plasterboard production | gypsum plasterboard | EN15804, U

exch = []
ID = 1


gips_input_gipssheet = olca.Exchange()
gips_input_gipssheet.input = True
gips_input_gipssheet.flow = plasterboard_flow
gips_input_gipssheet.default_provider = plasterboard_process
gips_input_gipssheet.amount = 1 
gips_input_gipssheet.unit = kg 
gips_input_gipssheet.flow_property = mass
gips_input_gipssheet.internal_id =ID;ID = ID + 1 
gips_input_gipssheet.avoided_product = False
exch.append(gips_input_gipssheet)

gips_process = olca.Process()
gips_process.category = client.find(olca.Category,"A1-A3")
gips_process.process_type = olca.ProcessType.UNIT_PROCESS
gips_process.id = str(uuid.uuid4())
gips_process.name = "gips_primaer"
gips_process.olca_type = olca.schema.Process.__name__

gips_output_gips = olca.Exchange()
gips_output_gips.input = False
gips_output_gips.flow = gips_flow
gips_output_gips.flow_property = mass
gips_output_gips.unit = kg
gips_output_gips.amount = 1
gips_output_gips.quantitative_reference = True
gips_output_gips.internal_id =ID;ID = ID + 1 
gips_output_gips.avoided_product = False
exch.append(gips_output_gips)

gips_process.exchanges= exch
client.insert(gips_process)
