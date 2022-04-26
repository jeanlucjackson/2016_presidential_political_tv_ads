#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:29:42 2021

@author: heyjcm
"""

from awesome_puppies import region_fips
import pandas as pd

fips_data = region_fips()

df_fips = pd.DataFrame({"location": fips_data.index, "fips": fips_data.values})

# Give each fips a line with region
df_fips_regions = df_fips.explode("fips")


from urllib.request import urlopen
import json

with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)


import plotly.express as px

fig = px.choropleth(
    df_fips_regions,
    geojson=counties,
    locations="fips",
    color="location",
    color_discrete_sequence=[
        "#9B2226",
        "#AE2012",
        "#BB3E03",
        "#CA6702",
        "#EE9B00",
        "#E9D8A6",
        "#94D2BD",
        "#0A9396",
        "#005F73",
        "#9B2226",
        "#AE2012",
        "#BB3E03",
        "#CA6702",
    ],  # use color_discrete_sequence b/c data values are non numeric
    scope="usa",
    labels={"location": "Regions"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show(renderer="png")
