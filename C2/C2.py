# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:44:21 2020

@author: cbuschbeck
"""

import sys
import pandas as pd

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"C2"):
    todelete = client.get(olca.Process,client.find(olca.Process,"C2").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"C2"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"C2").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
    
########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
from units import transportation,transportation_unit,items_unit,item_factor,item


########################
###     Amounts    #####
########################
    
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_kg = lvl_vol * lvl_dichte

bsh_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_kg = bsh_vol * bsh_dichte

timb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_kg = timb_vol * timb_dichte

osb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
osb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_kg = osb_vol * osb_dichte


fibre_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
fibre_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_kg = fibre_vol * fibre_dichte

con_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_kg =  con_vol * con_gewicht

verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])

glas_qm = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_dichte =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_kg = glas_qm * glas_dichte

bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])

hp_number = float(comp.loc[comp.loc[:,"vars"]=="include","hp"])
hp_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","hp"])
hp_kg = hp_number * hp_weight

elev_number = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
elev_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","elev"])
elev_kg = elev_number * elev_weight

pv_qm = float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
pv_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","pv"]) # Gewicht aus Ökobaudat MFR (C3) und NHWD (C4)
pv_kg = pv_qm * pv_weight

gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])

wool_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","wool"])

lehm_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])


mean_distance_lvl  = 20 #km ????
mean_distance_bsh  = 20 #km ???????
mean_distance_timb = 20 #km ???????
mean_distance_osb = 20 #km ???????
mean_distance_fibre = 20 #km ???????
mean_distance_verb = 20 #km ???????
mean_distance_con  = 20 #km ???????
mean_distance_hp   = 20 #km ???????
mean_distance_elev = 20 #km ???????
mean_distance_pv   = 200 #km ???????
mean_distance_glas = 20 #km ???????
mean_distance_bew  = 20 #km ???????
mean_distance_gips = 20 #km ???????
mean_distance_wool = 20 #km ???????
mean_distance_lehm = 20 #km ???????




bsh_transport = (bsh_kg/1000) * mean_distance_bsh
lvl_transport = (lvl_kg/1000) * mean_distance_lvl
timb_transport = (timb_kg/1000) * mean_distance_timb
osb_transport = (osb_kg/1000) * mean_distance_osb
fibre_transport = (fibre_kg/1000) * mean_distance_fibre
verb_transport = (verb_kg/1000) * mean_distance_verb
con_transport = (con_kg/1000) * mean_distance_con
hp_transport = (hp_kg/1000) * mean_distance_hp
elev_transport = (elev_kg/1000) * mean_distance_elev
pv_transport = (pv_kg/1000) * mean_distance_pv
glas_transport = (glas_kg/1000) * mean_distance_glas
bew_transport = (bew_kg/1000) * mean_distance_bew
gips_transport = (gips_kg/1000) * mean_distance_gips
wool_transport = (wool_kg/1000) * mean_distance_wool
lehm_transport = (lehm_kg/1000) * mean_distance_lehm


transport_total = lvl_transport + bsh_transport + timb_transport + osb_transport + fibre_transport + verb_transport + con_transport + hp_transport + elev_transport + pv_transport + glas_transport + bew_transport + gips_transport  + wool_transport + lehm_transport# -> in tonnen


########################
###     Flows      #####
########################

#at 
if not client.find(olca.Flow,"C2_flow"):            
    
    at_flow = olca.Flow()
    at_flow.id = str(uuid.uuid4())
    at_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    at_flow.name = "C2_flow"
    at_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    at_flow.unit = items_unit
    at_flow.flow_properties = [item_factor]
    at_flow.olca_type = olca.schema.Flow.__name__

    client.insert(at_flow)

at_flow = client.get(olca.Flow,client.find(olca.Flow,"C2_flow").id)


########################
###   Processes      ###
########################
ID = 1
exch=[]
waste_collection_flow = client.get(olca.Flow,"cfbce515-3f54-4411-ad9d-3d26b7faa15a") #transport, freight, lorry, unspecified 

#Collection 
waste_collection_proc = client.get(olca.Process,"68e9aab2-7411-4446-8447-247ae497bcf4") #market for transport, freight, lorry, unspecified | transport, freight, lorry, unspecified | EN15804, U

at_input = olca.Exchange()
at_input.input = True
at_input.flow = waste_collection_flow
at_input.amount = transport_total
at_input.default_provider = waste_collection_proc 
at_input.unit = transportation_unit  
at_input.flow_property = transportation 
at_input.internal_id = ID; ID = ID + 1
at_input.avoided_product = False
exch.append(at_input)

at = olca.Process()
at.category = client.find(olca.Category,"C2")
at.process_type = olca.ProcessType.UNIT_PROCESS
at.id = str(uuid.uuid4())
at.name = "C2"
at.olca_type = olca.schema.Process.__name__


at_output_at = olca.Exchange()
at_output_at.input = False
at_output_at.flow = at_flow
at_output_at.flow_property = item
at_output_at.unit = items_unit
at_output_at.amount = 1
at_output_at.quantitative_reference = True
at_output_at.internal_id = ID; ID = ID + 1
at_output_at.avoided_product = False
exch.append(at_output_at)


at.exchanges= exch
client.insert(at)

