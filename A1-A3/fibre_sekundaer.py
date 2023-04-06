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


if client.find(olca.Process,"fibre_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"fibre_sekundaer").id)
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

fibre_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
co2_for_heat = 158
co2_verpackung = 5
co2_foss = 18.61 + 73.83
co2_seq = co2_inh + co2_for_heat + co2_verpackung

energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","fibre"])


 

########################
###     Flows      #####
########################




carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"fibre_sekundaer"):    
    fibre_sekundaer_flow = olca.Flow()
    fibre_sekundaer_flow.id = str(uuid.uuid4())
    fibre_sekundaer_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    fibre_sekundaer_flow.name = "fibre_sekundaer"
    fibre_sekundaer_flow.description = "sekundaerer fibre"
    fibre_sekundaer_flow.unit = m3
    fibre_sekundaer_flow.flow_properties = [vol_factor]
    fibre_sekundaer_flow.olca_type = olca.schema.Flow.__name__

    client.insert(fibre_sekundaer_flow)

fibre_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)
PERM_flow = client.get(olca.Flow,"2b08df35-ebaf-4dcf-a5ac-d985915d5223")# Energy, gross calorific value, in biomass, used as raw material 


########################
###     Processes  #####
########################
exch=[]
ID=1

fibre_sekundaer_process_input_SM = olca.Exchange()
fibre_sekundaer_process_input_SM.input = True
fibre_sekundaer_process_input_SM.flow = SM_flow
fibre_sekundaer_process_input_SM.amount = fibre_dichte # in kg
fibre_sekundaer_process_input_SM.unit = kg  
fibre_sekundaer_process_input_SM.flow_property = mass
fibre_sekundaer_process_input_SM.internal_id =ID;ID = ID + 1 
fibre_sekundaer_process_input_SM.avoided_product = False
fibre_sekundaer_process_input_SM.quantitative_reference = False
exch.append(fibre_sekundaer_process_input_SM)


fibre_sekundaer_process_input_carbon = olca.Exchange()
fibre_sekundaer_process_input_carbon.input = True
fibre_sekundaer_process_input_carbon.flow = carbonin_flow
fibre_sekundaer_process_input_carbon.amount = co2_inh
fibre_sekundaer_process_input_carbon.unit = m3 
fibre_sekundaer_process_input_carbon.flow_property = vol 
fibre_sekundaer_process_input_carbon.internal_id = ID;ID = ID + 1
fibre_sekundaer_process_input_carbon.avoided_product = False
exch.append(fibre_sekundaer_process_input_carbon)

fibre_sekundaer_process_input_energy = olca.Exchange()
fibre_sekundaer_process_input_energy.input = True
fibre_sekundaer_process_input_energy.flow = energyin_flow
fibre_sekundaer_process_input_energy.amount = energy_inh  
fibre_sekundaer_process_input_energy.unit = MJ 
fibre_sekundaer_process_input_energy.flow_property = energy 
fibre_sekundaer_process_input_energy.internal_id = ID;ID = ID + 1
fibre_sekundaer_process_input_energy.avoided_product = False
exch.append(fibre_sekundaer_process_input_energy)

fibre_sekundaer_process_input_perm = olca.Exchange()
fibre_sekundaer_process_input_perm.input = True
fibre_sekundaer_process_input_perm.flow = PERM_flow
fibre_sekundaer_process_input_perm.amount = energy_inh 
fibre_sekundaer_process_input_perm.unit = MJ 
fibre_sekundaer_process_input_perm.flow_property = energy 
fibre_sekundaer_process_input_perm.internal_id =ID;ID = ID + 1 
fibre_sekundaer_process_input_perm.avoided_product = False
exch.append(fibre_sekundaer_process_input_perm)


fibre_sekundaer_process = olca.Process()
fibre_sekundaer_process.category = client.find(olca.Category,"A1-A3")
fibre_sekundaer_process.process_type = olca.ProcessType.UNIT_PROCESS
fibre_sekundaer_process.id = str(uuid.uuid4())
fibre_sekundaer_process.name = "fibre_sekundaer"
fibre_sekundaer_process.olca_type = olca.schema.Process.__name__


fibre_sekundaer_process_output_fibre = olca.Exchange()
fibre_sekundaer_process_output_fibre.input = False
fibre_sekundaer_process_output_fibre.flow = fibre_sekundaer_flow
fibre_sekundaer_process_output_fibre.flow_property = vol
fibre_sekundaer_process_output_fibre.unit = m3
fibre_sekundaer_process_output_fibre.amount = 1
fibre_sekundaer_process_output_fibre.quantitative_reference = True
fibre_sekundaer_process_output_fibre.internal_id = ID;ID = ID + 1
fibre_sekundaer_process_output_fibre.avoided_product = False
exch.append(fibre_sekundaer_process_output_fibre)



fibre_sekundaer_process.exchanges= exch

client.insert(fibre_sekundaer_process)
