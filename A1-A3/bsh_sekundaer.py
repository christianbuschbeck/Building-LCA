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


if client.find(olca.Process,"bsh_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"bsh_sekundaer").id)
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

bsh_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
co2_for_heat = 158
co2_verpackung = 5
co2_foss = 18.61 + 73.83
co2_seq = co2_inh + co2_for_heat + co2_verpackung

energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])


 

########################
###     Flows      #####
########################




carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"bsh_sekundaer"):    
    bsh_sekundaer_flow = olca.Flow()
    bsh_sekundaer_flow.id = str(uuid.uuid4())
    bsh_sekundaer_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    bsh_sekundaer_flow.name = "bsh_sekundaer"
    bsh_sekundaer_flow.description = "sekundaerer bsh"
    bsh_sekundaer_flow.unit = m3
    bsh_sekundaer_flow.flow_properties = [vol_factor]
    bsh_sekundaer_flow.olca_type = olca.schema.Flow.__name__

    client.insert(bsh_sekundaer_flow)

bsh_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)
PERM_flow = client.get(olca.Flow,"2b08df35-ebaf-4dcf-a5ac-d985915d5223")# Energy, gross calorific value, in biomass, used as raw material 


########################
###     Processes  #####
########################
exch=[]
ID=1

bsh_sekundaer_process_input_SM = olca.Exchange()
bsh_sekundaer_process_input_SM.input = True
bsh_sekundaer_process_input_SM.flow = SM_flow
bsh_sekundaer_process_input_SM.amount = bsh_dichte # in kg
bsh_sekundaer_process_input_SM.unit = kg  
bsh_sekundaer_process_input_SM.flow_property = mass
bsh_sekundaer_process_input_SM.internal_id =ID;ID = ID + 1 
bsh_sekundaer_process_input_SM.avoided_product = False
bsh_sekundaer_process_input_SM.quantitative_reference = False
exch.append(bsh_sekundaer_process_input_SM)


bsh_sekundaer_process_input_carbon = olca.Exchange()
bsh_sekundaer_process_input_carbon.input = True
bsh_sekundaer_process_input_carbon.flow = carbonin_flow
bsh_sekundaer_process_input_carbon.amount = co2_inh
bsh_sekundaer_process_input_carbon.unit = m3 
bsh_sekundaer_process_input_carbon.flow_property = vol 
bsh_sekundaer_process_input_carbon.internal_id = ID;ID = ID + 1
bsh_sekundaer_process_input_carbon.avoided_product = False
exch.append(bsh_sekundaer_process_input_carbon)

bsh_sekundaer_process_input_energy = olca.Exchange()
bsh_sekundaer_process_input_energy.input = True
bsh_sekundaer_process_input_energy.flow = energyin_flow
bsh_sekundaer_process_input_energy.amount = energy_inh  
bsh_sekundaer_process_input_energy.unit = MJ 
bsh_sekundaer_process_input_energy.flow_property = energy 
bsh_sekundaer_process_input_energy.internal_id = ID;ID = ID + 1
bsh_sekundaer_process_input_energy.avoided_product = False
exch.append(bsh_sekundaer_process_input_energy)

bsh_sekundaer_process_input_perm = olca.Exchange()
bsh_sekundaer_process_input_perm.input = True
bsh_sekundaer_process_input_perm.flow = PERM_flow
bsh_sekundaer_process_input_perm.amount = energy_inh 
bsh_sekundaer_process_input_perm.unit = MJ 
bsh_sekundaer_process_input_perm.flow_property = energy 
bsh_sekundaer_process_input_perm.internal_id =ID;ID = ID + 1 
bsh_sekundaer_process_input_perm.avoided_product = False
exch.append(bsh_sekundaer_process_input_perm)


bsh_sekundaer_process = olca.Process()
bsh_sekundaer_process.category = client.find(olca.Category,"A1-A3")
bsh_sekundaer_process.process_type = olca.ProcessType.UNIT_PROCESS
bsh_sekundaer_process.id = str(uuid.uuid4())
bsh_sekundaer_process.name = "bsh_sekundaer"
bsh_sekundaer_process.olca_type = olca.schema.Process.__name__


bsh_sekundaer_process_output_bsh = olca.Exchange()
bsh_sekundaer_process_output_bsh.input = False
bsh_sekundaer_process_output_bsh.flow = bsh_sekundaer_flow
bsh_sekundaer_process_output_bsh.flow_property = vol
bsh_sekundaer_process_output_bsh.unit = m3
bsh_sekundaer_process_output_bsh.amount = 1
bsh_sekundaer_process_output_bsh.quantitative_reference = True
bsh_sekundaer_process_output_bsh.internal_id = ID;ID = ID + 1
bsh_sekundaer_process_output_bsh.avoided_product = False
exch.append(bsh_sekundaer_process_output_bsh)



bsh_sekundaer_process.exchanges= exch

client.insert(bsh_sekundaer_process)
