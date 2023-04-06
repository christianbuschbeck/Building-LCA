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


if client.find(olca.Process,"fibre_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"fibre_primaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,m3,vol,mass,energy,MJ,vol_factor,landuse,m2a


#########################################
###     Inhärenter Kohlenstoff      #####
#########################################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

fibre_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_holz = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","fibre"])

co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","fibre"])

wffa_amount = 0.21 * fibre_holz 
NECE_amount   = -222 * fibre_holz

########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"fibre_primaer"):
    fibre_flow = olca.Flow()
    fibre_flow.id = str(uuid.uuid4())
    fibre_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    fibre_flow.name = "fibre_primaer"
    fibre_flow.description = "Furnierschichtholz aus der Oekobaudat"
    fibre_flow.unit = m3
    fibre_flow.flow_properties = [vol_factor]
    fibre_flow.olca_type = olca.schema.Flow.__name__

    client.insert(fibre_flow)

fibre_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_primaer").id)

WFFA_flow   = client.get(olca.Flow,client.find(olca.Flow,"WFFA").id)
NECE_flow  = client.get(olca.Flow,client.find(olca.Flow,"NECE").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)
               
fibreboard_flow = client.get(olca.Flow,"113b50d5-d900-4fbf-adde-c69b662b6834") #fibreboard, soft

########################
###     Processes  #####
########################
fibreboard_process = client.get(olca.Process,"d3e2ae9f-2ab1-41fd-b5ad-e334f248c99c") #fibreboard production, soft, from wet & dry processes | fibreboard, soft | EN15804, U


exch=[]
ID=1

lvl_primaer_input_carbon_inherent = olca.Exchange()
lvl_primaer_input_carbon_inherent.input = True
lvl_primaer_input_carbon_inherent.flow = carbonin_flow
lvl_primaer_input_carbon_inherent.amount = co2_inh
lvl_primaer_input_carbon_inherent.unit = m3 
lvl_primaer_input_carbon_inherent.flow_property = vol 
lvl_primaer_input_carbon_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_input_carbon_inherent.avoided_product = False
exch.append(lvl_primaer_input_carbon_inherent)

lvl_primaer_input_energy_inherent = olca.Exchange()
lvl_primaer_input_energy_inherent.input = True
lvl_primaer_input_energy_inherent.flow = energyin_flow
lvl_primaer_input_energy_inherent.amount = energy_inh
lvl_primaer_input_energy_inherent.unit = MJ 
lvl_primaer_input_energy_inherent.flow_property = energy 
lvl_primaer_input_energy_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_input_energy_inherent.avoided_product = False
exch.append(lvl_primaer_input_energy_inherent)




fibre_primaer_input_fibre = olca.Exchange()
fibre_primaer_input_fibre.input = True
fibre_primaer_input_fibre.flow = fibreboard_flow
fibre_primaer_input_fibre.default_provider = fibreboard_process
fibre_primaer_input_fibre.flow_property = vol
fibre_primaer_input_fibre.unit = m3
fibre_primaer_input_fibre.amount = 1
fibre_primaer_input_fibre.internal_id = ID;ID = ID + 1
fibre_primaer_input_fibre.avoided_product = False
exch.append(fibre_primaer_input_fibre)

fibre_primaer_input_wffa = olca.Exchange()
fibre_primaer_input_wffa.input = False
fibre_primaer_input_wffa.flow = WFFA_flow
fibre_primaer_input_wffa.flow_property = landuse
fibre_primaer_input_wffa.unit = m2a
fibre_primaer_input_wffa.amount = wffa_amount
fibre_primaer_input_wffa.quantitative_reference = False
fibre_primaer_input_wffa.internal_id =ID;ID = ID + 1 
fibre_primaer_input_wffa.avoided_product = False
exch.append(fibre_primaer_input_wffa)

fibre_primaer_process = olca.Process()
fibre_primaer_process.category = client.find(olca.Category,"A1-A3")
fibre_primaer_process.process_type = olca.ProcessType.UNIT_PROCESS
fibre_primaer_process.id = str(uuid.uuid4())
fibre_primaer_process.name = "fibre_primaer"
fibre_primaer_process.olca_type = olca.schema.Process.__name__


fibre_primaer_output_fibre = olca.Exchange()
fibre_primaer_output_fibre.input = False
fibre_primaer_output_fibre.flow = fibre_flow
fibre_primaer_output_fibre.flow_property = vol
fibre_primaer_output_fibre.unit = m3
fibre_primaer_output_fibre.amount = 1
fibre_primaer_output_fibre.quantitative_reference = True
fibre_primaer_output_fibre.internal_id = ID;ID = ID + 1
fibre_primaer_output_fibre.avoided_product = False
exch.append(fibre_primaer_output_fibre)


fibre_primaer_output_carbon_inherent = olca.Exchange()
fibre_primaer_output_carbon_inherent.input = False
fibre_primaer_output_carbon_inherent.flow = carbonout_flow
fibre_primaer_output_carbon_inherent.flow_property = mass
fibre_primaer_output_carbon_inherent.unit = kg
fibre_primaer_output_carbon_inherent.amount = 0
fibre_primaer_output_carbon_inherent.quantitative_reference = False
fibre_primaer_output_carbon_inherent.internal_id = ID;ID = ID + 1
fibre_primaer_output_carbon_inherent.avoided_product = False
exch.append(fibre_primaer_output_carbon_inherent)

fibre_primaer_output_NECE = olca.Exchange()
fibre_primaer_output_NECE.input = False
fibre_primaer_output_NECE.flow = NECE_flow
fibre_primaer_output_NECE.flow_property = mass
fibre_primaer_output_NECE.unit = kg
fibre_primaer_output_NECE.amount = NECE_amount
fibre_primaer_output_NECE.quantitative_reference = False
fibre_primaer_output_NECE.internal_id =ID;ID = ID + 1 
fibre_primaer_output_NECE.avoided_product = False
exch.append(fibre_primaer_output_NECE)

fibre_primaer_process.exchanges= exch

client.insert(fibre_primaer_process)
