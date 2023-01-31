import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sqlalchemy import create_engine
from random import randint
import numpy as np
import time
from INNOLAB.DAL.DataGetter import read_data_from_database
import streamlit as st
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

head_list = ['COLLISION ID', 'CRASH DATE', 'CRASH TIME', 'LATITUDE', 'LONGITUDE', 'BOROUGH',
             'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED']
token = "pk.eyJ1IjoiYWhtZXRzMTk5MyIsImEiOiJjbDNoZHY1MnAwdG1rM2NuMHRseWgxYTh5In0.R2WYqCHEKOQ2TZCeAhAEkA"

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

username = "root"
password = "root"
port = 3306
database = "inno"
engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/%s'
                       % (username, password, port, database))
Start = time.time()


@st.experimental_memo
def update_dataset(start) -> pd.DataFrame:
    df_updated = read_data_from_database(start)
    return df_updated


df = update_dataset(Start)


df2 = df.groupby(['VEHICLE_TYPE_CODE_2'], sort=False).size().reset_index(name='count').sort_values(['count'], ascending=False).head(4)


def get_number_of_total_case():
    return len(df)

def get_number_of_total_number_of_person_killed():
      return df["NUMBER_OF_PERSONS_KILLED"].sum()

def get_number_of_total_number_of_person_injured():
      return df["NUMBER_OF_PERSONS_INJURED"].sum()



def get_total_rows():
    total_rows = len(df.index)
    total_rows += 1
    total_rows = str(total_rows)
    info_0 = "Hi human, I'm Optimus Prime, I created this dashboard to help you get information about collisions in New York City. My database is based on New York police departments data. I have" + total_rows + " rows data. Which includes 14 different features. And all together around 1.5 gigabytes. If you want to learn more click on my handsome face."
    return info_0


def grouper(year):
    grouped = df.groupby('YEAR')
    grouped = grouped.get_group(year)
    return grouped


def numberOfCol(year):
    grouped = df.groupby('YEAR')
    x = len(grouped.get_group(year))
    return x


