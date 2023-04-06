# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:33:55 2020

@author: cbuschbeck
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:44:50 2020

@author: cbuschbeck
"""

import sys
import pandas as pd

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
import runpy
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"D_e_k"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_e_k").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    
if client.find(olca.Process,"D_e_g"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_e_g").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    
if client.find(olca.Process,"verbrennung_heat"):
    todelete = client.get(olca.Process,client.find(olca.Process,"verbrennung_heat").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    
if client.find(olca.Process,"verbrennung_power"):
    todelete = client.get(olca.Process,client.find(olca.Process,"verbrennung_power").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import items_unit,item_factor,kg,item,mass,energy,MJ,kwh



########################
###    Anteile    #####
########################
anteile=runpy.run_module(mod_name="anteile")

lvl_en_fac   =anteile.get("lvl_en_fac")
bsh_en_fac   =anteile.get("bsh_en_fac")
timb_en_fac   =anteile.get("timb_en_fac")
osb_en_fac   =anteile.get("osb_en_fac")
fibre_en_fac   =anteile.get("fibre_en_fac")

########################
###     Amounts    #####
########################
    
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_vol = float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
bsh_vol = float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
timb_vol = float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
osb_vol = float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
fibre_vol = float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])


lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
lvl_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])
lvl_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
lvl_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","lvl"])
lvl_kg = lvl_vol * lvl_gewicht # vol*dichte
lvl_en_kg = lvl_kg * lvl_en_fac
lvl_en_vol = lvl_vol *lvl_en_fac


bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
bsh_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])
bsh_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","bsh"])
bsh_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","bsh"])
bsh_kg = bsh_vol * bsh_gewicht # vol*dichte
bsh_en_kg = bsh_kg * bsh_en_fac
bsh_en_vol = bsh_vol *bsh_en_fac


timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
timb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","timb"])
timb_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","timb"])
timb_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","timb"])
timb_kg = timb_vol * timb_gewicht # vol*dichte
timb_en_kg = timb_kg * timb_en_fac
timb_en_vol = timb_vol *timb_en_fac

osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
osb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","osb"])
osb_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","osb"])
osb_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","osb"])
osb_kg = osb_vol * osb_gewicht # vol*dichte
osb_en_kg = osb_kg * osb_en_fac
osb_en_vol = osb_vol *osb_en_fac


fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
fibre_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","fibre"])
fibre_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","fibre"])
fibre_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","fibre"])
fibre_kg = fibre_vol * fibre_gewicht # vol*dichte
fibre_en_kg = fibre_kg * fibre_en_fac
fibre_en_vol = fibre_vol *fibre_en_fac

export_strom_amount= (float(serv.loc[serv.loc[:,"vars"]=="ee","strom"])/3.6)



########################
##  Nettoflüsse      ###
########################

input_woodchips_atro = 0 
output_woodchips_atro = lvl_en_kg *lvl_holzanteil + bsh_en_kg * bsh_holzanteil + timb_en_kg * timb_holzanteil + osb_en_kg * osb_holzanteil + fibre_en_kg * fibre_holzanteil ## ATRO holz !!!

netto_woodchips_atro = output_woodchips_atro - input_woodchips_atro 

#Verbrennung (net energy : 1.3 MJ/kg elektrisch, 2.74MJ/kg thermal):

    
########################
###     Flows      #####
########################

#Gutschrift/Kosten 
if not client.find(olca.Flow,"gk"):     
    gk_flow = olca.Flow()
    gk_flow.id = str(uuid.uuid4())
    gk_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    gk_flow.name = "gk"
    gk_flow.description = ""
    gk_flow.unit = items_unit
    gk_flow.flow_properties = [item_factor]
    gk_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(gk_flow)

gk_flow = client.get(olca.Flow,client.find(olca.Flow,"gk").id)

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


#######################
##### GK Prozesse   ###
#######################

kosten = olca.Process()
kosten.category = client.find(olca.Category,"D")
kosten.process_type = olca.ProcessType.UNIT_PROCESS
kosten.id = str(uuid.uuid4())
kosten.name = "D_e_k"
kosten.olca_type = olca.schema.Process.__name__


gutschrift = olca.Process()
gutschrift.category = client.find(olca.Category,"D")
gutschrift.process_type = olca.ProcessType.UNIT_PROCESS
gutschrift.id = str(uuid.uuid4())
gutschrift.name = "D_e_g"
gutschrift.olca_type = olca.schema.Process.__name__




########################
## Verbrennung        ##
########################
exch_k= []
ID = 1

#heat electricity ratio

#elec =0.041667 #kwh
#heat =0.45
#wc = 0.05291

# Aus Rüter 2012:

elec =1231 #kwh
heat =2313
wc = 1000

elec_factor=elec/wc 
heat_factor=heat/wc 

heat_power_flow = client.get(olca.Flow,"71e2f1db-a2c5-44d0-8337-dfff15be974d") # heat, district or industrial, other than natural gas
heat_power_proc = client.get(olca.Process,"0504bad7-8a95-4b19-9093-49aa2a9e556d") #heat and power co-generation, wood chips, 6667 kW, state-of-the-art 2014 | heat, district or industrial, other than natural gas | EN15804, U
pere_flow = client.get(olca.Flow,"01c12fca-ad8b-4902-8b48-2d5afe3d3a0f") #Energy, gross calorific value, in biomass

for ex in heat_power_proc.exchanges:
    if ex.flow.name == "wood chips, wet, measured as dry mass":
        wc_heat_power = ex.amount
        heat_power_proc.exchanges.remove(ex)

# Energieinhalt des Holzes hinzufügen
energypermass = 0

if lvl_vol > 0:
    
    energypermass = lvl_energy_inh/lvl_gewicht

if bsh_vol > 0:
    
    energypermass = bsh_energy_inh/bsh_gewicht

if timb_vol > 0:
    
    energypermass = timb_energy_inh/timb_gewicht

if osb_vol > 0:
    
    energypermass = osb_energy_inh/osb_gewicht

if fibre_vol > 0:
    
    energypermass = fibre_energy_inh/fibre_gewicht

#if export_strom_amount > 0:
#    energypermass = 0 

heat_power_input_energy = olca.Exchange()
heat_power_input_energy.input = True
heat_power_input_energy.flow = pere_flow
heat_power_input_energy.flow_property = energy
heat_power_input_energy.unit = MJ
heat_power_input_energy.amount = wc_heat_power * energypermass
heat_power_input_energy.quantitative_reference = False
heat_power_input_energy.internal_id = ID; ID = ID + 1
heat_power_input_energy.avoided_product = False
heat_power_proc.exchanges.append(heat_power_input_energy)
    
heat_power_proc.name = "verbrennung_heat"
heat_power_proc.id = str(uuid.uuid4())
heat_power_proc.olca_type = olca.schema.Process.__name__
client.insert(heat_power_proc)

heat_amount = heat_factor * netto_woodchips_atro

kosten_input_holzverbrennung1 = olca.Exchange()
kosten_input_holzverbrennung1.input = True
kosten_input_holzverbrennung1.flow = heat_power_flow
kosten_input_holzverbrennung1.flow_property = energy
kosten_input_holzverbrennung1.unit = MJ
kosten_input_holzverbrennung1.amount = heat_amount
kosten_input_holzverbrennung1.quantitative_reference = False
kosten_input_holzverbrennung1.default_provider = heat_power_proc
kosten_input_holzverbrennung1.internal_id = ID; ID = ID + 1
kosten_input_holzverbrennung1.avoided_product = False
exch_k.append(kosten_input_holzverbrennung1)

power_heat_flow = client.get(olca.Flow,"66c93e71-f32b-4591-901c-55395db5c132") # electricity, high voltage
power_heat_proc = client.get(olca.Process,"d63b33f5-e859-49df-bd9f-4007d10fa09b") #heat and power co-generation, wood chips, 6667 kW, state-of-the-art 2014 | electricity, high voltage | EN15804, U

for ex in power_heat_proc.exchanges:
    if ex.flow.name == "wood chips, wet, measured as dry mass":
        wc_power_heat = ex.amount
        power_heat_proc.exchanges.remove(ex)


power_heat_input_energy = olca.Exchange()
power_heat_input_energy.input = True
power_heat_input_energy.flow = pere_flow
power_heat_input_energy.flow_property = energy
power_heat_input_energy.unit = MJ
power_heat_input_energy.amount = wc_power_heat * energypermass
power_heat_input_energy.quantitative_reference = False
power_heat_input_energy.internal_id = ID; ID = ID + 1
power_heat_input_energy.avoided_product = False
power_heat_proc.exchanges.append(power_heat_input_energy)
    
power_heat_proc.name = "verbrennung_power"
power_heat_proc.id = str(uuid.uuid4())
power_heat_proc.olca_type = olca.schema.Process.__name__
client.insert(power_heat_proc)

elec_amount = elec_factor * netto_woodchips_atro

kosten_input_holzverbrennung2 = olca.Exchange()
kosten_input_holzverbrennung2.input = True
kosten_input_holzverbrennung2.flow = power_heat_flow
kosten_input_holzverbrennung2.flow_property = energy
kosten_input_holzverbrennung2.unit = kwh
kosten_input_holzverbrennung2.amount = elec_amount
kosten_input_holzverbrennung2.quantitative_reference = False
kosten_input_holzverbrennung2.default_provider = power_heat_proc
kosten_input_holzverbrennung2.internal_id = ID; ID = ID + 1
kosten_input_holzverbrennung2.avoided_product = False
exch_k.append(kosten_input_holzverbrennung2)

energy_flow = client.get(olca.Flow,"b2e8e329-f643-3fa0-8af9-95afa9347bbd") # Energy, from wood

kosten_output_energy = olca.Exchange()
kosten_output_energy.input = False
kosten_output_energy.flow = energy_flow
kosten_output_energy.flow_property = energy
kosten_output_energy.unit = MJ
kosten_output_energy.amount = heat_amount + (3.6 * elec_amount)
kosten_output_energy.quantitative_reference = False
kosten_output_energy.internal_id = ID; ID = ID + 1
kosten_output_energy.avoided_product = False
exch_k.append(kosten_output_energy)

kosten_input_carbon = olca.Exchange()
kosten_input_carbon.input = True
kosten_input_carbon.flow = carbonin_flow
kosten_input_carbon.amount = lvl_en_vol * lvl_co2_inh + bsh_en_vol * bsh_co2_inh + timb_en_vol * timb_co2_inh + osb_en_vol * osb_co2_inh  + fibre_en_vol * fibre_co2_inh  # in kg
kosten_input_carbon.unit = kg  
kosten_input_carbon.flow_property = mass
kosten_input_carbon.internal_id = ID; ID = ID + 1
kosten_input_carbon.avoided_product = False
kosten_input_carbon.quantitative_reference = False
exch_k.append(kosten_input_carbon)

kosten_output_carbon = olca.Exchange()
kosten_output_carbon.input = False
kosten_output_carbon.flow = carbonout_flow
kosten_output_carbon.amount = lvl_en_vol * lvl_co2_inh + bsh_en_vol * bsh_co2_inh + timb_en_vol * timb_co2_inh + osb_en_vol * osb_co2_inh  + fibre_en_vol * fibre_co2_inh   # in kg
kosten_output_carbon.unit = kg  
kosten_output_carbon.flow_property = mass
kosten_output_carbon.internal_id = ID; ID = ID + 1
kosten_output_carbon.avoided_product = False
kosten_output_carbon.quantitative_reference = False
exch_k.append(kosten_output_carbon)

kosten_input_energy = olca.Exchange()
kosten_input_energy.input = True
kosten_input_energy.flow = energyin_flow
kosten_input_energy.amount = lvl_en_vol * lvl_energy_inh + bsh_en_vol * bsh_energy_inh + timb_en_vol * timb_energy_inh  + osb_en_vol * osb_energy_inh + fibre_en_vol * fibre_energy_inh 
kosten_input_energy.unit = MJ  
kosten_input_energy.flow_property = energy
kosten_input_energy.internal_id = ID; ID = ID + 1
kosten_input_energy.avoided_product = False
kosten_input_energy.quantitative_reference = False
exch_k.append(kosten_input_energy)

kosten_output_energy = olca.Exchange()
kosten_output_energy.input = False
kosten_output_energy.flow = energyout_flow
kosten_output_energy.amount = lvl_en_vol * lvl_energy_inh + bsh_en_vol * bsh_energy_inh + timb_en_vol * timb_energy_inh    + osb_en_vol * osb_energy_inh    + fibre_en_vol * fibre_energy_inh    
kosten_output_energy.unit = MJ  
kosten_output_energy.flow_property = energy
kosten_output_energy.internal_id = ID; ID = ID + 1
kosten_output_energy.avoided_product = False
kosten_output_energy.quantitative_reference = False
exch_k.append(kosten_output_energy)


########################
## Substituierte      ##
########################
exch_g= []

elec_flow =  client.get(olca.Flow,"759b89bd-3aa6-42ad-b767-5bb9ef5d331d")   #electricity, medium voltage
elec_proc = client.get(olca.Process,"679c8c3e-d17a-4bc9-bee4-1a96840a6a6d") #market for electricity, medium voltage | electricity, medium voltage | EN15804, U

heat_flow =  client.get(olca.Flow,"b3c58f5d-5815-487c-8b9c-4366e00d22dc")   #heat, central or small-scale, natural gas
heat_proc = client.get(olca.Process,"211c23dd-3901-49c6-aae3-299708becfe8") #heat production, natural gas, at boiler condensing modulating <100kW | heat, central or small-scale, natural gas | EN15804, U


gutschrift_input_elec = olca.Exchange()
gutschrift_input_elec.input = True
gutschrift_input_elec.flow = elec_flow
gutschrift_input_elec.amount = elec_amount + export_strom_amount
gutschrift_input_elec.unit = kwh  
gutschrift_input_elec.flow_property = energy
gutschrift_input_elec.default_provider = elec_proc
gutschrift_input_elec.internal_id = ID; ID = ID + 1
gutschrift_input_elec.avoided_product = False
gutschrift_input_elec.quantitative_reference = False
exch_g.append(gutschrift_input_elec)

gutschrift_input_heat = olca.Exchange()
gutschrift_input_heat.input = True
gutschrift_input_heat.flow = heat_flow
gutschrift_input_heat.amount = heat_amount 
gutschrift_input_heat.unit = MJ  
gutschrift_input_heat.flow_property = energy
gutschrift_input_heat.default_provider = heat_proc
gutschrift_input_heat.internal_id = ID; ID = ID + 1
gutschrift_input_heat.avoided_product = False
gutschrift_input_heat.quantitative_reference = False
exch_g.append(gutschrift_input_heat)


gutschrift_input_carbon = olca.Exchange()
gutschrift_input_carbon.input = True
gutschrift_input_carbon.flow = carbonin_flow
gutschrift_input_carbon.amount = lvl_en_vol * lvl_co2_inh + bsh_en_vol * bsh_co2_inh + timb_en_vol * timb_co2_inh + osb_en_vol * osb_co2_inh  + fibre_en_vol * fibre_co2_inh  # in kg
gutschrift_input_carbon.unit = kg  
gutschrift_input_carbon.flow_property = mass
gutschrift_input_carbon.internal_id = ID; ID = ID + 1
gutschrift_input_carbon.avoided_product = False
gutschrift_input_carbon.quantitative_reference = False
exch_g.append(gutschrift_input_carbon)

gutschrift_output_carbon = olca.Exchange()
gutschrift_output_carbon.input = False
gutschrift_output_carbon.flow = carbonout_flow
gutschrift_output_carbon.amount = lvl_en_vol * lvl_co2_inh + bsh_en_vol * bsh_co2_inh + timb_en_vol * timb_co2_inh + osb_en_vol * osb_co2_inh  + fibre_en_vol * fibre_co2_inh   # in kg
gutschrift_output_carbon.unit = kg  
gutschrift_output_carbon.flow_property = mass
gutschrift_output_carbon.internal_id = ID; ID = ID + 1
gutschrift_output_carbon.avoided_product = False
gutschrift_output_carbon.quantitative_reference = False
exch_g.append(gutschrift_output_carbon)

gutschrift_input_energy = olca.Exchange()
gutschrift_input_energy.input = True
gutschrift_input_energy.flow = energyin_flow
gutschrift_input_energy.amount = lvl_en_vol * lvl_energy_inh + bsh_en_vol * bsh_energy_inh + timb_en_vol * timb_energy_inh  + osb_en_vol * osb_energy_inh + fibre_en_vol * fibre_energy_inh 
gutschrift_input_energy.unit = MJ  
gutschrift_input_energy.flow_property = energy
gutschrift_input_energy.internal_id = ID; ID = ID + 1
gutschrift_input_energy.avoided_product = False
gutschrift_input_energy.quantitative_reference = False
exch_g.append(gutschrift_input_energy)

gutschrift_output_energy = olca.Exchange()
gutschrift_output_energy.input = False
gutschrift_output_energy.flow = energyout_flow
gutschrift_output_energy.amount = lvl_en_vol * lvl_energy_inh + bsh_en_vol * bsh_energy_inh + timb_en_vol * timb_energy_inh    + osb_en_vol * osb_energy_inh    + fibre_en_vol * fibre_energy_inh    
gutschrift_output_energy.unit = MJ  
gutschrift_output_energy.flow_property = energy
gutschrift_output_energy.internal_id = ID; ID = ID + 1
gutschrift_output_energy.avoided_product = False
gutschrift_output_energy.quantitative_reference = False
exch_g.append(gutschrift_output_energy)



###############
## Exchanges ##
###############



gutschrift_kosten_output = olca.Exchange()
gutschrift_kosten_output.input = False
gutschrift_kosten_output.flow = gk_flow
gutschrift_kosten_output.flow_property = item
gutschrift_kosten_output.unit = items_unit
gutschrift_kosten_output.amount = 1
gutschrift_kosten_output.quantitative_reference = True
gutschrift_kosten_output.internal_id = ID; ID = ID + 1
gutschrift_kosten_output.avoided_product = False
exch_k.append(gutschrift_kosten_output)
exch_g.append(gutschrift_kosten_output)




kosten.exchanges= exch_k
gutschrift.exchanges= exch_g

client.insert(kosten)
client.insert(gutschrift)

