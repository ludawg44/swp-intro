#
# Created by Luis Vera
# Last edited October 1, 2024
#

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import random

st.set_page_config(page_title="SWP")

st.markdown("# Strategic Workforce Planning")
st.markdown("### A Primer")
st.write(
    """
    We are going to keep this Strategic Workforce Planning (SWP) primer relatively straightforward and simple.
    You have to know how to crawl before you start running.
    We understand there are various strategies, frameworks, and models used in SWP, but we're going to start with the fundamentals. 
    There are three topics we're going to cover in this primer. 
    The first one is Workforce Demand, followed by Workforce Supply, and lastly the Gap Analysis. 
    It is our hope that with these three fundamental concepts you will achieve a better understanding of how to implement SWP within your organization.
    """
)

# ----- Workforce Demand----- #

st.markdown("### Workforce Demand")
st.write(
    """
    Workforce Demand can be thought of having two views. One incorporates a high-level perspective with a minimal amount of factors incorporated into the calculation. 
    The second is an aggregate of the myopic demand for each position or role within an organization or team. We're going to demonstrate both perspective in this section.
    """
)

# ----- Macro Workforce ----- #

st.markdown("##### A Macro Case Study")

st.write(
    """
    You recently joined a biotech startup that received a new round of funding. 
    Researchers made new headways in advancing the genetics therapies and the excitement is palpable. 
    It's planning season and your hiring manager asked to get the latest workforce forecast for the next 5 years.
    Being new to the company, you're going to take the projected business growth and use that as your growth multiplier.
    The most recent analyst reported a 12% growth. 
    You're team is currently at 210. 
    We placed these numbers down below, but feel free to experiment. 
    """
)

user_wf_start = int(st.text_input("Enter your starting workforce here", 210))
user_wf_mult = int(st.text_input("Enter your growth multipler here", 12))
user_lt_yrs = int(st.text_input("Enter your company's long term time horizon here", 5))

today = datetime.date.today()
year = today.strftime("%Y")

years = []
for i in range(user_lt_yrs):
    years_col = int(year) + i
    years.append(years_col)

hc = []
hc.append(user_wf_start)
wf_start1 = user_wf_start
for i in range(user_lt_yrs-1):
    value= int(wf_start1)*(1+(int(user_wf_mult)/100))
    hc.append(value)
    wf_start1 = value

workforce = pd.DataFrame({'Year':years, 'Macro WFM':hc})
workforce['Year'] = pd.to_datetime(workforce['Year'], format='%Y').dt.strftime('%Y')
workforce['Macro WFM'] = workforce['Macro WFM'].astype('int64')
# workforce

st.write("Your forecast will look like like this:")
macro_df = workforce.copy()
macro_df = macro_df.set_index('Year')
macro_df = macro_df.transpose()
macro_df

# ----- Micro Workforce ----- #

st.markdown("##### A Micro Perspective")

st.write(
    """
    You hand in your projections to your hiring manager and he believes it looks a little downbeat.
    Based on this information you decide to turn to your counterparts across the organization. 
    You write an email to each department head and describe the ask. 
    They return with the following:
    """
)

for index, row in workforce.iterrows():
    workforce.at[index,'Execs'] = row['Macro WFM'] * .02
    workforce.at[index,'Mngrs'] = row['Macro WFM'] * .25
    workforce.at[index,'Engrs'] = row['Macro WFM'] * .2
    workforce.at[index,'Ops'] = row['Macro WFM'] * .3
    workforce.at[index,'HR'] = row['Macro WFM'] * .05
    workforce.at[index,'IT'] = row['Macro WFM'] * .2
    workforce.at[index,'Fin'] = row['Macro WFM'] * .05
    
workforce['Execs'] = workforce['Execs'].astype('int64')
workforce['Mngrs'] = workforce['Mngrs'].astype('int64')
workforce['Engrs'] = workforce['Engrs'].astype('int64')
workforce['Ops'] = workforce['Ops'].astype('int64')
workforce['HR'] = workforce['HR'].astype('int64')
workforce['IT'] = workforce['IT'].astype('int64')
workforce['Fin'] = workforce['Fin'].astype('int64')
# workforce

workforce['Micro WFM'] = workforce.iloc[:,2:9].sum(axis=1).astype('int64')
# workforce

micro_df = workforce.copy()
micro_df = micro_df.set_index('Year')
micro_df = micro_df.transpose()
micro_df = micro_df.iloc[1:-1]
micro_df

# ----- Workforce Demand Visualization ----- #

st.markdown("##### Putting it altogether")

st.write(
    """
    Now we can compare the difference between a macro and micro workforce demand. 
    One encapsulating a single growth multipler while the other incorporating more feedback.
    """
)

demand_df = workforce.copy()
demand_df = demand_df[['Year', 'Macro WFM', 'Micro WFM']]
demand_df = demand_df.set_index('Year')
demand_df_transpose = demand_df.transpose()
demand_df_transpose


fig = px.line(workforce,
              x='Year',
              y=['Macro WFM','Micro WFM'])
fig.update_yaxes(title_text='Workforce')
st.plotly_chart(fig)

st.write(
    """
    What does this tell us? 
    Aside from the obvious delta, this shows us that being able to distinguish from a macro to a micro mindset will show differences in our outlook. 
    Personally, I believe this is why we have so many discrepancies between the higher level managers and those on at the factory floor. 
    """
)

# ----- Workforce Supply----- #

st.markdown("### Workforce Supply")
st.write(
    """
    The next step in our primer is Workforce Supply. 
    We are only going to focus on the internal talent supply, specifically developing some understanding of attrition forecasting. 
    If you were to take this further, you would get into skills, experience, education, and eventually external talent supply. 
    For that you would need to understand how skills, experience, education, etc. work in external markets now and in the future. 
    """
)

# ----- Attrition ----- #

user_attrition = int(st.text_input("Enter your annual attrition here", 8))

attrition = []
wf_start2 = user_wf_start
attrition.append(wf_start2)
for i in range(user_lt_yrs-1):
    value = int(wf_start2)*(1-(int(user_attrition)/100))
    attrition.append(value)
    wf_start2 = value

workforce['Attrition'] = attrition

atrit_df = workforce.copy()
atrit_df = atrit_df[['Year', 'Attrition']]
atrit_df = atrit_df.set_index('Year')
atrit_df_transposed = atrit_df.transpose()
atrit_df_transposed
