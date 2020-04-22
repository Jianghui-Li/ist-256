import requests
import json
import pandas as pd

print("COVID19 Analysis")
country = input("Enter a country: ")
country = country.lower()
cases = input("Enter confirmed, recovered, or deaths: ")
cases = cases.lower()
date = input("Enter a date: ")
url = 'https://api.covid19api.com/live/country/'+country+'/status/'+cases+'/date/'+date+'T00:00:00Z'
response = requests.get(url)
print(response.url)
stats = response.json()

response.json()

url_1 = 'https://api.covid19api.com/summary'
response_summary = requests.get(url_1)
summary = response_summary.json()
response_summary.json()

New_Confirmed = summary['Global']['NewConfirmed']
Total_Confirmed = summary['Global']['TotalConfirmed']
New_Deaths = summary['Global']['NewDeaths']
Total_Deaths = summary['Global']['TotalDeaths']
New_Recovered = summary['Global']['NewRecovered']
Total_Recovered = summary['Global']['TotalRecovered']
print("New COVID19 Reports")
Overall_df = pd.DataFrame({'NewConfirmed': [New_Confirmed],'TotalConfirmed': [Total_Confirmed],'NewDeaths': [New_Deaths],'TotalDeaths': [Total_Deaths],'NewRecovered': [New_Recovered],'TotalRecovered': [Total_Recovered]})
Overall_df

def GetCountries():
    response = requests.get('https://api.covid19api.com/summary')
    data_dict = response.json()
    countries = data_dict['Countries']
    return countries
countries = GetCountries()
country_df = pd.DataFrame(countries)
country_df

top = country_df.sort_values(input('Enter TotalConfirmed, NewConfirmed, NewDeaths, TotalDeaths, NewRecovered, or TotalRecovered view top20 countries: '), ascending = False)
top.head(20)
