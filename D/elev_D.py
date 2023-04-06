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


if client.find(olca.Process,"elev_D"):
    todelete = client.get(olca.Process,client.find(olca.Process,"elev_D").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,mass,MJ,energy,items_unit,item_factor,item


########################
###     Flows      #####
########################

scen = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

anzahl_stockwerke = float(scen.loc[scen.loc[:,"vars"]=="include","stock"])

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)

if not client.find(olca.Flow,"elev_D"):
    elev_flow = olca.Flow()
    elev_flow.id = str(uuid.uuid4())
    elev_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    elev_flow.name = "elev_D"
    elev_flow.description = "Fahrstuhl aus der Oekobaudat"
    elev_flow.unit = items_unit
    elev_flow.flow_properties = [item_factor]
    elev_flow.olca_type = olca.schema.Flow.__name__

    client.insert(elev_flow)

elev_flow = client.get(olca.Flow,client.find(olca.Flow,"elev_D").id)

co2_flow = client.get(olca.Flow,"643975a8-03da-44bb-873f-4fe8e7740fe6") # Co2
co2_amount =     (    -1.58E+3 + (anzahl_stockwerke* -493.1)) * - 1
acid_flow = client.get(olca.Flow,"9990b51b-7023-4700-bca0-1a32ef921f74") #Ammonia
acid_amount =   (  ( -4.336 + (anzahl_stockwerke*  -1.137)) /1.6 ) * - 1
eutro_flow = client.get(olca.Flow,"48549f3b-606e-4e4f-b3eb-dd9f787f8827") #Phosphate
eutro_amount =    ( ( -0.3245 + (anzahl_stockwerke *     -0.09449))-(acid_amount*0.35)/1 ) * - 1
ozoa_flow = client.get(olca.Flow,"a916ca1b-4ece-4630-a563-ae3253efc04f") #Methane, trichlorofluoro-, CFC-11
ozoa_amount =    ( (6.892E-12 + (anzahl_stockwerke* 3.029E-12))/1 ) * - 1
ozob_flow = client.get(olca.Flow,"39946c56-cdf6-4a22-9ac9-1cd333b65533") #Tolulene
ozob_amount =     ((-0.4671 + (anzahl_stockwerke * -0.1486))/0.637 ) * - 1
adpe_flow = client.get(olca.Flow,"9dcebf82-e6b3-400d-98bb-353ac079cbe1") #Antimony
adpe_amount =    ( (-0.02495 + (anzahl_stockwerke * 0.00001174))/1 ) * - 1
adpf_flow = client.get(olca.Flow,"5e94ceb8-e8ac-3a24-b02e-f24ad54a7393") #Gas, off-gas, oil production, in ground
adpf_amount =    ( (-1.376E+4 + (anzahl_stockwerke * -3901))/38.84 ) * - 1
water_flow = client.get(olca.Flow,"0bb1a539-e7d2-3a36-bff0-7aa4558b0069") #water AI
water_amount =   ( -5.546 + (anzahl_stockwerke*         -0.3359) ) * - 1
penrt_flow = client.get(olca.Flow,"8842042d-7f07-45f8-bf43-fa83833d75de") #Energy, gross calorific value, in biomass, primary forest
penrt_amount =      (-1.336E+4 + (anzahl_stockwerke* -3729) ) * - 1
pere_flow = client.get(olca.Flow,"01c12fca-ad8b-4902-8b48-2d5afe3d3a0f") #Energy, gross calorific value, in biomass
pere_amount =      ( 355.1 + (anzahl_stockwerke * 425.5)) * - 1

perm_amount = 0

penrm_amount = 0
penrm_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_nr").id) 

########################
###     Processes  #####
########################
exch = []
ID = 1


elev_input_energy_inherent = olca.Exchange()
elev_input_energy_inherent.input = True
elev_input_energy_inherent.flow = energyin_flow
elev_input_energy_inherent.amount = perm_amount 
elev_input_energy_inherent.unit = MJ 
elev_input_energy_inherent.flow_property = energy 
elev_input_energy_inherent.internal_id =ID;ID = ID + 1 
elev_input_energy_inherent.avoided_product = False
exch.append(elev_input_energy_inherent)

elev_input_adpe = olca.Exchange()
elev_input_adpe.input = True
elev_input_adpe.flow = adpe_flow
elev_input_adpe.flow_property = mass
elev_input_adpe.unit = kg
elev_input_adpe.amount = adpe_amount
elev_input_adpe.quantitative_reference = True
elev_input_adpe.internal_id =ID;ID = ID + 1 
elev_input_adpe.avoided_product = False
exch.append(elev_input_adpe)

elev_input_adpf = olca.Exchange()
elev_input_adpf.input = True
elev_input_adpf.flow = adpf_flow
elev_input_adpf.flow_property = mass
elev_input_adpf.unit = kg
elev_input_adpf.amount = adpf_amount
elev_input_adpf.quantitative_reference = True
elev_input_adpf.internal_id =ID;ID = ID + 1 
elev_input_adpf.avoided_product = False
exch.append(elev_input_adpf)

