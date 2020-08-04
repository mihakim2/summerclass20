#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import required libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import os
from datetime import datetime
# set environment variable needed for basemap
os.environ["PROJ_LIB"] = r'/opt/conda/pkgs/proj4-5.2.0-he1b5a44_1006/share/proj/' 
import numpy as np
import mpl_toolkits
import pandas as pd
# import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from shapely.geometry import Point
import mapclassify
import matplotlib.pyplot as plt
from matplotlib import style
import csv
import matplotlib.patches as patches
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs # import projection
import cartopy.feature as cf # import features
import json
import folium
import mplleaflet
# import fiona
import pprint
import IPython
from shapely.geometry import Polygon



# In[2]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# ### Managing Eviction Lab Data

# In[3]:


al = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/AL/counties.geojson'))
ak = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/AK/counties.geojson'))
az = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/AZ/counties.geojson'))
ar = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/AR/counties.geojson'))
ca = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/CA/counties.geojson'))
co = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/CO/counties.geojson'))
ct = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/CT/counties.geojson'))
de = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/DE/counties.geojson'))
fl = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/FL/counties.geojson'))
ga = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/GA/counties.geojson'))
hi = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/HI/counties.geojson'))
ida = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/ID/counties.geojson'))
il = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/IL/counties.geojson'))
inn = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/IN/counties.geojson'))
ia = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/IA/counties.geojson'))
ks = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/KS/counties.geojson'))
ky = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/KY/counties.geojson'))
la = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/LA/counties.geojson'))
me = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/ME/counties.geojson'))
md = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MD/counties.geojson'))
ma = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MA/counties.geojson'))
mi = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MI/counties.geojson'))
mn = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MN/counties.geojson'))
ms = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MS/counties.geojson'))
mo = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MO/counties.geojson'))
mt = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/MT/counties.geojson'))
ne = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NE/counties.geojson'))
nv = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NV/counties.geojson'))
nh = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NH/counties.geojson'))
nj = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NJ/counties.geojson'))
nm = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NM/counties.geojson'))
ny = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NY/counties.geojson'))
nc = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/NC/counties.geojson'))
nd = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/ND/counties.geojson'))
oh = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/OH/counties.geojson'))
ok = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/OK/counties.geojson'))
orr = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/OR/counties.geojson'))
pa = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/PA/counties.geojson'))
ri = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/RI/counties.geojson'))
sc = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/SC/counties.geojson'))
sd = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/SD/counties.geojson'))
tn = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/TN/counties.geojson'))
tx = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/TX/counties.geojson'))
ut = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/UT/counties.geojson'))
vt = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/VT/counties.geojson'))
va = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/VA/counties.geojson'))
wa = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/WA/counties.geojson'))
wv = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/WV/counties.geojson'))
wi = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/WI/counties.geojson'))
wy = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/WY/counties.geojson'))
dc = gpd.read_file(os.path.join('https://eviction-lab-data-downloads.s3.amazonaws.com/DC/counties.geojson'))


# In[4]:


us_county_data = [al,
                  ak, 
az, 
ar, 
ca, 
co, 
ct, 
de, 
fl, 
ga, 
hi, 
ida, 
il, 
inn, 
ia, 
ks, 
ky, 
la, 
me, 
md, 
ma, 
mi, 
mn, 
ms, 
mo, 
mt, 
ne, 
nv, 
nh, 
nj, 
nm, 
ny, 
nc, 
nd, 
oh, 
ok, 
orr, 
pa, 
ri, 
sc, 
sd, 
tn, 
tx, 
ut, 
vt, 
va, 
wa, 
wv, 
wi, 
wy, 
dc, 
                 ]
    


# In[5]:


result = pd.concat(us_county_data)


# In[6]:


result['GEOID'] = result['GEOID'].apply(lambda x: '{0:0>5}'.format(x))


# In[7]:


select16 = result.loc[:,[ 
'GEOID',
"p-16", 
"pr-16", 
"mhi-16", 
"rb-16", 
"pw-16", 
"paa-16", 
"ph-16", 
"pai-16", 
"pa-16", 
"pnp-16", 
"pm-16", 
"po-16", 
"er-16", 
"efr-16",]]
select16['Year'] = int(2016)
select16= select16.rename(columns={"GEOID": "FIPS",
                               "p-16": "Population",
                               "pr-16": "PovertyRate",
                               "mhi-16": "MedianHHIncome",
                               "rb-16" : "RentBurden",
                               "pw-16" : "%White",
                               "paa-16": "%AfricanAmerican",
                               "ph-16": "%Hispanic",
                               "pai-16" : "%AmerIndian",
                               "pa-16": "%Asians",
                               "pnp-16": "%NAtiveH&PI",
                               "pm-16" : "%Multiple",
                               "po-16": "%Others",
                               "er-16": "EvictionRate",
                               "efr-16": "EvicFilingRate",
                            })


# In[8]:


eviction_lab_data = select16


# In[9]:


eviction_lab_data = eviction_lab_data.fillna(0)
eviction_lab_data['Population']=eviction_lab_data['Population'].astype(np.int64)
eviction_lab_data['MedianHHIncome']=eviction_lab_data['MedianHHIncome'].astype(np.int64)
eviction_lab_data.dtypes


# In[10]:


eviction_lab_data.head()


# ### Managing Covid Dataset

# In[31]:


covid_cases = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv')
covid_cases.shape


# In[32]:


covid_cases.dtypes


# In[33]:


#convert fips to integer type
covid_cases = covid_cases.fillna(0)
covid_cases['fips'] = covid_cases['fips'].astype(int)
#covid_cases['deaths'] = covid_cases['deaths'].astype(np.int64)
#covid_cases['date']=pd.to_datetime(covid_cases['date'])
#covid_cases.rename(columns={"county": "NAME", "state": "STATE_NAME", "fips": "FIPS"})


# In[34]:


#covid_cases['deaths']=covid_cases['deaths'].astype(int)
#covid_cases['cases']=covid_cases['cases'].astype(int)
covid_cases= covid_cases.rename(columns={"fips": "FIPS"})


# In[35]:


covid_cases.head()


# In[36]:


covid_cases['deaths'].sum()


# In[37]:


#total_covid['FIPS'] = total_covid['FIPS'].apply(lambda x: '{0:0>5}'.format(x))
covid_cases['FIPS'] = covid_cases['FIPS'].apply(lambda x: '{0:0>5}'.format(x))
covid_cases = covid_cases.fillna(0)
covid_cases['FIPS'] = covid_cases['FIPS'].astype(np.int64)
covid_cases['cases'].sum()


# In[42]:


covid_cases[covid_cases['state']=='Alabama']


# # Plotting

# In[49]:


import branca
import requests

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{url}/us_counties_20m_topo.json'

covid_cases_fol= covid_cases
df = covid_cases_fol.set_index('FIPS')

colorscale = branca.colormap.linear.PuRd_04.to_step(10).scale(5, 10000)
colorscale.caption = 'Cases Due to Covid-19'

cases_series = df['cases']


def style_function(feature):
    covid = cases_series.get(int(feature['id'][-5:]), None)
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': '#fdf7f6' if covid is None else colorscale(covid)
    }


m = folium.Map(
    location=[48, -102], zoom_start=3,
    tiles='cartodbpositron',
)

m.fit_bounds([[51.027594, -100.195910],[24.093070, -99.048598]])
folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',
    style_function=style_function
).add_to(m)
colorscale.add_to(m)
m


# In[57]:


import branca
import requests

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{url}/us_counties_20m_topo.json'

covid_cases_fol= covid_cases
df = covid_cases_fol.set_index('FIPS')

colorscale = branca.colormap.linear.Reds_05.to_step(10).scale(5, 100)
colorscale.caption = 'Deaths Due to Covid-19'

cases_series = df['deaths']


def style_function(feature):
    covid = cases_series.get(int(feature['id'][-5:]), None)
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': '#fdf7f6' if covid is None else colorscale(covid)
    }


m = folium.Map(
    location=[48, -102], zoom_start=3,
    tiles='cartodbpositron',
)
m.fit_bounds([[51.027594, -100.195910],[24.093070, -99.048598]])
folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m', name='choropleth',
    style_function=style_function
).add_to(m)
colorscale.add_to(m)
folium.LayerControl().add_to(m)
m


# In[71]:


import branca
from datetime import datetime, timedelta

# set  date one day before and load county level data

today = datetime.strftime(datetime.now() - timedelta(2),'%m-%d-%Y')
weburl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/'+today+'.csv'
covid_county = pd.read_csv(weburl)
covid_county = covid_county.dropna(subset = ['Lat', 'Long_'])

# Make a data frame with dots to show on the map
data = covid_county

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{url}/us_counties_20m_topo.json'

df = covid_cases.set_index('FIPS')

#colorscale = branca.colormap.linear.Reds_05.to_step(10).scale(5, 100)

#colorscale.caption = 'Deaths Due to Covid-19'

cases_series = df['deaths']
def style_function(feature):
    covid = cases_series.get(int(feature['id'][-5:]), None)
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': '#fdf7f6' if covid is None else colorscale(covid)
    }

m = folium.Map(
     location=[48, -102], zoom_start=3,
     tiles='cartodbpositron',
 )
m.fit_bounds([[51.027594, -100.195910],[24.093070, -99.048598]])
folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',name='Covid 19 Deaths',
    style_function=style_function
).add_to(m)
# colorscale.add_to(m)

cases_series = df['cases']
colorscale = branca.colormap.linear.PuRd_04.to_step(10).scale(5, 10000)

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',name='Covid 19 Cases',
    style_function=style_function
).add_to(m)

