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


if client.find(olca.Process,"D_w_k"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_w_k").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)  
if client.find(olca.Process,"D_w_g"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_w_g").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)  

if client.find(olca.ProductSystem,"D_w_k"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"D_w_k").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
if client.find(olca.ProductSystem,"D_w_g"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"D_w_g").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)


########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import items_unit,item_factor,item,vol,m3,kg,mass,energy,MJ,m2,area


########################
###    Anteile    #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
anteile=runpy.run_module(mod_name="anteile")

lvl_sek_share  =anteile.get("lvl_sek_share")
lvl_rueckbau   =anteile.get("lvl_rueckbau")
lvl_wieder_fac =anteile.get("lvl_wieder_fac")

bsh_sek_share  =anteile.get("bsh_sek_share")
bsh_rueckbau   =anteile.get("bsh_rueckbau")
bsh_wieder_fac =anteile.get("bsh_wieder_fac")

timb_sek_share  =anteile.get("timb_sek_share")
timb_rueckbau   =anteile.get("timb_rueckbau")
timb_wieder_fac =anteile.get("timb_wieder_fac")

osb_sek_share  =anteile.get("osb_sek_share")
osb_rueckbau   =anteile.get("osb_rueckbau")
osb_wieder_fac =anteile.get("osb_wieder_fac")

fibre_sek_share  =anteile.get("fibre_sek_share")
fibre_rueckbau   =anteile.get("fibre_rueckbau")
fibre_wieder_fac =anteile.get("fibre_wieder_fac")


con_wieder_fac =anteile.get("con_wieder_fac")
con_sek_share  =anteile.get("con_sek_share")
con_rueckbau   =anteile.get("con_rueckbau")

verb_wieder_fac=anteile.get("verb_wieder_fac")
verb_sek_share =anteile.get("verb_sek_share")
verb_rueckbau  =anteile.get("verb_rueckbau")

glas_wieder_fac=anteile.get("glas_wieder_fac")
glas_rueckbau  =anteile.get("glas_rueckbau")
glas_sek_share =anteile.get("glas_sek_share")

bew_wieder_fac=anteile.get("bew_wieder_fac")
bew_rueckbau  =anteile.get("bew_rueckbau")
bew_sek_share =anteile.get("bew_sek_share")

gips_wieder_fac=anteile.get("gips_wieder_fac")
gips_rueckbau  =anteile.get("gips_rueckbau")
gips_sek_share =anteile.get("gips_sek_share")


########################
###     Amounts    #####
########################
    
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
lvl_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])
lvl_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
lvl_kg = lvl_vol * lvl_gewicht # vol*gewicht
lvl_wieder_kg = lvl_kg * lvl_wieder_fac
lvl_wieder_vol = lvl_vol *lvl_wieder_fac

bsh_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
bsh_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])
bsh_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
bsh_kg = bsh_vol * bsh_gewicht # vol*gewicht
bsh_wieder_kg = bsh_kg * bsh_wieder_fac
bsh_wieder_vol = bsh_vol *bsh_wieder_fac

timb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
timb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","timb"])
timb_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
timb_kg = timb_vol * timb_gewicht # vol*gewicht
timb_wieder_kg = timb_kg * timb_wieder_fac
timb_wieder_vol = timb_vol *timb_wieder_fac

osb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
osb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","osb"])
osb_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
osb_kg = osb_vol * osb_gewicht # vol*gewicht
osb_wieder_kg = osb_kg * osb_wieder_fac
osb_wieder_vol = osb_vol *osb_wieder_fac

fibre_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
fibre_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","fibre"])
fibre_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
fibre_kg = fibre_vol * fibre_gewicht # vol*gewicht
fibre_wieder_kg = fibre_kg * fibre_wieder_fac
fibre_wieder_vol = fibre_vol *fibre_wieder_fac


con_vol = float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","concrete"])
con_wieder_vol = con_vol * con_wieder_fac

glas_m2 =  float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_kg = glas_m2 * glas_gewicht
glas_wieder_kg = glas_kg * glas_wieder_fac
glas_wieder_m2 = glas_m2 * glas_wieder_fac

verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])
verb_wieder_kg = verb_kg * verb_wieder_fac

bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])
bew_wieder_kg = bew_kg * bew_wieder_fac

gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])
gips_wieder_kg = gips_kg * gips_wieder_fac


