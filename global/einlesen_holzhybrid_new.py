# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:19:19 2020

@author: cbuschbeck
"""

def einlesen_holzhybrid():

    import pandas as pd
    import numpy as np
    
    data = {'lvl'     :["m³"  , 0    , 0     , 0     ,0     , 0   ,400],
            'lvl_rb'  :["-"  , 0    ,0    , 0   , 0    , 0   , 0],
            'bsh'     :["m³"  , 0    ,0    , 0   , 0    , 0   , 200],
            'bsh_rb'  :["-"  , 0    ,0    , 0   , 0    , 0   , 0],
            'concrete'   :["m³"  , 0    ,0    , 0   , 0    , 0   , 0],
            'concrete_rb':["-"  , 0    ,0    , 0   , 0    , 0   , 0],
            'verb'    :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],
            'verb_rb' :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],
            'bew'     :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],
            'bew_rb'     :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],
            'glas'     :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],
            'glas_rb'     :['kg'  , 0   , 0   , 0   ,0    ,0 ,0],

            
            'stuetze': ['lfm', 0, 0 , 0 , 0 , 0, 0],
            'stuetze_rb': ['lfm', 0, 0 , 0 , 0 , 0, 0],
            'decke'  : ['m2' , 0  , 0   , 0   , 0   , 0  , 0],
            'decke_rb'  : ['m2' , 0  , 0   , 0   , 0   , 0  , 0],
            'wand'   : ['m2' , 0   , 0    , 0    , 0    , 0   , 0],
            'wand_rb'   : ['m2' , 0   , 0    , 0    , 0    , 0   , 0],
            'huelle'   : ['m2' , 0   , 0    , 0    , 0    , 0   , 0],
            
            "phase"  : [""   ,"gebaeude_in"       , "austausch"       , "umbau_out"       , "umbau_in"      , "gebaeude_out"       , "huelle"]
            }
    
    BIM = pd.DataFrame(data, columns = ['lvl','lvl_rb',"bsh","bsh_rb",'concrete','concrete_rb','verb','verb_rb','bew','bew_rb','glas','glas_rb',"stuetze","stuetze_rb","decke","decke_rb","wand","wand_rb","phase"])  

   
    gebaeude_in_wd = "C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/gebaeude_in"
    umbau_in_wd = "C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/umbau_in"
    umbau_out_wd = "C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/umbau_out"
    
    phase_wd = [gebaeude_in_wd,umbau_in_wd,umbau_out_wd]
        
    phasen = ["gebaeude_in" , "umbau_in","umbau_out"  ]    
    for i in range(0,3):
        
        ph_wd = phase_wd[i]
        phase_idx = BIM.index[BIM['phase'] == phasen[i]].tolist()[0]
        
                
        ### Components ####
        
        #Skelett#
        
        skelett = pd.read_csv(ph_wd+'/Skelettbauliste.csv',sep= ',',header=[0],engine = "python")
        
        skelett_lvl    = skelett[skelett.loc[:,"Material"]== "BauBuche"]
        skelett_lvl_rb = skelett_lvl[skelett_lvl.loc[:,"rueckbaubarkeit"]== "Ja"]
                
        skelett_bsh   = skelett[skelett.loc[:,"Material"]== "BSH"]
        skelett_bsh_rb = skelett_bsh[skelett_bsh.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        skelett_beton = skelett[skelett.loc[:,"Material"]== "Beton"]
        skelett_beton_rb = skelett_beton[skelett_beton.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        
        
        skelett_lvl_vol      =[]
        skelett_lvl_vol_rb   =[]
        skelett_bsh_vol      =[]
        skelett_bsh_vol_rb   =[]
        skelett_beton_vol    =[]
        skelett_beton_vol_rb =[]
        skelett_bew_kg       =[]
        skelett_bew_kg_rb    =[]

        
        for i in skelett_lvl.index:
            skelett_lvl_vol.append(float(skelett_lvl.loc[i,"Anzahl"]) * float(skelett_lvl.loc[i,"Volumen"]))
        for i in skelett_lvl_rb.index:            
            skelett_lvl_vol_rb.append(float(skelett_lvl_rb.loc[i,"Anzahl"]) * float(skelett_lvl_rb.loc[i,"Volumen"]))
            
        for i in skelett_bsh.index:
            skelett_bsh_vol.append(float(skelett_bsh.loc[i,"Anzahl"]) * float(skelett_bsh.loc[i,"Volumen"]))
        for i in skelett_bsh_rb.index:
            skelett_bsh_vol_rb.append(float(skelett_bsh_rb.loc[i,"Anzahl"]) * float(skelett_bsh_rb.loc[i,"Volumen"]))
        
        for i in skelett_beton.index:
            skelett_beton_vol.append(float(skelett_beton.loc[i,"Anzahl"]) * float(skelett_beton.loc[i,"Volumen"]))
            skelett_bew_kg.append(float(skelett_beton.loc[i,"Anzahl"]) * float(skelett_beton.loc[i,"Gewicht bew"]))
    
        for i in skelett_beton_rb.index:
            skelett_beton_vol_rb.append(float(skelett_beton_rb.loc[i,"Anzahl"]) * float(skelett_beton_rb.loc[i,"Volumen"]))
            skelett_bew_kg_rb.append(float(skelett_beton_rb.loc[i,"Anzahl"]) * float(skelett_beton_rb.loc[i,"Gewicht bew"]))
    
        
        BIM.iloc[phase_idx]["lvl"]      = BIM.iloc[phase_idx]["lvl"]   + sum(skelett_lvl_vol)
        BIM.iloc[phase_idx]["bsh"]      = BIM.iloc[phase_idx]["bsh"]   + sum(skelett_bsh_vol)
        BIM.iloc[phase_idx]["concrete"] = BIM.iloc[phase_idx]["concrete"] + sum(skelett_beton_vol)
        BIM.iloc[phase_idx]["bew"]      = BIM.iloc[phase_idx]["bew"]   + sum(skelett_bew_kg)
        
        BIM.iloc[phase_idx]["lvl_rb"]      = BIM.iloc[phase_idx]["lvl_rb"]   + sum(skelett_lvl_vol_rb)
        BIM.iloc[phase_idx]["bsh_rb"]      = BIM.iloc[phase_idx]["bsh_rb"]   + sum(skelett_bsh_vol_rb)
        BIM.iloc[phase_idx]["concrete_rb"] = BIM.iloc[phase_idx]["concrete_rb"] + sum(skelett_beton_vol_rb)
        BIM.iloc[phase_idx]["bew_rb"]      = BIM.iloc[phase_idx]["bew_rb"]   + sum(skelett_bew_kg_rb)
                
        #Tragwerk#
            
        tragwerk = pd.read_csv(ph_wd+'/Tragwerksstuetzenliste.csv',sep= ',',header=[0],engine = "python")
        
        tragwerk_lvl    = tragwerk[tragwerk.loc[:,"Material"]== "BauBuche"]
        tragwerk_lvl_rb = tragwerk_lvl[tragwerk_lvl.loc[:,"rueckbaubarkeit"]== "Ja"]
                
        tragwerk_bsh   = tragwerk[tragwerk.loc[:,"Material"]== "BSH"]
        tragwerk_bsh_rb = tragwerk_bsh[tragwerk_bsh.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        tragwerk_beton = tragwerk[tragwerk.loc[:,"Material"]== "Beton"]
        tragwerk_beton_rb = tragwerk_beton[tragwerk_beton.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        
        tragwerk_lvl_vol      =[]
        tragwerk_lvl_vol_rb   =[]
        tragwerk_bsh_vol      =[]
        tragwerk_bsh_vol_rb   =[]
        tragwerk_beton_vol    =[]
        tragwerk_beton_vol_rb =[]
        tragwerk_bew_kg       =[]
        tragwerk_bew_kg_rb    =[]

        
        for i in tragwerk_lvl.index:
            tragwerk_lvl_vol.append(float(tragwerk_lvl.loc[i,"Anzahl"]) * float(tragwerk_lvl.loc[i,"Volumen"]))
        for i in tragwerk_lvl_rb.index:            
            tragwerk_lvl_vol_rb.append(float(tragwerk_lvl_rb.loc[i,"Anzahl"]) * float(tragwerk_lvl_rb.loc[i,"Volumen"]))
            
        for i in tragwerk_bsh.index:
            tragwerk_bsh_vol.append(float(tragwerk_bsh.loc[i,"Anzahl"]) * float(tragwerk_bsh.loc[i,"Volumen"]))
        for i in tragwerk_bsh_rb.index:
            tragwerk_bsh_vol_rb.append(float(tragwerk_bsh_rb.loc[i,"Anzahl"]) * float(tragwerk_bsh_rb.loc[i,"Volumen"]))
        
        for i in tragwerk_beton.index:
            tragwerk_beton_vol.append(float(tragwerk_beton.loc[i,"Anzahl"]) * float(tragwerk_beton.loc[i,"Volumen"]))
            tragwerk_bew_kg.append(float(tragwerk_beton.loc[i,"Anzahl"]) * float(tragwerk_beton.loc[i,"Gewicht bew"]))
    
        for i in tragwerk_beton_rb.index:
            tragwerk_beton_vol_rb.append(float(tragwerk_beton_rb.loc[i,"Anzahl"]) * float(tragwerk_beton_rb.loc[i,"Volumen"]))
            tragwerk_bew_kg_rb.append(float(tragwerk_beton_rb.loc[i,"Anzahl"]) * float(tragwerk_beton_rb.loc[i,"Gewicht bew"]))
    
        
        BIM.iloc[phase_idx]["lvl"]      = BIM.iloc[phase_idx]["lvl"]   + sum(tragwerk_lvl_vol)
        BIM.iloc[phase_idx]["bsh"]      = BIM.iloc[phase_idx]["bsh"]   + sum(tragwerk_bsh_vol)
        BIM.iloc[phase_idx]["concrete"] = BIM.iloc[phase_idx]["concrete"] + sum(tragwerk_beton_vol)
        BIM.iloc[phase_idx]["bew"]      = BIM.iloc[phase_idx]["bew"]   + sum(tragwerk_bew_kg)
        
        BIM.iloc[phase_idx]["lvl_rb"]      = BIM.iloc[phase_idx]["lvl_rb"]   + sum(tragwerk_lvl_vol_rb)
        BIM.iloc[phase_idx]["bsh_rb"]      = BIM.iloc[phase_idx]["bsh_rb"]   + sum(tragwerk_bsh_vol_rb)
        BIM.iloc[phase_idx]["concrete_rb"] = BIM.iloc[phase_idx]["concrete_rb"] + sum(tragwerk_beton_vol_rb)
        BIM.iloc[phase_idx]["bew_rb"]      = BIM.iloc[phase_idx]["bew_rb"]   + sum(tragwerk_bew_kg_rb)
   
        
        #Decke
        decke = pd.read_csv(ph_wd+'/Geschossdeckenliste.csv',sep= ',',header=[0],engine = "python")

        decke_lvl    = decke[decke.loc[:,"Material"]== "BauBuche"]
        decke_lvl_rb = decke_lvl[decke_lvl.loc[:,"rueckbaubarkeit"]== "Ja"]
                
        decke_bsh   = decke[decke.loc[:,"Material"]== "BSH"]
        decke_bsh_rb = decke_bsh[decke_bsh.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        decke_beton = decke[decke.loc[:,"Material"]== "Beton"]
        decke_beton_rb = decke_beton[decke_beton.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        
        decke_lvl_vol      =[]
        decke_lvl_vol_rb   =[]
        decke_bsh_vol      =[]
        decke_bsh_vol_rb   =[]
        decke_beton_vol    =[]
        decke_beton_vol_rb =[]
        decke_bew_kg       =[]
        decke_bew_kg_rb    =[]

        
        for i in decke_lvl.index:
            decke_lvl_vol.append(float(decke_lvl.loc[i,"Anzahl"]) * float(decke_lvl.loc[i,"Volumen"]))
        for i in decke_lvl_rb.index:            
            decke_lvl_vol_rb.append(float(decke_lvl_rb.loc[i,"Anzahl"]) * float(decke_lvl_rb.loc[i,"Volumen"]))
            
        for i in decke_bsh.index:
            decke_bsh_vol.append(float(decke_bsh.loc[i,"Anzahl"]) * float(decke_bsh.loc[i,"Volumen"]))
        for i in decke_bsh_rb.index:
            decke_bsh_vol_rb.append(float(decke_bsh_rb.loc[i,"Anzahl"]) * float(decke_bsh_rb.loc[i,"Volumen"]))
        
        for i in decke_beton.index:
            decke_beton_vol.append(float(decke_beton.loc[i,"Anzahl"]) * float(decke_beton.loc[i,"Volumen"]))
            decke_bew_kg.append(float(decke_beton.loc[i,"Anzahl"]) * float(decke_beton.loc[i,"Gewicht bew"]))
    
        for i in decke_beton_rb.index:
            decke_beton_vol_rb.append(float(decke_beton_rb.loc[i,"Anzahl"]) * float(decke_beton_rb.loc[i,"Volumen"]))
            decke_bew_kg_rb.append(float(decke_beton_rb.loc[i,"Anzahl"]) * float(decke_beton_rb.loc[i,"Gewicht bew"]))
    
        
        BIM.iloc[phase_idx]["lvl"]      = BIM.iloc[phase_idx]["lvl"]   + sum(decke_lvl_vol)
        BIM.iloc[phase_idx]["bsh"]      = BIM.iloc[phase_idx]["bsh"]   + sum(decke_bsh_vol)
        BIM.iloc[phase_idx]["concrete"] = BIM.iloc[phase_idx]["concrete"] + sum(decke_beton_vol)
        BIM.iloc[phase_idx]["bew"]      = BIM.iloc[phase_idx]["bew"]   + sum(decke_bew_kg)
        
        BIM.iloc[phase_idx]["lvl_rb"]      = BIM.iloc[phase_idx]["lvl_rb"]   + sum(decke_lvl_vol_rb)
        BIM.iloc[phase_idx]["bsh_rb"]      = BIM.iloc[phase_idx]["bsh_rb"]   + sum(decke_bsh_vol_rb)
        BIM.iloc[phase_idx]["concrete_rb"] = BIM.iloc[phase_idx]["concrete_rb"] + sum(decke_beton_vol_rb)
        BIM.iloc[phase_idx]["bew_rb"]      = BIM.iloc[phase_idx]["bew_rb"]   + sum(decke_bew_kg_rb)
     
     
        #Wände
        wand = pd.read_csv(ph_wd+'/Wandliste.csv',sep= ',',header=[0],engine = "python")
        
        
        wand_lvl    = wand[wand.loc[:,"Material"]== "BauBuche"]
        wand_lvl_rb = wand_lvl[wand_lvl.loc[:,"rueckbaubarkeit"]== "Ja"]
                
        wand_bsh   = wand[wand.loc[:,"Material"]== "BSH"]
        wand_bsh_rb = wand_bsh[wand_bsh.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        wand_beton = wand[wand.loc[:,"Material"]== "Beton"]
        wand_beton_rb = wand_beton[wand_beton.loc[:,"rueckbaubarkeit"]== "Ja"]
        
        
        wand_lvl_vol      =[]
        wand_lvl_vol_rb   =[]
        wand_bsh_vol      =[]
        wand_bsh_vol_rb   =[]
        wand_beton_vol    =[]
        wand_beton_vol_rb =[]
        wand_bew_kg       =[]
        wand_bew_kg_rb    =[]

        
        for i in wand_lvl.index:
            wand_lvl_vol.append(float(wand_lvl.loc[i,"Anzahl"]) * float(wand_lvl.loc[i,"Volumen"]))
        for i in wand_lvl_rb.index:            
            wand_lvl_vol_rb.append(float(wand_lvl_rb.loc[i,"Anzahl"]) * float(wand_lvl_rb.loc[i,"Volumen"]))
            
        for i in wand_bsh.index:
            wand_bsh_vol.append(float(wand_bsh.loc[i,"Anzahl"]) * float(wand_bsh.loc[i,"Volumen"]))
        for i in wand_bsh_rb.index:
            wand_bsh_vol_rb.append(float(wand_bsh_rb.loc[i,"Anzahl"]) * float(wand_bsh_rb.loc[i,"Volumen"]))
        
        for i in wand_beton.index:
            wand_beton_vol.append(float(wand_beton.loc[i,"Anzahl"]) * float(wand_beton.loc[i,"Volumen"]))
            wand_bew_kg.append(float(wand_beton.loc[i,"Anzahl"]) * float(wand_beton.loc[i,"Gewicht bew"]))
    
        for i in wand_beton_rb.index:
            wand_beton_vol_rb.append(float(wand_beton_rb.loc[i,"Anzahl"]) * float(wand_beton_rb.loc[i,"Volumen"]))
            wand_bew_kg_rb.append(float(wand_beton_rb.loc[i,"Anzahl"]) * float(wand_beton_rb.loc[i,"Gewicht bew"]))
    
        
        BIM.iloc[phase_idx]["lvl"]      = BIM.iloc[phase_idx]["lvl"]   + sum(wand_lvl_vol)
        BIM.iloc[phase_idx]["bsh"]      = BIM.iloc[phase_idx]["bsh"]   + sum(wand_bsh_vol)
        BIM.iloc[phase_idx]["concrete"] = BIM.iloc[phase_idx]["concrete"] + sum(wand_beton_vol)
        BIM.iloc[phase_idx]["bew"]      = BIM.iloc[phase_idx]["bew"]   + sum(wand_bew_kg)
        
        BIM.iloc[phase_idx]["lvl_rb"]      = BIM.iloc[phase_idx]["lvl_rb"]   + sum(wand_lvl_vol_rb)
        BIM.iloc[phase_idx]["bsh_rb"]      = BIM.iloc[phase_idx]["bsh_rb"]   + sum(wand_bsh_vol_rb)
        BIM.iloc[phase_idx]["concrete_rb"] = BIM.iloc[phase_idx]["concrete_rb"] + sum(wand_beton_vol_rb)
        BIM.iloc[phase_idx]["bew_rb"]      = BIM.iloc[phase_idx]["bew_rb"]   + sum(wand_bew_kg_rb)

       
        
        #Verbindungen
        verb = pd.read_csv(ph_wd+'/Tragwerksverbindungen.csv',sep= ',',header=[0],engine = "python")

        verb_stahl = verb[verb.loc[:,"Material"]== "Stahl"]
        verb_stahl_rb = verb_stahl[verb_stahl.loc[:,"rueckbaubarkeit"]== "Ja"]       
        
        verb_stahl_kg    =[]
        verb_stahl_kg_rb =[]
        
        for i in verb_stahl.index:
            verb_stahl_kg.append(float(verb_stahl.loc[i,"Anzahl"]) * float(verb_stahl.loc[i,"Gewicht"]))
        for i in verb_stahl_rb.index:
            verb_stahl_kg_rb.append(float(verb_stahl_rb.loc[i,"Anzahl"]) * float(verb_stahl_rb.loc[i,"Gewicht"]))

        BIM.iloc[phase_idx]["verb"]  = BIM.iloc[phase_idx]["verb"] + sum(verb_stahl_kg)

        BIM.iloc[phase_idx]["verb_rb"]  = BIM.iloc[phase_idx]["verb_rb"] + sum(verb_stahl_kg_rb)
        
        
        ### Services ####
        
        BIM.iloc[phase_idx]["stuetze"] = np.nansum(tragwerk.loc[:,"Laenge"]*tragwerk.loc[:,"Anzahl"])
        BIM.iloc[phase_idx]["decke"]   = np.nansum(decke.loc[:,"Flaeche"]*decke.loc[:,"Anzahl"])
        BIM.iloc[phase_idx]["wand"]    = np.nansum(wand.loc[:,"Flaeche"]*wand.loc[:,"Anzahl"])
        
        tragwerk_rb = tragwerk[tragwerk.loc[:,"rueckbaubarkeit"]== "Ja"]
        decke_rb = decke[decke.loc[:,"rueckbaubarkeit"]== "Ja"]
        wand_rb = wand[wand.loc[:,"rueckbaubarkeit"]== "Ja"]

        BIM.iloc[phase_idx]["stuetze_rb"] = np.nansum(tragwerk_rb.loc[:,"Laenge"]*tragwerk_rb.loc[:,"Anzahl"])
        BIM.iloc[phase_idx]["decke_rb"]   = np.nansum(decke_rb.loc[:,"Flaeche"]*decke_rb.loc[:,"Anzahl"])
        BIM.iloc[phase_idx]["wand_rb"]    = np.nansum(wand_rb.loc[:,"Flaeche"]*wand_rb.loc[:,"Anzahl"])

    
        
    geb_in = BIM.index[BIM['phase'] == "gebaeude_in"].tolist()[0]
    umbau_out = BIM.index[BIM['phase'] == "umbau_out"].tolist()[0]
    umbau_in = BIM.index[BIM['phase'] == "umbau_in"].tolist()[0]
    geb_out = BIM.index[BIM['phase'] == "gebaeude_out"].tolist()[0]
       
    BIM.iloc[geb_out]["lvl"]      = BIM.iloc[geb_in]["lvl"] - BIM.iloc[umbau_out]["lvl"]  + BIM.iloc[umbau_in]["lvl"]
    BIM.iloc[geb_out]["lvl_rb"]      = BIM.iloc[geb_in]["lvl_rb"] - BIM.iloc[umbau_out]["lvl_rb"]  + BIM.iloc[umbau_in]["lvl_rb"]
    
    BIM.iloc[geb_out]["bsh"]      = BIM.iloc[geb_in]["bsh"] - BIM.iloc[umbau_out]["bsh"]  + BIM.iloc[umbau_in]["bsh"]
    BIM.iloc[geb_out]["bsh_rb"]      = BIM.iloc[geb_in]["bsh_rb"] - BIM.iloc[umbau_out]["bsh_rb"]  + BIM.iloc[umbau_in]["bsh_rb"]
    
    BIM.iloc[geb_out]["verb"]     = BIM.iloc[geb_in]["verb"] - BIM.iloc[umbau_out]["verb"]  + BIM.iloc[umbau_in]["verb"]
    BIM.iloc[geb_out]["verb_rb"]     = BIM.iloc[geb_in]["verb_rb"] - BIM.iloc[umbau_out]["verb_rb"]  + BIM.iloc[umbau_in]["verb_rb"]
    
    BIM.iloc[geb_out]["concrete"] = BIM.iloc[geb_in]["concrete"] - BIM.iloc[umbau_out]["concrete"]  + BIM.iloc[umbau_in]["concrete"]
    BIM.iloc[geb_out]["concrete_rb"] = BIM.iloc[geb_in]["concrete_rb"] - BIM.iloc[umbau_out]["concrete_rb"]  + BIM.iloc[umbau_in]["concrete_rb"]
    
    BIM.iloc[geb_out]["bew"]      = BIM.iloc[geb_in]["bew"] - BIM.iloc[umbau_out]["bew"]  + BIM.iloc[umbau_in]["bew"]
    BIM.iloc[geb_out]["bew_rb"]      = BIM.iloc[geb_in]["bew_rb"] - BIM.iloc[umbau_out]["bew_rb"]  + BIM.iloc[umbau_in]["bew_rb"]
    
    BIM.iloc[geb_out]["stuetze"]  = BIM.iloc[geb_in]["stuetze"] - BIM.iloc[umbau_out]["stuetze"]  + BIM.iloc[umbau_in]["stuetze"]
    BIM.iloc[geb_out]["stuetze_rb"]  = BIM.iloc[geb_in]["stuetze_rb"] - BIM.iloc[umbau_out]["stuetze_rb"]  + BIM.iloc[umbau_in]["stuetze_rb"]
    
    BIM.iloc[geb_out]["wand"]     = BIM.iloc[geb_in]["wand"] - BIM.iloc[umbau_out]["wand"]  + BIM.iloc[umbau_in]["wand"]
    BIM.iloc[geb_out]["wand_rb"]     = BIM.iloc[geb_in]["wand_rb"] - BIM.iloc[umbau_out]["wand_rb"]  + BIM.iloc[umbau_in]["wand_rb"]
    
    BIM.iloc[geb_out]["decke"]    = BIM.iloc[geb_in]["decke"] - BIM.iloc[umbau_out]["decke"]  + BIM.iloc[umbau_in]["decke"]
    BIM.iloc[geb_out]["decke_rb"]    = BIM.iloc[geb_in]["decke_rb"] - BIM.iloc[umbau_out]["decke_rb"]  + BIM.iloc[umbau_in]["decke_rb"]
    
    
    
    BIM.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/BIM_HH.csv",index=False,sep=";")

    return(BIM)



