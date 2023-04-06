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
 
if client.find(olca.Process,"crushing and sorting"):
    todelete = client.get(olca.Process,client.find(olca.Process,"crushing and sorting").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    


if client.find(olca.Process,"C3"):
    todelete = client.get(olca.Process,client.find(olca.Process,"C3").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)    

if client.find(olca.ProductSystem,"C3"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"C3").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
        

########################
###     Anteile    #####
########################

sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

anteile=runpy.run_module(mod_name="anteile")

lvl_en_fac     =anteile.get("lvl_en_fac")
lvl_sn_fac     =anteile.get("lvl_sn_fac")
lvl_depo_fac   =anteile.get("lvl_depo_fac")
lvl_wieder_fac =anteile.get("lvl_wieder_fac")

bsh_en_fac     =anteile.get("bsh_en_fac")
bsh_sn_fac     =anteile.get("bsh_sn_fac")
bsh_depo_fac   =anteile.get("bsh_depo_fac")
bsh_wieder_fac =anteile.get("bsh_wieder_fac")

timb_en_fac     =anteile.get("timb_en_fac")
timb_sn_fac     =anteile.get("timb_sn_fac")
timb_depo_fac   =anteile.get("timb_depo_fac")
timb_wieder_fac =anteile.get("timb_wieder_fac")

osb_en_fac     =anteile.get("osb_en_fac")
osb_sn_fac     =anteile.get("osb_sn_fac")
osb_depo_fac   =anteile.get("osb_depo_fac")
osb_wieder_fac =anteile.get("osb_wieder_fac")

fibre_en_fac     =anteile.get("fibre_en_fac")
fibre_sn_fac     =anteile.get("fibre_sn_fac")
fibre_depo_fac   =anteile.get("fibre_depo_fac")
fibre_wieder_fac =anteile.get("fibre_wieder_fac")

con_sn_fac      =anteile.get("con_sn_fac")
con_depo_fac    =anteile.get("con_depo_fac")
con_wieder_fac  =anteile.get("con_wieder_fac")

verb_sn_fac     =anteile.get("verb_sn_fac")
verb_depo_fac   =anteile.get("verb_depo_fac")
verb_wieder_fac =anteile.get("verb_wieder_fac")

glas_sn_fac     =anteile.get("glas_sn_fac")
glas_depo_fac   =anteile.get("glas_depo_fac")
glas_wieder_fac =anteile.get("glas_wieder_fac")

bew_sn_fac     =anteile.get("bew_sn_fac")
bew_depo_fac   =anteile.get("bew_depo_fac")
bew_wieder_fac =anteile.get("bew_wieder_fac")

gips_sn_fac     =anteile.get("gips_sn_fac")
gips_depo_fac   =anteile.get("gips_depo_fac")
gips_wieder_fac =anteile.get("gips_wieder_fac")



########################
###     Units      #####
########################

from units import items_unit,item_factor,kg,m3,vol,item,mass,mass_factor,energy,MJ
    
########################
###     Amounts    #####
########################
  
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
lvl_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])
lvl_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","lvl"])
lvl_kg = lvl_vol * lvl_gewicht # vol*gewicht
lvl_wieder_vol = lvl_vol * lvl_wieder_fac  
lvl_wieder_kg = lvl_kg * lvl_wieder_fac
lvl_sn_kg = lvl_kg * lvl_sn_fac
lvl_en_kg = lvl_kg * lvl_en_fac
lvl_deponie_kg = lvl_kg * lvl_depo_fac


bsh_vol = float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
bsh_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])
bsh_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","bsh"])
bsh_kg = bsh_vol * bsh_gewicht # vol*gewicht
bsh_wieder_vol = bsh_vol * bsh_wieder_fac  
bsh_wieder_kg = bsh_kg * bsh_wieder_fac
bsh_sn_kg = bsh_kg * bsh_sn_fac
bsh_en_kg = bsh_kg * bsh_en_fac
bsh_deponie_kg = bsh_kg * bsh_depo_fac


timb_vol = float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
timb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","timb"])
timb_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","timb"])
timb_kg = timb_vol * timb_gewicht # vol*gewicht
timb_wieder_vol = timb_vol * timb_wieder_fac  
timb_wieder_kg = timb_kg * timb_wieder_fac
timb_sn_kg = timb_kg * timb_sn_fac
timb_en_kg = timb_kg * timb_en_fac
timb_deponie_kg = timb_kg * timb_depo_fac


