# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:22:46 2022

@author: cbuschbeck
"""
from org.openlca.core.database import ImpactMethodDao
 
# the name of the indicator / LCIA category you want to copy
INDICATOR = "Total material requirement (TMR), all materials"
# the method that contains the indicator
SOURCE_METHOD = "Material footprint"
# the method where you want to have the indicator copied to
TARGET_METHOD = "EN15804_A2_2020_3"
 
def main():
  dao = ImpactMethodDao(db)
 
  # load the targe method
  target = dao.getForName(TARGET_METHOD)
  if len(target) == 0:
    log.error("Could not find method {}", TARGET_METHOD)
    return
  target = target[0]
 
  # check that the indicator is not already there
  for i in target.impactCategories:
    if i.name == INDICATOR:
      log.error("The indicator {} already exists in {}",
                INDICATOR, TARGET_METHOD)
      return
 
  # load the source method
  source = dao.getForName(SOURCE_METHOD)
  if len(source) == 0:
    log.error("Could not find method {}", SOURCE_METHOD)
    return
  source = source[0]
 
  # find the indicator
  indicator = None
  for i in source.impactCategories:
    if i.name == INDICATOR:
      indicator = i
      break
  if indicator is None:
    log.error("Could not find indicator {} in method {}",
              INDICATOR, SOURCE_METHOD)
    return
 
  # finally, copy the indicator
  log.info("Copy indicator {} from {} to {}",
           INDICATOR, SOURCE_METHOD, TARGET_METHOD)
  cloned = indicator.clone()
  target.impactCategories.add(cloned)
  dao.update(target)
  log.info("done")
 
if __name__ == "__main__":
  main()