def figureCreaterByYear(year):
    df = grouper(year)
    fig_bar = px.histogram(df, x="MONTH", y="NUMBER_OF_PERSONS_KILLED", height=340)
    fig_bar.update_yaxes(matches=None, showticklabels=True, visible=True, title=None)
    fig_bar.update_xaxes(matches=None, showticklabels=True, visible=True, title=None)
    fig_bar.update_layout(
        font={"color": "#ffc434"},
        title={
            'text': "Bar plot to show number of persons killed",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'}, paper_bgcolor="#1f2d58", plot_bgcolor="#1f2d58", xaxis_showgrid=False,
        yaxis_showgrid=False)
    fig_bar.update_traces(marker_color='#ffa703')
    fig_bar.update_layout(bargap=0.2)
    return fig_bar


def mapCreaterByYear(year):
    df = grouper(year)
    fig_map = px.scatter_mapbox(df, lat="LATITUDE", lon="LONGITUDE", hover_name="ON_STREET_NAME",
                                hover_data=["NUMBER_OF_PERSONS_KILLED", "NUMBER_OF_PERSONS_INJURED"],
                                color_discrete_sequence=["#ffc434"], zoom=5, height=450)
    fig_map.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
    fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig_map


def mapCreaterBySearchedValue(id):
    sql_search = "SELECT * FROM nyc_collisions WHERE COLLISION_ID = %s" % id
    df = pd.read_sql_query(sql_search, engine)
    fig_map = px.scatter_mapbox(df, lat="LATITUDE", lon="LONGITUDE", hover_name="ON_STREET_NAME",
                                hover_data=["NUMBER_OF_PERSONS_KILLED", "NUMBER_OF_PERSONS_INJURED"],
                                color_discrete_sequence=["#ffc434"], zoom=10, height=590)
    fig_map.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
    fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig_map


def tableCreaterByYear(year):
    df = grouper(year)
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(head_list), align='left', line_color='#ffc434', fill_color='#1f2d58',
                font=dict(color='white', size=12)),
    cells=dict(values=[df.COLLISION_ID, df.CRASH_DATE, df.CRASH_TIME,
                       df.LATITUDE, df.LONGITUDE, df.BOROUGH, df.NUMBER_OF_PERSONS_INJURED,
                       df.NUMBER_OF_PERSONS_KILLED], align='left',
               line_color='#ffc434',
               # 2-D list of colors for alternating rows
               fill_color="#1f2d58",
               font=dict(color='white', size=11)))])

    fig.update_layout(
        font={"color": "#808080"},
        title={
            'text': "In this table you are seeing the all collisions information from "+year,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor="#1f2d58")
    return fig


# Create Line Figure
def lineChartCreater():
    cols = ['Year', 'Count']
    lst = []
    xy = 2012
    for a in range(11):
        lst.append([xy, numberOfCol(str(xy))])
        xy = xy + 1
    df_line = pd.DataFrame(lst, columns=cols)
    fig_line = px.line(df_line, x="Year", y="Count")
    fig_line.update_layout(
        font={"color": "#ffc434"},
        title={
            'text': "Line chart to show count of collisions by year",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'}, paper_bgcolor="#1f2d58", plot_bgcolor="#1f2d58", xaxis_showgrid=True,
        yaxis_showgrid=False)
    fig_line.update_yaxes(matches=None, showticklabels=True, visible=True, title=None)
    fig_line.update_xaxes(matches=None, showticklabels=True, visible=True, title=None)
    return fig_line


def fig_searched(value):
    sql_search = "SELECT * FROM nyc_collisions WHERE COLLISION_ID = %s" % value
    df_searched = pd.read_sql_query(sql_search, engine)
    fig_searched = go.Figure(data=[go.Table(
        header=dict(values=list(head_list),line_color='#ffc434', fill_color='#1f2d58', align='left', font=dict(color='white', size=12)),
        cells=dict(values=[df_searched.COLLISION_ID, df_searched.CRASH_DATE, df_searched.CRASH_TIME,
                           df_searched.LATITUDE, df_searched.LONGITUDE, df_searched.BOROUGH,
                           df_searched.NUMBER_OF_PERSONS_INJURED,
                           df_searched.NUMBER_OF_PERSONS_KILLED], align='left',
                   line_color='#ffc434',
                   # 2-D list of colors for alternating rows
                   fill_color="#1f2d58",
                   font=dict(color='white', size=11)))])
    fig_searched.update_layout(
        title={
            'text': "In this table you are seeing the information about collisions, that has the id no: "+str(value),
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig_searched.update_layout(paper_bgcolor="#1f2d58")
    fig_searched.update_layout(
        font=dict(
        family="Courier New, monospace",
        size=12,
        color="white"
    ))
    return fig_searched


def randomInfoCreater():
    randon_info_array = np.array([
                                     'Queens is home to the highest number of fatal accidents. In 2018, the borough saw 69 traffic accident deaths, which is 35% percent of the city’s total. Brooklyn wasn’t far behind, with 58 reported fatalities. Manhattan and the Bronx weren’t far behind, with 28 and 33 fatal crashes, respectively. Staten Island reported the fewest number of fatalities in 2018, with 9.',
                                     'While the summer months are the most dangerous for biking, the winter months tend to pose the greatest threat for walking. Accidents involving pedestrians peak in November and December – perhaps because of increased congestion and traffic due to the holidays. In 2018, there were almost twice as many pedestrian accidents in December (1,295) as there were in July (678).',
                                     'Every year, there are thousands of motorcycle crashes in New York City. In 2018, there were a total of 2,548. Once again, Brooklyn’s streets proved to be the most dangerous:  Brooklyn: 820 motorcycle accidents, or 32.2% Queens: 693 motorcycle accidents, or 27.2%, Manhattan: 534 motorcycle accidents, or 21%',
                                     'Truck accidents happen across all five boroughs. According to crash statistics for 2018, the breakdown for truck accidents was as follows: Manhattan: 5,428 truck accidents, or 30.2%, Brooklyn: 5,028 truck accidents, or 27.9%, Queens: 3,290 truck accidents, or 21.8%, Bronx: 3,205 truck accidents, or 17.8%, and Staten Island: 401 truck accidents, or 2.2%.',
                                     '33 passengers were killed in car accidents in New York City in 2021. This is the highest yearly number of passenger fatalities since 2015 when 34 passengers died in auto accidents.  After reaching its lowest in 2018 at 8, passengers fatalities gradually climbed to 17, 28 and 33 over the next 3 years. The trend is pretty much similar to the one seen in motorist fatalities.',
                                     'The National Highway Traffic Safety Administration, a division of the Department of Transportation, estimates 42,915 people died in motor vehicle traffic crashes in 2021, a 10.5% increase from the 38,824 fatalities in 2020.',
                                     'In 2018, there were a total of 277,971 car accidents in New York City. In 2019, the Big Apple saw 206,754 collisions. In 2020, the year of a raging pandemic, reported collisions declined by 46%, for a total of 110,834.',
                                     'According to statistics from the New York Police Department, May 2021 was the third-deadliest year for fatalities since 2014 when de Blasio took office. Hit-and-runs in particular have increased. ',
                                     'In an average month in New York City, there were will about 19,000 car accidents. However, that’s just an average. Some days – and some months – see more accidents than others. According to the NYPD’s crash data, May is the month with the highest number of reported accidents (20,551), followed closely by June (20,479) and October (20,470).',
                                     'New York City has gone to great lengths to make its roads a little bit safer for bicyclists. However, bikes are still involved in a significant number of traffic accidents in the city every year. In 2018, there were 4,289 bike accidents across the five boroughs. So, roughly 2% of all traffic accidents in the city involve a bicyclist.',
                                     'In 2018, every borough with the exception of Staten Island reported at least one bicycle accident fatality. Manhattan had the most (3), while the Bronx, Brooklyn, and Queens all saw 2 fatal bike crashes. Bicyclists are much more vulnerable to sustaining injuries or dying in a traffic accident than occupants of motor vehicles.',
                                     'It might not be a surprise to learn that bike accidents surge in the warm summer months. Months with the highest number of reported bike accidents include: August: 542, or 12.6% July: 500, or 11.6%, and September: 494, or 11.5%. The fewest number of collisions involving bikes occurred in the months of January and February, with 184 and 201 accidents, respectively.',
                                     'Queens, Manhattan, and the Bronx are very dangerous for pedestrian accidents. Those boroughs account for 24.9%, 21%, and 17.3% of pedestrian accidents, respectively. Staten Island reports the fewest number of pedestrian accidents. The borough sees less than 4 percent of the city’s pedestrian-related collisions.',
                                     'When it comes to fatal pedestrian accidents, Brooklyn and Queens lead the way. In 2018, both boroughs had 35 pedestrian deaths. Manhattan and the Bronx were a little bit safer, reporting 17 and 15 fatal pedestrian crashes. Once again, Staten Island was the safest, relatively speaking, with just 5 pedestrian deaths last year.',
                                     'On average there were 1,098 deaths each year due to unintentional motor vehicle traffic-related injuries, killing 5.6 of every 100,000 New Yorkers. The rates were highest for males and New Yorkers ages 65 and older followed by those 20-24',
                                     'On average there were 136,913 emergency department (ED) visits each year due to unintentional motor vehicle traffic-related injuries, requiring the treatment of 696.6 of every 100,000 New Yorkers. The rates were highest for females and New Yorkers ages 20-24 followed by ages 15 – 19.',
                                     'On average there were 12,093 hospitalizations each year due to motor vehicle traffic-related injuries, hospitalizing 61.5 of every 100,000 New Yorkers. The rates were highest for males and New Yorkers ages 20-24 followed by those ages 65 and older.',
                                     'NYPD records show 58 people — including pedestrians — died in car crashes through April 3, a sharp increase over the 43 killed in the same period in 2021.',
                                     'For the most recent year reported, 371,368 traffic collisions occurred throughout the state of New York, according to the Traffic Safety Statistical Repository maintained by the New York Department of Motor Vehicles (DMV). These crashes resulted in 1,103 fatalities and 11,174 serious injuries. Over 100,000 additional people suffered minor to moderate injuries in these accidents.',
                                     'Traffic crashes killed 59 people in New York City during the first three months of 2022, a 44 percent increase over this point last year. The first quarter also saw the 100th child, 18-years-old and under, killed in a traffic crash since Vision Zero began in 2014.', ])
    value = randint(0, 19)
    info = randon_info_array[value]
    return info


def pieChartCreater():
    fig_pie = px.pie(df, values='NUMBER_OF_PERSONS_INJURED',
                     names='VEHICLE_TYPE_CODE_1',
                     title='Population of European continent',
                     color_discrete_map={'Thur': 'lightcyan',
                                         'Fri': 'cyan',
                                         'Sat': 'royalblue',
                                         'Sun': 'darkblue'},
                     hole=0.5
                     )
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={"color": "#ffc434"},
        title={
            'text': "Vehicles causing collisions",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
    )
    fig_pie.update_layout(showlegend=False, )
    fig_pie.update_traces(textposition='inside')
    fig_pie.update_layout(uniformtext_minsize=12)
    return fig_pie

colors = ['#ffa703', '#a8294b', '#0a7715', '#d74f67']
def pie2ChartCreater():
    fig_pie2 = px.pie(df2,
                      values='count',
                      names='VEHICLE_TYPE_CODE_2',

                      title='Population of European continent',

                      hole=0.5,

                      )
    fig_pie2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={"color": "#ffc434"},
        title={
            'text': "Vehicles affected by the collisions",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'orientation': 'h',
            'xanchor': 'center', 'x': 0.5, 'y': -0.07
        }
    )

    fig_pie2.update_layout(showlegend=True)
    fig_pie2.update_traces(textposition='inside')
    fig_pie2.update_traces(marker=dict(colors=colors))
    fig_pie2.update_layout(uniformtext_minsize=1200)
    return fig_pie2