osb_vol = float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","osb"])
osb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","osb"])
osb_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","osb"])
osb_kg = osb_vol * osb_gewicht # vol*gewicht
osb_wieder_vol = osb_vol * osb_wieder_fac  
osb_wieder_kg = osb_kg * osb_wieder_fac
osb_sn_kg = osb_kg * osb_sn_fac
osb_en_kg = osb_kg * osb_en_fac
osb_deponie_kg = osb_kg * osb_depo_fac


fibre_vol = float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","fibre"])
fibre_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","fibre"])
fibre_energy_inh_nr = float(comp.loc[comp.loc[:,"vars"]=="energy_inh_nr","fibre"])
fibre_kg = fibre_vol * fibre_gewicht # vol*gewicht
fibre_wieder_vol = fibre_vol * fibre_wieder_fac  
fibre_wieder_kg = fibre_kg * fibre_wieder_fac
fibre_sn_kg = fibre_kg * fibre_sn_fac
fibre_en_kg = fibre_kg * fibre_en_fac
fibre_deponie_kg = fibre_kg * fibre_depo_fac

con_vol = float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","concrete"])
con_kg = con_vol * con_gewicht
con_wieder_kg = con_kg * con_wieder_fac
con_sn_kg = con_kg * con_sn_fac
con_deponie_kg = con_kg * con_depo_fac

glas_qm = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_kg = glas_qm * glas_gewicht
glas_wieder_kg = glas_kg * glas_wieder_fac
glas_sn_kg = glas_kg * glas_sn_fac
glas_deponie_kg = glas_kg * glas_depo_fac

verb_kg = float(comp.loc[comp.loc[:,"vars"]=="include","verb"])
verb_sn_kg = verb_kg * verb_sn_fac
verb_wieder_kg = verb_kg * verb_wieder_fac

bew_kg = float(comp.loc[comp.loc[:,"vars"]=="include","bew"])
bew_sn_kg = bew_kg * bew_sn_fac
bew_wieder_kg = bew_kg * bew_wieder_fac


elev_no = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])

gips_kg = float(comp.loc[comp.loc[:,"vars"]=="include","gips"])
gips_sn_kg = gips_kg * gips_sn_fac
gips_wieder_kg = gips_kg * gips_wieder_fac
gips_deponie_kg = gips_kg * gips_depo_fac


chipping_amount = lvl_sn_kg + lvl_en_kg + bsh_sn_kg + bsh_en_kg + timb_sn_kg + timb_en_kg + osb_sn_kg + osb_en_kg
crushing_amount = con_sn_kg + con_deponie_kg 
glassorting_amount = glas_sn_kg + glas_deponie_kg
gipscrushing_amount = gips_sn_kg
########################
###     Flows      #####
########################

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


if not client.find(olca.Flow,"lvl_wieder"):            
    lvl_wieder_flow = olca.Flow()
    lvl_wieder_flow.id = str(uuid.uuid4())
    lvl_wieder_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    lvl_wieder_flow.name = "lvl_wieder"
    lvl_wieder_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    lvl_wieder_flow.unit = kg
    lvl_wieder_flow.flow_properties = [mass_factor]
    lvl_wieder_flow.olca_type = olca.schema.Flow.__name__

    
    client.insert(lvl_wieder_flow)
lvl_wieder_flow = client.get(olca.Flow,client.find(olca.Flow,"lvl_wieder").id)


if not client.find(olca.Flow,"bsh_wieder"):            
    bsh_wieder_flow = olca.Flow()
    bsh_wieder_flow.id = str(uuid.uuid4())
    bsh_wieder_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    bsh_wieder_flow.name = "bsh_wieder"
    bsh_wieder_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    bsh_wieder_flow.unit = kg
    bsh_wieder_flow.flow_properties = [mass_factor]
    bsh_wieder_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(bsh_wieder_flow)
bsh_wieder_flow = client.get(olca.Flow,client.find(olca.Flow,"bsh_wieder").id)


if not client.find(olca.Flow,"timb_wieder"):            
    timb_wieder_flow = olca.Flow()
    timb_wieder_flow.id = str(uuid.uuid4())
    timb_wieder_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    timb_wieder_flow.name = "timb_wieder"
    timb_wieder_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    timb_wieder_flow.unit = kg
    timb_wieder_flow.flow_properties = [mass_factor]
    timb_wieder_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(timb_wieder_flow)
