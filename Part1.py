import pandas as pd
import datetime as dt
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader.data as web
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc

style.use("ggplot")

start = dt.datetime(2010, 2, 15) #Upper bound limit
end = dt.datetime(2020, 9, 27)#Lower bound limit
df = web.DataReader("AMZN", "yahoo", start, end) # Using yahoo API to pull data from S&P 500 logs

print(df.head(9)) #Test print the 9 most ancient entries

print(df.tail(18)) #Test print the 18 most recent entries

df.to_csv("amazon.csv") #Converts all the data into comma separated values
df = pd.read_csv("amazon.csv", parse_dates = True, index_col = 0) #Reads the dataframe previously saved as csv, parse the dates, and assign them as the index column {as opposed to the default [0::] indexing}

print(df.head()) #Test print
df.plot()

print(df["Volume"].head()) #Testing a plot call for simply the Volume column and only asking for the oldest five data points
plt.show()

df["90ma"] = df["Adj Close"].rolling(window=90).mean() #Calculates the moving average over 90 days
print(df.head()) #Test print which should NaN at the column "90ma" for all of the 5 rows printed {it should do the same for the 90 first rows}

df.dropna(inplace=True) #Will simply take out of the data frame call, the days where "90ma" is NaN

"""
To bypass the .dropna funtion, we can simply set the minimum period required to "calculate" "90ma" to zero. This allows for the column "90ma" to be populated by incremented averages of "Adj Close" from the very first day onwards. {as it reaches 90 days, the intended window calculations will take effect}
The code will look like this : df["90ma"] = df["Adj Close"].rolling(window = 90, min_periods = 0).mean() #Feel free to copy and test it.
"""
print(df.tail()) #Test Print

"""
Let us now create two subplots on a 6x1 grid

    their second variables indicate where they start
    the function sharex aligns ax2's x-axis to ax1's
"""

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)

ax1.plot(df.index, df["Adj Close"]) #Adj Close on the first axis
ax1.plot(df.index, df["90ma"]) #90ma on the first axis
ax2.bar(df.index, df["Volume"]) #Volume on the second axis
plt.show()

"""
The coming part brings us all the way back to when we read and parsed the "amazon.csv" file. We are going to explore resampling {depending of the time span of our liking as to adjust data granularity} using candlestick_ohlc from the python module matplotlib.finance {we are going to set up the import at the top of the script}. We'll use the module on "Adj Close". We'll resample to every 18 days of data.
It is worth noting that appropriate OHLC data is necessary. Splits in company history, for example, can render such an analysis a little bumpy.
"""

df_ohlc = df["Adj Close"].resample("18D").ohlc() #Defining OHLC data with resampled data points for every 45 minutes
df_volume = df["Volume"].resample("18D").sum() #Resampling the volume just the same but asking for a ".sum()" as to reflect the actual {true} volume

print(df_ohlc.head()) #Test print of data points

"""
Reminder that we had already set the dates as indexes; however, with ohlc, we no longer want that. We'll simply reset the indexes to the default [0::] format.
"""

df_ohlc.reset_index(inplace = True) 
print(df_ohlc.head()) #Verification

df_ohlc["Date"] = df_ohlc["Date"].map(mdates.date2num) #Map out the dates after converting our current date time objects to matplotlib's mdates
print(df_ohlc.head()) #Test print

ax1.xaxis_date() #Convert m_dates back to beautiful dates
print(df_ohlc.tail()) #Test print

""" 
Now to map it into a comprehensive OHLC graph.
"""

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()
