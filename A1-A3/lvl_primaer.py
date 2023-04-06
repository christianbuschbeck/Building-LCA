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


if client.find(olca.Process,"lvl_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"lvl_primaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,m3,vol,mass,vol_factor,MJ,energy,landuse,m2a


###################################################
###     Inhärenter Materialeigenschaften      #####
###################################################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_holz = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])

co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
co2_for_heat = 1872 
GWP_amount = 10.34 + 263.1
co2_seq = co2_inh + co2_for_heat


energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])
lvl_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","lvl"])

wffa_amount = 0.66 * lvl_holz 
########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"lvl_primaer"):
    lvl_flow = olca.Flow()
    lvl_flow.id = str(uuid.uuid4())
    lvl_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    lvl_flow.name = "lvl_primaer"
    lvl_flow.description = "Furnierschichtholz aus der Oekobaudat"
    lvl_flow.unit = m3
    lvl_flow.flow_properties = [vol_factor]
    lvl_flow.olca_type = olca.schema.Flow.__name__

    client.insert(lvl_flow)

lvl_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_primaer").id)

ODP_flow = client.get(olca.Flow,client.find(olca.Flow,"ODP (EN15804)").id) #Methane, trichlorofluoro-, CFC-11
GWP_flow = client.get(olca.Flow,"f9749677-9c9f-4678-ab55-c607dfdc2cb9") # Carbon dioxide, fossil
AP_flow = client.get(olca.Flow,client.find(olca.Flow,"AP (EN15804)").id) #Ammonia
EP_flow = client.get(olca.Flow,client.find(olca.Flow,"EP (EN15804)").id) #Phosphate
POCP_flow = client.get(olca.Flow,client.find(olca.Flow,"POCP (EN15804)").id) #Tolulene
ADPE_flow = client.get(olca.Flow,client.find(olca.Flow,"ADPE (EN15804)").id) #Antimony
ADPF_flow = client.get(olca.Flow,client.find(olca.Flow,"ADPF (EN15804)").id) #Gas, off-gas, oil production, in ground
FW_flow = client.get(olca.Flow,client.find(olca.Flow,"FW (EN15804)").id) #FW AI
PENRT_flow = client.get(olca.Flow,"8842042d-7f07-45f8-bf43-fa83833d75de") #Energy, gross calorific value, in biomass, primary forest
PERT_flow = client.get(olca.Flow,"01c12fca-ad8b-4902-8b48-2d5afe3d3a0f") #Energy, gross calorific value, in biomass
PENRM_flow = client.get(olca.Flow,client.find(olca.Flow,"PENRM (EN15804)").id) 
PERM_flow = client.get(olca.Flow,client.find(olca.Flow,"PERM (EN15804)").id) 
PERE_flow = client.get(olca.Flow,client.find(olca.Flow,"PERE (EN15804)").id) 
PENRE_flow = client.get(olca.Flow,client.find(olca.Flow,"PENRE (EN15804)").id) 


SM_flow = client.get(olca.Flow,client.find(olca.Flow,"secondary material (EN15804)").id) 


NECE_flow  = client.get(olca.Flow,client.find(olca.Flow,"NECE").id)
WFFA_flow   = client.get(olca.Flow,client.find(olca.Flow,"WFFA").id)

AP_amount  = 1.637
EP_amount = 0.3694
ODP_amount  = 3.288E-9
POCP_amount  = 0.2773
ADPE_amount  = 0.0001747
ADPF_amount  = 5134
FW_amount = -2.185
PENRT_amount = 4945
PERT_amount  = 34210
PERM_amount  = 13150
PENRM_amount = lvl_energy_inh_nr
NECE_amount   = -341 * lvl_holz

#PERT = 34210
#PERE = 21050

########################
###     Processes  #####
########################
exch = []
ID = 1

lvl_primaer_input_carbon_inherent = olca.Exchange()
lvl_primaer_input_carbon_inherent.input = True
lvl_primaer_input_carbon_inherent.flow = carbonin_flow
lvl_primaer_input_carbon_inherent.amount = co2_seq
lvl_primaer_input_carbon_inherent.unit = m3 
lvl_primaer_input_carbon_inherent.flow_property = vol 
lvl_primaer_input_carbon_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_input_carbon_inherent.avoided_product = False
exch.append(lvl_primaer_input_carbon_inherent)

lvl_primaer_input_energy_inherent = olca.Exchange()
lvl_primaer_input_energy_inherent.input = True
lvl_primaer_input_energy_inherent.flow = energyin_flow
lvl_primaer_input_energy_inherent.amount = PERM_amount 
lvl_primaer_input_energy_inherent.unit = MJ 
lvl_primaer_input_energy_inherent.flow_property = energy 
lvl_primaer_input_energy_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_input_energy_inherent.avoided_product = False
exch.append(lvl_primaer_input_energy_inherent)