timb_wieder_flow = client.get(olca.Flow,client.find(olca.Flow,"timb_wieder").id)


if not client.find(olca.Flow,"osb_wieder"):            
    osb_wieder_flow = olca.Flow()
    osb_wieder_flow.id = str(uuid.uuid4())
    osb_wieder_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    osb_wieder_flow.name = "osb_wieder"
    osb_wieder_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    osb_wieder_flow.unit = kg
    osb_wieder_flow.flow_properties = [mass_factor]
    osb_wieder_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(osb_wieder_flow)
osb_wieder_flow = client.get(olca.Flow,client.find(olca.Flow,"osb_wieder").id)


if not client.find(olca.Flow,"fibre_wieder"):            
    fibre_wieder_flow = olca.Flow()
    fibre_wieder_flow.id = str(uuid.uuid4())
    fibre_wieder_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    fibre_wieder_flow.name = "fibre_wieder"
    fibre_wieder_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    fibre_wieder_flow.unit = kg
    fibre_wieder_flow.flow_properties = [mass_factor]
    fibre_wieder_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(fibre_wieder_flow)
fibre_wieder_flow = client.get(olca.Flow,client.find(olca.Flow,"fibre_wieder").id)



if not client.find(olca.Flow,"woodchips_en"):            
    woodchips_en_flow = olca.Flow()
    woodchips_en_flow.id = str(uuid.uuid4())
    woodchips_en_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    woodchips_en_flow.name = "woodchips_en"
    woodchips_en_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    woodchips_en_flow.unit = kg
    woodchips_en_flow.flow_properties = [mass_factor]
    woodchips_en_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(woodchips_en_flow)
woodchips_en_flow = client.get(olca.Flow,client.find(olca.Flow,"woodchips_en").id)


if not client.find(olca.Flow,"woodchips_sn"):            
    woodchips_sn_flow = olca.Flow()
    woodchips_sn_flow.id = str(uuid.uuid4())
    woodchips_sn_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    woodchips_sn_flow.name = "woodchips_sn"
    woodchips_sn_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    woodchips_sn_flow.unit = kg
    woodchips_sn_flow.flow_properties = [mass_factor]
    woodchips_sn_flow.olca_type = olca.schema.Flow.__name__
    
    client.insert(woodchips_sn_flow)
woodchips_sn_flow = client.get(olca.Flow,client.find(olca.Flow,"woodchips_sn").id)


if not client.find(olca.Flow,"deponieholz"):            
    
    deponieholz_flow = olca.Flow()
    deponieholz_flow.id = str(uuid.uuid4())
    deponieholz_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    deponieholz_flow.name = "deponieholz"
    deponieholz_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    deponieholz_flow.unit = kg
    deponieholz_flow.flow_properties = [mass_factor]
    deponieholz_flow.olca_type = olca.schema.Flow.__name__

    client.insert(deponieholz_flow)
deponieholz_flow = client.get(olca.Flow,client.find(olca.Flow,"deponieholz").id)


if not client.find(olca.Flow,"C3_flow"):            
    
    av_flow = olca.Flow()
    av_flow.id = str(uuid.uuid4())
    av_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    av_flow.name = "C3_flow"
    av_flow.description = "z. B. Sammlung von Abfallfraktionen aus dem Rückbau und der av der Materialströme, die für die Wiederverwendung, das Recycling und die Energierückgewinnung vorgesehen sind"
    av_flow.unit = items_unit
    av_flow.flow_properties = [item_factor]
    av_flow.olca_type = olca.schema.Flow.__name__

    client.insert(av_flow)

av_flow = client.get(olca.Flow,client.find(olca.Flow,"C3_flow").id)

perm_flow = client.get(olca.Flow,"2b08df35-ebaf-4dcf-a5ac-d985915d5223")# Energy, gross calorific value, in biomass, used as raw material

########################
###   Processes      ###
########################
exch = []
ID = 1

