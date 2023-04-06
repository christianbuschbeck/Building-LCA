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


if client.find(olca.Process,"C4"):
    todelete = client.get(olca.Process,client.find(olca.Process,"C4").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    

if client.find(olca.ProductSystem,"C4"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"C4").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)


########################
###    Anteile    #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
anteile=runpy.run_module(mod_name="anteile")

lvl_depo_fac   =anteile.get("lvl_depo_fac")
bsh_depo_fac   =anteile.get("bsh_depo_fac")
timb_depo_fac   =anteile.get("timb_depo_fac")
osb_depo_fac   =anteile.get("osb_depo_fac")
fibre_depo_fac =anteile.get("fibre_depo_fac")
con_depo_fac   =anteile.get("con_depo_fac")
verb_depo_fac   =anteile.get("verb_depo_fac")
glas_depo_fac   =anteile.get("glas_depo_fac")
bew_depo_fac   =anteile.get("bew_depo_fac")
gips_depo_fac   =anteile.get("gips_depo_fac")
wool_depo_fac   =anteile.get("wool_depo_fac")
lehm_depo_fac   =anteile.get("lehm_depo_fac")


########################
###     Units      #####
########################

from units import items_unit,item_factor,kg,item,mass



########################
###     Amounts    #####
########################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
lvl_kg = lvl_vol * lvl_gewicht 

bsh_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
bsh_kg = bsh_vol * bsh_gewicht 

timb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
timb_kg = timb_vol * timb_gewicht 

osb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
osb_kg = osb_vol * osb_gewicht 


fibre_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
fibre_kg = fibre_vol * fibre_gewicht 


verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])

bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])

gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])

wool_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","wool"])

lehm_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])


con_vol = float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","concrete"])
con_kg = con_vol * con_gewicht

glas_qm = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_kg = glas_qm * glas_gewicht

lvl_depo_kg = lvl_kg * lvl_depo_fac
bsh_depo_kg = bsh_kg * bsh_depo_fac
timb_depo_kg = timb_kg * timb_depo_fac
osb_depo_kg = osb_kg * osb_depo_fac
fibre_depo_kg = fibre_kg * fibre_depo_fac
verb_depo_kg = verb_kg * verb_depo_fac
con_depo_kg = con_kg * con_depo_fac
glas_depo_kg = glas_kg * glas_depo_fac
bew_depo_kg = bew_kg * bew_depo_fac
gips_depo_kg = gips_kg * gips_depo_fac
wool_depo_kg = wool_kg * wool_depo_fac
lehm_depo_kg = lehm_kg * lehm_depo_fac


pv_qm = float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
elev_no = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
hp_no = float(comp.loc[comp.loc[:,"vars"]=="include","hp"])

hp_depo_inert_kg = hp_no *1.6* 11 # aus ecoinvent 
hp_depo_refri_kg = hp_no *1.6* 3.09 # aus ecoinvent 

elev_depo_inert_kg = elev_no * (4.7+ 2.1 + 16.1 + 5.54194554849452 + 38.7966845344329 + 4.35851516651855 + 4.35851516651855 + 1 + 14.627219284657 + 15.9630377733847 + 7.58126572718271 + 6.94685045672503) # aus ecoinvent 
elev_depo_oil_kg   = elev_no * 130

pv_depo_inert_kg = pv_qm * 5 # aus ecoinvent geschätzt

########################
###     Flows      #####
########################

#ab 
if not client.find(olca.Flow,"C4_flow"):            
    
    ab_flow = olca.Flow()
    ab_flow.id = str(uuid.uuid4())
    ab_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    ab_flow.name = "C4_flow"
    ab_flow.description = "deponierung"
    ab_flow.unit = items_unit
    ab_flow.flow_properties = [item_factor]
    ab_flow.olca_type = olca.schema.Flow.__name__

    client.insert(ab_flow)

ab_flow = client.get(olca.Flow,client.find(olca.Flow,"C4_flow").id)



########################
###   Processes      ###
########################
exch = []
ID = 1

ab = olca.Process()
ab.category = client.find(olca.Category,"C4")
ab.process_type = olca.ProcessType.UNIT_PROCESS
ab.id = str(uuid.uuid4())
ab.name = "C4"
ab.olca_type = olca.schema.Process.__name__

if lvl_depo_kg + bsh_depo_kg + timb_depo_kg + osb_depo_kg + fibre_depo_kg > 0:

    waste_wood_flow = client.get(olca.Flow,"6f2eb438-cde2-4d07-a770-d023a988a9c4") # waste wood, untreated
    wood_treatment_proc = client.get(olca.Process,"16c2d9b0-a9cf-4024-b047-af41b2d95b61") #treatment of waste wood, untreated, sanitary landfill | waste wood, untreated | EN15804, U
    
    
    ab_output_holz = olca.Exchange()
    ab_output_holz.input = False
    ab_output_holz.flow = waste_wood_flow
    ab_output_holz.flow_property = mass
    ab_output_holz.unit = kg
    ab_output_holz.amount = lvl_depo_kg + bsh_depo_kg + timb_depo_kg + osb_depo_kg + fibre_depo_kg
    ab_output_holz.default_provider = wood_treatment_proc
    ab_output_holz.quantitative_reference = False
    ab_output_holz.internal_id = ID;ID=ID+1
    ab_output_holz.avoided_product = False
    exch.append(ab_output_holz)