########################
##  Nettoflüsse      ###
########################

input_lvl_sekundaer = lvl_vol * lvl_sek_share * lvl_rueckbau
output_lvl_sekundaer = lvl_vol * lvl_wieder_fac 

input_bsh_sekundaer = bsh_vol * bsh_sek_share * bsh_rueckbau
output_bsh_sekundaer = bsh_vol * bsh_wieder_fac 

input_timb_sekundaer = timb_vol * timb_sek_share * timb_rueckbau
output_timb_sekundaer = timb_vol * timb_wieder_fac 

input_osb_sekundaer = osb_vol * osb_sek_share * osb_rueckbau
output_osb_sekundaer = osb_vol * osb_wieder_fac 

input_fibre_sekundaer = fibre_vol * fibre_sek_share * fibre_rueckbau
output_fibre_sekundaer = fibre_vol * fibre_wieder_fac 


input_con_sekundaer = con_vol * con_sek_share * con_rueckbau
output_con_sekundaer = con_vol * con_wieder_fac 

input_verb_sekundaer = verb_kg * verb_sek_share * verb_rueckbau
output_verb_sekundaer = verb_kg * verb_wieder_fac 

input_glas_sekundaer = glas_m2 * glas_sek_share * glas_rueckbau
output_glas_sekundaer = glas_m2 * glas_wieder_fac 

input_bew_sekundaer = bew_kg * bew_sek_share * bew_rueckbau
output_bew_sekundaer = bew_kg * bew_wieder_fac 

input_gips_sekundaer = gips_kg * gips_sek_share * gips_rueckbau
output_gips_sekundaer = gips_kg * gips_wieder_fac 


netto_lvl = output_lvl_sekundaer - input_lvl_sekundaer # in m3
netto_bsh = output_bsh_sekundaer - input_bsh_sekundaer # in m3
netto_timb = output_timb_sekundaer - input_timb_sekundaer # in m3
netto_osb = output_osb_sekundaer - input_osb_sekundaer # in m3
netto_fibre = output_fibre_sekundaer - input_fibre_sekundaer # in m3
netto_con = output_con_sekundaer - input_con_sekundaer # in m3
netto_verb = output_verb_sekundaer - input_verb_sekundaer # in kg
netto_glas = output_glas_sekundaer - input_glas_sekundaer # in m2
netto_bew = output_bew_sekundaer - input_bew_sekundaer # in kg
netto_gips = output_gips_sekundaer - input_gips_sekundaer # in kg



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
    
    client.insert(gk_flow)

gk_flow = client.get(olca.Flow,client.find(olca.Flow,"gk").id)

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


#######################
##### GK Prozesse    ###
#######################

kosten = olca.Process()
kosten.category = client.find(olca.Category,"D")
kosten.process_type = olca.ProcessType.UNIT_PROCESS
kosten.id = str(uuid.uuid4())
kosten.name = "D_w_k"
kosten.olca_type = olca.schema.Process.__name__

gutschrift = olca.Process()
gutschrift.category = client.find(olca.Category,"D")
gutschrift.process_type = olca.ProcessType.UNIT_PROCESS
gutschrift.id = str(uuid.uuid4())
gutschrift.name = "D_w_g"
gutschrift.olca_type = olca.schema.Process.__name__

gutschrift_kosten_output = olca.Exchange()
gutschrift_kosten_output.input = False
gutschrift_kosten_output.flow = gk_flow
gutschrift_kosten_output.flow_property = item
gutschrift_kosten_output.unit = items_unit
gutschrift_kosten_output.amount = 1
gutschrift_kosten_output.quantitative_reference = True
gutschrift_kosten_output.internal_id = 666
gutschrift_kosten_output.avoided_product = False



########################
## Wiederverwendung   ##
########################
exch_k =  []

ID=1

if netto_lvl != 0:
    
    lvl_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_sekundaer").id)
    lvl_secondary_process = client.get(olca.Process,client.find(olca.Process,"lvl_sekundaer").id)
   
    
    kosten_input_lvl = olca.Exchange()
    kosten_input_lvl.input = True
    kosten_input_lvl.flow = lvl_secondary_flow
    kosten_input_lvl.default_provider = lvl_secondary_process
    kosten_input_lvl.amount = netto_lvl
    kosten_input_lvl.unit = m3
    kosten_input_lvl.flow_property = vol
    kosten_input_lvl.internal_id = ID;ID = ID + 1
    kosten_input_lvl.avoided_product = False
    kosten_input_lvl.quantitative_reference = False
    exch_k.append(kosten_input_lvl)