av_input_perm = olca.Exchange()
av_input_perm.input = True
av_input_perm.flow = perm_flow
av_input_perm.flow_property = energy
av_input_perm.unit = MJ
av_input_perm.amount = -( lvl_vol* lvl_energy_inh + bsh_vol * bsh_energy_inh + timb_vol * timb_energy_inh + osb_vol * osb_energy_inh + fibre_vol * fibre_energy_inh)
av_input_perm.quantitative_reference = False
av_input_perm.internal_id = ID; ID = ID + 1
av_input_perm.avoided_product = False
exch.append(av_input_perm)

### Holz
chipping_flow = client.get(olca.Flow,"86cf2137-cb67-4ab6-8041-8e767c0579f0") #wood chipping, industrial residual wood, stationary electric chipper
chipping_proc = client.get(olca.Process,"009f04a6-487d-4d99-9d77-b5c0642b4074") #  wood chipping, industrial residual wood, stationary electric chipper | wood chipping, industrial residual wood, stationary electric chipper | EN15804, U


av_input_chipping = olca.Exchange()
av_input_chipping.input = True
av_input_chipping.flow = chipping_flow
av_input_chipping.amount = chipping_amount
av_input_chipping.unit = kg  
av_input_chipping.flow_property = mass
av_input_chipping.internal_id = ID; ID = ID + 1
av_input_chipping.default_provider = chipping_proc
av_input_chipping.avoided_product = False
av_input_chipping.quantitative_reference = False
exch.append(av_input_chipping)





av = olca.Process()
av.category = client.find(olca.Category,"C3")
av.process_type = olca.ProcessType.UNIT_PROCESS
av.id = str(uuid.uuid4())
av.name = "C3"
av.olca_type = olca.schema.Process.__name__


### Beton

crushing_proc = client.get(olca.Process,"4bdfb3a2-306b-4453-91d4-cafe1bda951f") #  treatment of waste concrete gravel, sorting plant | waste concrete gravel | EN15804, U
#Der Datensatz treatment of waste concrete sorting plant enthält noch den Abriss von Beton. Dieser muss entfernt werden um lediglich die Abfallaufbereitung abzubilden.
for ex in crushing_proc.exchanges:
    if ex.flow.name == "diesel, burned in building machine":
        crushing_proc.exchanges.remove(ex)

crushing_proc.name = "crushing and sorting"
crushing_proc.id = str(uuid.uuid4())
crushing_proc.olca_type = olca.schema.Process.__name__

client.insert(crushing_proc)

crushing_flow = client.get(olca.Flow,"b2011f87-e037-4f68-8dec-6d8e6de4ae25") # waste concrete gravel
crushing_proc = client.get(olca.Process,client.find(olca.Process,"crushing and sorting").id) #  treatment of waste concrete gravel, sorting plant | waste concrete gravel | Cutoff, U

av_output_crushing = olca.Exchange()
av_output_crushing.input = False
av_output_crushing.flow = crushing_flow
av_output_crushing.amount = crushing_amount
av_output_crushing.unit = kg  
av_output_crushing.flow_property = mass
av_output_crushing.internal_id = ID; ID = ID + 1
av_output_crushing.default_provider = crushing_proc
av_output_crushing.avoided_product = False
av_output_crushing.quantitative_reference = False
exch.append(av_output_crushing)


### Glas

glassorting_flow = client.get(olca.Flow,"42b1c202-8308-422e-bfb7-3efe54dfcef6") # waste glass sheet
glassorting_proc = client.get(olca.Process,"9e8b54c1-40c3-43ee-8064-5701a354e457") #  treatment of waste glass sheet, sorting plant | waste glass sheet | EN15804, U

av_output_glassorting   = olca.Exchange()
av_output_glassorting.input = False
av_output_glassorting.flow = glassorting_flow
av_output_glassorting.amount = glassorting_amount
av_output_glassorting.unit = kg  
av_output_glassorting.flow_property = mass
av_output_glassorting.internal_id = ID; ID = ID + 1
av_output_glassorting.default_provider = glassorting_proc
av_output_glassorting.avoided_product = False
av_output_glassorting.quantitative_reference = False
exch.append(av_output_glassorting)

### Gips

gipscrushing_flow = client.get(olca.Flow,"4058ca6d-92c0-4ce5-bdc9-a3a96eeade93") # waste gypsum plasterboard
gipscrushing_proc = client.get(olca.Process,"99386f10-e93f-4c91-bb8c-b314dd1c15b6") # treatment of waste gypsum plasterboard, sorting plant | waste gypsum plasterboard | EN15804, U