if verb_depo_kg + bew_depo_kg > 0:

    waste_stahl_flow = client.get(olca.Flow,"d1a4a803-c563-4740-84cf-3c21a488bd74")# scrap steel
    stahl_treatment_proc = client.get(olca.Process,"fe21c594-0dce-42f3-a9cf-3bc64cc10042") #treatment of scrap steel, inert material landfill | scrap steel | EN15804, U

    ab_output_stahl = olca.Exchange()
    ab_output_stahl.input = False
    ab_output_stahl.flow = waste_stahl_flow
    ab_output_stahl.flow_property = mass
    ab_output_stahl.unit = kg
    ab_output_stahl.amount = verb_depo_kg + bew_depo_kg
    ab_output_stahl.default_provider = stahl_treatment_proc
    ab_output_stahl.quantitative_reference = False
    ab_output_stahl.internal_id = ID;ID=ID+1
    ab_output_stahl.avoided_product = False
    exch.append(ab_output_stahl)

if glas_depo_kg > 0:

    waste_glas_flow = client.get(olca.Flow,"dae141a8-7daa-4f03-a649-b85b718ac65b")# waste glass
    glas_treatment_proc = client.get(olca.Process,"c5bd184d-233b-422a-a888-2b9f04b7b04b") #treatment of waste glass, sanitary landfill | waste glass | EN15804, U
    
    ab_output_glas = olca.Exchange()
    ab_output_glas.input = False
    ab_output_glas.flow = waste_glas_flow
    ab_output_glas.flow_property = mass
    ab_output_glas.unit = kg
    ab_output_glas.amount = glas_depo_kg
    ab_output_glas.default_provider = glas_treatment_proc
    ab_output_glas.quantitative_reference = False
    ab_output_glas.internal_id = ID;ID=ID+1
    ab_output_glas.avoided_product = False
    exch.append(ab_output_glas)


if con_depo_kg > 0:

    waste_con_flow = client.get(olca.Flow,"b2011f87-e037-4f68-8dec-6d8e6de4ae25")# waste concrete gravel
    con_treatment_proc = client.get(olca.Process,"c14b8821-7ade-475c-93ab-309b135f2076") #treatment of waste concrete gravel, collection for final disposal | waste concrete gravel | EN15804, U
     
    ab_output_con = olca.Exchange()
    ab_output_con.input = False
    ab_output_con.flow = waste_con_flow
    ab_output_con.flow_property = mass
    ab_output_con.unit = kg
    ab_output_con.amount = con_depo_kg
    ab_output_con.default_provider = con_treatment_proc
    ab_output_con.quantitative_reference = False
    ab_output_con.internal_id = ID;ID=ID+1
    ab_output_con.avoided_product = False
    exch.append(ab_output_con)

if hp_depo_inert_kg + elev_depo_inert_kg + pv_depo_inert_kg > 0:

    waste_mix_flow = client.get(olca.Flow,"240c1a3c-1aba-4528-afc3-3f27f56583be")# inert waste, for final disposal
    mix_treatment_proc = client.get(olca.Process,"83400c1f-0a28-4c60-a96e-5d5c4e8b5302") #treatment of inert waste, inert material landfill | inert waste, for final disposal | EN15804, U

    ab_output_mix = olca.Exchange()
    ab_output_mix.input = False
    ab_output_mix.flow = waste_mix_flow
    ab_output_mix.flow_property = mass
    ab_output_mix.unit = kg
    ab_output_mix.amount = hp_depo_inert_kg + elev_depo_inert_kg + pv_depo_inert_kg + lehm_depo_kg
    ab_output_mix.default_provider = mix_treatment_proc
    ab_output_mix.quantitative_reference = False
    ab_output_mix.internal_id = ID;ID=ID+1
    ab_output_mix.avoided_product = False
    exch.append(ab_output_mix)


if hp_depo_refri_kg > 0:

    waste_refri_flow = client.get(olca.Flow,"c2156600-205e-41a9-b1bb-c760eccb773c")# used refrigerant R134a
    refri_treatment_proc = client.get(olca.Process,"a6bba18a-e706-4afc-aab6-8f1db7a95439") #treatment of used refrigerant R134a, reclamation | used refrigerant R134a | EN15804, U

    ab_output_refri = olca.Exchange()
    ab_output_refri.input = False
    ab_output_refri.flow = waste_refri_flow
    ab_output_refri.flow_property = mass
    ab_output_refri.unit = kg
    ab_output_refri.amount = hp_depo_refri_kg
    ab_output_refri.default_provider = refri_treatment_proc
    ab_output_refri.quantitative_reference = False
    ab_output_refri.internal_id = ID;ID=ID+1
    ab_output_refri.avoided_product = False
    exch.append(ab_output_refri)
    