lvl_primaer_input_ADPE = olca.Exchange()
lvl_primaer_input_ADPE.input = True
lvl_primaer_input_ADPE.flow = ADPE_flow
lvl_primaer_input_ADPE.flow_property = mass
lvl_primaer_input_ADPE.unit = kg
lvl_primaer_input_ADPE.amount = ADPE_amount
lvl_primaer_input_ADPE.quantitative_reference = True
lvl_primaer_input_ADPE.internal_id =ID;ID = ID + 1 
lvl_primaer_input_ADPE.avoided_product = False
exch.append(lvl_primaer_input_ADPE)

lvl_primaer_input_ADPF = olca.Exchange()
lvl_primaer_input_ADPF.input = True
lvl_primaer_input_ADPF.flow = ADPF_flow
lvl_primaer_input_ADPF.flow_property = mass
lvl_primaer_input_ADPF.unit = kg
lvl_primaer_input_ADPF.amount = ADPF_amount
lvl_primaer_input_ADPF.quantitative_reference = True
lvl_primaer_input_ADPF.internal_id =ID;ID = ID + 1 
lvl_primaer_input_ADPF.avoided_product = False
exch.append(lvl_primaer_input_ADPF)

lvl_primaer_input_FW = olca.Exchange()
lvl_primaer_input_FW.input = True
lvl_primaer_input_FW.flow = FW_flow
lvl_primaer_input_FW.flow_property = mass
lvl_primaer_input_FW.unit = kg
lvl_primaer_input_FW.amount = FW_amount
lvl_primaer_input_FW.quantitative_reference = True
lvl_primaer_input_FW.internal_id =ID;ID = ID + 1 
lvl_primaer_input_FW.avoided_product = False
exch.append(lvl_primaer_input_FW)

lvl_primaer_input_PENRT = olca.Exchange()
lvl_primaer_input_PENRT.input = True
lvl_primaer_input_PENRT.flow = PENRT_flow
lvl_primaer_input_PENRT.flow_property = energy
lvl_primaer_input_PENRT.unit = MJ
lvl_primaer_input_PENRT.amount = PENRT_amount
lvl_primaer_input_PENRT.quantitative_reference = True
lvl_primaer_input_PENRT.internal_id =ID;ID = ID + 1 
lvl_primaer_input_PENRT.avoided_product = False
exch.append(lvl_primaer_input_PENRT)

lvl_primaer_input_PERT = olca.Exchange()
lvl_primaer_input_PERT.input = True
lvl_primaer_input_PERT.flow = PERT_flow
lvl_primaer_input_PERT.flow_property = energy
lvl_primaer_input_PERT.unit = MJ
lvl_primaer_input_PERT.amount = PERT_amount
lvl_primaer_input_PERT.quantitative_reference = True
lvl_primaer_input_PERT.internal_id =ID;ID = ID + 1 
lvl_primaer_input_PERT.avoided_product = False
exch.append(lvl_primaer_input_PERT)

lvl_primaer_input_PENRM = olca.Exchange()
lvl_primaer_input_PENRM.input = False
lvl_primaer_input_PENRM.flow = PENRM_flow
lvl_primaer_input_PENRM.flow_property = energy
lvl_primaer_input_PENRM.unit = MJ
lvl_primaer_input_PENRM.amount = PENRM_amount
lvl_primaer_input_PENRM.quantitative_reference = False
lvl_primaer_input_PENRM.internal_id =ID;ID = ID + 1 
lvl_primaer_input_PENRM.avoided_product = False
exch.append(lvl_primaer_input_PENRM)

lvl_primaer_input_wffa = olca.Exchange()
lvl_primaer_input_wffa.input = False
lvl_primaer_input_wffa.flow = WFFA_flow
lvl_primaer_input_wffa.flow_property = landuse
lvl_primaer_input_wffa.unit = m2a
lvl_primaer_input_wffa.amount = wffa_amount
lvl_primaer_input_wffa.quantitative_reference = False
lvl_primaer_input_wffa.internal_id =ID;ID = ID + 1 
lvl_primaer_input_wffa.avoided_product = False
exch.append(lvl_primaer_input_wffa)

lvl_primaer_process = olca.Process()
lvl_primaer_process.category = client.find(olca.Category,"A1-A3")
lvl_primaer_process.process_type = olca.ProcessType.UNIT_PROCESS
lvl_primaer_process.id = str(uuid.uuid4())
lvl_primaer_process.name = "lvl_primaer"
lvl_primaer_process.olca_type = olca.schema.Process.__name__


lvl_primaer_output_lvl = olca.Exchange()
lvl_primaer_output_lvl.input = False
lvl_primaer_output_lvl.flow = lvl_flow
lvl_primaer_output_lvl.flow_property = vol
lvl_primaer_output_lvl.unit = m3
lvl_primaer_output_lvl.amount = 1
lvl_primaer_output_lvl.quantitative_reference = True
lvl_primaer_output_lvl.internal_id =ID;ID = ID + 1 
lvl_primaer_output_lvl.avoided_product = False
exch.append(lvl_primaer_output_lvl)

