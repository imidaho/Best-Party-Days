Hello!  

My project answers the question:  "What weekend days or extended holiday weekend days will be the best candidates to host a party at Code Louisville headquarters in 2019?"

The goal of this project is to predict the best (standard and extended) weekdend days to host an outdoor party at Code Louisville Headquarters in 2019. So, in essence, I am assuming that this party will take place on either a Saturday, Sunday, or a Holiday Monday, such as Labor Day.  

I have provided some code in my file that I had to use to get my data, but you will not need to run in order to test my project.  I have commented out the functions that you will need to call in order to spare your computer the demands on your RAM.  

My first step was to create a script to determine what dates in 2019 fell on a Saturday, a Sunday or a holiday Monday, format them to match the api call I will be using (Dark Sky), and store them in a list called 'potential_dates'.  I Then ran the list of potential dates to pull weather summary data for Code Louisville Headquarters for the past ten years, and stored that data into a CSV and into a .db file.  

I ran into some troubles with the datetime library and converting the Unix time to a MM-DD-YYY format, so I appended lists with those dates and years at the end of the loop to facilitate my sorting needs for visualization


Dependencies:
import requests
import pandas as pd
import sqlite3
from datetime import date
import calendar
import matplotlib.pyplot as plt


        # What question are you answering or problem are you analyzing
        # A brief overview of how you accomplished this, including any necessary background for someone to understand the problem, where your data came from, what you used from that data, any analysis you applied to the data, and what you chose to visualize/display/report in the final product
        # Any special requirements, dependencies, or steps to run the project
