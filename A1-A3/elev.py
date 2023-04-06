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
import pandas as pd

#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"elev"):
    todelete = client.get(olca.Process,client.find(olca.Process,"elev").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.Process,"fahrstuhl"):
    todelete = client.get(olca.Process,client.find(olca.Process,"fahrstuhl").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import items_unit,item_factor,item


########################
###     Flows      #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

anzahl_stockwerke = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
aufzug_factor = 2

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"elev"):
    elev_flow = olca.Flow()
    elev_flow.id = str(uuid.uuid4())
    elev_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    elev_flow.name = "elev"
    elev_flow.description = "Furnierschichtholz aus der Oekobaudat"
    elev_flow.unit = items_unit
    elev_flow.flow_properties = [item_factor]
    elev_flow.olca_type = olca.schema.Flow.__name__

    client.insert(elev_flow)

elev_flow = client.get(olca.Flow,client.find(olca.Flow,"elev").id)



fahrstuhl_flow = client.get(olca.Flow,"b4cbfdca-29f0-4a59-8c59-47777a13e628") #elevator, hydraulic

########################
###     Processes  #####
########################
fahrstuhl_process = client.get(olca.Process,"2212d56e-d66c-40d8-9e4e-28b8a288bbbe") #elevator production, hydraulic | elevator, hydraulic | EN15804, U

#Weil Disposal auch noch im process ist muss das raus
for i in range(1,5):

    for ex in fahrstuhl_process.exchanges:
        if ex.input==False:
            if ex.flow_property.name == "Mass":
                fahrstuhl_process.exchanges.remove(ex)
  

fahrstuhl_process.name = "fahrstuhl"
fahrstuhl_process.id = str(uuid.uuid4())
fahrstuhl_process.olca_type = olca.schema.Process.__name__
client.insert(fahrstuhl_process)    

fahrstuhl_process = client.get(olca.Process,client.find(olca.Process,"fahrstuhl").id) #eigen


exch = []
ID = 1



elev_input_fahrstuhl = olca.Exchange()
elev_input_fahrstuhl.input = True
elev_input_fahrstuhl.flow = fahrstuhl_flow
elev_input_fahrstuhl.default_provider = fahrstuhl_process
elev_input_fahrstuhl.flow_property = item
elev_input_fahrstuhl.unit = items_unit
elev_input_fahrstuhl.amount = 1
elev_input_fahrstuhl.quantitative_reference = False
elev_input_fahrstuhl.internal_id =ID;ID = ID + 1 
elev_input_fahrstuhl.avoided_product = False
exch.append(elev_input_fahrstuhl)

elev_process = olca.Process()
elev_process.category = client.find(olca.Category,"A1-A3")
elev_process.process_type = olca.ProcessType.UNIT_PROCESS
elev_process.id = str(uuid.uuid4())
elev_process.name = "elev"
elev_process.olca_type = olca.schema.Process.__name__

elev_output_elev = olca.Exchange()
elev_output_elev.input = False
elev_output_elev.flow = elev_flow
elev_output_elev.flow_property = item
elev_output_elev.unit = items_unit
elev_output_elev.amount = 1
elev_output_elev.quantitative_reference = True
elev_output_elev.internal_id =ID;ID = ID + 1 
elev_output_elev.avoided_product = False
exch.append(elev_output_elev)



elev_process.exchanges= exch
client.insert(elev_process)




