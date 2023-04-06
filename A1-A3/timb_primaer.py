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


if client.find(olca.Process,"timb_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"timb_primaer").id)
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

timb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_holz = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","timb"])

co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","timb"])

wffa_amount = 0.21 * timb_holz 
NECE_amount   = -222 * timb_holz

########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"timb_primaer"):
    timb_flow = olca.Flow()
    timb_flow.id = str(uuid.uuid4())
    timb_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    timb_flow.name = "timb_primaer"
    timb_flow.description = "Furnierschichtholz aus der Oekobaudat"
    timb_flow.unit = m3
    timb_flow.flow_properties = [vol_factor]
    timb_flow.olca_type = olca.schema.Flow.__name__

    client.insert(timb_flow)

timb_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_primaer").id)

WFFA_flow   = client.get(olca.Flow,client.find(olca.Flow,"WFFA").id)
NECE_flow  = client.get(olca.Flow,client.find(olca.Flow,"NECE").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)
               
timber_flow = client.get(olca.Flow,"92292ccd-ecbb-5ae6-8141-03114dd9c07c") #structural timber

########################
###     Processes  #####
########################
timber_process = client.get(olca.Process,"19958e35-bbda-4f3a-a92c-04270ac71ed9") #structural timber production | structural timber | EN15804, U


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




timb_primaer_input_timber = olca.Exchange()
timb_primaer_input_timber.input = True
timb_primaer_input_timber.flow = timber_flow
timb_primaer_input_timber.default_provider = timber_process
timb_primaer_input_timber.flow_property = vol
timb_primaer_input_timber.unit = m3
timb_primaer_input_timber.amount = 1
timb_primaer_input_timber.internal_id = ID;ID = ID + 1
timb_primaer_input_timber.avoided_product = False
exch.append(timb_primaer_input_timber)

timb_primaer_input_wffa = olca.Exchange()
timb_primaer_input_wffa.input = False
timb_primaer_input_wffa.flow = WFFA_flow
timb_primaer_input_wffa.flow_property = landuse
timb_primaer_input_wffa.unit = m2a
timb_primaer_input_wffa.amount = wffa_amount
timb_primaer_input_wffa.quantitative_reference = False
timb_primaer_input_wffa.internal_id =ID;ID = ID + 1 
timb_primaer_input_wffa.avoided_product = False
exch.append(timb_primaer_input_wffa)

timb_primaer_process = olca.Process()
timb_primaer_process.category = client.find(olca.Category,"A1-A3")
timb_primaer_process.process_type = olca.ProcessType.UNIT_PROCESS
timb_primaer_process.id = str(uuid.uuid4())
timb_primaer_process.name = "timb_primaer"
timb_primaer_process.olca_type = olca.schema.Process.__name__


timb_primaer_output_timb = olca.Exchange()
timb_primaer_output_timb.input = False
timb_primaer_output_timb.flow = timb_flow
timb_primaer_output_timb.flow_property = vol
timb_primaer_output_timb.unit = m3
timb_primaer_output_timb.amount = 1
timb_primaer_output_timb.quantitative_reference = True
timb_primaer_output_timb.internal_id = ID;ID = ID + 1
timb_primaer_output_timb.avoided_product = False
exch.append(timb_primaer_output_timb)


timb_primaer_output_carbon_inherent = olca.Exchange()
timb_primaer_output_carbon_inherent.input = False
timb_primaer_output_carbon_inherent.flow = carbonout_flow
timb_primaer_output_carbon_inherent.flow_property = mass
timb_primaer_output_carbon_inherent.unit = kg
timb_primaer_output_carbon_inherent.amount = 0
timb_primaer_output_carbon_inherent.quantitative_reference = False
timb_primaer_output_carbon_inherent.internal_id = ID;ID = ID + 1
timb_primaer_output_carbon_inherent.avoided_product = False
exch.append(timb_primaer_output_carbon_inherent)

timb_primaer_output_NECE = olca.Exchange()
timb_primaer_output_NECE.input = False
timb_primaer_output_NECE.flow = NECE_flow
timb_primaer_output_NECE.flow_property = mass
timb_primaer_output_NECE.unit = kg
timb_primaer_output_NECE.amount = NECE_amount
timb_primaer_output_NECE.quantitative_reference = False
timb_primaer_output_NECE.internal_id =ID;ID = ID + 1 
timb_primaer_output_NECE.avoided_product = False
exch.append(timb_primaer_output_NECE)

timb_primaer_process.exchanges= exch

client.insert(timb_primaer_process)
