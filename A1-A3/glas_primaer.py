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


if client.find(olca.Process,"glas_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"glas_primaer").id)
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

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"glas_primaer"):
    glas_flow = olca.Flow()
    glas_flow.id = str(uuid.uuid4())
    glas_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    glas_flow.name = "glas_primaer"
    glas_flow.description = "Furnierschichtholz aus der Oekobaudat"
    glas_flow.unit = m3
    glas_flow.flow_properties = [vol_factor]
    glas_flow.olca_type = olca.schema.Flow.__name__

    client.insert(glas_flow)

glas_flow = client.get(olca.Flow,client.find(olca.Flow,"glas_primaer").id)

glassheet_flow = client.get(olca.Flow,"a9e29d5c-c101-4560-afce-118c572871f3") #flat glass, coated

########################
###     Processes  #####
########################
glassheet_process = client.get(olca.Process,"dfcd3134-bc9a-404a-acd6-40a563395c04") #flat glass production, coated | flat glass, coated | EN15804, U

exch = []
ID = 1


glas_input_glassheet = olca.Exchange()
glas_input_glassheet.input = True
glas_input_glassheet.flow = glassheet_flow
glas_input_glassheet.default_provider = glassheet_process
glas_input_glassheet.amount = 15 
glas_input_glassheet.unit = kg 
glas_input_glassheet.flow_property = mass
glas_input_glassheet.internal_id =ID;ID = ID + 1 
glas_input_glassheet.avoided_product = False
exch.append(glas_input_glassheet)

glas_process = olca.Process()
glas_process.category = client.find(olca.Category,"A1-A3")
glas_process.process_type = olca.ProcessType.UNIT_PROCESS
glas_process.id = str(uuid.uuid4())
glas_process.name = "glas_primaer"
glas_process.olca_type = olca.schema.Process.__name__

glas_output_glas = olca.Exchange()
glas_output_glas.input = False
glas_output_glas.flow = glas_flow
glas_output_glas.flow_property = area
glas_output_glas.unit = m2
glas_output_glas.amount = 1
glas_output_glas.quantitative_reference = True
glas_output_glas.internal_id =ID;ID = ID + 1 
glas_output_glas.avoided_product = False
exch.append(glas_output_glas)

glas_process.exchanges= exch
client.insert(glas_process)
