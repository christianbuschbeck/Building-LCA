# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:36:17 2020

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


if client.find(olca.Process,"lvl_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"lvl_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import m3,vol,vol_factor,MJ,energy,kg,mass


#########################################
###     Inhärenter Kohlenstoff      #####
#########################################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
co2_for_heat = 1872
co2_verpackung = 5
co2_foss = 10.34 + 263.1
co2_seq = co2_inh + co2_for_heat + co2_verpackung

energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])


 

########################
###     Flows      #####
########################




carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"lvl_sekundaer"):    
    lvl_sekundaer_flow = olca.Flow()
    lvl_sekundaer_flow.id = str(uuid.uuid4())
    lvl_sekundaer_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    lvl_sekundaer_flow.name = "lvl_sekundaer"
    lvl_sekundaer_flow.description = "sekundaerer lvl"
    lvl_sekundaer_flow.unit = m3
    lvl_sekundaer_flow.flow_properties = [vol_factor]
    lvl_sekundaer_flow.olca_type = olca.schema.Flow.__name__

    client.insert(lvl_sekundaer_flow)

lvl_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)
PERM_flow = client.get(olca.Flow,"2b08df35-ebaf-4dcf-a5ac-d985915d5223")# Energy, gross calorific value, in biomass, used as raw material 

########################
###     Processes  #####
########################
exch=[]
ID=1

lvl_sekundaer_process_input_SM = olca.Exchange()
lvl_sekundaer_process_input_SM.input = True
lvl_sekundaer_process_input_SM.flow = SM_flow
lvl_sekundaer_process_input_SM.amount = lvl_dichte # in kg
lvl_sekundaer_process_input_SM.unit = kg  
lvl_sekundaer_process_input_SM.flow_property = mass
lvl_sekundaer_process_input_SM.internal_id =ID;ID = ID + 1 
lvl_sekundaer_process_input_SM.avoided_product = False
lvl_sekundaer_process_input_SM.quantitative_reference = False
exch.append(lvl_sekundaer_process_input_SM)



lvl_sekundaer_process_input_carbon = olca.Exchange()
lvl_sekundaer_process_input_carbon.input = True
lvl_sekundaer_process_input_carbon.flow = carbonin_flow
lvl_sekundaer_process_input_carbon.amount = co2_inh
lvl_sekundaer_process_input_carbon.unit = kg 
lvl_sekundaer_process_input_carbon.flow_property = mass
lvl_sekundaer_process_input_carbon.internal_id = ID;ID = ID + 1 
lvl_sekundaer_process_input_carbon.avoided_product = False
exch.append(lvl_sekundaer_process_input_carbon)


lvl_sekundaer_process_input_energy = olca.Exchange()
lvl_sekundaer_process_input_energy.input = True
lvl_sekundaer_process_input_energy.flow = energyin_flow
lvl_sekundaer_process_input_energy.amount = energy_inh  
lvl_sekundaer_process_input_energy.unit = MJ 
lvl_sekundaer_process_input_energy.flow_property = energy 
lvl_sekundaer_process_input_energy.internal_id = ID;ID = ID + 1 
lvl_sekundaer_process_input_energy.avoided_product = False
exch.append(lvl_sekundaer_process_input_energy)


lvl_sekundaer_process_input_perm = olca.Exchange()
lvl_sekundaer_process_input_perm.input = True
lvl_sekundaer_process_input_perm.flow = PERM_flow
lvl_sekundaer_process_input_perm.amount = energy_inh 
lvl_sekundaer_process_input_perm.unit = MJ 
lvl_sekundaer_process_input_perm.flow_property = energy 
lvl_sekundaer_process_input_perm.internal_id =ID;ID = ID + 1 
lvl_sekundaer_process_input_perm.avoided_product = False
exch.append(lvl_sekundaer_process_input_perm)



lvl_sekundaer_process = olca.Process()
lvl_sekundaer_process.category = client.find(olca.Category,"A1-A3")
lvl_sekundaer_process.process_type = olca.ProcessType.UNIT_PROCESS
lvl_sekundaer_process.id = str(uuid.uuid4())
lvl_sekundaer_process.name = "lvl_sekundaer"
lvl_sekundaer_process.olca_type = olca.schema.Process.__name__


lvl_sekundaer_process_output_lvl = olca.Exchange()
lvl_sekundaer_process_output_lvl.input = False
lvl_sekundaer_process_output_lvl.flow = lvl_sekundaer_flow
lvl_sekundaer_process_output_lvl.flow_property = vol
lvl_sekundaer_process_output_lvl.unit = m3
lvl_sekundaer_process_output_lvl.amount = 1
lvl_sekundaer_process_output_lvl.quantitative_reference = True
lvl_sekundaer_process_output_lvl.internal_id = ID;ID = ID + 1 
lvl_sekundaer_process_output_lvl.avoided_product = False
exch.append(lvl_sekundaer_process_output_lvl)



lvl_sekundaer_process.exchanges= exch

client.insert(lvl_sekundaer_process)
