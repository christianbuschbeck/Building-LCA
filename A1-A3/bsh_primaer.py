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


if client.find(olca.Process,"bsh_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"bsh_primaer").id)
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

bsh_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_holz = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","bsh"])

co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])

wffa_amount = 0.21 * bsh_holz 
NECE_amount   = -222 * bsh_holz

########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"bsh_primaer"):
    bsh_flow = olca.Flow()
    bsh_flow.id = str(uuid.uuid4())
    bsh_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    bsh_flow.name = "bsh_primaer"
    bsh_flow.description = "Furnierschichtholz aus der Oekobaudat"
    bsh_flow.unit = m3
    bsh_flow.flow_properties = [vol_factor]
    bsh_flow.olca_type = olca.schema.Flow.__name__

    client.insert(bsh_flow)

bsh_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_primaer").id)

WFFA_flow   = client.get(olca.Flow,client.find(olca.Flow,"WFFA").id)
NECE_flow  = client.get(olca.Flow,client.find(olca.Flow,"NECE").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)
               
glulam_flow = client.get(olca.Flow,"d16a46cf-4cbd-592c-8b46-f91333d63b5d") #glued laminated timber, average glue mix

########################
###     Processes  #####
########################
glulam_process = client.get(olca.Process,"d80a8e70-5bd2-415c-92bb-c7ddaa795424") #glued laminated timber production, average glue mix | glued laminated timber, average glue mix | EN15804, U


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




bsh_primaer_input_glulam = olca.Exchange()
bsh_primaer_input_glulam.input = True
bsh_primaer_input_glulam.flow = glulam_flow
bsh_primaer_input_glulam.default_provider = glulam_process
bsh_primaer_input_glulam.flow_property = vol
bsh_primaer_input_glulam.unit = m3
bsh_primaer_input_glulam.amount = 1
bsh_primaer_input_glulam.internal_id = ID;ID = ID + 1
bsh_primaer_input_glulam.avoided_product = False
exch.append(bsh_primaer_input_glulam)

bsh_primaer_input_wffa = olca.Exchange()
bsh_primaer_input_wffa.input = False
bsh_primaer_input_wffa.flow = WFFA_flow
bsh_primaer_input_wffa.flow_property = landuse
bsh_primaer_input_wffa.unit = m2a
bsh_primaer_input_wffa.amount = wffa_amount
bsh_primaer_input_wffa.quantitative_reference = False
bsh_primaer_input_wffa.internal_id =ID;ID = ID + 1 
bsh_primaer_input_wffa.avoided_product = False
exch.append(bsh_primaer_input_wffa)

bsh_primaer_process = olca.Process()
bsh_primaer_process.category = client.find(olca.Category,"A1-A3")
bsh_primaer_process.process_type = olca.ProcessType.UNIT_PROCESS
bsh_primaer_process.id = str(uuid.uuid4())
bsh_primaer_process.name = "bsh_primaer"
bsh_primaer_process.olca_type = olca.schema.Process.__name__


bsh_primaer_output_bsh = olca.Exchange()
bsh_primaer_output_bsh.input = False
bsh_primaer_output_bsh.flow = bsh_flow
bsh_primaer_output_bsh.flow_property = vol
bsh_primaer_output_bsh.unit = m3
bsh_primaer_output_bsh.amount = 1
bsh_primaer_output_bsh.quantitative_reference = True
bsh_primaer_output_bsh.internal_id = ID;ID = ID + 1
bsh_primaer_output_bsh.avoided_product = False
exch.append(bsh_primaer_output_bsh)


bsh_primaer_output_carbon_inherent = olca.Exchange()
bsh_primaer_output_carbon_inherent.input = False
bsh_primaer_output_carbon_inherent.flow = carbonout_flow
bsh_primaer_output_carbon_inherent.flow_property = mass
bsh_primaer_output_carbon_inherent.unit = kg
bsh_primaer_output_carbon_inherent.amount = 0
bsh_primaer_output_carbon_inherent.quantitative_reference = False
bsh_primaer_output_carbon_inherent.internal_id = ID;ID = ID + 1
bsh_primaer_output_carbon_inherent.avoided_product = False
exch.append(bsh_primaer_output_carbon_inherent)

bsh_primaer_output_NECE = olca.Exchange()
bsh_primaer_output_NECE.input = False
bsh_primaer_output_NECE.flow = NECE_flow
bsh_primaer_output_NECE.flow_property = mass
bsh_primaer_output_NECE.unit = kg
bsh_primaer_output_NECE.amount = NECE_amount
bsh_primaer_output_NECE.quantitative_reference = False
bsh_primaer_output_NECE.internal_id =ID;ID = ID + 1 
bsh_primaer_output_NECE.avoided_product = False
exch.append(bsh_primaer_output_NECE)

bsh_primaer_process.exchanges= exch

client.insert(bsh_primaer_process)