elev_input_water = olca.Exchange()
elev_input_water.input = True
elev_input_water.flow = water_flow
elev_input_water.flow_property = mass
elev_input_water.unit = kg
elev_input_water.amount = water_amount
elev_input_water.quantitative_reference = True
elev_input_water.internal_id =ID;ID = ID + 1 
elev_input_water.avoided_product = False
exch.append(elev_input_water)

elev_input_penrt = olca.Exchange()
elev_input_penrt.input = True
elev_input_penrt.flow = penrt_flow
elev_input_penrt.flow_property = energy
elev_input_penrt.unit = MJ
elev_input_penrt.amount = penrt_amount
elev_input_penrt.quantitative_reference = True
elev_input_penrt.internal_id =ID;ID = ID + 1 
elev_input_penrt.avoided_product = False
exch.append(elev_input_penrt)

elev_input_pere = olca.Exchange()
elev_input_pere.input = True
elev_input_pere.flow = pere_flow
elev_input_pere.flow_property = energy
elev_input_pere.unit = MJ
elev_input_pere.amount = pere_amount
elev_input_pere.quantitative_reference = True
elev_input_pere.internal_id =ID;ID = ID + 1 
elev_input_pere.avoided_product = False
exch.append(elev_input_pere)

elev_input_penrm = olca.Exchange()
elev_input_penrm.input = False
elev_input_penrm.flow = penrm_flow
elev_input_penrm.flow_property = energy
elev_input_penrm.unit = MJ
elev_input_penrm.amount = penrm_amount
elev_input_penrm.quantitative_reference = False
elev_input_penrm.internal_id =ID;ID = ID + 1 
elev_input_penrm.avoided_product = False
exch.append(elev_input_penrm)

elev_process = olca.Process()
elev_process.category = client.find(olca.Category,"D")
elev_process.process_type = olca.ProcessType.UNIT_PROCESS
elev_process.id = str(uuid.uuid4())
elev_process.name = "elev_D"
elev_process.olca_type = olca.schema.Process.__name__


elev_output_co2 = olca.Exchange()
elev_output_co2.input = False
elev_output_co2.flow = co2_flow
elev_output_co2.flow_property = mass
elev_output_co2.unit = kg
elev_output_co2.amount = co2_amount
elev_output_co2.quantitative_reference = False
elev_output_co2.internal_id =ID;ID = ID + 1 
elev_output_co2.avoided_product = False
exch.append(elev_output_co2)


elev_output_elev = olca.Exchange()
elev_output_elev.input = False
elev_output_elev.flow = elev_flow
elev_output_elev.flow_property = item
elev_output_elev.unit = items_unit
elev_output_elev.amount = 1
elev_output_elev.quantitative_reference = True
elev_output_elev.internal_id =ID;ID = ID + 1 
elev_output_elev.avoided_product = False
exch.append(elev_output_elev)


elev_output_acid = olca.Exchange()
elev_output_acid.input = False
elev_output_acid.flow = acid_flow
elev_output_acid.flow_property = mass
elev_output_acid.unit = kg
elev_output_acid.amount = acid_amount
elev_output_acid.quantitative_reference = False
elev_output_acid.internal_id =ID;ID = ID + 1 
elev_output_acid.avoided_product = False
exch.append(elev_output_acid)

elev_output_eutro = olca.Exchange()
elev_output_eutro.input = False
elev_output_eutro.flow = eutro_flow
elev_output_eutro.flow_property = mass
elev_output_eutro.unit = kg
elev_output_eutro.amount = eutro_amount
elev_output_eutro.quantitative_reference = False
elev_output_eutro.internal_id =ID;ID = ID + 1 
elev_output_eutro.avoided_product = False
exch.append(elev_output_eutro)

elev_output_ozoa = olca.Exchange()
elev_output_ozoa.input = False
elev_output_ozoa.flow = ozoa_flow
elev_output_ozoa.flow_property = mass
elev_output_ozoa.unit = kg
elev_output_ozoa.amount = ozoa_amount
elev_output_ozoa.quantitative_reference = False
elev_output_ozoa.internal_id =ID;ID = ID + 1 
elev_output_ozoa.avoided_product = False
exch.append(elev_output_ozoa)

elev_output_ozob = olca.Exchange()
elev_output_ozob.input = False
elev_output_ozob.flow = ozob_flow
elev_output_ozob.flow_property = mass
elev_output_ozob.unit = kg
elev_output_ozob.amount = ozob_amount
elev_output_ozob.quantitative_reference = False
elev_output_ozob.internal_id =ID;ID = ID + 1 
elev_output_ozob.avoided_product = False
exch.append(elev_output_ozob)

elev_output_energy_inherent = olca.Exchange()
elev_output_energy_inherent.input = False
elev_output_energy_inherent.flow = energyout_flow
elev_output_energy_inherent.amount = 0   
elev_output_energy_inherent.unit = MJ 
elev_output_energy_inherent.flow_property = energy 
elev_output_energy_inherent.internal_id =ID;ID = ID + 1 
elev_output_energy_inherent.avoided_product = False
exch.append(elev_output_energy_inherent)

elev_process.exchanges= exch
client.insert(elev_process)
