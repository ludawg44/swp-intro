#
# Created by Luis Vera
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
# st.markdown("#### A Primer")
st.write(
    """
    We're going to keep this Strategic Workforce Planning (SWP) primer relatively straightforward and simple.
    You have to know how to crawl before you start running.
    We understand there are various strategies, frameworks, and models used in SWP, but we're going to start with the fundamentals. 
    There are three topics we're going to cover in this primer. 
    The first one is Workforce Demand, followed by Workforce Supply, and lastly Gap Analysis. 
    It is our hope that with these three fundamental concepts you will achieve a better understanding of how to implement SWP within your organization.
    """
)

# ----- Workforce Demand----- #

st.markdown("#### Workforce Demand")
st.write(
    """
    Workforce Demand can be thought of having two views of the workforce you or your company desires. One incorporates a high-level perspective with a minimal amount of factors incorporated into the calculation (think really busy VPs and Director levels folks).
    The second is an aggregate of the demand for each position or role within an organization or team (think managers or boots on the ground). We're going to demonstrate both perspective in this section.
    """
)

# ----- Macro Workforce ----- #

st.markdown("##### A Micro Perspecitve - Case Study 🧬")

st.write(
    """
    You recently joined a biotech startup specializing in gene-editing technology that received a new round of funding. 
    Researchers made new headways in advancing the platform and the excitement is palpable both internally and externally the company. 
    It's workforce planning season and your boss asked to get the latest forecast for the next 5 years.
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
    You hand in your projections to your boss and he believes it looks a little downbeat.
    Based on this feedback you decide to turn to your subordinates across the organization. 
    You write an email to each department head and describe the ask. 
    They return with the following numbers:
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
    One encapsulating a single growth multipler while the other incorporating multiple factors.
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
    Aside from the obvious delta, this shows us a macro vs. a micro mindset will that will cause differing outlooks. 
    Personally, I believe this is why we have so many discrepancies between the higher level managers and those on at the metatphorical floor. 
    """
)

# ----- Workforce Supply----- #

st.markdown("#### Workforce Supply")
st.write(
    """
    The next step in our primer is Workforce Supply. 
    We are only going to focus on the internal talent supply, specifically developing some understanding of how attrition plays a role. 
    If you were to take this further, you would get into skills, experience, education, and eventually external talent supply datasets. 
    For that, you would need to understand how skills, experience, and education, etc. work in external markets now and in the future. 
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

st.write(
    """
    I would agree with you that this is harsh decline in the workforce and has an immediate sticker shock effect. 
    Any good manager would do anything in their power to stop the decline. 
    But the decline is yet another reminder of how quickly teams can unravelled.  
    \nAnother item I'd like to point out is how unsightly it is to see this visually displayed as a table or line chart.
    That is why most SWP practitioners would prefer to view this decline along with antipated growth, in a waterfall format. 
    And for that we turn to the Gap Analysis. 
    """
)

# ----- Gap Analysis ----- #
st.markdown("#### Gap Analysis")
st.write(
    """
    Lastly, we cover the Gap Analysis. In essence, this allows us to have a better understanding of the gap between our demand and our supply. 
    Great, you understand the basic principle, but what does that mean and how are you going to apply it to your plan and the insights you'll be able to provide to your team? 
    The gap, depending you're above or below status quo, will help you put into context how mych surplus or scarcity of your workforce you will have over time. 
    Each concept on it's own has it's own strategy in place that will allow you to help optimize your workforce over time. 
    \nHere are some ideas on how you can deal with a scarcity or a surplus when analyzing your workforce. 
    
    """
)
# ----- Waterfall Chart ----- #

workforce

fig = go.Figure(go.Waterfall(
    name = "20ls", 
    orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total"],
    x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    textposition = "outside",
    text = ["+60", "+80", "", "-40", "-20", "Total"],
    y = [60, 80, 0, -40, -20, 0],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "Gap Analysis Waterfall Chart",
        showlegend = True
)


tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit")
with tab2:
    st.plotly_chart(fig, theme=None)