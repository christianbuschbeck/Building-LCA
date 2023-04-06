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


if client.find(olca.Process,"osb_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"osb_primaer").id)
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

osb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_holz = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","osb"])

co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","osb"])

wffa_amount = 0.21 * osb_holz 
NECE_amount   = -222 * osb_holz

########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"osb_primaer"):
    osb_flow = olca.Flow()
    osb_flow.id = str(uuid.uuid4())
    osb_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    osb_flow.name = "osb_primaer"
    osb_flow.description = "Furnierschichtholz aus der Oekobaudat"
    osb_flow.unit = m3
    osb_flow.flow_properties = [vol_factor]
    osb_flow.olca_type = olca.schema.Flow.__name__

    client.insert(osb_flow)

osb_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_primaer").id)

WFFA_flow   = client.get(olca.Flow,client.find(olca.Flow,"WFFA").id)
NECE_flow  = client.get(olca.Flow,client.find(olca.Flow,"NECE").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)
               
orientedstrandboard_flow = client.get(olca.Flow,"888353c6-711d-4ba3-95eb-0368b6592c66") #oriented strand board

########################
###     Processes  #####
########################
orientedstrandboard_process = client.get(olca.Process,"d5105c93-ee9c-4c21-a170-f5a6ae69c870") #oriented strand board production | oriented strand board | EN15804, U


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




osb_primaer_input_osb = olca.Exchange()
osb_primaer_input_osb.input = True
osb_primaer_input_osb.flow = orientedstrandboard_flow
osb_primaer_input_osb.default_provider = orientedstrandboard_process
osb_primaer_input_osb.flow_property = vol
osb_primaer_input_osb.unit = m3
osb_primaer_input_osb.amount = 1
osb_primaer_input_osb.internal_id = ID;ID = ID + 1
osb_primaer_input_osb.avoided_product = False
exch.append(osb_primaer_input_osb)

osb_primaer_input_wffa = olca.Exchange()
osb_primaer_input_wffa.input = False
osb_primaer_input_wffa.flow = WFFA_flow
osb_primaer_input_wffa.flow_property = landuse
osb_primaer_input_wffa.unit = m2a
osb_primaer_input_wffa.amount = wffa_amount
osb_primaer_input_wffa.quantitative_reference = False
osb_primaer_input_wffa.internal_id =ID;ID = ID + 1 
osb_primaer_input_wffa.avoided_product = False
exch.append(osb_primaer_input_wffa)

osb_primaer_process = olca.Process()
osb_primaer_process.category = client.find(olca.Category,"A1-A3")
osb_primaer_process.process_type = olca.ProcessType.UNIT_PROCESS
osb_primaer_process.id = str(uuid.uuid4())
osb_primaer_process.name = "osb_primaer"
osb_primaer_process.olca_type = olca.schema.Process.__name__


osb_primaer_output_osb = olca.Exchange()
osb_primaer_output_osb.input = False
osb_primaer_output_osb.flow = osb_flow
osb_primaer_output_osb.flow_property = vol
osb_primaer_output_osb.unit = m3
osb_primaer_output_osb.amount = 1
osb_primaer_output_osb.quantitative_reference = True
osb_primaer_output_osb.internal_id = ID;ID = ID + 1
osb_primaer_output_osb.avoided_product = False
exch.append(osb_primaer_output_osb)


osb_primaer_output_carbon_inherent = olca.Exchange()
osb_primaer_output_carbon_inherent.input = False
osb_primaer_output_carbon_inherent.flow = carbonout_flow
osb_primaer_output_carbon_inherent.flow_property = mass
osb_primaer_output_carbon_inherent.unit = kg
osb_primaer_output_carbon_inherent.amount = 0
osb_primaer_output_carbon_inherent.quantitative_reference = False
osb_primaer_output_carbon_inherent.internal_id = ID;ID = ID + 1
osb_primaer_output_carbon_inherent.avoided_product = False
exch.append(osb_primaer_output_carbon_inherent)

osb_primaer_output_NECE = olca.Exchange()
osb_primaer_output_NECE.input = False
osb_primaer_output_NECE.flow = NECE_flow
osb_primaer_output_NECE.flow_property = mass
osb_primaer_output_NECE.unit = kg
osb_primaer_output_NECE.amount = NECE_amount
osb_primaer_output_NECE.quantitative_reference = False
osb_primaer_output_NECE.internal_id =ID;ID = ID + 1 
osb_primaer_output_NECE.avoided_product = False
exch.append(osb_primaer_output_NECE)

osb_primaer_process.exchanges= exch

client.insert(osb_primaer_process)
