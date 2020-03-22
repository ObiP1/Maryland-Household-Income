import pandas as pd
import plotly.figure_factory as ff
from chart_studio.plotly import iplot
plotly.tools.set_credentials_file(username='', api_key='')

scope = ['Maryland']
df = pd.read_csv('https://raw.githubusercontent.com/ObiP1/Maryland-Household-Income/master/DataTable.csv')

df_new = df[df['ST_NAME'].isin(scope)]

values = df_new['MEDIAN_INCOME'].tolist()
fips = df_new['FIPS'].tolist()

# Initializes colors to distinguish counties from each other(we need at least 24 for each county)
colorscale = ['#bebada', '#0068a0', '#00778b', '#d9d9d9', '#ffed6f', '#ea1717', '#f0c800', '#ffffb3',
              '#8dd3c7', '#3697dd', '#fb8072', '#afcbc7', '#5a3791', '#ccebc5', '#ffed6f', '#f6c4d2',
             '#80b1d3', '#2daa4b', '#4f5573', '#436e6f', '#1d2d43', '#af3205', '#ff0000', '#460606']

fig = ff.create_choropleth(
      fips=fips, values=values, scope=scope,
      colorscale=colorscale, round_legend_values=True,
      simplify_county=0, simplify_state=0,
      county_outline={'color': 'rgb(15,15,55)','width': 0.5},
      state_outline={'width': 0.5},
      legend_title='Median Household Income Per County',
      title='Maryland')

iplot(fig, filename='Choropleth Maryland Map')
