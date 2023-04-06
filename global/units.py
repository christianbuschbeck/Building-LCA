# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:35:09 2020

@author: cbuschbeck
"""


import sys

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


########################
###     Units      #####
########################
# Energy

energy_ref = client.find(olca.FlowProperty, 'Energy')
energy = client.get(olca.FlowProperty, energy_ref.id)

units_of_energy = client.get(olca.UnitGroup, energy.unit_group.id)

for unit in units_of_energy.units:
    if unit.name == "MJ":
        MJ = unit
    if unit.name == "kWh":
        kwh = unit
        

energy_factor = olca.FlowPropertyFactor()
energy_factor.conversion_factor = 1.0
energy_factor.flow_property = energy
energy_factor.reference_flow_property = True

#Items

item_ref = client.find(olca.FlowProperty, 'Number of items')
item = client.get(olca.FlowProperty, item_ref.id)

units_of_item = client.get(olca.UnitGroup, item.unit_group.id)

for unit in units_of_item.units:
    if unit.name == "Item(s)":
        items_unit = unit
        break

item_factor = olca.FlowPropertyFactor()
item_factor.conversion_factor = 1.0
item_factor.flow_property = item
item_factor.reference_flow_property = True

# Volume

vol_ref = client.find(olca.FlowProperty, 'Volume')
vol = client.get(olca.FlowProperty, vol_ref.id)

units_of_vol = client.get(olca.UnitGroup, vol.unit_group.id)

for unit in units_of_vol.units:
    if unit.name == "m3":
        m3 = unit
        break

vol_factor = olca.FlowPropertyFactor()
vol_factor.conversion_factor = 1.0
vol_factor.flow_property = vol
vol_factor.reference_flow_property = True

# Mass

mass_ref = client.find(olca.FlowProperty, 'Mass')
mass = client.get(olca.FlowProperty, mass_ref.id)

units_of_mass = client.get(olca.UnitGroup, mass.unit_group.id)

for unit in units_of_mass.units:
    if unit.name == "kg":
        kg = unit
        break

mass_factor = olca.FlowPropertyFactor()
mass_factor.conversion_factor = 1.0
mass_factor.flow_property = mass
mass_factor.reference_flow_property = True

# Transportation

transportation_ref = client.find(olca.FlowProperty, 'Goods transport (mass*distance)')
transportation = client.get(olca.FlowProperty, transportation_ref.id)

units_of_transporation = client.get(olca.UnitGroup, transportation.unit_group.id)

for unit in units_of_transporation.units:
    if unit.name == "t*km":
        transportation_unit = unit
        break

transportation_factor = olca.FlowPropertyFactor()
transportation_factor.conversion_factor = 1.0
transportation_factor.flow_property = transportation
transportation_factor.reference_flow_property = True

# Area
area_ref = client.find(olca.FlowProperty, 'Area')
area = client.get(olca.FlowProperty, area_ref.id)

units_of_area = client.get(olca.UnitGroup, area.unit_group.id)

for unit in units_of_area.units:
    if unit.name == "m2":
        m2 = unit
        break

area_factor = olca.FlowPropertyFactor()
area_factor.conversion_factor = 1.0
area_factor.flow_property = area
area_factor.reference_flow_property = True


# time
time_ref = client.find(olca.FlowProperty, 'Duration')
time = client.get(olca.FlowProperty, time_ref.id)

units_of_time = client.get(olca.UnitGroup, time.unit_group.id)

for unit in units_of_time.units:
    if unit.name == "h":
        h = unit
        break

time_factor = olca.FlowPropertyFactor()
time_factor.conversion_factor = 1.0
time_factor.flow_property = time
time_factor.reference_flow_property = True


# landuse
landuse_ref = client.find(olca.FlowProperty, 'Area*time')
landuse = client.get(olca.FlowProperty, landuse_ref.id)

units_of_landuse = client.get(olca.UnitGroup, landuse.unit_group.id)

for unit in units_of_landuse.units:
    if unit.name == "m2*a":
        m2a = unit
        break

landuse_factor = olca.FlowPropertyFactor()
landuse_factor.conversion_factor = 1.0
landuse_factor.flow_property = landuse
landuse_factor.reference_flow_property = True