if netto_bsh != 0:
    
    bsh_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_sekundaer").id)
    bsh_secondary_process = client.get(olca.Process,client.find(olca.Process,"bsh_sekundaer").id)

    kosten_input_bsh = olca.Exchange()
    kosten_input_bsh.input = True
    kosten_input_bsh.flow = bsh_secondary_flow
    kosten_input_bsh.default_provider = bsh_secondary_process
    kosten_input_bsh.amount = netto_bsh
    kosten_input_bsh.unit = m3
    kosten_input_bsh.flow_property = vol
    kosten_input_bsh.internal_id = ID;ID = ID + 1
    kosten_input_bsh.avoided_product = False
    kosten_input_bsh.quantitative_reference = False
    exch_k.append(kosten_input_bsh)


if netto_timb != 0:
    
    timb_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_sekundaer").id)
    timb_secondary_process = client.get(olca.Process,client.find(olca.Process,"timb_sekundaer").id)

    kosten_input_timb = olca.Exchange()
    kosten_input_timb.input = True
    kosten_input_timb.flow = timb_secondary_flow
    kosten_input_timb.default_provider = timb_secondary_process
    kosten_input_timb.amount = netto_timb
    kosten_input_timb.unit = m3
    kosten_input_timb.flow_property = vol
    kosten_input_timb.internal_id = ID;ID = ID + 1
    kosten_input_timb.avoided_product = False
    kosten_input_timb.quantitative_reference = False
    exch_k.append(kosten_input_timb)


if netto_osb != 0:
    
    osb_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_sekundaer").id)
    osb_secondary_process = client.get(olca.Process,client.find(olca.Process,"osb_sekundaer").id)

    kosten_input_osb = olca.Exchange()
    kosten_input_osb.input = True
    kosten_input_osb.flow = osb_secondary_flow
    kosten_input_osb.default_provider = osb_secondary_process
    kosten_input_osb.amount = netto_osb
    kosten_input_osb.unit = m3
    kosten_input_osb.flow_property = vol
    kosten_input_osb.internal_id = ID;ID = ID + 1
    kosten_input_osb.avoided_product = False
    kosten_input_osb.quantitative_reference = False
    exch_k.append(kosten_input_osb)

if netto_fibre != 0:
    
    fibre_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_sekundaer").id)
    fibre_secondary_process = client.get(olca.Process,client.find(olca.Process,"fibre_sekundaer").id)

    kosten_input_fibre = olca.Exchange()
    kosten_input_fibre.input = True
    kosten_input_fibre.flow = fibre_secondary_flow
    kosten_input_fibre.default_provider = fibre_secondary_process
    kosten_input_fibre.amount = netto_fibre
    kosten_input_fibre.unit = m3
    kosten_input_fibre.flow_property = vol
    kosten_input_fibre.internal_id = ID;ID = ID + 1
    kosten_input_fibre.avoided_product = False
    kosten_input_fibre.quantitative_reference = False
    exch_k.append(kosten_input_fibre)


if netto_con != 0:
    
    con_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"concrete_sekundaer").id)
    con_secondary_process = client.get(olca.Process,client.find(olca.Process,"concrete_sekundaer").id)

    kosten_input_con = olca.Exchange()
    kosten_input_con.input = True
    kosten_input_con.flow = con_secondary_flow
    kosten_input_con.default_provider = con_secondary_process
    kosten_input_con.amount = netto_con
    kosten_input_con.unit = m3
    kosten_input_con.flow_property = vol
    kosten_input_con.internal_id = ID;ID = ID + 1
    kosten_input_con.avoided_product = False
    kosten_input_con.quantitative_reference = False
    exch_k.append(kosten_input_con)


if netto_verb != 0:
    
    verb_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"verb_sekundaer").id)
    verb_secondary_process = client.get(olca.Process,client.find(olca.Process,"verb_sekundaer").id)

    kosten_input_verb = olca.Exchange()
    kosten_input_verb.input = True
    kosten_input_verb.flow = verb_secondary_flow
    kosten_input_verb.default_provider = verb_secondary_process
    kosten_input_verb.amount = netto_verb
    kosten_input_verb.unit = kg
    kosten_input_verb.flow_property = mass
    kosten_input_verb.internal_id = ID;ID = ID + 1
    kosten_input_verb.avoided_product = False
    kosten_input_verb.quantitative_reference = False
    exch_k.append(kosten_input_verb)


