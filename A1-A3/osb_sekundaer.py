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


if client.find(olca.Process,"osb_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"osb_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

########################
###     Units      #####
########################

sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import m3,vol,energy,MJ,vol_factor,kg,mass


#########################################
###     Inhärenter Kohlenstoff      #####
#########################################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

osb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
co2_for_heat = 158
co2_verpackung = 5
co2_foss = 18.61 + 73.83
co2_seq = co2_inh + co2_for_heat + co2_verpackung

energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","osb"])


 

########################
###     Flows      #####
########################




carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"osb_sekundaer"):    
    osb_sekundaer_flow = olca.Flow()
    osb_sekundaer_flow.id = str(uuid.uuid4())
    osb_sekundaer_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    osb_sekundaer_flow.name = "osb_sekundaer"
    osb_sekundaer_flow.description = "sekundaerer osb"
    osb_sekundaer_flow.unit = m3
    osb_sekundaer_flow.flow_properties = [vol_factor]
    osb_sekundaer_flow.olca_type = olca.schema.Flow.__name__

    client.insert(osb_sekundaer_flow)

osb_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)
PERM_flow = client.get(olca.Flow,"2b08df35-ebaf-4dcf-a5ac-d985915d5223")# Energy, gross calorific value, in biomass, used as raw material 


########################
###     Processes  #####
########################
exch=[]
ID=1

osb_sekundaer_process_input_SM = olca.Exchange()
osb_sekundaer_process_input_SM.input = True
osb_sekundaer_process_input_SM.flow = SM_flow
osb_sekundaer_process_input_SM.amount = osb_dichte # in kg
osb_sekundaer_process_input_SM.unit = kg  
osb_sekundaer_process_input_SM.flow_property = mass
osb_sekundaer_process_input_SM.internal_id =ID;ID = ID + 1 
osb_sekundaer_process_input_SM.avoided_product = False
osb_sekundaer_process_input_SM.quantitative_reference = False
exch.append(osb_sekundaer_process_input_SM)


osb_sekundaer_process_input_carbon = olca.Exchange()
osb_sekundaer_process_input_carbon.input = True
osb_sekundaer_process_input_carbon.flow = carbonin_flow
osb_sekundaer_process_input_carbon.amount = co2_inh
osb_sekundaer_process_input_carbon.unit = kg 
osb_sekundaer_process_input_carbon.flow_property = mass
osb_sekundaer_process_input_carbon.internal_id = ID;ID = ID + 1
osb_sekundaer_process_input_carbon.avoided_product = False
exch.append(osb_sekundaer_process_input_carbon)

osb_sekundaer_process_input_energy = olca.Exchange()
osb_sekundaer_process_input_energy.input = True
osb_sekundaer_process_input_energy.flow = energyin_flow
osb_sekundaer_process_input_energy.amount = energy_inh  
osb_sekundaer_process_input_energy.unit = MJ 
osb_sekundaer_process_input_energy.flow_property = energy 
osb_sekundaer_process_input_energy.internal_id = ID;ID = ID + 1
osb_sekundaer_process_input_energy.avoided_product = False
exch.append(osb_sekundaer_process_input_energy)

osb_sekundaer_process_input_perm = olca.Exchange()
osb_sekundaer_process_input_perm.input = True
osb_sekundaer_process_input_perm.flow = PERM_flow
osb_sekundaer_process_input_perm.amount = energy_inh 
osb_sekundaer_process_input_perm.unit = MJ 
osb_sekundaer_process_input_perm.flow_property = energy 
osb_sekundaer_process_input_perm.internal_id =ID;ID = ID + 1 
osb_sekundaer_process_input_perm.avoided_product = False
exch.append(osb_sekundaer_process_input_perm)


osb_sekundaer_process = olca.Process()
osb_sekundaer_process.category = client.find(olca.Category,"A1-A3")
osb_sekundaer_process.process_type = olca.ProcessType.UNIT_PROCESS
osb_sekundaer_process.id = str(uuid.uuid4())
osb_sekundaer_process.name = "osb_sekundaer"
osb_sekundaer_process.olca_type = olca.schema.Process.__name__


osb_sekundaer_process_output_osb = olca.Exchange()
osb_sekundaer_process_output_osb.input = False
osb_sekundaer_process_output_osb.flow = osb_sekundaer_flow
osb_sekundaer_process_output_osb.flow_property = vol
osb_sekundaer_process_output_osb.unit = m3
osb_sekundaer_process_output_osb.amount = 1
osb_sekundaer_process_output_osb.quantitative_reference = True
osb_sekundaer_process_output_osb.internal_id = ID;ID = ID + 1
osb_sekundaer_process_output_osb.avoided_product = False
exch.append(osb_sekundaer_process_output_osb)



osb_sekundaer_process.exchanges= exch

client.insert(osb_sekundaer_process)
