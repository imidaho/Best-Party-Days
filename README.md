Hello!  

My project answers the question:  "What weekend days or extended holiday weekend days will be the best candidates to host a party at Code Louisville headquarters in 2019?"

The goal of this project is to predict the best (standard and extended) weekend days to host an outdoor party at Code Louisville Headquarters in 2019. So, in essence, I am assuming that this party will take place on either a Saturday, Sunday, or a Holiday Monday, such as Labor Day.  

My first step was to create a script to determine what dates in 2019 fell on a Saturday, a Sunday or a holiday Monday, format them to match the api call I will be using (Dark Sky), and store them in a list called 'potential_dates'.  I Then ran the list of potential dates to pull weather summary data for Code Louisville Headquarters for the past ten years, and stored that data into a CSV and into a .db file.  

I ran into some troubles with the datetime library and converting the Unix time to a MM-DD-YYY format, so I appended lists with those dates and years at the end of the loop to facilitate my sorting needs for visualization.  Future versions will omit this 'hack' and include the highs and lows from 12pm to 10pm only.  

YOU DO NOT NEED TO RUN THE LOOP.  I've left it in the notebook so you can see it, and I kinda want to show it off.  BUT the .CSV file is already populated, so I've commented out the line that runs the loop. You can run the loop if you like, but it takes several minutes to finish (it'll cost me like 10 cents too if you run it for ten years of weather history :-) )

You will need to update your pandas library if your current library is older than version 0.14.  The SQL to pd.dataframe hand-off will not work without pandas version 0.14 or newer.  

The first graph shows the Saturdays, Sundays or Monday Holidays where the average high temps are below 80 degrees, and the average low temps stay above 50 degrees.  The second graph shows the number of times it has rained on the corresponding dates from the above graph for the past ten years.  

Dependencies:
requests
pandas version 0.14 or later
sqlite3
datetime
calendar
matplotlib.pyplot
