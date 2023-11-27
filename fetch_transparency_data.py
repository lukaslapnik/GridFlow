# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:06:15 2023

@author: slluka
"""

import pandas as pd
# from settings import api_key
from entsoe import EntsoePandasClient as Entsoe
from entsoe import EntsoeRawClient

api_key = "nice_try"

client = EntsoeRawClient(api_key=api_key)

e = Entsoe(api_key=api_key, retry_count=20, retry_delay=1)

# european_country_codes = [
#     "AL",  # Albania
#     "AD",  # Andorra
#     "AT",  # Austria
#     "BY",  # Belarus
#     "BE",  # Belgium
#     "BA",  # Bosnia and Herzegovina
#     "BG",  # Bulgaria
#     "HR",  # Croatia
#     "CY",  # Cyprus
#     "CZ",  # Czech Republic
#     "DK",  # Denmark
#     "EE",  # Estonia
#     "FO",  # Faroe Islands
#     "FI",  # Finland
#     "FR",  # France
#     "DE",  # Germany
#     "GI",  # Gibraltar
#     "GR",  # Greece
#     "HU",  # Hungary
#     "IS",  # Iceland
#     "IE",  # Ireland
#     "IM",  # Isle of Man
#     "IT",  # Italy
#     "XK",  # Kosovo
#     "LV",  # Latvia
#     "LI",  # Liechtenstein
#     "LT",  # Lithuania
#     "LU",  # Luxembourg
#     "MT",  # Malta
#     "MD",  # Moldova
#     "MC",  # Monaco
#     "ME",  # Montenegro
#     "NL",  # Netherlands
#     "MK",  # North Macedonia
#     "NO",  # Norway
#     "PL",  # Poland
#     "PT",  # Portugal
#     "RO",  # Romania
#     "RU",  # Russia
#     "SM",  # San Marino
#     "RS",  # Serbia
#     "SK",  # Slovakia
#     "SI",  # Slovenia
#     "ES",  # Spain
#     "SE",  # Sweden
#     "CH",  # Switzerland
#     "UA",  # Ukraine
#     "GB",  # United Kingdom
#     "VA",  # Vatican City
# ]

european_neighbors = {
    "AL": ["GR", "ME", "RS", "XK"],
    "AT": ["CH", "CZ", "DE", "HU", "IT", "SI", "HU"],
    "BY": ["LV", "LT", "PL", "RU", "UA"],
    "BE": ["FR", "DE", "LU", "NL"],
    "BA": ["HR", "ME", "RS"],
    "BG": ["GR", "MK", "RO", "RS", "TR"],
    "HR": ["BA", "HU", "ME", "RS", "SI"],
    "CY": [],
    "CZ": ["AT", "DE", "PL", "SK"],
    "DK": ["DE"],
    "EE": ["LV"],
    "FO": [],
    "FI": ["NO", "SE"],
    "FR": ["AD", "BE", "DE", "IT", "LU", "MC", "ES", "CH"],
    "DE": ["AT", "BE", "CZ", "DK", "FR", "LU", "NL", "PL", "CH"],
    "GI": ["ES"],
    "GR": ["AL", "BG", "TR"],
    "HU": ["AT", "HR", "RO", "RS", "SK", "SI", "UA"],
    "IS": [],
    "IE": ["GB"],
    "IM": [],
    "IT": ["AT", "CH", "FR", "SM", "SI", "VA"],
    "XK": ["AL", "ME", "RS"],
    "LV": ["BY", "EE", "LT"],
    "LI": ["AT", "CH"],
    "LT": ["BY", "LV", "PL"],
    "LU": ["BE", "DE", "FR"],
    "MT": [],
    "MD": ["RO", "UA"],
    "MC": ["FR"],
    "ME": ["AL", "BA", "HR", "XK", "RS"],
    "NL": ["BE", "DE"],
    "MK": ["AL", "BG", "GR", "RS"],
    "NO": ["FI", "SE"],
    "PL": ["BY", "CZ", "DE", "LT", "RU", "SK", "UA"],
    "PT": ["ES"],
    "RO": ["BG", "HU", "MD", "RS", "UA"],
    "RU": ["BY", "EE", "FI", "LV", "LT", "NO", "PL", "UA"],
    "SM": ["IT"],
    "RS": ["BA", "BG", "HR", "HU", "ME", "MK", "XK"],
    "SK": ["AT", "CZ", "HU", "PL", "UA"],
    "SI": ["AT", "HR", "IT", "HU"],
    "ES": ["AD", "FR", "GI", "PT"],
    "SE": ["FI", "NO"],
    "CH": ["AT", "DE", "FR", "IT", "LI"],
    "UA": ["BY", "HU", "MD", "PL", "RO", "RU", "SK"],
    "GB": ["IE"],
    "VA": ["IT"]
}

borders = {
    # "AL": ["GR", "ME", "RS", "XK"],
    "AT": ["CH", "CZ", "DE", "HU", "IT", "SI"],
    # "BY": ["LV", "LT", "PL", "RU", "UA"],
    # "BE": ["FR", "DE", "LU", "NL"],
    # "BA": ["HR", "ME", "RS"],
    # "BG": ["GR", "MK", "RO", "RS", "TR"],
    "HR": ["BA", "HU", "RS", "SI"],
    # "CY": [],
    # "CZ": ["AT", "DE", "PL", "SK"],
    # "DK": ["DE"],
    # "EE": ["LV"],
    # "FO": [],
    # "FI": ["NO", "SE"],
    # "FR": ["AD", "BE", "DE", "IT", "LU", "MC", "ES", "CH"],
    # "DE": ["AT", "BE", "CZ", "DK", "FR", "LU", "NL", "PL", "CH"],
    # "GI": ["ES"],
    # "GR": ["AL", "BG", "TR"],
    "HU": ["AT", "HR", "RO", "RS", "SI", "SK", "UA"],
    # "IS": [],
    # "IE": ["GB"],
    # "IM": [],
    "IT": ["AT", "CH", "FR", "SI", "ME", "GR", "MT"],
    # "XK": ["AL", "ME", "RS"],
    # "LV": ["BY", "EE", "LT"],
    # "LI": ["AT", "CH"],
    # "LT": ["BY", "LV", "PL"],
    # "LU": ["BE", "DE", "FR"],
    # "MT": [],
    # "MD": ["RO", "UA"],
    # "MC": ["FR"],
    # "ME": ["AL", "BA", "HR", "XK", "RS"],
    # "NL": ["BE", "DE"],
    # "MK": ["AL", "BG", "GR", "RS"],
    # "NO": ["FI", "SE"],
    # "PL": ["BY", "CZ", "DE", "LT", "RU", "SK", "UA"],
    # "RO": ["BG", "HU", "MD", "RS", "UA"],
    # "RU": ["BY", "EE", "FI", "LV", "LT", "NO", "PL", "UA"],
    # "SM": ["IT"],
    # "RS": ["BA", "BG", "HR", "HU", "ME", "MK", "XK"],
    # "SK": ["AT", "CZ", "HU", "PL", "UA"],
    "SI": ["AT", "HR", "IT", "HU"],
    # "ES": ["AD", "FR", "GI", "PT"],
    # "SE": ["FI", "NO"],
    # "CH": ["AT", "DE", "FR", "IT", "LI"],
    # "UA": ["BY", "HU", "MD", "PL", "RO", "RU", "SK"],
    # "GB": ["IE"],
    # "VA": ["IT"]
}

# Print the dictionary
for country, neighbors in borders.items():
    print(f"{country}: {neighbors}")

# Print the list
# print(european_country_codes)

year = 2022
month = 1
day = 1
hour = 0

location = "folder"

start = pd.Timestamp(year=year, month=month, day=day, hour=hour, tz='UTC')
end = pd.Timestamp(year=year+1, month=month+10, day=day+8, hour=hour, tz='UTC')

country_code = 'BE'  # Belgium
country_code_from = 'SI'  # France
country_code_to = 'IT' # Germany-Luxembourg
type_marketagreement_type = 'A01'
contract_marketagreement_type = 'A01'

df_data = pd.DataFrame()

for country, neighbors in borders.items():
    # try:
    print(country)
        
    load_forecast = e.query_load(country, start=start, end=end)
    load_forecast.index = load_forecast.index.tz_localize(None)
    load_forecast = load_forecast[(load_forecast.index.minute == 0)]
    load_forecast.columns = load_forecast.columns + " " + country
    load_forecast.to_excel(location + "\Load forecast " + country + ".xlsx")
    
    # df_data = df_data.append(load_forecast)
    
    load_actual = e.query_load_forecast(country, start=start, end=end)
    load_actual.index = load_actual.index.tz_localize(None)
    load_actual = load_actual[(load_actual.index.minute == 0)]
    load_actual.columns = load_actual.columns + " " + country
    load_actual.to_excel(location + "\Load actual " + country + ".xlsx")
    
    # df_data = df_data.append(load_actual)
    
    generation_forecast = e.query_generation_forecast(country, start=start, end=end)
    generation_forecast.index = generation_forecast.index.tz_localize(None)
    generation_forecast = generation_forecast[(generation_forecast.index.minute == 0)]
    if isinstance(generation_forecast, pd.Series):
        print("s is a Pandas Series.")
        generation_forecast = generation_forecast.to_frame()
    else:
        print("s is not a Pandas Series.")
    
    generation_forecast.columns = generation_forecast.columns + " " + country
    generation_forecast.to_excel(location + "\Generation forecast " + country + ".xlsx")
    
    # df_data = df_data.append(generation_forecast)
    
    generation_actual = e.query_generation(country, start=start, end=end)
    generation_actual.index = generation_actual.index.tz_localize(None)
    generation_actual = generation_actual[(generation_actual.index.minute == 0)]
    
    print(generation_actual)
    
    df_gen_new = pd.DataFrame()
    gen_cats = set(generation_actual.columns.get_level_values(0).tolist())
    if generation_actual.columns.nlevels > 1:
        try: 
            for gen_cat in gen_cats:
                df_gen_new[gen_cat] = generation_actual[gen_cat]['Actual Aggregated'] - generation_actual[gen_cat]['Actual Consumption']
        except:
            for gen_cat in gen_cats:
                df_gen_new[gen_cat] = generation_actual[gen_cat]['Actual Aggregated']
    else: 
        df_gen_new = generation_actual
    
    df_gen_new.columns = df_gen_new.columns + " " + country
    df_gen_new['Actual Generation ' + country] = df_gen_new.sum(axis=1)
    df_gen_new.to_excel(location + "\Generation actual " + country + ".xlsx")
    
    # df_data = df_data.append(generation_actual)
    df_data = pd.concat([df_data, load_forecast, load_actual, generation_forecast, df_gen_new['Actual Generation ' + country]], axis=1)
    # save_data  
        
# Print the dictionary
# for country, neighbors in borders.items():
#     for neighbor in neighbors:
#         # print(f"{country} {neighbor}")
#         try:
#             load_forecast = e.query_load
#             load_actual = e.query_load_forecast
#             generation_forecast = e.query_generation_forecast
#             generation_actual = e.query_generation
#             scheduled_exchanges = e.query_scheduled_exchanges(country, neighbor, start=start, end=end)
#             actual_exchanges = e.query_crossborder_flows(country, neighbor, start=start, end=end)
            
#             # flow = flow[(flow.index.minute == 0)]
#             df_data["Sch " + country + "-"  + neighbor] = scheduled_exchanges
#             df_data["Act " + country + "-"  + neighbor] = actual_exchanges
#             print(f"Flow between {country} and {neighbor} is {actual_exchanges[0]}, schedule {scheduled_exchanges[0]}")
#         except:
#             print(f"No flow data between {country} and {neighbor}")
#             df_data["Sch " + country + "-"  + neighbor] = "NO DATA"
#             df_data["Act" + country + "-"  + neighbor] = "NO DATA"

#Strip timezone from index
# df_data.index = df_data.index.tz_localize(None)     
       
# df_data.to_excel(location)  
            
# print(f"{country} {neighbor}")
# try:
#     scheduled_exchanges = e.query_scheduled_exchanges(country_code_from, country_code_to, start=start, end=end)
#     flow_actual = e.query_crossborder_flows(country_code_from, country_code_to, start=start, end=end)
#     # flow_actual = flow_actual[(flow_actual.index.minute == 0)]
#     print(type(flow_actual))
#     print(f"scheduled between {country_code_from} and {country_code_to} is {scheduled_exchanges}")
#     print(f"Flow between {country_code_from} and {country_code_to} is {flow_actual}")
    
# except:
#     print("No flow data")
#     flow_value = "NO DATA"

# list_of_dicts = {}
# df_flows_2 = pd.DataFrame()

# for country1 in european_country_codes:
#     for country2 in european_country_codes:
#         # print(f"Getting data for {country1} to {country2}")
#         try:
#             flow = e.query_crossborder_flows(country1, country2, start=start, end=end)
#             flow = flow[(flow.index.minute == 0)]
#             flow = flow[0]
#         except:
#             flow = "NONE"
#         if type(flow) == int or type(flow) == float:
#             list_of_dicts[country1].append(country2)
#             print(f"Appendet {country2} to {country1}")
#         # else:
#             # print('The variable is not a number')
                

# si_it = e.query_crossborder_flows('IT', 'SI', start=start, end=end)
# it_si = e.query_crossborder_flows('IT', 'SI', start=start, end=end)
# si_at = e.query_crossborder_flows('SI', 'AT', start=start, end=end)
# si_at = e.query_crossborder_flows('AT', 'SI', start=start, end=end)
# si_hr = e.query_crossborder_flows('SI', 'HR', start=start, end=end)
# si_hr = e.query_crossborder_flows('SI', 'HR', start=start, end=end)
# si_hu = e.query_crossborder_flows('SI', 'HU', start=start, end=end)
# si_hu = e.query_crossborder_flows('SI', 'HU', start=start, end=end)

# si_it = si_it[(si_it.index.minute == 0)]
# si_at = si_at[(si_at.index.minute == 0)]
# si_hr = si_hr[(si_hr.index.minute == 0)]
# si_hu = si_hu[(si_hu.index.minute == 0)]

# print(si_it[0])
