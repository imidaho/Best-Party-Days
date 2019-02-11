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
########## WORKIING CODE #########
# import libraries:
import requests
import datetime
# for get_potential_dates
from datetime import date
import calendar


DS_API_KEY = "00b999d3b38cbf3fd6f7c14b01244f79"
LAT = "38.2535367"
LONG = "-85.7481863"

potential_dates = []
this_day_in_time = []
year = 2019


def get_potential_dates(year):
    c = calendar.TextCalendar(calendar.SUNDAY)
    for m in range(1, 13):
        for i in c.itermonthdays(year, m):
            # calendar constructs months with leading zeros (days belongng to the previous month)
            if i != 0:
                day = date(year, m, i)
                if day.weekday() == 0:
                    #   Monday Holidays to include:
                        #   Presidents day: third Monday in February (formerly February 22)
                        #   Memorial Day: last Monday in May (formerly May 30)
                        #   Labor Day: first Monday in September
                        #   Columbus Day: second Monday in October (formerly observed in some states on October 12)
                        #   Veterans Day: fourth Monday in October
                    if m == 2 and 15 <= i <= 21:  # third Monday
                        potential_dates.append(
                            "{}-0{}-{}, President's Day".format(year, m, i))
                    if m == 5 and 25 <= i <= 31:  # last monday of May
                        potential_dates.append(
                            "{}-0{}-{}, Memorial Day".format(year, m, i))
                    if m == 9 and 1 <= i <= 7:  # 1st Monday
                        potential_dates.append(
                            "{}-0{}-{}, Labor Day".format(year, m, i))
                    if m == 10 and 8 <= i <= 14:  # 2nd Monday
                        potential_dates.append(
                            "{}-{}-{}, Columbus Day*".format(year, m, i))
                    if m == 10 and 22 <= i <= 28:  # 4th Monday
                        potential_dates.append(
                            "{}-{}-{}, Veterans Day".format(year, m, i))
                if day.weekday() == 5 or day.weekday() == 6:  # if its Saturday or Sunday
                    if m < 10:  # output needs to be YYYY-MM-DD
                        if i < 10:
                            potential_dates.append(
                                "{}-0{}-0{}".format(year, m, i))
                        else:
                            potential_dates.append(
                                "{}-0{}-{}".format(year, m, i))
                    elif m > 9 and i < 10:
                        potential_dates.append("{}-{}-0{}".format(year, m, i))
                    else:
                        potential_dates.append("{}-{}-{}".format(year, m, i))


def request_loop(list, year, years_back):
    for target_day in list:
        mm_dd = target_day[5:]
        starting_year = int(year) - years_back
        ending_year = int(year)-1
        for year in range(starting_year, ending_year):
            dark_sky_request = requests.get("https://api.darksky.net/forecast/" + DS_API_KEY + "/" + LAT +
                                            "," + LONG + "," + str(year) + "-" + mm_dd + "T00:00:00?exclude=currently,flags,alerts")
            this_day_in_time.append(dark_sky_request.json())


get_potential_dates(year)
request_loop(potential_dates, year, years_back)
request_loop(test_list, 2014, 6)
print(this_day_in_time)


#####Need to watch json vids####


# TODO stores each desired day in a variable that we can use to call the dark sky API for historical weather data of that day
# TODO ask API to return data for that day and time slice.  Get:  Higest temp, lowest temp[possibly all hourly temps in range, which can be calculated to hi/lows after], and precipitation events, store in the variable ex: 2008_Sat_wk1 = ((year,month,day), (high temp: 40, low temp: 20, precipitation [before andor during timeslice?]: [bool or quant]))
# TODO Loop requesting data by day.  approximately 1090 API requests needed.  API daily request max# is 1000
# TODO Output of the above loop will store json data in txt file for later use.
# TODO Function to convert Unix Time to User friendly format and rewrite that format into the txt file. Additionally, adjust time to show EST, not GMT.  ACCOUNT FOR DAYLIGHT SAVINGS
# Take all aligning variables(ex: 2008_Sat_wk1, 2009_Sat_wk2, 2010_Sat_wk2, etc.) Create average high's and lows, max&min highs and lows and medians, [store in new variable?? or dict??]
# TODO set desired temp high-low range-Start at 80-65 F- create input later
# TODO create graph of all variables with avg highs and lows within desired range
# TODO show count of precipitation events
# TODO highlight or create new graph with top five days with desired temp range, and least number of precipitation events
