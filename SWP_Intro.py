#
# Created by Luis Vera
#

import streamlit as st # type: ignore
import pandas as pd
import numpy as np
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore
import datetime
import random

st.set_page_config(
    page_title="SWP",
    layout='wide'
)

st.markdown("# Strategic Workforce Planning")
# st.markdown("#### A Primer")
st.write(
    """
    We're going to keep this Strategic Workforce Planning (SWP) primer straightforward and simple. You have to know how to crawl before you can start running. While there are various strategies, frameworks, and models within SWP, we'll begin with the fundamentals. In this primer, we’ll focus on three key topics: Workforce Demand, Workforce Supply, and Gap Analysis. Our goal is that by mastering these foundational concepts, you’ll gain a better understanding of how to effectively implement SWP within your organization.
    """
)

# ----- Workforce Demand----- #

st.markdown("#### Workforce Demand")
st.write(
    """
    Workforce Demand can be viewed from two perspectives. The first takes a high-level approach, incorporating only a few key factors into the calculation—ideal for busy VPs and Directors who need a quick, strategic overview. The second perspective is more detailed, focusing on the demand for each specific position or role within the organization, which is often used by managers or frontline teams. In this section, we’ll demonstrate both approaches to help you understand how Workforce Demand can be analyzed at different levels.
    """
)

# ----- Macro Workforce ----- #

st.markdown("##### Case Study Introduction: A CRISPR-based gene editing company 🧬")
st.markdown("##### A Macro Perspecitve")

