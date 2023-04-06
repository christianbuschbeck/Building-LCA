# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:36:25 2020

@author: cbuschbeck
"""

import pandas as pd

########################
###    Anteile    #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, quoting = 3)

kaskade_lvl = float(comp.loc[comp.loc[:,"vars"]=="kaskade","lvl"])
CE_lvl = float(comp.loc[comp.loc[:,"vars"]=="CE","lvl"])
lvl_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","lvl"])
lvl_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_include = float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
val_lvl= float(comp.loc[comp.loc[:,"vars"]=="val","lvl"])

kaskade_bsh = float(comp.loc[comp.loc[:,"vars"]=="kaskade","bsh"])
CE_bsh = float(comp.loc[comp.loc[:,"vars"]=="CE","bsh"])
bsh_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","bsh"])
bsh_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_include = float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
val_bsh = float(comp.loc[comp.loc[:,"vars"]=="val","bsh"])

kaskade_timb = float(comp.loc[comp.loc[:,"vars"]=="kaskade","timb"])
CE_timb = float(comp.loc[comp.loc[:,"vars"]=="CE","timb"])
timb_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","timb"])
timb_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_include = float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
val_timb = float(comp.loc[comp.loc[:,"vars"]=="val","timb"])

kaskade_osb = float(comp.loc[comp.loc[:,"vars"]=="kaskade","osb"])
CE_osb = float(comp.loc[comp.loc[:,"vars"]=="CE","osb"])
osb_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","osb"])
osb_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","osb"])
osb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","osb"])
osb_include = float(comp.loc[comp.loc[:,"vars"]=="include","osb"])
val_osb = float(comp.loc[comp.loc[:,"vars"]=="val","osb"])


kaskade_fibre = float(comp.loc[comp.loc[:,"vars"]=="kaskade","fibre"])
CE_fibre = float(comp.loc[comp.loc[:,"vars"]=="CE","fibre"])
fibre_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","fibre"])
fibre_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","fibre"])
fibre_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","fibre"])
fibre_include = float(comp.loc[comp.loc[:,"vars"]=="include","fibre"])
val_fibre = float(comp.loc[comp.loc[:,"vars"]=="val","fibre"])


kaskade_verb = float(comp.loc[comp.loc[:,"vars"]=="kaskade","verb"])
CE_verb = float(comp.loc[comp.loc[:,"vars"]=="CE","verb"])
verb_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","verb"])
verb_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","verb"])
verb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","verb"])
verb_include = float(comp.loc[comp.loc[:,"vars"]=="include","verb"])
val_verb = float(comp.loc[comp.loc[:,"vars"]=="val","verb"])

kaskade_con = float(comp.loc[comp.loc[:,"vars"]=="kaskade","concrete"])
CE_con = float(comp.loc[comp.loc[:,"vars"]=="CE","concrete"])
con_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","concrete"])
con_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","concrete"])
con_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_include = float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
val_con = float(comp.loc[comp.loc[:,"vars"]=="val","concrete"])

kaskade_glas = float(comp.loc[comp.loc[:,"vars"]=="kaskade","glas"])
CE_glas = float(comp.loc[comp.loc[:,"vars"]=="CE","glas"])
glas_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","glas"])
glas_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","glas"])
glas_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_include = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
val_glas = float(comp.loc[comp.loc[:,"vars"]=="val","glas"])

kaskade_bew = float(comp.loc[comp.loc[:,"vars"]=="kaskade","bew"])
CE_bew = float(comp.loc[comp.loc[:,"vars"]=="CE","bew"])
bew_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","bew"])
bew_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","bew"])
bew_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bew"])
bew_include = float(comp.loc[comp.loc[:,"vars"]=="include","bew"])
val_bew = float(comp.loc[comp.loc[:,"vars"]=="val","bew"])

kaskade_gips = float(comp.loc[comp.loc[:,"vars"]=="kaskade","gips"])
CE_gips = float(comp.loc[comp.loc[:,"vars"]=="CE","gips"])
gips_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","gips"])
gips_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","gips"])
gips_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","gips"])
gips_include = float(comp.loc[comp.loc[:,"vars"]=="include","gips"])
val_gips = float(comp.loc[comp.loc[:,"vars"]=="val","gips"])

kaskade_wool = float(comp.loc[comp.loc[:,"vars"]=="kaskade","wool"])
CE_wool = float(comp.loc[comp.loc[:,"vars"]=="CE","wool"])
wool_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","wool"])
wool_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","wool"])
wool_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","wool"])
wool_include = float(comp.loc[comp.loc[:,"vars"]=="include","wool"])
val_wool = float(comp.loc[comp.loc[:,"vars"]=="val","wool"])

kaskade_lehm = float(comp.loc[comp.loc[:,"vars"]=="kaskade","lehm"])
CE_lehm = float(comp.loc[comp.loc[:,"vars"]=="CE","lehm"])
lehm_rueckbau = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","lehm"])
lehm_sek_share = float(comp.loc[comp.loc[:,"vars"]=="sekundaer","lehm"])
lehm_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lehm"])
lehm_include = float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])
val_lehm = float(comp.loc[comp.loc[:,"vars"]=="val","lehm"])

#Annahmen: 1. ein Teil der Baubuche kann wiederverwendet werden (= rueckbau )
#          2. Die Lebensdauer eines Bauteils wird auf 150 Jahre geschätzt (=drei lebenszyklen)
#          2. damit nicht die ganzen aufwendungen auf dem ersten Lebenszyklus lasten,wird die Primärproduktion
#             aufgeteilt: pro Lebenszyklus ein drittel PP und zwei drittel sekundärmaterial (=sekundaer)
#          3. dadurch erreicht jedoch in jedem Lebenszyklus ein drittel des wiederverwertbaren materials
#             das Ende seiner haltbarkeit und kann nicht mehr wiederverwendet werden. Dieser Teil geht
#             den nächsten schritt der Kaskade und wird stofflich genutzt. 

#LVL

lvl_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","lvl"])
lvl_en_fac = (1-lvl_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","lvl"])
lvl_sn_fac = (1-lvl_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","lvl"])
lvl_depo_fac = (1-lvl_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","lvl"])     


if kaskade_lvl == 1:
    
    lvl_wieder_fac = lvl_rueckbau
    
      
    #unterschiedliche anteile verwertung
    lvl_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","lvl"])
    lvl_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","lvl"])
    lvl_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","lvl"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    lvl_sn_fac = ((1-lvl_wieder_fac) * lvl_sn_fac) + (lvl_wieder_fac * lvl_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    lvl_en_fac = ((1-lvl_wieder_fac) * lvl_en_fac) + (lvl_wieder_fac * lvl_en_fac) + (lvl_wieder_fac * lvl_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    lvl_depo_fac = ((1- lvl_wieder_fac) * lvl_depo_fac) + (lvl_wieder_fac * lvl_depo_fac)
    

if CE_lvl == 1:
    lvl_wieder_fac = lvl_rueckbau * lvl_sek_share
    lvl_en_fac = ((1-lvl_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","lvl"]))
    lvl_sn_fac = ((1-lvl_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","lvl"]))
    lvl_depo_fac =((1-lvl_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","lvl"]))  

if val_lvl == 1:
    lvl_wieder_fac = 1
    lvl_en_fac     = 1
    lvl_sn_fac     = 1
    lvl_depo_fac   = 1
    
      

#BSH


bsh_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","bsh"])
bsh_en_fac = (1-bsh_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","bsh"])
bsh_sn_fac = (1-bsh_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","bsh"])
bsh_depo_fac = (1-bsh_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","bsh"])     

    
if kaskade_bsh == 1:    
    
    bsh_wieder_fac = bsh_rueckbau
        
    #unterschiedliche anteile verwertung
    bsh_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","bsh"])
    bsh_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","bsh"])
    bsh_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","bsh"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    bsh_sn_fac = ((1-bsh_wieder_fac) * bsh_sn_fac) + (bsh_wieder_fac * bsh_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    bsh_en_fac = ((1-bsh_wieder_fac) * bsh_en_fac) + (bsh_wieder_fac * bsh_en_fac) + (bsh_wieder_fac * bsh_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    bsh_depo_fac = ((1- bsh_wieder_fac) * bsh_depo_fac) + (bsh_wieder_fac * bsh_depo_fac)
 

if CE_bsh == 1:
    bsh_wieder_fac = bsh_rueckbau * bsh_sek_share
    bsh_en_fac = ((1-bsh_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","bsh"]))
    bsh_sn_fac = ((1-bsh_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","bsh"]))
    bsh_depo_fac =((1-bsh_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","bsh"]))

if val_bsh == 1:
    bsh_wieder_fac = 1
    bsh_en_fac     = 1
    bsh_sn_fac     = 1
    bsh_depo_fac   = 1


#timb

timb_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","timb"])
timb_en_fac = (1-timb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","timb"])
timb_sn_fac = (1-timb_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","timb"])
timb_depo_fac = (1-timb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","timb"])     

    
if kaskade_timb == 1:    
    
    timb_wieder_fac = timb_rueckbau
        
    #unterschiedliche anteile verwertung
    timb_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","timb"])
    timb_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","timb"])
    timb_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","timb"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    timb_sn_fac = ((1-timb_wieder_fac) * timb_sn_fac) + (timb_wieder_fac * timb_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    timb_en_fac = ((1-timb_wieder_fac) * timb_en_fac) + (timb_wieder_fac * timb_en_fac) + (timb_wieder_fac * timb_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    timb_depo_fac = ((1- timb_wieder_fac) * timb_depo_fac) + (timb_wieder_fac * timb_depo_fac)
 

if CE_timb == 1:
    timb_wieder_fac = timb_rueckbau * timb_sek_share
    timb_en_fac = ((1-timb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","timb"]))
    timb_sn_fac = ((1-timb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","timb"]))
    timb_depo_fac =((1-timb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","timb"]))

if val_timb == 1:
    timb_wieder_fac = 1
    timb_en_fac     = 1
    timb_sn_fac     = 1
    timb_depo_fac   = 1


#osb 

osb_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","osb"])
osb_en_fac = (1-osb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","osb"])
osb_sn_fac = (1-osb_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","osb"])
osb_depo_fac = (1-osb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","osb"])     

    
if kaskade_osb == 1:    
    
    osb_wieder_fac = osb_rueckbau
        
    #unterschiedliche anteile verwertung
    osb_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","osb"])
    osb_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","osb"])
    osb_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","osb"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    osb_sn_fac = ((1-osb_wieder_fac) * osb_sn_fac) + (osb_wieder_fac * osb_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    osb_en_fac = ((1-osb_wieder_fac) * osb_en_fac) + (osb_wieder_fac * osb_en_fac) + (osb_wieder_fac * osb_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    osb_depo_fac = ((1- osb_wieder_fac) * osb_depo_fac) + (osb_wieder_fac * osb_depo_fac)
 

if CE_osb == 1:
    osb_wieder_fac = osb_rueckbau * osb_sek_share
    osb_en_fac = ((1-osb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","osb"]))
    osb_sn_fac = ((1-osb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","osb"]))
    osb_depo_fac =((1-osb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","osb"]))

if val_osb == 1:
    osb_wieder_fac = 1
    osb_en_fac     = 1
    osb_sn_fac     = 1
    osb_depo_fac   = 1



#fibre 

fibre_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","fibre"])
fibre_en_fac = (1-fibre_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","fibre"])
fibre_sn_fac = (1-fibre_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","fibre"])
fibre_depo_fac = (1-fibre_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","fibre"])     

    
if kaskade_fibre == 1:    
    
    fibre_wieder_fac = fibre_rueckbau
        
    #unterschiedliche anteile verwertung
    fibre_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","fibre"])
    fibre_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","fibre"])
    fibre_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","fibre"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    fibre_sn_fac = ((1-fibre_wieder_fac) * fibre_sn_fac) + (fibre_wieder_fac * fibre_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    fibre_en_fac = ((1-fibre_wieder_fac) * fibre_en_fac) + (fibre_wieder_fac * fibre_en_fac) + (fibre_wieder_fac * fibre_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    fibre_depo_fac = ((1- fibre_wieder_fac) * fibre_depo_fac) + (fibre_wieder_fac * fibre_depo_fac)
 

if CE_fibre == 1:
    fibre_wieder_fac = fibre_rueckbau * fibre_sek_share
    fibre_en_fac = ((1-fibre_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","fibre"]))
    fibre_sn_fac = ((1-fibre_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","fibre"]))
    fibre_depo_fac =((1-fibre_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","fibre"]))

if val_fibre == 1:
    fibre_wieder_fac = 1
    fibre_en_fac     = 1
    fibre_sn_fac     = 1
    fibre_depo_fac   = 1



#verb

verb_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","verb"])
verb_en_fac = (1-verb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","verb"])
verb_sn_fac = (1-verb_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","verb"])
verb_depo_fac = (1-verb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","verb"])     


if kaskade_verb == 1:    
    
    verb_wieder_fac = verb_rueckbau
  
 
    #unterschiedliche anteile verwertung
    verb_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","verb"])
    verb_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","verb"])
    verb_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","verb"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    verb_sn_fac = ((1-verb_wieder_fac) * verb_sn_fac) + (verb_wieder_fac * verb_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    verb_en_fac = ((1-verb_wieder_fac) * verb_en_fac) + (verb_wieder_fac * verb_en_fac) + (verb_wieder_fac * verb_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    verb_depo_fac = ((1- verb_wieder_fac) * verb_depo_fac) + (verb_wieder_fac * verb_depo_fac)
    
     
   
if CE_verb == 1:
    verb_wieder_fac = verb_rueckbau * verb_sek_share
    verb_en_fac = ((1-verb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","verb"]))
    verb_sn_fac = ((1-verb_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","verb"]))
    verb_depo_fac =((1-verb_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","verb"]))    

if val_verb == 1:
    verb_wieder_fac = 1
    verb_en_fac     = 0
    verb_sn_fac     = 1
    verb_depo_fac   = 1


#con

con_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","concrete"])
con_en_fac = (1-con_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","concrete"])
con_sn_fac = (1-con_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","concrete"])
con_depo_fac = (1-con_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","concrete"])     


if kaskade_con == 1:    
    
    con_wieder_fac = con_rueckbau
    
    #unterschiedliche anteile verwertung
    con_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","concrete"])
    con_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","concrete"])
    con_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","concrete"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    con_sn_fac = ((1-con_wieder_fac) * con_sn_fac) + (con_wieder_fac * con_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    con_en_fac = ((1-con_wieder_fac) * con_en_fac) + (con_wieder_fac * con_en_fac) + (con_wieder_fac * con_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    con_depo_fac = ((1- con_wieder_fac) * con_depo_fac) + (con_wieder_fac * con_depo_fac)
     

        

if CE_con == 1:
    con_wieder_fac = con_rueckbau * con_sek_share
    con_en_fac = ((1-con_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","concrete"]))
    con_sn_fac = ((1-con_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","concrete"]))
    con_depo_fac =((1-con_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","concrete"]))

if val_con == 1:
    con_wieder_fac = 1
    con_en_fac     = 0
    con_sn_fac     = 1
    con_depo_fac   = 1

    
#glas

glas_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","glas"])
glas_en_fac = (1-glas_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","glas"])
glas_sn_fac = (1-glas_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","glas"])
glas_depo_fac = (1-glas_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","glas"])     



if kaskade_glas == 1:    
    
    glas_wieder_fac = glas_rueckbau
    

    #unterschiedliche anteile verwertung
    glas_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","glas"])
    glas_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","glas"])
    glas_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","glas"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    glas_sn_fac = ((1-glas_wieder_fac) * glas_sn_fac) + (glas_wieder_fac * glas_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    glas_en_fac = ((1-glas_wieder_fac) * glas_en_fac) + (glas_wieder_fac * glas_en_fac) + (glas_wieder_fac * glas_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    glas_depo_fac = ((1- glas_wieder_fac) * glas_depo_fac) + (glas_wieder_fac * glas_depo_fac)
     
    
if CE_glas == 1:
    glas_wieder_fac = glas_rueckbau * glas_sek_share
    glas_en_fac = ((1-glas_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","glas"]))
    glas_sn_fac = ((1-glas_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","glas"]))
    glas_depo_fac =((1-glas_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","glas"]))
    
if val_glas == 1:
    glas_wieder_fac = 1
    glas_en_fac     = 0
    glas_sn_fac     = 1
    glas_depo_fac   = 1
    

#bew

bew_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","bew"])
bew_en_fac = (1-bew_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","bew"])
bew_sn_fac = (1-bew_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","bew"])
bew_depo_fac = (1-bew_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","bew"])     


if kaskade_bew == 1:    
    
    bew_wieder_fac = bew_rueckbau
  
 
    #unterschiedliche anteile verwertung
    bew_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","bew"])
    bew_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","bew"])
    bew_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","bew"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    bew_sn_fac = ((1-bew_wieder_fac) * bew_sn_fac) + (bew_wieder_fac * bew_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    bew_en_fac = ((1-bew_wieder_fac) * bew_en_fac) + (bew_wieder_fac * bew_en_fac) + (bew_wieder_fac * bew_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    bew_depo_fac = ((1- bew_wieder_fac) * bew_depo_fac) + (bew_wieder_fac * bew_depo_fac)
    
     
     
if CE_bew == 1:
    bew_wieder_fac = bew_rueckbau * bew_sek_share
    bew_en_fac = ((1-bew_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","bew"]))
    bew_sn_fac = ((1-bew_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","bew"]))
    bew_depo_fac =((1-bew_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","bew"]))    

if val_bew == 1:
    bew_wieder_fac = 1
    bew_en_fac     = 0
    bew_sn_fac     = 1
    bew_depo_fac   = 1



#gips

gips_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","gips"])
gips_en_fac = (1-gips_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","gips"])
gips_sn_fac = (1-gips_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","gips"])
gips_depo_fac = (1-gips_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","gips"])     


if kaskade_gips == 1:    
    
    gips_wieder_fac = gips_rueckbau
  
 
    #unterschiedliche anteile verwertung
    gips_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","gips"])
    gips_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","gips"])
    gips_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","gips"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    gips_sn_fac = ((1-gips_wieder_fac) * gips_sn_fac) + (gips_wieder_fac * gips_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    gips_en_fac = ((1-gips_wieder_fac) * gips_en_fac) + (gips_wieder_fac * gips_en_fac) + (gips_wieder_fac * gips_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    gips_depo_fac = ((1- gips_wieder_fac) * gips_depo_fac) + (gips_wieder_fac * gips_depo_fac)
    
     
     
if CE_gips == 1:
    gips_wieder_fac = gips_rueckbau * gips_sek_share
    gips_en_fac = ((1-gips_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","gips"]))
    gips_sn_fac = ((1-gips_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","gips"]))
    gips_depo_fac =((1-gips_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","gips"]))    

if val_gips == 1:
    gips_wieder_fac = 1
    gips_en_fac     = 0
    gips_sn_fac     = 1
    gips_depo_fac   = 1



#wool

wool_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","wool"])
wool_en_fac = (1-wool_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","wool"])
wool_sn_fac = (1-wool_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","wool"])
wool_depo_fac = (1-wool_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","wool"])     


if kaskade_wool == 1:    
    
    wool_wieder_fac = wool_rueckbau
  
 
    #unterschiedliche anteile verwertung
    wool_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","wool"])
    wool_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","wool"])
    wool_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","wool"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    wool_sn_fac = ((1-wool_wieder_fac) * wool_sn_fac) + (wool_wieder_fac * wool_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    wool_en_fac = ((1-wool_wieder_fac) * wool_en_fac) + (wool_wieder_fac * wool_en_fac) + (wool_wieder_fac * wool_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    wool_depo_fac = ((1- wool_wieder_fac) * wool_depo_fac) + (wool_wieder_fac * wool_depo_fac)
    
     
     
if CE_wool == 1:
    wool_wieder_fac = wool_rueckbau * wool_sek_share
    wool_en_fac = ((1-wool_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","wool"]))
    wool_sn_fac = ((1-wool_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","wool"]))
    wool_depo_fac =((1-wool_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","wool"]))    

if val_wool == 1:
    wool_wieder_fac = 1
    wool_en_fac     = 0
    wool_sn_fac     = 1
    wool_depo_fac   = 1



lehm_wieder_fac = float(comp.loc[comp.loc[:,"vars"]=="rueckbau","lehm"])
lehm_en_fac = (1-lehm_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="energie","lehm"])
lehm_sn_fac = (1-lehm_wieder_fac)*float(comp.loc[comp.loc[:,"vars"]=="stoff","lehm"])
lehm_depo_fac = (1-lehm_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","lehm"])     


if kaskade_lehm == 1:    
    
    lehm_wieder_fac = lehm_rueckbau
  
 
    #unterschiedliche anteile verwertung
    lehm_sn_fac = float(comp.loc[comp.loc[:,"vars"]=="stoff","lehm"])
    lehm_en_fac = float(comp.loc[comp.loc[:,"vars"]=="energie","lehm"])
    lehm_depo_fac = float(comp.loc[comp.loc[:,"vars"]=="depo","lehm"])
    #kaskadierung
    #stoffliche Nutzung aus primaer nutzung + stoffliche nutzung aus sekundär nutzung
    lehm_sn_fac = ((1-lehm_wieder_fac) * lehm_sn_fac) + (lehm_wieder_fac * lehm_sn_fac) 
    #energetische Nutzung aus primaer nutzung + energetische nutzung aus sekundär nutzung + energetische nutzung nach recycling
    lehm_en_fac = ((1-lehm_wieder_fac) * lehm_en_fac) + (lehm_wieder_fac * lehm_en_fac) + (lehm_wieder_fac * lehm_sn_fac)
    #deponierung nach primärnutzung + deponierung nach sekundärnutzung
    lehm_depo_fac = ((1- lehm_wieder_fac) * lehm_depo_fac) + (lehm_wieder_fac * lehm_depo_fac)
    
     
     
if CE_lehm == 1:
    lehm_wieder_fac = lehm_rueckbau * lehm_sek_share
    lehm_en_fac = ((1-lehm_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="energie","lehm"]))
    lehm_sn_fac = ((1-lehm_wieder_fac)*  float(comp.loc[comp.loc[:,"vars"]=="stoff","lehm"]))
    lehm_depo_fac =((1-lehm_wieder_fac)* float(comp.loc[comp.loc[:,"vars"]=="depo","lehm"]))    

if val_lehm == 1:
    lehm_wieder_fac = 1
    lehm_en_fac     = 0
    lehm_sn_fac     = 1
    lehm_depo_fac   = 1
