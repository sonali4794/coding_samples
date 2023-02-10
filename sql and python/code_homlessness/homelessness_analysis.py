import os
import pandas as pd 
import matplotlib as plt

from dotenv import load_dotenv
from sqlalchemy import create_engine

#We use a dot env file to store our database credentials which are not to be made public. This file is accessible only to the creator.
load_dotenv()

DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

#The below steps establish a connection between the database instance thta I have created in GCP and postgres. 
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
conn = engine.connect()

#Below is an exmaple of one command to read a csv file into the postgres database. 
#dfpit15 = pd.read_csv('PIT_2015.csv',encoding='cp1252')
#dfpit15.to_sql('pit2015', con=conn, if_exists='replace', index = False)

#the first query reads data on homeless count across subpopulation and focuss on 4 categories of interest
#we reduce the size and perform a useful window function here which is easiest in SQL and then read from sql into pandas dataframe
#we will later use this dataframe to plot graph
dfst1 = pd.read_sql("""
        select
	subpop ,
	no_homeless ,
	yr ,
	coc ,
	SUM(no_homeless) over(partition by yr,
	coc) as total_homeless
from
	subpop
where
	subpop = 'Mental Illness'
	or subpop = 'HIV/AIDS'
	or subpop = 'Victims of Domestic Violence'
	or subpop = 'Chronic Substance Abuse'""", con=SQLALCHEMY_DATABASE_URL)

#the second query reads data on leavers and stayers from shelter homes and subsequently how their income level has changed in due course
#We read this information across all years and combine them to generate data in long format as that will make plotting easier later on
dfst2 = pd.read_sql("""
        select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2015 as year
from
	spm2015
group by
	state
union 
select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2016 as "year"
from
	spm2016
group by
	state
union 
select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2017 as "year"
from
	spm2017
group by
	state
union
select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2018 as "year"
from
	spm2018
group by
	state
union
select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2019 as "year"
from
	spm2019
group by
	state
union
select
	"State" as state,
	sum("Total Stayers (persons)") as tot_stayers,
	sum("Total Stayers increased total income") as tot_income_incr_stayers,
	sum("Total Leavers (persons)") as tot_leavers,
	sum("Total Leavers increased total income") as tot_income_incr_leavers,
	2020 as "year"
from
	spm2020
group by
	state
order by 
	state
""", con=SQLALCHEMY_DATABASE_URL)

dfst1["proportion_homeless"] = dfst1["no_homeless"]/dfst1["total_homeless"]

def subpop_plot(data):
    """We plot the trands in portion of homelessness across the 4 subpopulation over the years, to assess the magnitude 
    of homelessness due to that category"""
    pd.pivot_table(dfst1.reset_index(),
               index='yr', columns='subpop', values='proportion_homeless'
              ).plot(subplots=True, layout=(2,2))

def income_improvement_stayer_plot(data):
    """we plot the section of stayers whose income increased over the years"""
    pd.pivot_table(dfst2.reset_index(),
               index='state', columns='year', values='income_incr_stayer'
              ).plot(subplots=True, layout=(3,3))

def income_improvement_leaver_plot(data):
    """we plot the section of leavers whose income increased over the years"""
    pd.pivot_table(dfst2.reset_index(),
               index='state', columns='year', values='income_incr_leaver'
              ).plot(subplots=True, layout=(3,3))

subpop_plot(dfst1)
income_improvement_leaver_plot(dfst2)
income_improvement_stayer_plot(dfst2)