if netto_glas != 0:
            
    glas_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"glas_sekundaer").id)
    glas_secondary_process = client.get(olca.Process,client.find(olca.Process,"glas_sekundaer").id)

    kosten_input_glas = olca.Exchange()
    kosten_input_glas.input = True
    kosten_input_glas.flow = glas_secondary_flow
    kosten_input_glas.default_provider = glas_secondary_process
    kosten_input_glas.amount = netto_glas
    kosten_input_glas.unit = m2
    kosten_input_glas.flow_property = area
    kosten_input_glas.internal_id = ID;ID = ID + 1
    kosten_input_glas.avoided_product = False
    kosten_input_glas.quantitative_reference = False
    exch_k.append(kosten_input_glas)

if netto_bew != 0:
            
    bew_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"bew_sekundaer").id)
    bew_secondary_process = client.get(olca.Process,client.find(olca.Process,"bew_sekundaer").id)

    kosten_input_bew = olca.Exchange()
    kosten_input_bew.input = True
    kosten_input_bew.flow = bew_secondary_flow
    kosten_input_bew.default_provider = bew_secondary_process
    kosten_input_bew.amount = netto_bew
    kosten_input_bew.unit = kg
    kosten_input_bew.flow_property = mass
    kosten_input_bew.internal_id = ID;ID = ID + 1
    kosten_input_bew.avoided_product = False
    kosten_input_bew.quantitative_reference = False
    exch_k.append(kosten_input_bew)


if netto_gips != 0:
            
    gips_secondary_flow = client.get(olca.Flow,client.find(olca.Flow,"gips_sekundaer").id)
    gips_secondary_process = client.get(olca.Process,client.find(olca.Process,"gips_sekundaer").id)

    kosten_input_gips = olca.Exchange()
    kosten_input_gips.input = True
    kosten_input_gips.flow = gips_secondary_flow
    kosten_input_gips.default_provider = gips_secondary_process
    kosten_input_gips.amount = netto_gips
    kosten_input_gips.unit = kg
    kosten_input_gips.flow_property = mass
    kosten_input_gips.internal_id = ID;ID = ID + 1
    kosten_input_gips.avoided_product = False
    kosten_input_gips.quantitative_reference = False
    exch_k.append(kosten_input_gips)



kosten_input_carbon = olca.Exchange()
kosten_input_carbon.input = True
kosten_input_carbon.flow = carbonin_flow
kosten_input_carbon.amount = netto_lvl * lvl_co2_inh + netto_bsh * bsh_co2_inh + netto_timb * timb_co2_inh + netto_osb * osb_co2_inh + netto_fibre * fibre_co2_inh # in kg
kosten_input_carbon.unit = kg  
kosten_input_carbon.flow_property = mass
kosten_input_carbon.internal_id = ID;ID = ID + 1
kosten_input_carbon.avoided_product = False
kosten_input_carbon.quantitative_reference = False
exch_k.append(kosten_input_carbon)

kosten_input_energy = olca.Exchange()
kosten_input_energy.input = True
kosten_input_energy.flow = energyin_flow
kosten_input_energy.amount = netto_lvl * lvl_energy_inh + netto_bsh * bsh_energy_inh + netto_timb * timb_energy_inh + netto_osb * osb_energy_inh  + netto_fibre * fibre_energy_inh# in kg
kosten_input_energy.unit = MJ  
kosten_input_energy.flow_property = energy
kosten_input_energy.internal_id = ID;ID = ID + 1
kosten_input_energy.avoided_product = False
kosten_input_energy.quantitative_reference = False
exch_k.append(kosten_input_energy)

sm_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)

kosten_input_sm = olca.Exchange()
kosten_input_sm.input = True
kosten_input_sm.flow = sm_flow
kosten_input_sm.amount =  (netto_lvl*lvl_gewicht) + (netto_bsh*bsh_gewicht) + (netto_timb*timb_gewicht) + (netto_osb*osb_gewicht) + (netto_fibre*fibre_gewicht) + (netto_glas*glas_gewicht) + (netto_con*con_gewicht) + netto_verb + netto_bew + netto_gips
kosten_input_sm.unit = kg  
kosten_input_sm.flow_property = mass
kosten_input_sm.internal_id = ID;ID = ID + 1
kosten_input_sm.avoided_product = False
kosten_input_sm.quantitative_reference = False
exch_k.append(kosten_input_sm)

kosten_output_carbon = olca.Exchange()
kosten_output_carbon.input = False
kosten_output_carbon.flow = carbonout_flow
kosten_output_carbon.amount = netto_lvl * lvl_co2_inh + netto_bsh * bsh_co2_inh + netto_timb * timb_co2_inh + netto_osb * osb_co2_inh + netto_fibre * fibre_co2_inh   # in kg
kosten_output_carbon.unit = kg  
kosten_output_carbon.flow_property = mass
kosten_output_carbon.internal_id = ID;ID = ID + 1
kosten_output_carbon.avoided_product = False
kosten_output_carbon.quantitative_reference = False
exch_k.append(kosten_output_carbon)


kosten_output_energy = olca.Exchange()
kosten_output_energy.input = False
kosten_output_energy.flow = energyout_flow
kosten_output_energy.amount = netto_lvl * lvl_energy_inh + netto_bsh * bsh_energy_inh + netto_timb * timb_energy_inh + netto_osb * osb_energy_inh + netto_fibre * fibre_energy_inh   # in kg
kosten_output_energy.unit = MJ  
kosten_output_energy.flow_property = energy
kosten_output_energy.internal_id = ID;ID = ID + 1
kosten_output_energy.avoided_product = False
kosten_output_energy.quantitative_reference = False
exch_k.append(kosten_output_energy)


########################
## Substituierte      ##
########################
exch_g= []
ID = 1



if netto_lvl != 0:


    lvl_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_primaer").id)
    lvl_primary_process = client.get(olca.Process,client.find(olca.Process,"lvl_primaer").id)
        
        
    gutschrift_input_lvl = olca.Exchange()
    gutschrift_input_lvl.input = True
    gutschrift_input_lvl.flow = lvl_primary_flow
    gutschrift_input_lvl.amount = netto_lvl
    gutschrift_input_lvl.unit = m3  
    gutschrift_input_lvl.flow_property = vol
    gutschrift_input_lvl.default_provider = lvl_primary_process
    gutschrift_input_lvl.internal_id = ID;ID = ID + 1
    gutschrift_input_lvl.avoided_product = False
    gutschrift_input_lvl.quantitative_reference = False
    exch_g.append(gutschrift_input_lvl)


if netto_bsh != 0:
    
    bsh_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_primaer").id)
    bsh_primary_process = client.get(olca.Process,client.find(olca.Process,"bsh_primaer").id)
      
        
    gutschrift_input_bsh = olca.Exchange()
    gutschrift_input_bsh.input = True
    gutschrift_input_bsh.flow = bsh_primary_flow
    gutschrift_input_bsh.amount = netto_bsh
    gutschrift_input_bsh.unit = m3  
    gutschrift_input_bsh.flow_property = vol
    gutschrift_input_bsh.default_provider = bsh_primary_process
    gutschrift_input_bsh.internal_id = ID;ID = ID + 1
    gutschrift_input_bsh.avoided_product = False
    gutschrift_input_bsh.quantitative_reference = False  
    exch_g.append(gutschrift_input_bsh)


if netto_timb != 0:
    
    timb_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_primaer").id)
    timb_primary_process = client.get(olca.Process,client.find(olca.Process,"timb_primaer").id)
      
        
    gutschrift_input_timb = olca.Exchange()
    gutschrift_input_timb.input = True
    gutschrift_input_timb.flow = timb_primary_flow
    gutschrift_input_timb.amount = netto_timb
    gutschrift_input_timb.unit = m3  
    gutschrift_input_timb.flow_property = vol
    gutschrift_input_timb.default_provider = timb_primary_process
    gutschrift_input_timb.internal_id = ID;ID = ID + 1
    gutschrift_input_timb.avoided_product = False
    gutschrift_input_timb.quantitative_reference = False  
    exch_g.append(gutschrift_input_timb)