if gips_depo_kg > 0:

    waste_gips_flow = client.get(olca.Flow,"4058ca6d-92c0-4ce5-bdc9-a3a96eeade93")# waste gypsum plasterboard
    gips_treatment_proc = client.get(olca.Process,"a7beb8db-031c-49a7-84d7-09c1bc81d76f") #treatment of waste gypsum plasterboard, collection for final disposal | waste gypsum plasterboard | EN15804, U

    ab_output_gips = olca.Exchange()
    ab_output_gips.input = False
    ab_output_gips.flow = waste_gips_flow
    ab_output_gips.flow_property = mass
    ab_output_gips.unit = kg
    ab_output_gips.amount = gips_depo_kg
    ab_output_gips.default_provider = gips_treatment_proc
    ab_output_gips.quantitative_reference = False
    ab_output_gips.internal_id = ID;ID=ID+1
    ab_output_gips.avoided_product = False
    exch.append(ab_output_gips)


if wool_depo_kg > 0:

    waste_wool_flow = client.get(olca.Flow,"817fa2e4-cb4c-49bb-b52f-eac84d1053ff")# waste mineral wool, for final disposal
    wool_treatment_proc = client.get(olca.Process,"0698a0d8-dc4c-4318-b30c-4125b914b711") #treatment of waste mineral wool, inert material landfill | waste mineral wool, for final disposal | EN15804, U

    ab_output_wool = olca.Exchange()
    ab_output_wool.input = False
    ab_output_wool.flow = waste_wool_flow
    ab_output_wool.flow_property = mass
    ab_output_wool.unit = kg
    ab_output_wool.amount = wool_depo_kg
    ab_output_wool.default_provider = wool_treatment_proc
    ab_output_wool.quantitative_reference = False
    ab_output_wool.internal_id = ID;ID=ID+1
    ab_output_wool.avoided_product = False
    exch.append(ab_output_wool)


if lehm_depo_kg > 0:

    waste_lehm_flow = client.get(olca.Flow,"bd4b5819-02c6-41c3-97ea-a91f14b3e0bc")# waste brick
    lehm_treatment_proc = client.get(olca.Process,"16827001-2b5c-4179-acaa-6ab0aff58e6e") #treatment of waste brick, collection for final disposal | waste brick | EN15804, U

    ab_output_lehm = olca.Exchange()
    ab_output_lehm.input = False
    ab_output_lehm.flow = waste_lehm_flow
    ab_output_lehm.flow_property = mass
    ab_output_lehm.unit = kg
    ab_output_lehm.amount = lehm_depo_kg
    ab_output_lehm.default_provider = lehm_treatment_proc
    ab_output_lehm.quantitative_reference = False
    ab_output_lehm.internal_id = ID;ID=ID+1
    ab_output_lehm.avoided_product = False
    exch.append(ab_output_lehm)




if elev_depo_oil_kg > 0:

    waste_oil_flow = client.get(olca.Flow,"1b30b018-ac39-41f4-a9e0-92057eef8bb8")#waste mineral oil
    oil_treatment_proc = client.get(olca.Process,"50b40494-3837-4786-a04f-b527cd6093fd") #market for waste mineral oil | waste mineral oil | EN15804, U

    ab_output_oil = olca.Exchange()
    ab_output_oil.input = False
    ab_output_oil.flow = waste_oil_flow
    ab_output_oil.flow_property = mass
    ab_output_oil.unit = kg
    ab_output_oil.amount = elev_depo_oil_kg
    ab_output_oil.default_provider = oil_treatment_proc
    ab_output_oil.quantitative_reference = False
    ab_output_oil.internal_id = ID;ID=ID+1
    ab_output_oil.avoided_product = False
    exch.append(ab_output_oil)


if len(exch)==0:
    
    dummy_flow  = client.get(olca.Flow,client.find(olca.Flow,"dummy").id)
    
    ab_input_dummy = olca.Exchange()
    ab_input_dummy.input = True
    ab_input_dummy.flow = dummy_flow
    ab_input_dummy.amount = 1 
    ab_input_dummy.unit = items_unit
    ab_input_dummy.flow_property = item 
    ab_input_dummy.internal_id = ID;ID = ID + 1
    ab_input_dummy.avoided_product = False
    exch.append(ab_input_dummy)


ab_output_ab = olca.Exchange()
ab_output_ab.input = False
ab_output_ab.flow = ab_flow
ab_output_ab.flow_property = item
ab_output_ab.unit = items_unit
ab_output_ab.amount = 1
ab_output_ab.quantitative_reference = True
ab_output_ab.internal_id = ID;ID=ID +1 
ab_output_ab.avoided_product = False
exch.append(ab_output_ab)

ab.exchanges= exch

client.insert(ab)

