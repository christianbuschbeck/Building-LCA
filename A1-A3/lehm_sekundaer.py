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
import pandas as pd

#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"lehm_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"lehm_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,mass,MJ,energy



########################
###     Amounts    #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
lehm_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lehm"])



########################
###     Flows      #####
########################

if not client.find(olca.Flow,"lehm_sekundaer"):
    lehm_flow = olca.Flow()
    lehm_flow.id = str(uuid.uuid4())
    lehm_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    lehm_flow.name = "lehm_sekundaer"
    lehm_flow.description = "lehmindungen des Holzhybrides"
    lehm_flow.unit = kg
    lehm_flow.olca_type = olca.schema.Flow.__name__

    client.insert(lehm_flow)

lehm_flow = client.get(olca.Flow,client.find(olca.Flow,"lehm_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)



########################
###     Processes  #####
########################
exch = []
ID=1

lehm_input_SM = olca.Exchange()
lehm_input_SM.input = True
lehm_input_SM.flow = SM_flow
lehm_input_SM.amount =  lehm_dichte # in kg
lehm_input_SM.unit = kg  
lehm_input_SM.flow_property = mass
lehm_input_SM.internal_id =ID;ID = ID + 1 
lehm_input_SM.avoided_product = False
lehm_input_SM.quantitative_reference = False
exch.append(lehm_input_SM)


lehm_process = olca.Process()
lehm_process.category = client.find(olca.Category,"A1-A3")
lehm_process.process_type = olca.ProcessType.UNIT_PROCESS
lehm_process.id = str(uuid.uuid4())
lehm_process.name = "lehm_sekundaer"
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
