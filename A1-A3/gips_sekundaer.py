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


if client.find(olca.Process,"gips_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"gips_sekundaer").id)
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
gips_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","gips"])


########################
###     Flows      #####
########################


if not client.find(olca.Flow,"gips_sekundaer"):
    gips_flow = olca.Flow()
    gips_flow.id = str(uuid.uuid4())
    gips_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    gips_flow.name = "gips_sekundaer"
    gips_flow.description = "Furnierschichtholz aus der Oekobaudat"
    gips_flow.unit = m3
    gips_flow.flow_properties = [vol_factor]
    gips_flow.olca_type = olca.schema.Flow.__name__

    client.insert(gips_flow)

gips_flow = client.get(olca.Flow,client.find(olca.Flow,"gips_sekundaer").id)


SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)

########################
###     Processes  #####
########################
exch = []
ID = 1


gips_input_SM = olca.Exchange()
gips_input_SM.input = True
gips_input_SM.flow = SM_flow
gips_input_SM.amount =  1 # in kg
gips_input_SM.unit = kg  
gips_input_SM.flow_property = mass
gips_input_SM.internal_id =ID;ID = ID + 1 
gips_input_SM.avoided_product = False
gips_input_SM.quantitative_reference = False
exch.append(gips_input_SM)

gips_process = olca.Process()
gips_process.category = client.find(olca.Category,"A1-A3")
gips_process.process_type = olca.ProcessType.UNIT_PROCESS
gips_process.id = str(uuid.uuid4())
gips_process.name = "gips_sekundaer"
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
