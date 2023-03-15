#importing libraries
import os
import pyspark
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import warnings
warnings.filterwarnings("ignore")
import matplotlib.dates as mdates


class Analysis:
    def  __init__(self):
        pass
    def analysis_helper(self):
        df=pd.read_csv('cryptocurrencies_df.csv')

        df['Datetime']=pd.to_datetime(df['Datetime']).dt.date

        print(df)

        spark = SparkSession.builder.appName('CheckPyspark').master("local").getOrCreate()

        sparkDF=spark.createDataFrame(df)

        sparkDF.createOrReplaceTempView("crypto")

        dfBTC = spark.sql(" select * from crypto where Symbol='BTC' ")

        #df.show()

        dfETH = spark.sql(" select * from crypto where Symbol='ETH' ")

        #dfETH .show()

        pandasBTCDF = dfBTC.toPandas()
        pandasETHDF = dfETH.toPandas()


        print("Finding the top 5 crytpocurrencies by market closing time")

        plt.figure(figsize=(18,5))
        ax = df.groupby(['Symbol'])['Close'].last().sort_values(ascending=False).head(5).sort_values().plot(kind='barh')
        ax.set_xlabel("Market Closing price (in billion USD)")
        ax.ticklabel_format( style='plain', axis='x')
        plt.title("Top 5 Cryptocurrencies by Market Closing time", fontsize=15)
        plt.show()

        print("Plotting Graphs of Closing Prices of Top 4 Cryptocurrencies as per Market Cap")

        dx=df.copy()

        top_4_currency_names = dx.groupby(['Symbol'])['Close'].last().sort_values(ascending=False).head(4).index
        top_4_currency_names_except_first=dx[dx['Symbol']!='BTC'].groupby(['Symbol'])['Close'].last().sort_values(ascending=False).head(4).index
        top_4_currency_names_except_first_two=dx[(dx['Symbol']!='BTC') & (dx['Symbol']!='ETH')].groupby(['Symbol'])['Close'].last().sort_values(ascending=False).head(4).index
        top_4_currency_names_except_first_two_three=dx[(dx['Symbol']!='BTC') & (dx['Symbol']!='ETH')& (dx['Symbol']!='USDT')].groupby(['Symbol'])['Close'].last().sort_values(ascending=False).head(4).index


        data_top_4_currencies = dx[dx['Symbol'].isin(top_4_currency_names)]
        top_4_currencies_after_BTC = dx[dx['Symbol'].isin(top_4_currency_names_except_first)]
        top_4_currencies_after_BTC_ETH = dx[dx['Symbol'].isin(top_4_currency_names_except_first_two)]
        top_4_currencies_after_BTC_ETH_USDT = dx[dx['Symbol'].isin(top_4_currency_names_except_first_two_three)]

        plt.figure(figsize=(20,25))

        plt.subplot(4,1,1)
        sns.lineplot(data=data_top_4_currencies, x="Datetime", y="Close", hue='Symbol')
        plt.title("Closing Prices of Top 4 Cryptocurrencies", fontsize=20)
        plt.legend(loc='upper left')

        plt.subplot(4,1,2)
        sns.lineplot(data=top_4_currencies_after_BTC, x="Datetime", y="Close", hue='Symbol')
        plt.title("Closing Prices of Top 4 Cryptocurrencies except BTC", fontsize=20)
        plt.legend(loc='upper left')

        print("Pattern of data: bitcoin value always greater than etherium")

        print("Last 30 days average,max,min,std of Bitcoin")
    

        df_last30 = pandasBTCDF.groupby(['Datetime']).tail(30)
        #last 30 days Btc average
        df_average=df_last30.mean(axis = 0)
        print("Last 30 days average price of Bitcoin\n",df_average)
        print("\n\n")
        df_btcmax=df_last30.max()
        df_btcmin=df_last30.min()
        print("Last 30 days MAX price of Bitcoin \n",df_btcmax)
        print("\n\n")
        print("Last 30 days MIN price of Bitcoin \n",df_btcmin)
        print("\n\n")
        stddf=df_last30.std(axis = 0, skipna = True)
        print("standard deviation",stddf)

        df1_last30 = pandasETHDF.groupby(['Datetime']).tail(30)
        #last 30 days Btc average
        df1_average=df1_last30.mean(axis = 0)
        print("Last 30 days average price of Ethereum \n",df1_average)
        print("\n\n")
        df1_ethmax=df1_last30.max()
        df1_ethmin=df1_last30.min()
        print("Last 30 days MAX price of Ethereum \n",df1_ethmax)
        print("\n\n")
        print("Last 30 days MIN price of Ethereum \n",df1_ethmin)
        print("\n\n")
        stddf1=df1_last30.std(axis = 0, skipna = True)
        print("standard deviation",stddf1)

        print("Correlation between Ethereum OPEN VS BITCOIN OPEN",df1_last30['Open'].corr(df_last30['Open']))
        print("Correlation between Ethereum CLOSE VS BITCOIN CLOSE",df1_last30['Close'].corr(df_last30['Close']))

        # adds the title
        plt.title('Correlation')

        # plot the data
        plt.scatter(df_last30['Open'],df1_last30['Open'])

        # fits the best fitting line to the data
        plt.plot(np.unique(df_last30['Open']),
                np.poly1d(np.polyfit(df_last30['Open'], df1_last30['Open'], 1))
                (np.unique(df1_last30['Open'])), color='red')

        # Labelling axes
        plt.xlabel('ETC axis')
        plt.ylabel('ETH axis')

    

        # checking correlation using heatmap
        #Loading dataset
 

        print("plotting the heatmap for correlation\n")
        ax = sns.heatmap(pandasETHDF.corr(), annot=True)

        print("NO OUTLIERS")

        fig = px.box(df_last30,df_last30['Low'])

        fig.show()

        print("How do the prices of Bitcoin and Ethereum vary")

        datebtc=df_last30['Datetime']
        valuebtc=df_last30['Open']
        fig, ax = plt.subplots(figsize=(18, 10))
        ax.plot(datebtc, valuebtc);

        datebtc=df_last30['Datetime']
        valuebtc=df_last30['Open']
        datebtc1=df1_last30['Datetime']
        valuebtc1=df1_last30['Open']
        fig, ax = plt.subplots(figsize=(18, 6))

        half_year_locator = mdates.MonthLocator(interval=200)
        ax.xaxis.set_major_locator(half_year_locator) # Locator for major axis only.
        line1, = ax.plot(datebtc, valuebtc, label='Bitcoin')
        line2, = ax.plot(datebtc1,valuebtc1, label='Ethereum')
        ax.legend(handles=[line1, line2])
        #ax.plot(datebtc, valuebtc,datebtc1,valuebtc1,label='Bitcoin VS Ethereum market open price');
        plt.xlabel("Date")
        plt.ylabel("Market open price")
        plt.title('Bitcoin VS Ethereum market open price')
        ax.legend()

        fig, ax = plt.subplots(figsize=(18, 6))

        half_year_locator = mdates.MonthLocator(interval=200)
        ax.xaxis.set_major_locator(half_year_locator) # Locator for major axis only.

        ax.plot(datebtc, valuebtc,label='Bitcoin market open price')
        plt.xlabel("Date")
        plt.ylabel("Market open price")
        plt.legend()


if __name__=="__main__":
    obj=Analysis()
    obj.analysis_helper()