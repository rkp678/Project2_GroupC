import json
import pandas as pd
# %%

# Create File Path
filepath = "C:/Users/piercerachel/Desktop/git/Project2_GroupC/"
filename = "monster_india_latest_jobs_free_dataset.json"

# Opening JSON file
f = open(filepath + filename)

# returns JSON object as a dictionary
data = json.load(f)
# %%

# Create data list
address_country = []
address_locality = []
address_region = []
company = []
description = []
industry = []
postal_code = []
posted_at = []
salary = []  # the target
salary_type = []
skills = []
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
    industry.append(each["industry"])
    postal_code.append(each["postal_code"])
    posted_at.append(each["posted_at"])
    salary.append(each["salary"])
    salary_type.append(each["salary_type"])
    skills.append(each["skills"]) 
    title.append(each["title"])
    url.append(each["url"])
# %%

# create df, using string header and list as rows
df = pd.DataFrame({"address_country": address_country,
                   "address_locality": address_locality,
                   "address_region": address_region,
                   "company": company,
                   "description": description,
                   "industry": industry,
                   "postal_code": postal_code,
                   "posted_at": posted_at,
                   "salary": salary,
                   "salary_type": salary_type,
                   "skills": skills,
                   "title": title,
                   "url": url,
                  })

# %%

# Preview dataframe
df.head()

# %%

# Clean data, drop unnecessary columns
df.drop(['address_country', 'address_locality', 'address_region', 'postal_code', 'salary_type', 'url'], axis=1, inplace=True)

# %%

df.head()

# %%

# Drop any salaries that are Not disclosed
df = df[df["salary"]!="Not disclosed"]
df.head()

# %%

# Check if there are any NAs/nulls
df.isnull().sum()