lvl_primaer_output_carbon = olca.Exchange()
lvl_primaer_output_carbon.input = False
lvl_primaer_output_carbon.flow = GWP_flow
lvl_primaer_output_carbon.flow_property = mass
lvl_primaer_output_carbon.unit = kg
lvl_primaer_output_carbon.amount = GWP_amount
lvl_primaer_output_carbon.quantitative_reference = False
lvl_primaer_output_carbon.internal_id =ID;ID = ID + 1 
lvl_primaer_output_carbon.avoided_product = False
exch.append(lvl_primaer_output_carbon)

lvl_primaer_output_carbon_inherent = olca.Exchange()
lvl_primaer_output_carbon_inherent.input = False
lvl_primaer_output_carbon_inherent.flow = carbonout_flow
lvl_primaer_output_carbon_inherent.flow_property = mass
lvl_primaer_output_carbon_inherent.unit = kg
lvl_primaer_output_carbon_inherent.amount = co2_for_heat
lvl_primaer_output_carbon_inherent.quantitative_reference = False
lvl_primaer_output_carbon_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_output_carbon_inherent.avoided_product = False
exch.append(lvl_primaer_output_carbon_inherent)

lvl_primaer_output_NECE = olca.Exchange()
lvl_primaer_output_NECE.input = False
lvl_primaer_output_NECE.flow = NECE_flow
lvl_primaer_output_NECE.flow_property = mass
lvl_primaer_output_NECE.unit = kg
lvl_primaer_output_NECE.amount = NECE_amount
lvl_primaer_output_NECE.quantitative_reference = False
lvl_primaer_output_NECE.internal_id =ID;ID = ID + 1 
lvl_primaer_output_NECE.avoided_product = False
exch.append(lvl_primaer_output_NECE)


lvl_primaer_output_AP = olca.Exchange()
lvl_primaer_output_AP.input = False
lvl_primaer_output_AP.flow = AP_flow
lvl_primaer_output_AP.flow_property = mass
lvl_primaer_output_AP.unit = kg
lvl_primaer_output_AP.amount = AP_amount
lvl_primaer_output_AP.quantitative_reference = False
lvl_primaer_output_AP.internal_id =ID;ID = ID + 1 
lvl_primaer_output_AP.avoided_product = False
exch.append(lvl_primaer_output_AP)

lvl_primaer_output_EP = olca.Exchange()
lvl_primaer_output_EP.input = False
lvl_primaer_output_EP.flow = EP_flow
lvl_primaer_output_EP.flow_property = mass
lvl_primaer_output_EP.unit = kg
lvl_primaer_output_EP.amount = EP_amount
lvl_primaer_output_EP.quantitative_reference = False
lvl_primaer_output_EP.internal_id =ID;ID = ID + 1 
lvl_primaer_output_EP.avoided_product = False
exch.append(lvl_primaer_output_EP)

lvl_primaer_output_ODP = olca.Exchange()
lvl_primaer_output_ODP.input = False
lvl_primaer_output_ODP.flow = ODP_flow
lvl_primaer_output_ODP.flow_property = mass
lvl_primaer_output_ODP.unit = kg
lvl_primaer_output_ODP.amount = ODP_amount
lvl_primaer_output_ODP.quantitative_reference = False
lvl_primaer_output_ODP.internal_id =ID;ID = ID + 1 
lvl_primaer_output_ODP.avoided_product = False
exch.append(lvl_primaer_output_ODP)

lvl_primaer_output_POCP = olca.Exchange()
lvl_primaer_output_POCP.input = False
lvl_primaer_output_POCP.flow = POCP_flow
lvl_primaer_output_POCP.flow_property = mass
lvl_primaer_output_POCP.unit = kg
lvl_primaer_output_POCP.amount = POCP_amount
lvl_primaer_output_POCP.quantitative_reference = False
lvl_primaer_output_POCP.internal_id =ID;ID = ID + 1 
lvl_primaer_output_POCP.avoided_product = False
exch.append(lvl_primaer_output_POCP)

lvl_primaer_output_energy_inherent = olca.Exchange()
lvl_primaer_output_energy_inherent.input = False
lvl_primaer_output_energy_inherent.flow = energyout_flow
lvl_primaer_output_energy_inherent.amount = 0   
lvl_primaer_output_energy_inherent.unit = MJ 
lvl_primaer_output_energy_inherent.flow_property = energy 
lvl_primaer_output_energy_inherent.internal_id =ID;ID = ID + 1 
lvl_primaer_output_energy_inherent.avoided_product = False
exch.append(lvl_primaer_output_energy_inherent)

lvl_primaer_process.exchanges= exch
client.insert(lvl_primaer_process)

