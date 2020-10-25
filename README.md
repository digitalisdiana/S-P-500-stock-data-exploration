## Investment Portfolio Strategy Development : Data Analysis

This 6 Part Series is a guide to the tech curious Financial Investor. It breaks down the entire process of building an informed portfolio making the most out of the best free tools of forecast available on the market. This series has been made possible thanks to SentDex's guided project :>> https://bit.ly/31xc1no.

The different Python files and their contents are :

- Part1.py : Amazon Intro

This is the introductory part of the project; it explores aspects such as retrieving stock price data, grapnhing and handling data as well as techniques of stock data manipulation.
To simplify the process, we have only used data from one company : Amazon. This introduction prepares us for what is to come : manipulating stock data for multiple entities of a market or across markets.

- Part2.py : Complete S&P 500 overview

Here we start an exploration of data points for a greater list of companies. We first consult the list of S&P from wikipedia then automate the process of getting the S&P 500 list. We also get all company pricing data in the S&P 500, combine them all on one dataframe, before creating a correlation table {using their Adjusted Close values} of all the companies. It must be noted that, in the example, the number of companies has been limited to 81; in order to see the entirety of the S&P 500 in one dataframe, one can simply delete the "{}" on line "{}" in the code.

- Part3.py : Creating Machine Learning Model

Now that we have all of our training data into the dataframe, it is time we get to predicting!