av_output_gipscrushing   = olca.Exchange()
av_output_gipscrushing.input = False
av_output_gipscrushing.flow = gipscrushing_flow
av_output_gipscrushing.amount = gipscrushing_amount
av_output_gipscrushing.unit = kg  
av_output_gipscrushing.flow_property = mass
av_output_gipscrushing.internal_id = ID; ID = ID + 1
av_output_gipscrushing.default_provider = gipscrushing_proc
av_output_gipscrushing.avoided_product = False
av_output_gipscrushing.quantitative_reference = False
exch.append(av_output_gipscrushing)


av_output_carbon = olca.Exchange()
av_output_carbon.input = False
av_output_carbon.flow = carbonout_flow
av_output_carbon.flow_property = mass
av_output_carbon.unit = kg
av_output_carbon.amount = lvl_vol* lvl_co2_inh + bsh_vol * bsh_co2_inh + timb_vol * timb_co2_inh + osb_vol * osb_co2_inh + fibre_vol * fibre_co2_inh
av_output_carbon.quantitative_reference = False
av_output_carbon.internal_id = ID; ID = ID + 1
av_output_carbon.avoided_product = False
exch.append(av_output_carbon)

av_output_energie = olca.Exchange()
av_output_energie.input = False
av_output_energie.flow = energyout_flow
av_output_energie.flow_property = energy
av_output_energie.unit = MJ
av_output_energie.amount = lvl_vol* lvl_energy_inh + bsh_vol * bsh_energy_inh + timb_vol * timb_energy_inh + osb_vol * osb_energy_inh + fibre_vol * fibre_energy_inh
av_output_energie.quantitative_reference = False
av_output_energie.internal_id = ID; ID = ID + 1
av_output_energie.avoided_product = False
exch.append(av_output_energie)


av_output_av = olca.Exchange()
av_output_av.input = False
av_output_av.flow = av_flow
av_output_av.flow_property = item
av_output_av.unit = items_unit
av_output_av.amount = 1
av_output_av.quantitative_reference = True
av_output_av.internal_id = ID; ID = ID + 1
av_output_av.avoided_product = False
exch.append(av_output_av)

av_output_lvl_wieder = olca.Exchange()
av_output_lvl_wieder.input = False
av_output_lvl_wieder.flow = lvl_wieder_flow
av_output_lvl_wieder.flow_property = vol
av_output_lvl_wieder.unit = m3
av_output_lvl_wieder.amount = lvl_wieder_vol
av_output_lvl_wieder.quantitative_reference = False
av_output_lvl_wieder.internal_id =ID; ID = ID + 1
av_output_lvl_wieder.avoided_product = False
exch.append(av_output_lvl_wieder)

av_output_bsh_wieder = olca.Exchange()
av_output_bsh_wieder.input = False
av_output_bsh_wieder.flow = bsh_wieder_flow
av_output_bsh_wieder.flow_property = vol
av_output_bsh_wieder.unit = m3
av_output_bsh_wieder.amount = bsh_wieder_vol
av_output_bsh_wieder.quantitative_reference = False
av_output_bsh_wieder.internal_id = ID; ID = ID + 1
av_output_bsh_wieder.avoided_product = False
exch.append(av_output_bsh_wieder)

av_output_timb_wieder = olca.Exchange()
av_output_timb_wieder.input = False
av_output_timb_wieder.flow = timb_wieder_flow
av_output_timb_wieder.flow_property = vol
av_output_timb_wieder.unit = m3
av_output_timb_wieder.amount = timb_wieder_vol
av_output_timb_wieder.quantitative_reference = False
av_output_timb_wieder.internal_id = ID; ID = ID + 1
av_output_timb_wieder.avoided_product = False
exch.append(av_output_timb_wieder)

av_output_osb_wieder = olca.Exchange()
av_output_osb_wieder.input = False
av_output_osb_wieder.flow = osb_wieder_flow
av_output_osb_wieder.flow_property = vol
av_output_osb_wieder.unit = m3
av_output_osb_wieder.amount = osb_wieder_vol
av_output_osb_wieder.quantitative_reference = False
av_output_osb_wieder.internal_id = ID; ID = ID + 1
av_output_osb_wieder.avoided_product = False
exch.append(av_output_osb_wieder)