st.write(
    """
    You recently joined a biotech startup specializing in gene-editing technology that has just secured a new round of funding. Researchers have made significant advancements in the platform, and the excitement is palpable both within the company and in the broader market. It’s workforce planning season, and your boss has asked for the latest forecast for the next five years. As you're new to the company, you plan to base your projections on the expected business growth, using that as your growth multiplier. The latest analyst report predicts a 12% growth rate. Your team currently consists of 210 people. We've outlined these numbers below, but feel free to experiment with different projections. 
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

# Create a CSS style to center the DataFrame
st.markdown(
    """
    <style>
    .centered-dataframe {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.write("Your forecast will look like like this:")
macro_df = workforce.copy()
macro_df = macro_df.set_index('Year')
macro_df = macro_df.transpose()

st.dataframe(macro_df)

# ----- Micro Workforce ----- #

st.markdown("##### A Micro Perspective")

st.write(
    """
    You submit your projections to your boss, but he feels they seem a bit conservative. Based on this feedback, you decide to reach out to your subordinates across the organization for additional input. You send an email to each department head, outlining your request. They respond with the following numbers:
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
    value = int((wf_start2)*(1-(int(user_attrition)/100)))
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
# ----- Waterfall Chart ----- #

attrition_w_hc = []
attrition_factor = 1 - (user_attrition/100)
wf_start3 = user_wf_start
attrition_w_hc.append(wf_start3)

for i in range(user_lt_yrs-1):
    value = int(wf_start3 * attrition_factor)
    attrition_w_hc.append(value)
    wf_start3 = value

# attrition_w_hc

waterfall = workforce.copy()
waterfall = waterfall[['Year','Macro WFM']]
waterfall = waterfall.rename(columns={'Macro WFM':'Forecasted Growth'})
waterfall['Planned Headcount'] = user_wf_start
waterfall = waterfall[['Year', 'Planned Headcount', 'Forecasted Growth']]
waterfall['Growth'] = waterfall['Forecasted Growth'].subtract(waterfall['Planned Headcount'])
waterfall['Forecasted Attrition'] = -(waterfall['Forecasted Growth']*float(user_attrition/100))
waterfall['Forecasted Attrition'] = waterfall['Forecasted Attrition'].astype('int64')
waterfall['Actual Headcount'] = waterfall['Forecasted Growth'].add(waterfall['Forecasted Attrition'])
waterfall = waterfall[['Year','Planned Headcount','Forecasted Growth','Growth','Forecasted Attrition','Actual Headcount']]
waterfall_df = waterfall[['Planned Headcount','Growth','Forecasted Attrition','Actual Headcount']]
# waterfall


fig = go.Figure(go.Waterfall(
    name = "Workforce Supply", 
    orientation = "v",
    measure = ["relative","relative", "relative", "total"],
    x = waterfall_df.columns,
    textposition = "outside",
    text = ["Planned Headcount", "Forecasted Growth", "Forecasted Attrition", "Actual Headcount"],
    y = waterfall_df.loc[1],
    connector = {"line":{"color":"rgb(63,63,63)"}}
))
fig.update_layout(
    title = f"{int(year)+1} Projection",
    showlegend = True,
    height = 500
)
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(go.Waterfall(
    name = "Workforce Supply", 
    orientation = "v",
    measure = ["relative","relative", "relative", "total"],
    x = waterfall_df.columns,
    textposition = "outside",
    text = ["Planned Headcount", "Forecasted Growth", "Forecasted Attrition", "Actual Headcount"],
    y = waterfall_df.loc[user_lt_yrs-1],
    connector = {"line":{"color":"rgb(63,63,63)"}}
))
fig.update_layout(
    title = f"{int(year)+user_lt_yrs-1} Projection",
    showlegend = True,
    height = 500
)
st.plotly_chart(fig, use_container_width=True)

st.write("While the main focus is on the delta, we have to remind ourselves that SWP aids in optimizing your future workforce.")

st.info(
    """At this point you should be thinking what inflows and outflows better reflect your situation. 
    Is it attrition or is it retirement? 
    Is the rate of transfers into the organization meeting expeCctations or should you rethinking internal marketing campaigns?
    These visualizations will help you articulate what is next in the evolution of your workforce. 
    """
)

# ----- Gap Analysis ----- #
st.markdown("#### Gap Analysis")
st.write(
    """
    I would usually congratulate the reader for making it this far, but this is the most complex and challenging part of SWP. 
    That is because we are revealing the gaps between the various forecasts and it is now time to understand how they implicate your future business goals and objectives.
    One has to be critical - yet unbiased - when evaluating the bench strength of your existing employees against the strategic needs of the business. 
    \nAs you dig deeper, you will find it helpful to have your talent strategy near you to rank what gaps need to be addressed.
    For each area of your talent strategy, consider how well you're prepared to handle the future state and how much impact it will have on your organization or team. 
    If you're blanking out on external factors that could effect your talent strategy, I wrote a couple down to get the ball rolling:  \n
    - Global talent challenges
    - Aging population in the labor market
    - Competition for talent will intensify
    - Industry consolidations
    - Competition for technical and managerial talent
    - Navigating through larger and more complex organizations
    - Shifting organizational structures
    - Availability of skilled workers
    - Tightening labor market
    - Availability and accessibility of technology
    
    """
)
# ----- Gap Analysis Visualization ----- #

gap_df = waterfall.copy()
gap_df.drop('Planned Headcount', axis=1,inplace=True)
gap_df = gap_df.rename(columns={'Forecasted Growth':'Total Headcount Demand','Actual Headcount':'Supply with Hiring'})
gap_df['Supply without Hiring'] = attrition
gap_df['Micro Demand Forecast'] = demand_df['Micro WFM'].values
# gap_df

fig = go.Figure()

fig.add_trace(go.Bar(
    x=gap_df['Year'],
    y=gap_df['Supply without Hiring'],
    name='Supply without Hiring Impact'
))

fig.add_trace(go.Scatter(
    x=gap_df['Year'],
    y=gap_df['Total Headcount Demand'],
    name='Total Headcount Demand'
))

fig.add_trace(go.Scatter(
    x=gap_df['Year'],
    y=gap_df['Micro Demand Forecast'],
    name='Micro Demand Forecast'
))

fig.add_trace(go.Scatter(
    x=gap_df['Year'],
    y=gap_df['Supply with Hiring'],
    name='Supply with Hiring'
))

fig.update_layout(
    title_text='Overall Headcount Demand vs Supply'
)

st.plotly_chart(fig)

# ----- Next Steps ----- #

st.markdown("#### Next Steps")
st.write(
    """
    Usually at the end of any SWP tutorial, a practioner would offer guidance on designing a change management plan.
    They would start by defining the scope, identifying champions, thinking of clever communication slogans and project names.
    Unfortunately we just scraped the surface. 
    \nI would ask you to seriously consider the metrics you need to achieve those business goals. 
    If they don't exist, then work with teams that can help make it happen. 
    For example, ROI on human capital projects, seem to be absent in almost every organization. 
    Find a way to make it happen and be diligent on monitoring those metrics. 
    \nBe on the look out for more primers and tools coming out soon. 
    """
)