if netto_osb != 0:
    
    osb_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_primaer").id)
    osb_primary_process = client.get(olca.Process,client.find(olca.Process,"osb_primaer").id)
      
        
    gutschrift_input_osb = olca.Exchange()
    gutschrift_input_osb.input = True
    gutschrift_input_osb.flow = osb_primary_flow
    gutschrift_input_osb.amount = netto_osb
    gutschrift_input_osb.unit = m3  
    gutschrift_input_osb.flow_property = vol
    gutschrift_input_osb.default_provider = osb_primary_process
    gutschrift_input_osb.internal_id = ID;ID = ID + 1
    gutschrift_input_osb.avoided_product = False
    gutschrift_input_osb.quantitative_reference = False  
    exch_g.append(gutschrift_input_osb)

if netto_fibre != 0:
    
    fibre_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_primaer").id)
    fibre_primary_process = client.get(olca.Process,client.find(olca.Process,"fibre_primaer").id)
      
        
    gutschrift_input_fibre = olca.Exchange()
    gutschrift_input_fibre.input = True
    gutschrift_input_fibre.flow = fibre_primary_flow
    gutschrift_input_fibre.amount = netto_fibre
    gutschrift_input_fibre.unit = m3  
    gutschrift_input_fibre.flow_property = vol
    gutschrift_input_fibre.default_provider = fibre_primary_process
    gutschrift_input_fibre.internal_id = ID;ID = ID + 1
    gutschrift_input_fibre.avoided_product = False
    gutschrift_input_fibre.quantitative_reference = False  
    exch_g.append(gutschrift_input_fibre)



if netto_con != 0:


    con_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"concrete_primaer").id)
    con_primary_process = client.get(olca.Process,client.find(olca.Process,"concrete_primaer").id)
        
    gutschrift_input_con = olca.Exchange()
    gutschrift_input_con.input = True
    gutschrift_input_con.flow = con_primary_flow
    gutschrift_input_con.amount = netto_con
    gutschrift_input_con.unit = m3  
    gutschrift_input_con.flow_property = vol
    gutschrift_input_con.default_provider = con_primary_process
    gutschrift_input_con.internal_id = ID;ID = ID + 1
    gutschrift_input_con.avoided_product = False
    gutschrift_input_con.quantitative_reference = False
    exch_g.append(gutschrift_input_con)


if netto_verb != 0:

    verb_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"verb_primaer").id)
    verb_primary_process = client.get(olca.Process,client.find(olca.Process,"verb_primaer").id)
        
    gutschrift_input_verb = olca.Exchange()
    gutschrift_input_verb.input = True
    gutschrift_input_verb.flow = verb_primary_flow
    gutschrift_input_verb.amount = netto_verb
    gutschrift_input_verb.unit = kg  
    gutschrift_input_verb.flow_property = mass
    gutschrift_input_verb.default_provider = verb_primary_process
    gutschrift_input_verb.internal_id = ID;ID = ID + 1
    gutschrift_input_verb.avoided_product = False
    gutschrift_input_verb.quantitative_reference = False
    exch_g.append(gutschrift_input_verb)



if netto_glas != 0:
    
    glas_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"glas_primaer").id)
    glas_primary_process = client.get(olca.Process,client.find(olca.Process,"glas_primaer").id)
     
    gutschrift_input_glas = olca.Exchange()
    gutschrift_input_glas.input = True
    gutschrift_input_glas.flow = glas_primary_flow
    gutschrift_input_glas.amount = netto_glas
    gutschrift_input_glas.unit = m2  
    gutschrift_input_glas.flow_property = area
    gutschrift_input_glas.default_provider = glas_primary_process
    gutschrift_input_glas.internal_id = ID;ID = ID + 1
    gutschrift_input_glas.avoided_product = False 
    gutschrift_input_glas.quantitative_reference = False
    exch_g.append(gutschrift_input_glas)



if netto_bew != 0:
    
    bew_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"bew_primaer").id)
    bew_primary_process = client.get(olca.Process,client.find(olca.Process,"bew_primaer").id)
        
    gutschrift_input_bew = olca.Exchange()
    gutschrift_input_bew.input = True
    gutschrift_input_bew.flow = bew_primary_flow
    gutschrift_input_bew.amount = netto_bew
    gutschrift_input_bew.unit = kg 
    gutschrift_input_bew.flow_property = mass
    gutschrift_input_bew.default_provider = bew_primary_process
    gutschrift_input_bew.internal_id = ID;ID = ID + 1
    gutschrift_input_bew.avoided_product = False
    gutschrift_input_bew.quantitative_reference = False
    exch_g.append(gutschrift_input_bew)


