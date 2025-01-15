# SERIES 

import pandas as pd

country_gdp = pd.Series([122222, 23324, 435646, 5645,3746587, 3436764], index=['India', 'Pakistan', 'Japan', 'USA', 'UK', 'Germany'])
print(country_gdp.iloc[1])