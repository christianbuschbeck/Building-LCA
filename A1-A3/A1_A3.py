# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:29:52 2020

@author: cbuschbeck
"""


import sys
import pandas as pd

home_dir = "C:/Users/cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
import runpy
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"A1-A3"):
    todelete = client.get(olca.Process,client.find(olca.Process,"A1-A3").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)
    
if client.find(olca.ProductSystem,"A1-A3"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"A1-A3").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)


########################
###     Anteile    #####
########################

sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

anteile=runpy.run_module(mod_name="anteile")

lvl_sek_share  =anteile.get("lvl_sek_share")
lvl_rueckbau   =anteile.get("lvl_rueckbau")

bsh_sek_share  =anteile.get("bsh_sek_share")
bsh_rueckbau   =anteile.get("bsh_rueckbau")

timb_sek_share  =anteile.get("timb_sek_share")
timb_rueckbau   =anteile.get("timb_rueckbau")

osb_sek_share  =anteile.get("osb_sek_share")
osb_rueckbau   =anteile.get("osb_rueckbau")

con_sek_share  =anteile.get("con_sek_share")
con_rueckbau   =anteile.get("con_rueckbau")

verb_sek_share =anteile.get("verb_sek_share")
verb_rueckbau  =anteile.get("verb_rueckbau")

glas_rueckbau  =anteile.get("glas_rueckbau")
glas_sek_share =anteile.get("glas_sek_share")

bew_rueckbau  =anteile.get("bew_rueckbau")
bew_sek_share =anteile.get("bew_sek_share")

gips_rueckbau  =anteile.get("gips_rueckbau")
gips_sek_share =anteile.get("gips_sek_share")

wool_rueckbau  =anteile.get("wool_rueckbau")
wool_sek_share =anteile.get("wool_sek_share")

lehm_rueckbau  =anteile.get("lehm_rueckbau")
lehm_sek_share =anteile.get("lehm_sek_share")

fibre_rueckbau  =anteile.get("fibre_rueckbau")
fibre_sek_share =anteile.get("fibre_sek_share")


########################
###     Units      #####
########################

from units import items_unit,item_factor,kg,m3,vol,item,mass,m2,area


########################
###   Amounts        ###
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, quoting = 3)
lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
bsh_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
timb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
osb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])
con_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
hp_number =  float(comp.loc[comp.loc[:,"vars"]=="include","hp"])
elev_number =  float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
pv_qm =  float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
glas_qm =  float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])
gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])
wool_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","wool"])
lehm_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])
fibre_vol = float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"A1-A3_flow"):    
    holzhybrid = olca.Flow()
    holzhybrid.id = str(uuid.uuid4())
    holzhybrid.flow_type = olca.FlowType.PRODUCT_FLOW
    holzhybrid.name = "A1-A3_flow"
    holzhybrid.description = "An awesome new building"
    holzhybrid.unit = items_unit
    holzhybrid.flow_properties = [item_factor]
    holzhybrid.olca_type = olca.schema.Flow.__name__

    client.insert(holzhybrid)

holzhybrid = client.get(olca.Flow,client.find(olca.Flow,"A1-A3_flow").id)




########################
###   Processes      ###
########################
exch =[]
ID = 1


if float(comp.loc[comp.loc[:,"vars"]=="include","lvl"]) > 0:
    
    lvl_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_primaer").id)
    lvl_process = client.get(olca.Process,client.find(olca.Process,"lvl_primaer").id)
    lvl_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_sekundaer").id)
    lvl_sekundaer_process = client.get(olca.Process,client.find(olca.Process,"lvl_sekundaer").id)

    herstellung_input_lvl = olca.Exchange()
    herstellung_input_lvl.input = True
    herstellung_input_lvl.flow = lvl_flow
    herstellung_input_lvl.amount = lvl_vol * (1- (lvl_sek_share*lvl_rueckbau))
    herstellung_input_lvl.default_provider = lvl_process
    herstellung_input_lvl.unit = m3 
    herstellung_input_lvl.flow_property = vol 
    herstellung_input_lvl.internal_id =ID;ID = ID + 1
    herstellung_input_lvl.avoided_product = False
    exch.append(herstellung_input_lvl)
    
    herstellung_input_lvl_sekundaer = olca.Exchange()
    herstellung_input_lvl_sekundaer.input = True
    herstellung_input_lvl_sekundaer.flow = lvl_sekundaer_flow
    herstellung_input_lvl_sekundaer.amount = lvl_vol* (lvl_sek_share*lvl_rueckbau)
    herstellung_input_lvl_sekundaer.default_provider = lvl_sekundaer_process
    herstellung_input_lvl_sekundaer.unit = m3 
    herstellung_input_lvl_sekundaer.flow_property = vol 
    herstellung_input_lvl_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_lvl_sekundaer.avoided_product = False
    exch.append(herstellung_input_lvl_sekundaer)
    
if float(comp.loc[comp.loc[:,"vars"]=="include","bsh"]) > 0:

    bsh_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_primaer").id)
    bsh_process = client.get(olca.Process,client.find(olca.Process,"bsh_primaer").id)
    bsh_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_sekundaer").id)
    bsh_sekundaer_process = client.get(olca.Process,client.find(olca.Process,"bsh_sekundaer").id)
    
    herstellung_input_bsh = olca.Exchange()
    herstellung_input_bsh.input = True
    herstellung_input_bsh.flow = bsh_flow
    herstellung_input_bsh.amount = bsh_vol * (1- (bsh_sek_share*bsh_rueckbau))
    herstellung_input_bsh.default_provider = bsh_process
    herstellung_input_bsh.unit = m3 
    herstellung_input_bsh.flow_property = vol 
    herstellung_input_bsh.internal_id = ID;ID = ID + 1
    herstellung_input_bsh.avoided_product = False
    exch.append(herstellung_input_bsh)

    herstellung_input_bsh_sekundaer = olca.Exchange()
    herstellung_input_bsh_sekundaer.input = True
    herstellung_input_bsh_sekundaer.flow = bsh_sekundaer_flow
    herstellung_input_bsh_sekundaer.amount = bsh_vol* (bsh_sek_share*bsh_rueckbau)
    herstellung_input_bsh_sekundaer.default_provider = bsh_sekundaer_process
    herstellung_input_bsh_sekundaer.unit = m3 
    herstellung_input_bsh_sekundaer.flow_property = vol 
    herstellung_input_bsh_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_bsh_sekundaer.avoided_product = False
    exch.append(herstellung_input_bsh_sekundaer)


if float(comp.loc[comp.loc[:,"vars"]=="include","timb"]) > 0:

    timb_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_primaer").id)
    timb_process = client.get(olca.Process,client.find(olca.Process,"timb_primaer").id)
    timb_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_sekundaer").id)
    timb_sekundaer_process = client.get(olca.Process,client.find(olca.Process,"timb_sekundaer").id)
    
    herstellung_input_timb = olca.Exchange()
    herstellung_input_timb.input = True
    herstellung_input_timb.flow = timb_flow
    herstellung_input_timb.amount = timb_vol * (1- (timb_sek_share*timb_rueckbau))
    herstellung_input_timb.default_provider = timb_process
    herstellung_input_timb.unit = m3 
    herstellung_input_timb.flow_property = vol 
    herstellung_input_timb.internal_id = ID;ID = ID + 1
    herstellung_input_timb.avoided_product = False
    exch.append(herstellung_input_timb)

    herstellung_input_timb_sekundaer = olca.Exchange()
    herstellung_input_timb_sekundaer.input = True
    herstellung_input_timb_sekundaer.flow = timb_sekundaer_flow
    herstellung_input_timb_sekundaer.amount = timb_vol* (timb_sek_share*timb_rueckbau)
    herstellung_input_timb_sekundaer.default_provider = timb_sekundaer_process
    herstellung_input_timb_sekundaer.unit = m3 
    herstellung_input_timb_sekundaer.flow_property = vol 
    herstellung_input_timb_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_timb_sekundaer.avoided_product = False
    exch.append(herstellung_input_timb_sekundaer)


if float(comp.loc[comp.loc[:,"vars"]=="include","osb"]) > 0:

    osb_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_primaer").id)
    osb_process = client.get(olca.Process,client.find(olca.Process,"osb_primaer").id)
        
    osb_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_sekundaer").id)
    osb_sekundaer_process = client.get(olca.Process,client.find(olca.Process,"osb_sekundaer").id)
    
    herstellung_input_osb = olca.Exchange()
    herstellung_input_osb.input = True
    herstellung_input_osb.flow = osb_flow
    herstellung_input_osb.amount = osb_vol * (1- (osb_sek_share*osb_rueckbau))
    herstellung_input_osb.default_provider = osb_process
    herstellung_input_osb.unit = m3 
    herstellung_input_osb.flow_property = vol 
    herstellung_input_osb.internal_id = ID;ID = ID + 1
    herstellung_input_osb.avoided_product = False
    exch.append(herstellung_input_osb)

    herstellung_input_osb_sekundaer = olca.Exchange()
    herstellung_input_osb_sekundaer.input = True
    herstellung_input_osb_sekundaer.flow = osb_sekundaer_flow
    herstellung_input_osb_sekundaer.amount = osb_vol* (osb_sek_share*osb_rueckbau)
    herstellung_input_osb_sekundaer.default_provider = osb_sekundaer_process
    herstellung_input_osb_sekundaer.unit = m3 
    herstellung_input_osb_sekundaer.flow_property = vol 
    herstellung_input_osb_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_osb_sekundaer.avoided_product = False
    exch.append(herstellung_input_osb_sekundaer)


if float(comp.loc[comp.loc[:,"vars"]=="include","fibre"]) > 0:

    fibre_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_primaer").id)
    fibre_process = client.get(olca.Process,client.find(olca.Process,"fibre_primaer").id)
        
    fibre_sekundaer_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_sekundaer").id)
    fibre_sekundaer_process = client.get(olca.Process,client.find(olca.Process,"fibre_sekundaer").id)
    
    herstellung_input_fibre = olca.Exchange()
    herstellung_input_fibre.input = True
    herstellung_input_fibre.flow = fibre_flow
    herstellung_input_fibre.amount = fibre_vol * (1- (fibre_sek_share*fibre_rueckbau))
    herstellung_input_fibre.default_provider = fibre_process
    herstellung_input_fibre.unit = m3 
    herstellung_input_fibre.flow_property = vol 
    herstellung_input_fibre.internal_id = ID;ID = ID + 1
    herstellung_input_fibre.avoided_product = False
    exch.append(herstellung_input_fibre)

    herstellung_input_fibre_sekundaer = olca.Exchange()
    herstellung_input_fibre_sekundaer.input = True
    herstellung_input_fibre_sekundaer.flow = fibre_sekundaer_flow
    herstellung_input_fibre_sekundaer.amount = fibre_vol* (fibre_sek_share*fibre_rueckbau)
    herstellung_input_fibre_sekundaer.default_provider = fibre_sekundaer_process
    herstellung_input_fibre_sekundaer.unit = m3 
    herstellung_input_fibre_sekundaer.flow_property = vol 
    herstellung_input_fibre_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_fibre_sekundaer.avoided_product = False
    exch.append(herstellung_input_fibre_sekundaer)


    
if float(comp.loc[comp.loc[:,"vars"]=="include","verb"]) > 0:

    verb_flow  = client.get(olca.Flow,client.find(olca.Flow,"verb_primaer").id)
    verb_process  = client.get(olca.Process,client.find(olca.Process,"verb_primaer").id)
    
    verb_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"verb_sekundaer").id)
    verb_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"verb_sekundaer").id)
           
    herstellung_input_verb = olca.Exchange()
    herstellung_input_verb.input = True
    herstellung_input_verb.flow = verb_flow
    herstellung_input_verb.amount = verb_kg * (1- (verb_sek_share * verb_rueckbau))
    herstellung_input_verb.default_provider = verb_process
    herstellung_input_verb.unit = kg 
    herstellung_input_verb.flow_property = mass 
    herstellung_input_verb.internal_id = ID;ID = ID + 1
    herstellung_input_verb.avoided_product = False
    exch.append(herstellung_input_verb)
    
    herstellung_input_verb_sekundaer = olca.Exchange()
    herstellung_input_verb_sekundaer.input = True
    herstellung_input_verb_sekundaer.flow = verb_sekundaer_flow
    herstellung_input_verb_sekundaer.amount = verb_kg * (verb_sek_share * verb_rueckbau)
    herstellung_input_verb_sekundaer.default_provider = verb_sekundaer_process
    herstellung_input_verb_sekundaer.unit = kg 
    herstellung_input_verb_sekundaer.flow_property = mass 
    herstellung_input_verb_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_verb_sekundaer.avoided_product = False
    exch.append(herstellung_input_verb_sekundaer)
    
if float(comp.loc[comp.loc[:,"vars"]=="include","concrete"]) > 0:

    con_flow  = client.get(olca.Flow,client.find(olca.Flow,"concrete_primaer").id)
    con_process  = client.get(olca.Process,client.find(olca.Process,"concrete_primaer").id)
    
    con_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"concrete_sekundaer").id)
    con_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"concrete_sekundaer").id)
        
    herstellung_input_con = olca.Exchange()
    herstellung_input_con.input = True
    herstellung_input_con.flow = con_flow
    herstellung_input_con.amount = con_vol * (1-(con_sek_share * con_rueckbau))
    herstellung_input_con.default_provider = con_process
    herstellung_input_con.unit = kg 
    herstellung_input_con.flow_property = mass 
    herstellung_input_con.internal_id = ID;ID = ID + 1
    herstellung_input_con.avoided_product = False
    exch.append(herstellung_input_con)

    herstellung_input_con_sekundaer = olca.Exchange()
    herstellung_input_con_sekundaer.input = True
    herstellung_input_con_sekundaer.flow = con_sekundaer_flow
    herstellung_input_con_sekundaer.amount = con_vol * (con_sek_share * con_rueckbau)
    herstellung_input_con_sekundaer.default_provider = con_sekundaer_process
    herstellung_input_con_sekundaer.unit = kg 
    herstellung_input_con_sekundaer.flow_property = mass 
    herstellung_input_con_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_con_sekundaer.avoided_product = False
    exch.append(herstellung_input_con_sekundaer)


if float(comp.loc[comp.loc[:,"vars"]=="include","glas"]) > 0:

    glas_flow  = client.get(olca.Flow,client.find(olca.Flow,"glas_primaer").id)
    glas_process  = client.get(olca.Process,client.find(olca.Process,"glas_primaer").id)

    glas_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"glas_sekundaer").id)
    glas_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"glas_sekundaer").id)
        
    herstellung_input_glas = olca.Exchange()
    herstellung_input_glas.input = True
    herstellung_input_glas.flow = glas_flow
    herstellung_input_glas.amount = glas_qm * (1 - (glas_sek_share * glas_rueckbau))
    herstellung_input_glas.default_provider = glas_process
    herstellung_input_glas.unit = m2
    herstellung_input_glas.flow_property = area 
    herstellung_input_glas.internal_id = ID;ID = ID + 1
    herstellung_input_glas.avoided_product = False
    exch.append(herstellung_input_glas)

    herstellung_input_glas_sekundaer = olca.Exchange()
    herstellung_input_glas_sekundaer.input = True
    herstellung_input_glas_sekundaer.flow = glas_sekundaer_flow
    herstellung_input_glas_sekundaer.amount = glas_qm * (glas_sek_share * glas_rueckbau)
    herstellung_input_glas_sekundaer.default_provider = glas_sekundaer_process
    herstellung_input_glas_sekundaer.unit = m2
    herstellung_input_glas_sekundaer.flow_property = area 
    herstellung_input_glas_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_glas_sekundaer.avoided_product = False
    exch.append(herstellung_input_glas_sekundaer)


if float(comp.loc[comp.loc[:,"vars"]=="include","bew"]) > 0:

    bew_flow  = client.get(olca.Flow,client.find(olca.Flow,"bew_primaer").id)
    bew_process  = client.get(olca.Process,client.find(olca.Process,"bew_primaer").id)
    
    bew_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"bew_sekundaer").id)
    bew_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"bew_sekundaer").id)
           
    herstellung_input_bew = olca.Exchange()
    herstellung_input_bew.input = True
    herstellung_input_bew.flow = bew_flow
    herstellung_input_bew.amount = bew_kg * (1- (bew_sek_share * bew_rueckbau))
    herstellung_input_bew.default_provider = bew_process
    herstellung_input_bew.unit = kg 
    herstellung_input_bew.flow_property = mass 
    herstellung_input_bew.internal_id = ID;ID = ID + 1
    herstellung_input_bew.avoided_product = False
    exch.append(herstellung_input_bew)
    
    herstellung_input_bew_sekundaer = olca.Exchange()
    herstellung_input_bew_sekundaer.input = True
    herstellung_input_bew_sekundaer.flow = bew_sekundaer_flow
    herstellung_input_bew_sekundaer.amount = bew_kg * (bew_sek_share * bew_rueckbau)
    herstellung_input_bew_sekundaer.default_provider = bew_sekundaer_process
    herstellung_input_bew_sekundaer.unit = kg 
    herstellung_input_bew_sekundaer.flow_property = mass 
    herstellung_input_bew_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_bew_sekundaer.avoided_product = False
    exch.append(herstellung_input_bew_sekundaer)
    


if float(comp.loc[comp.loc[:,"vars"]=="include","gips"]) > 0:

    gips_flow  = client.get(olca.Flow,client.find(olca.Flow,"gips_primaer").id)
    gips_process  = client.get(olca.Process,client.find(olca.Process,"gips_primaer").id)
    
    gips_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"gips_sekundaer").id)
    gips_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"gips_sekundaer").id)
           
    herstellung_input_gips = olca.Exchange()
    herstellung_input_gips.input = True
    herstellung_input_gips.flow = gips_flow
    herstellung_input_gips.amount = gips_kg * (1- (gips_sek_share * gips_rueckbau))
    herstellung_input_gips.default_provider = gips_process
    herstellung_input_gips.unit = kg 
    herstellung_input_gips.flow_property = mass 
    herstellung_input_gips.internal_id = ID;ID = ID + 1
    herstellung_input_gips.avoided_product = False
    exch.append(herstellung_input_gips)
    
    herstellung_input_gips_sekundaer = olca.Exchange()
    herstellung_input_gips_sekundaer.input = True
    herstellung_input_gips_sekundaer.flow = gips_sekundaer_flow
    herstellung_input_gips_sekundaer.amount = gips_kg * (gips_sek_share * gips_rueckbau)
    herstellung_input_gips_sekundaer.default_provider = gips_sekundaer_process
    herstellung_input_gips_sekundaer.unit = kg 
    herstellung_input_gips_sekundaer.flow_property = mass 
    herstellung_input_gips_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_gips_sekundaer.avoided_product = False
    exch.append(herstellung_input_gips_sekundaer)
    

if float(comp.loc[comp.loc[:,"vars"]=="include","wool"]) > 0:

    wool_flow  = client.get(olca.Flow,client.find(olca.Flow,"wool_primaer").id)
    wool_process  = client.get(olca.Process,client.find(olca.Process,"wool_primaer").id)
    
    wool_sekundaer_flow  = client.get(olca.Flow,client.find(olca.Flow,"wool_sekundaer").id)
    wool_sekundaer_process  = client.get(olca.Process,client.find(olca.Process,"wool_sekundaer").id)
           
    herstellung_input_wool = olca.Exchange()
    herstellung_input_wool.input = True
    herstellung_input_wool.flow = wool_flow
    herstellung_input_wool.amount = wool_kg * (1- (wool_sek_share * wool_rueckbau))
    herstellung_input_wool.default_provider = wool_process
    herstellung_input_wool.unit = kg 
    herstellung_input_wool.flow_property = mass 
    herstellung_input_wool.internal_id = ID;ID = ID + 1
    herstellung_input_wool.avoided_product = False
    exch.append(herstellung_input_wool)
    
    herstellung_input_wool_sekundaer = olca.Exchange()
    herstellung_input_wool_sekundaer.input = True
    herstellung_input_wool_sekundaer.flow = wool_sekundaer_flow
    herstellung_input_wool_sekundaer.amount = wool_kg * (wool_sek_share * wool_rueckbau)
    herstellung_input_wool_sekundaer.default_provider = wool_sekundaer_process
    herstellung_input_wool_sekundaer.unit = kg 
    herstellung_input_wool_sekundaer.flow_property = mass 
    herstellung_input_wool_sekundaer.internal_id = ID;ID = ID + 1
    herstellung_input_wool_sekundaer.avoided_product = False
    exch.append(herstellung_input_wool_sekundaer)



if float(comp.loc[comp.loc[:,"vars"]=="include","lehm"]) > 0:

    lehm_flow  = client.get(olca.Flow,client.find(olca.Flow,"lehm_primaer").id)
    lehm_process  = client.get(olca.Process,client.find(olca.Process,"lehm_primaer").id)
    
          
    herstellung_input_lehm = olca.Exchange()
    herstellung_input_lehm.input = True
    herstellung_input_lehm.flow = lehm_flow
    herstellung_input_lehm.amount = lehm_kg * (1- (lehm_sek_share * lehm_rueckbau))
    herstellung_input_lehm.default_provider = lehm_process
    herstellung_input_lehm.unit = kg 
    herstellung_input_lehm.flow_property = mass 
    herstellung_input_lehm.internal_id = ID;ID = ID + 1
    herstellung_input_lehm.avoided_product = False
    exch.append(herstellung_input_lehm)
    


if float(comp.loc[comp.loc[:,"vars"]=="include","hp"]) > 0:

    hp_flow  = client.get(olca.Flow,client.find(olca.Flow,"hp").id)
    hp_process  = client.get(olca.Process,client.find(olca.Process,"hp").id)
        
    herstellung_input_hp = olca.Exchange()
    herstellung_input_hp.input = True
    herstellung_input_hp.flow = hp_flow
    herstellung_input_hp.amount = hp_number
    herstellung_input_hp.default_provider = hp_process
    herstellung_input_hp.unit = items_unit
    herstellung_input_hp.flow_property = item 
    herstellung_input_hp.internal_id = ID;ID = ID + 1
    herstellung_input_hp.avoided_product = False
    exch.append(herstellung_input_hp)

if float(comp.loc[comp.loc[:,"vars"]=="include","elev"]) > 0:

    elev_flow  = client.get(olca.Flow,client.find(olca.Flow,"elev").id)
    elev_process  = client.get(olca.Process,client.find(olca.Process,"elev").id)
        
    herstellung_input_elev = olca.Exchange()
    herstellung_input_elev.input = True
    herstellung_input_elev.flow = elev_flow
    herstellung_input_elev.amount = 1 
    herstellung_input_elev.default_provider = elev_process
    herstellung_input_elev.unit = items_unit
    herstellung_input_elev.flow_property = item 
    herstellung_input_elev.internal_id = ID;ID = ID + 1
    herstellung_input_elev.avoided_product = False
    exch.append(herstellung_input_elev)

if float(comp.loc[comp.loc[:,"vars"]=="include","pv"]) > 0:

    pv_flow  = client.get(olca.Flow,client.find(olca.Flow,"pv").id)
    pv_process  = client.get(olca.Process,client.find(olca.Process,"pv").id)
        
    herstellung_input_pv = olca.Exchange()
    herstellung_input_pv.input = True
    herstellung_input_pv.flow = pv_flow
    herstellung_input_pv.amount = pv_qm 
    herstellung_input_pv.default_provider = pv_process
    herstellung_input_pv.unit = m2
    herstellung_input_pv.flow_property = area 
    herstellung_input_pv.internal_id = ID;ID = ID + 1
    herstellung_input_pv.avoided_product = False
    exch.append(herstellung_input_pv)


if len(exch)==0:
    
    dummy_flow  = client.get(olca.Flow,client.find(olca.Flow,"dummy").id)
    
    herstellung_input_dummy = olca.Exchange()
    herstellung_input_dummy.input = True
    herstellung_input_dummy.flow = dummy_flow
    herstellung_input_dummy.amount = 1 
    herstellung_input_dummy.unit = items_unit
    herstellung_input_dummy.flow_property = item 
    herstellung_input_dummy.internal_id = ID;ID = ID + 1
    herstellung_input_dummy.avoided_product = False
    exch.append(herstellung_input_dummy)


herstellung = olca.Process()
herstellung.category = client.find(olca.Category,"A1-A3")
herstellung.process_type = olca.ProcessType.UNIT_PROCESS
herstellung.id = str(uuid.uuid4())
herstellung.name = "A1-A3"
herstellung.olca_type = olca.schema.Process.__name__



herstellung_output = olca.Exchange()
herstellung_output.input = False
herstellung_output.flow = holzhybrid
herstellung_output.flow_property = item
herstellung_output.unit = items_unit
herstellung_output.amount = 1
herstellung_output.quantitative_reference = True
herstellung_output.internal_id = ID;ID = ID + 1
herstellung_output.avoided_product = False
exch.append(herstellung_output)


herstellung.exchanges= exch
client.insert(herstellung)