if netto_gips != 0:
    
    gips_primary_flow = client.get(olca.Flow,client.find(olca.Flow,"gips_primaer").id)
    gips_primary_process = client.get(olca.Process,client.find(olca.Process,"gips_primaer").id)
        
    gutschrift_input_gips = olca.Exchange()
    gutschrift_input_gips.input = True
    gutschrift_input_gips.flow = gips_primary_flow
    gutschrift_input_gips.amount = netto_gips
    gutschrift_input_gips.unit = kg 
    gutschrift_input_gips.flow_property = mass
    gutschrift_input_gips.default_provider = gips_primary_process
    gutschrift_input_gips.internal_id = ID;ID = ID + 1
    gutschrift_input_gips.avoided_product = False
    gutschrift_input_gips.quantitative_reference = False
    exch_g.append(gutschrift_input_gips)




gutschrift_input_carbon = olca.Exchange()
gutschrift_input_carbon.input = True
gutschrift_input_carbon.flow = carbonin_flow
gutschrift_input_carbon.amount = netto_lvl * lvl_co2_inh + netto_bsh * bsh_co2_inh + netto_timb * timb_co2_inh + netto_osb * osb_co2_inh + netto_fibre * fibre_co2_inh # in kg
gutschrift_input_carbon.unit = kg  
gutschrift_input_carbon.flow_property = mass
gutschrift_input_carbon.internal_id = ID;ID = ID + 1
gutschrift_input_carbon.avoided_product = False
gutschrift_input_carbon.quantitative_reference = False
exch_g.append(gutschrift_input_carbon)

gutschrift_input_energy = olca.Exchange()
gutschrift_input_energy.input = True
gutschrift_input_energy.flow = energyin_flow
gutschrift_input_energy.amount = netto_lvl * lvl_energy_inh + netto_bsh * bsh_energy_inh + netto_timb * timb_energy_inh + netto_osb * osb_energy_inh  + netto_fibre * fibre_energy_inh# in kg
gutschrift_input_energy.unit = MJ  
gutschrift_input_energy.flow_property = energy
gutschrift_input_energy.internal_id = ID;ID = ID + 1
gutschrift_input_energy.avoided_product = False
gutschrift_input_energy.quantitative_reference = False
exch_g.append(gutschrift_input_energy)

gutschrift_output_carbon = olca.Exchange()
gutschrift_output_carbon.input = False
gutschrift_output_carbon.flow = carbonout_flow
gutschrift_output_carbon.amount = netto_lvl * lvl_co2_inh + netto_bsh * bsh_co2_inh + netto_timb * timb_co2_inh + netto_osb * osb_co2_inh + netto_fibre * fibre_co2_inh   # in kg
gutschrift_output_carbon.unit = kg  
gutschrift_output_carbon.flow_property = mass
gutschrift_output_carbon.internal_id = ID;ID = ID + 1
gutschrift_output_carbon.avoided_product = False
gutschrift_output_carbon.quantitative_reference = False
exch_g.append(gutschrift_output_carbon)


gutschrift_output_energy = olca.Exchange()
gutschrift_output_energy.input = False
gutschrift_output_energy.flow = energyout_flow
gutschrift_output_energy.amount = netto_lvl * lvl_energy_inh + netto_bsh * bsh_energy_inh + netto_timb * timb_energy_inh + netto_osb * osb_energy_inh + netto_fibre * fibre_energy_inh   # in kg
gutschrift_output_energy.unit = MJ  
gutschrift_output_energy.flow_property = energy
gutschrift_output_energy.internal_id = ID;ID = ID + 1
gutschrift_output_energy.avoided_product = False
gutschrift_output_energy.quantitative_reference = False
exch_g.append(gutschrift_output_energy)




if len(exch_g)==0:
    
    dummy_flow = client.get(olca.Flow,client.find(olca.Flow,"dummy").id)

        
    gutschrift_input_dummy = olca.Exchange()
    gutschrift_input_dummy.input = True
    gutschrift_input_dummy.flow = dummy_flow
    gutschrift_input_dummy.amount = 1
    gutschrift_input_dummy.unit = kg 
    gutschrift_input_dummy.flow_property = mass
    gutschrift_input_dummy.internal_id = ID;ID = ID + 1
    gutschrift_input_dummy.avoided_product = False
    gutschrift_input_dummy.quantitative_reference = False
    exch_g.append(gutschrift_input_dummy)



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

