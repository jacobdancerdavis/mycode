#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

nonanimals= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
choice = input("Choose a farm!\n")
 
for farm in farms:
    if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in nonanimals:
                    print(ag_item)