#colorscale.add_to(m)
# Marker Cases
for i in range(0,len(data)):
    popup_text = "<b>{}<b><br><br> <b>Cases:</b> {:,}<br> <b>Deaths:</b< {:,}<br><b> Recovered:</b> {:,}"
    popup_text = popup_text.format(
                      data.iloc[i]['Province_State'],
                      data.iloc[i]['Confirmed'],
                      data.iloc[i]['Deaths'],
                      data.iloc[i]['Recovered'],
                      )
    folium.CircleMarker(
        location=[data.iloc[i]['Lat'], data.iloc[i]['Long_']],
        popup= popup_text,
        radius=data.iloc[i]['Confirmed']*0.0001,
        color='crimson',
        fill=True,
        fill_color='crimson').add_to(m)

# Marker Deaths
for i in range(0,len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['Lat'], data.iloc[i]['Long_']],
        popup= popup_text,
        radius=data.iloc[i]['Deaths']*0.001,
        color='purple',
        fill=True,
        fill_color='purple').add_to(m)

folium.LayerControl().add_to(m)

# Save it as html
m.save('mymap.html')


# In[72]:


import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')
df.head()

data = []
layout = dict(
    title = 'New Walmart Stores per year 1962-2006<br>\
Source: <a href="http://www.econ.umn.edu/~holmes/data/WalMart/index.html">\
University of Minnesota</a>',
    # showlegend = False,
    autosize = False,
    width = 1000,
    height = 900,
    hovermode = False,
    legend = dict(
        x=0.7,
        y=-0.1,
        bgcolor="rgba(255, 255, 255, 0)",
        font = dict( size=11 ),
    )
)
years = df['YEAR'].unique()

for i in range(len(years)):
    geo_key = 'geo'+str(i+1) if i != 0 else 'geo'
    lons = list(df[ df['YEAR'] == years[i] ]['LON'])
    lats = list(df[ df['YEAR'] == years[i] ]['LAT'])
    # Walmart store data
    data.append(
        dict(
            type = 'scattergeo',
            showlegend=False,
            lon = lons,
            lat = lats,
            geo = geo_key,
            name = int(years[i]),
            marker = dict(
                color = "rgb(0, 0, 255)",
                opacity = 0.5
            )
        )
    )
    # Year markers
    data.append(
        dict(
            type = 'scattergeo',
            showlegend = False,
            lon = [-78],
            lat = [47],
            geo = geo_key,
            text = [years[i]],
            mode = 'text',
        )
    )
    layout[geo_key] = dict(
        scope = 'usa',
        showland = True,
        landcolor = 'rgb(229, 229, 229)',
        showcountries = False,
        domain = dict( x = [], y = [] ),
        subunitcolor = "rgb(255, 255, 255)",
    )


def draw_sparkline( domain, lataxis, lonaxis ):
    ''' Returns a sparkline layout object for geo coordinates  '''
    return dict(
        showland = False,
        showframe = False,
        showcountries = False,
        showcoastlines = False,
        domain = domain,
        lataxis = lataxis,
        lonaxis = lonaxis,
        bgcolor = 'rgba(255,200,200,0.0)'
    )

# Stores per year sparkline
layout['geo44'] = draw_sparkline({'x':[0.6,0.8], 'y':[0,0.15]},                                  {'range':[-5.0, 30.0]}, {'range':[0.0, 40.0]} )
data.append(
    dict(
        type = 'scattergeo',
        mode = 'lines',
        lat = list(df.groupby(by=['YEAR']).count()['storenum']/1e1),
        lon = list(range(len(df.groupby(by=['YEAR']).count()['storenum']/1e1))),
        line = dict( color = "rgb(0, 0, 255)" ),
        name = "New stores per year<br>Peak of 178 stores per year in 1990",
        geo = 'geo44',
    )
)

# Cumulative sum sparkline
layout['geo45'] = draw_sparkline({'x':[0.8,1], 'y':[0,0.15]},                                  {'range':[-5.0, 50.0]}, {'range':[0.0, 50.0]} )
data.append(
    dict(
        type = 'scattergeo',
        mode = 'lines',
        lat = list(df.groupby(by=['YEAR']).count().cumsum()['storenum']/1e2),
        lon = list(range(len(df.groupby(by=['YEAR']).count()['storenum']/1e1))),
        line = dict( color = "rgb(214, 39, 40)" ),
        name ="Cumulative sum<br>3176 stores total in 2006",
        geo = 'geo45',
    )
)

z = 0
COLS = 5
ROWS = 9
for y in reversed(range(ROWS)):
    for x in range(COLS):
        geo_key = 'geo'+str(z+1) if z != 0 else 'geo'
        layout[geo_key]['domain']['x'] = [float(x)/float(COLS), float(x+1)/float(COLS)]
        layout[geo_key]['domain']['y'] = [float(y)/float(ROWS), float(y+1)/float(ROWS)]
        z=z+1
        if z > 42:
            break

fig = go.Figure(data=data, layout=layout)
fig.update_layout(width=800)
fig.show()


# In[ ]:





# In[74]:


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[ ]:




