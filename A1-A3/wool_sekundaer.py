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


if client.find(olca.Process,"wool_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"wool_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,m3,mass,vol_factor,MJ,energy


########################
###     Amounts    #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
wool_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","wool"])


########################
###     Flows      #####
########################


if not client.find(olca.Flow,"wool_sekundaer"):
    wool_flow = olca.Flow()
    wool_flow.id = str(uuid.uuid4())
    wool_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    wool_flow.name = "wool_sekundaer"
    wool_flow.description = "Furnierschichtholz aus der Oekobaudat"
    wool_flow.unit = m3
    wool_flow.flow_properties = [vol_factor]
    wool_flow.olca_type = olca.schema.Flow.__name__

    client.insert(wool_flow)

wool_flow = client.get(olca.Flow,client.find(olca.Flow,"wool_sekundaer").id)


SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)

########################
###     Processes  #####
########################
exch = []
ID = 1


wool_input_SM = olca.Exchange()
wool_input_SM.input = True
wool_input_SM.flow = SM_flow
wool_input_SM.amount =  1 # in kg
wool_input_SM.unit = kg  
wool_input_SM.flow_property = mass
wool_input_SM.internal_id =ID;ID = ID + 1 
wool_input_SM.avoided_product = False
wool_input_SM.quantitative_reference = False
exch.append(wool_input_SM)

wool_process = olca.Process()
wool_process.category = client.find(olca.Category,"A1-A3")
wool_process.process_type = olca.ProcessType.UNIT_PROCESS
wool_process.id = str(uuid.uuid4())
wool_process.name = "wool_sekundaer"
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
