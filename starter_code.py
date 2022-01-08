# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:33:08 2022

@author: Margee
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:43:04 2022

@author: morte
"""

import json
import pandas as pd

# =============================================================================
# import data
# =============================================================================

filepath = "C:/jobs_india/"
filename = "monster_india_latest_jobs_free_dataset.json"

# Opening JSON file
f = open(filepath + filename)

# returns JSON object as a dictionary
data = json.load(f)

# %%

listy = [1, 2, 3, 4, 5]

for each in listy:
    print(each)

# %%

address_country = []
address_locality = []
address_region = []
company = []
description = []
expires_at = []
industry = []
postal_code = []
posted_at = []
qualification = []
salary = []  # the target
salary_type = []
scraped_at = []
skill = []
street_address = []
title = []
url = []

# iterate through each element in the data list
for each in data:

    # append values to list, given each key
    address_country.append(each["address_country"])
    address_locality.append(each["address_locality"])
    address_region.append(each["address_region"])
    company.append(each["company"])
    description.append(each["description"])
    expires_at.append(each["expires_at"])
    salary.append(each["salary"])  # the target

# %%

# create df, using string header and list as rows
df = pd.DataFrame({"address_country": address_country,
                   "address_locality": address_locality,
                   "address_region": address_region,
                   "company": company,
                   "description": description,
                   "expires_at": expires_at,
                   "salary": salary})  # the target

# %%

# =============================================================================
# clean data
# =============================================================================