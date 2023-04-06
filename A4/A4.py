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


if client.find(olca.Process,"A4"):
    todelete = client.get(olca.Process,client.find(olca.Process,"A4").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"A4"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"A4").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)

    
########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import items_unit,item_factor,item,transportation,transportation_unit

########################
###     Amounts    #####
########################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_kg = lvl_vol * lvl_gewicht

bsh_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_kg = bsh_vol * bsh_gewicht

timb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_kg = timb_vol * timb_gewicht

osb_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_kg = osb_vol * osb_gewicht

fibre_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_kg = fibre_vol * fibre_gewicht

con_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_kg =  con_vol * con_gewicht

verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])

hp_number = float(comp.loc[comp.loc[:,"vars"]=="include","hp"])
hp_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","hp"])
hp_kg = hp_number * hp_weight

elev_number = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
elev_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","elev"])
elev_kg = elev_number * elev_weight

pv_qm = float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
pv_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","pv"]) # Gewicht aus Ökobaudat MFR (C3) und NHWD (C4)
pv_kg = pv_qm * pv_weight

glas_qm = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_weight = float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"]) # Gewicht aus Ökobaudat MFR (C3) und NHWD (C4)
glas_kg = glas_qm * glas_weight

bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])

gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])

wool_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","wool"])

lehm_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])

mean_distance_lvl = 354 #km -> wheighted mean von creuzheim
mean_distance_bsh = 100 #km ???????
mean_distance_timb = 100 #km ???????
mean_distance_osb = 100 #km ???????
mean_distance_fibre = 100 #km ???????
mean_distance_verb = 100 #km ???????
mean_distance_con = 15 #km ???????
mean_distance_hp = 100 #km ???????
mean_distance_elev = 100 #km ???????
mean_distance_pv = 100 #km ???????
mean_distance_glas = 100 #km ???????
mean_distance_bew = 100 #km ???????
mean_distance_gips = 100 #km ???????
mean_distance_wool = 100 #km ???????
mean_distance_lehm = 100 #km ???????




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


transport_total = lvl_transport + bsh_transport + timb_transport + osb_transport + fibre_transport + verb_transport + con_transport + hp_transport + elev_transport + pv_transport + glas_transport + bew_transport + gips_transport + wool_transport + lehm_transport# -> in tonnen
########################
###     Flows      #####
########################

#transportiertes_material 
if not client.find(olca.Flow,"A4_flow"):    
        
    transportiertes_material = olca.Flow()
    transportiertes_material.id = str(uuid.uuid4())
    transportiertes_material.flow_type = olca.FlowType.PRODUCT_FLOW
    transportiertes_material.name = "A4_flow"
    transportiertes_material.description = "z. B. Sammlung von materialfraktionen aus dem Rückbau und der materialtransport der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    transportiertes_material.unit = items_unit
    transportiertes_material.flow_properties = [item_factor]
    transportiertes_material.olca_type = olca.schema.Flow.__name__

    client.insert(transportiertes_material)

transportiertes_material = client.get(olca.Flow,client.find(olca.Flow,"A4_flow").id)


########################
###   Processes      ###
########################
exch=[]
ID = 1

transport_flow = client.get(olca.Flow,"cfbce515-3f54-4411-ad9d-3d26b7faa15a") # transport, freight, lorry, unspecified
transport_proc = client.get(olca.Process,"68e9aab2-7411-4446-8447-247ae497bcf4") # market for transport, freight, lorry, unspecified | transport, freight, lorry, unspecified | EN15804, U


materialtransport_input = olca.Exchange()
materialtransport_input.input = True
materialtransport_input.flow = transport_flow
materialtransport_input.amount = transport_total
materialtransport_input.default_provider = transport_proc 
materialtransport_input.unit = transportation_unit  
materialtransport_input.flow_property = transportation 
materialtransport_input.internal_id = ID; ID = ID+1
materialtransport_input.avoided_product = False
exch.append(materialtransport_input)

materialtransport = olca.Process()
materialtransport.category = client.find(olca.Category,"A4")
materialtransport.process_type = olca.ProcessType.UNIT_PROCESS
materialtransport.id = str(uuid.uuid4())
materialtransport.name = "A4"
materialtransport.olca_type = olca.schema.Process.__name__


materialtransport_output = olca.Exchange()
materialtransport_output.input = False
materialtransport_output.flow = transportiertes_material
materialtransport_output.flow_property = item
materialtransport_output.unit = items_unit
materialtransport_output.amount = 1
materialtransport_output.quantitative_reference = True
materialtransport_output.internal_id = ID; ID = ID+1
materialtransport_output.avoided_product = False
exch.append(materialtransport_output)

materialtransport.exchanges= exch

client.insert(materialtransport)

