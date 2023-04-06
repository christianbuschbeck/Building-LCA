# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:44:40 2020

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


if client.find(olca.Process,"lvl_verpackung"):
    todelete = client.get(olca.Process,client.find(olca.Process,"lvl_verpackung").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

########################
###     Units      #####
########################

exec(open(r'C:/Schaffeschaffe/Holzhybrid/skripte/global/units.py').read())


########################
###   Amounts        ###
########################

scen = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/szenarien.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)

co2_inh = float(scen.loc[scen.loc[:,"vars"]=="co2_inh","lvl"])
energy_inh = float(scen.loc[scen.loc[:,"vars"]=="energy_inh","lvl"])

co2_verpackung = 5

########################
###     Flows      #####
########################
carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"lvl_verpackung"):    

    verpackung_flow = olca.Flow()
    verpackung_flow.id = str(uuid.uuid4())
    verpackung_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    verpackung_flow.name = "lvl_verpackung"
    verpackung_flow.unit = items_unit
    verpackung_flow.flow_properties = [item_factor]

    client.insert(verpackung_flow)
verpackung_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_verpackung").id)

########################
###   Processes      ###
########################


verpackung = olca.Process()
verpackung.category = client.find(olca.Category,"A5")
verpackung.process_type = olca.ProcessType.UNIT_PROCESS
verpackung.id = str(uuid.uuid4())
verpackung.name = "lvl_verpackung"
verpackung.olca_type = olca.schema.Process.__name__


verpackung_output_carbon = olca.Exchange()
verpackung_output_carbon.input_lvl = False
verpackung_output_carbon.flow = carbonout_flow
verpackung_output_carbon.flow_property = mass
verpackung_output_carbon.unit = kg
verpackung_output_carbon.amount = co2_verpackung
verpackung_output_carbon.quantitative_reference = False
verpackung_output_carbon.internal_id = 1
verpackung_output_carbon.avoided_product = False

verpackung_output_energy = olca.Exchange()
verpackung_output_energy.input_lvl = False
verpackung_output_energy.flow = energyout_flow
verpackung_output_energy.flow_property = energy
verpackung_output_energy.unit = MJ
verpackung_output_energy.amount = co2_verpackung/co2_inh * energy_inh 
verpackung_output_energy.quantitative_reference = False
verpackung_output_energy.internal_id = 2
verpackung_output_energy.avoided_product = False


verpackung_output = olca.Exchange()
verpackung_output.input = False
verpackung_output.flow = verpackung_flow
verpackung_output.flow_property = item
verpackung_output.unit = items_unit
verpackung_output.amount = 1
verpackung_output.quantitative_reference = True
verpackung_output.internal_id = 3
verpackung_output.avoided_product = False

verpackung.exchanges= [verpackung_output,verpackung_output_carbon,verpackung_output_energy]

client.insert(verpackung)
