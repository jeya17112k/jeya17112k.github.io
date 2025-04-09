#!/usr/bin/env python
# coding: utf-8

# # Plot 1: Top 10 Building Usage Types by Count

# In[2]:


import pandas as pd
import altair as alt
import warnings

# Setup
alt.data_transformers.enable('default', max_rows=None)
warnings.filterwarnings("ignore", category=FutureWarning)

# Load and clean the data
url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
df = pd.read_csv(url)
df.columns = df.columns.str.strip()
usage_col = 'Usage Description'

# Filter top 10 usage types
top_usages = df[usage_col].value_counts().nlargest(10).index
df_top = df[df[usage_col].isin(top_usages)]

# Create transparent stacked bar chart with zoom
bar_chart = alt.Chart(df_top).mark_bar(opacity=0.7).encode(
    x=alt.X(f'{usage_col}:N', sort='-y', title='Usage Description', axis=alt.Axis(labelAngle=30)),
    y=alt.Y('count():Q', title='Number of Buildings'),
    color=alt.Color('Bldg Status:N', title='Building Status'),
    tooltip=[usage_col, 'Bldg Status', 'count()']
).properties(
    title='Top 10 Building Usage Types by Count',
    width=700,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_legend(
    labelFontSize=12,
    titleFontSize=13
).interactive()  # Enable zoom/scroll

bar_chart


# # Plot 2: Building Size vs Year Accquired 

# In[5]:


# Legend-based selection
selection = alt.selection_point(fields=[usage_col], bind='legend')

# Create scatter plot
scatter_plot = alt.Chart(df).mark_circle().encode(
    x=alt.X('Year Acquired:Q', title='Year Acquired'),
    y=alt.Y('Square Footage:Q', title='Square Footage'),
    size=alt.Size('Total Floors:Q', title='Total Floors', scale=alt.Scale(range=[20, 400])),
    color=alt.Color(f'{usage_col}:N', legend=alt.Legend(title='Usage Type')),
    tooltip=['Location Name:N', usage_col, 'Square Footage:Q', 'Total Floors:Q', 'Year Acquired:Q'],
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).add_params(
    selection
).properties(
    title='Building Size vs Year Acquired',
    width=800,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_legend(
    labelFontSize=12,
    titleFontSize=13
).interactive()  # Enable zoom/scroll

scatter_plot


# In[ ]:





# In[ ]:





# In[ ]:




