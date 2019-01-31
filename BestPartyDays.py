# PROJECT REQUIREMENTS
    # Must include a README file that states the following:
        # What question are you answering or problem are you analyzing
        # A brief overview of how you accomplished this, including any necessary background for someone to understand the problem, where your data came from, what you used from that data, any analysis you applied to the data, and what you chose to visualize/display/report in the final product
        # Any special requirements, dependencies, or steps to run the project
    # You must include a SQL database (MySQL or SQLite) where your data will be stored
        # You need to include the script that sets up/creates your database
    # You must include a Python script used to fetch data from a data source and load it into your SQL database
        # Your data source may be an external API, database, a CSV file, or any other data source that you can read/parse via Python code
    # You must include a Python script to retrieve the data from your SQL database into a Python object
    # Visualize the results of your analysis using Matplotlib, Seaborn, Bokeh or another Python Data Visualization library. Your results cannot be a plain text representation and you are encouraged to explore a visualization approach that clearly supports a conclusion/result of the analysis of your data.
    # Your data retrieval for visualization uses at least one SQL query, meaning you can't parse records from your data set using only Python or an ORM. Pushing and retrieving an entire dataframe to and from SQL also does not meet the requirement, e.g. the SQL query should not simply be SELECT * FROM database
    # Your project code is on your GitHub account in its own repository

# import libraries:
import requests
import datetime

# create function to determine API request for each day needed for calculations- All saturdays, sundays, and holiday mondays, 12pm-10pm from 2008, 2018 [seperate script to do before-hand and create a json or csv?]
#####Need to watch json vids####


def get_dates(range):
    for dates in range:  # 2019
        '''pick out days of calendar from 2008 through 2018 that are Saturdays, Sundays, and holiday mondays'''
        # variable values must work with darksky api in some way
        if date.day == Saturday or Sunday
        '''store date.day in new variable'''
        elif date.day ==  # third monday in februrary
        '''store date.day in new variable called 3rd_feb_mon'''
        elif date.day ==  # last monday in May
        '''store date.day in new variable called may_last_mon'''
        elif date.day ==  # second monday in october
        '''store date.day in new variable called 2nd_oct_mon'''
        elif date.day ==  # fourth monday in october
        ''' store date.day in new variable called 4th_oct_mon'''
    #  Monday Holidays to include:
    #                     Washington's Birthday: third Monday in February (formerly February 22)
    #                     Memorial Day: last Monday in May (formerly May 30)
    #                     Labor Day: first Monday in September
    #                     Columbus Day: second Monday in October (formerly observed in some states on October 12)
    #                     Veterans Day: fourth Monday in October


# stores each desired day in a variable that we can use to call the dark sky API for historical weather data of that day
# ask API to return data for that day and time slice.  Get:  Higest temp, lowest temp[possibly all hourly temps in range, which can be calculated to hi/lows after], and precipitation events, store in the variable ex: 2008_Sat_wk1 = ((year,month,day), (high temp: 40, low temp: 20, precipitation [before andor during timeslice?]: [bool or quant]))

DS_API_KEY = "00b999d3b38cbf3fd6f7c14b01244f79"
LAT = "38.2535367"
LONG = "-85.7481863"
year = "2008"
month = "01"
day = "01"
wknds_and_mons = ()

# TODO Loop that picks out selected dates and stores them in a tuple in the format needed for the API: YYYY-MM-DD
# WORKING API REQUEST
dark_sky_request = requests.get("https://api.darksky.net/forecast/" + DS_API_KEY + "/" + LAT +
                                "," + LONG + "," + year + "-" + month + "-" + day + "T00:00:01?exclude=currently,flags,alerts")
dark_sky_request.json()
#####
# TODO Loop requesting data by day.  approximately 1090 API requests needed.  API daily request max# is 1000
# TODO Output of the above loop will store json data in txt file for later use.
# TODO Function to convert Unix Time to User friendly format and rewrite that format into the txt file. Additionally, adjust time to show EST, not GMT.  ACCOUNT FOR DAYLIGHT SAVINGS


def request_loop(tuple):
    for date in tuple:
        dark_sky_request = requests.get(
            "https://api.darksky.net/forecast/" + DS_API_KEY + "/" + LAT + "," + LONG + "," + date + " 00:00:01")
        dark_sky_request.json()
    # print to txt file


request_loop(wknds_and_mons)


for time in date_lib:
    call_dark_sky(time)

# Take all aligning variables(ex: 2008_Sat_wk1, 2009_Sat_wk2, 2010_Sat_wk2, etc.) Create average high's and lows, max&min highs and lows and medians, [store in new variable?? or dict??]
# TODO set desired temp high-low range-Start at 80-65 F- create input later
# TODO create graph of all variables with avg highs and lows within desired range
# TODO show count of precipitation events
# TODO highlight or create new graph with top five days with desired temp range, and least number of precipitation events