av_output_fibre_wieder = olca.Exchange()
av_output_fibre_wieder.input = False
av_output_fibre_wieder.flow = fibre_wieder_flow
av_output_fibre_wieder.flow_property = vol
av_output_fibre_wieder.unit = m3
av_output_fibre_wieder.amount = fibre_wieder_vol
av_output_fibre_wieder.quantitative_reference = False
av_output_fibre_wieder.internal_id = ID; ID = ID + 1
av_output_fibre_wieder.avoided_product = False
exch.append(av_output_fibre_wieder)

av_output_holz_en = olca.Exchange()
av_output_holz_en.input = False
av_output_holz_en.flow = woodchips_en_flow
av_output_holz_en.flow_property = mass
av_output_holz_en.unit = kg
av_output_holz_en.amount = lvl_en_kg + bsh_en_kg  + timb_en_kg + osb_en_kg + fibre_en_kg
av_output_holz_en.quantitative_reference = False
av_output_holz_en.internal_id =ID; ID = ID + 1
av_output_holz_en.avoided_product = False
exch.append(av_output_holz_en)

av_output_holz_sn = olca.Exchange()
av_output_holz_sn.input = False
av_output_holz_sn.flow = woodchips_sn_flow
av_output_holz_sn.flow_property = mass
av_output_holz_sn.unit = kg
av_output_holz_sn.amount = lvl_sn_kg + bsh_sn_kg + timb_sn_kg 
av_output_holz_sn.quantitative_reference = False
av_output_holz_sn.internal_id = ID; ID = ID + 1
av_output_holz_sn.avoided_product = False
exch.append(av_output_holz_sn)

av_output_holz_deponie = olca.Exchange()
av_output_holz_deponie.input = False
av_output_holz_deponie.flow = deponieholz_flow
av_output_holz_deponie.flow_property = mass
av_output_holz_deponie.unit = kg
av_output_holz_deponie.amount = lvl_deponie_kg + bsh_deponie_kg + timb_deponie_kg + osb_deponie_kg + fibre_deponie_kg
av_output_holz_deponie.quantitative_reference = False
av_output_holz_deponie.internal_id = ID; ID = ID + 1
av_output_holz_deponie.avoided_product = False
exch.append(av_output_holz_deponie)

mer_flow = client.get(olca.Flow,"fff53104-0c99-44cb-88af-e782f75feec2")  # material for energy recovery
mfr_flow = client.get(olca.Flow,"7b137121-84f1-45e4-a98d-e8e617773e94")  #material for recycling
cru_flow = client.get(olca.Flow,"5e1ead53-97b4-46c5-a37d-f206bf0e458f")  # component for re-use

av_output_mer = olca.Exchange()
av_output_mer.input = False
av_output_mer.flow = mer_flow
av_output_mer.flow_property = mass
av_output_mer.unit = kg
av_output_mer.amount = lvl_en_kg + bsh_en_kg + timb_en_kg + osb_en_kg  + fibre_en_kg  
av_output_mer.quantitative_reference = False
av_output_mer.internal_id = ID; ID = ID + 1
av_output_mer.avoided_product = False
exch.append(av_output_mer)

av_output_mfr = olca.Exchange()
av_output_mfr.input = False
av_output_mfr.flow = mfr_flow
av_output_mfr.flow_property = mass
av_output_mfr.unit = kg
av_output_mfr.amount = lvl_sn_kg + bsh_sn_kg + timb_sn_kg  + glas_sn_kg + verb_sn_kg + con_sn_kg + gips_sn_kg
av_output_mfr.quantitative_reference = False
av_output_mfr.internal_id = ID; ID = ID + 1
av_output_mfr.avoided_product = False
exch.append(av_output_mfr)

av_output_cru = olca.Exchange()
av_output_cru.input = False
av_output_cru.flow = cru_flow
av_output_cru.flow_property = mass
av_output_cru.unit = kg
av_output_cru.amount = lvl_wieder_kg + bsh_wieder_kg + timb_wieder_kg + osb_wieder_kg + glas_wieder_kg + verb_wieder_kg + con_wieder_kg + gips_wieder_kg
av_output_cru.quantitative_reference = False
av_output_cru.internal_id = ID; ID = ID + 1
av_output_cru.avoided_product = False
exch.append(av_output_cru)


av.exchanges= exch
client.insert(av)

