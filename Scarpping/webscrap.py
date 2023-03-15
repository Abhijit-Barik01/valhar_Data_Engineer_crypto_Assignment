# Import Libraries
import requests
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Scrap:
    def __init__(self):
        pass
    # The List of 20 type of cryptocurrency
    def ScrapCsv(self):
        coin_list = ['BTC', 'ETH', 'XRP', 'ADA', 'USDT', 'DOGE', 'XLM', 'DOT', 'UNI', 'LINK', 'USDC', 'BCH', 'LTC', 'GRT', 'ETC', 'FIL', 'AAVE', 'ALGO', 'EOS']

        #defining the dataframe
        main_df = pd.DataFrame()

        for coin in coin_list:
            coin_df = pd.DataFrame()
            df = pd.DataFrame(index=[0])
            
            # Defining the Start Date and End Date
            datetime_end = datetime(2023, 3,14, 0, 0)
            datetime_check = datetime(2023, 2, 10, 0, 0)
            
            while len(df) > 0:
                if datetime_end == datetime_check:
                    break
                
                datetime_start = datetime_end - relativedelta(hours = 12)
                
                #Api for the scrapping
                url = 'https://production.api.coindesk.com/v2/price/values/'+ coin +'?start_date='+datetime_start.strftime("%Y-%m-%dT%H:%M") + '&end_date=' + datetime_end.strftime("%Y-%m-%dT%H:%M") + '&ohlc=true'
                
                #we are using the request to fetch the data from the api in the json format and then storing it into the dataframe.
                temp_data = requests.get(url).json()
                df = pd.DataFrame(temp_data['data']['entries'])
                df.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
                
                # To handle the Missing Data
                insert_ids_list = [np.nan]

                
                while len(insert_ids_list) > 0:
                    timestamp_checking = np.array(df['Timestamp'][1:]) - np.array(df['Timestamp'][:-1])
                    insert_ids_list = np.where(timestamp_checking!= 60000)[0]
                    if len(insert_ids_list) > 0:
                        print(str(len(insert_ids_list)) + ' mismatched.')
                        insert_ids = insert_ids_list[0]
                        temp_df = df.iloc[insert_ids.repeat(int(timestamp_checking[insert_ids]/60000)-1)].reset_index(drop=True)
                        temp_df['Timestamp'] = [temp_df['Timestamp'][0] + i*60000 for i in range(1, len(temp_df)+1)]
                        df = df.loc[:insert_ids].append(temp_df).append(df.loc[insert_ids+1:]).reset_index(drop=True)
                        insert_ids_list = insert_ids_list[1:]
                        
                
                #adding datetime and symbol to dataframe
                df = df.drop(['Timestamp'], axis=1)
                df['Datetime'] = [datetime_end - relativedelta(minutes=len(df)-i) for i in range(0, len(df))]
                coin_df = df.append(coin_df)
                datetime_end = datetime_start
                
            coin_df['Symbol'] = coin
            main_df = main_df.append(coin_df)

        main_df = main_df[['Datetime', 'Symbol', 'Open', 'High', 'Low', 'Close']].reset_index(drop=True)
        print(main_df)
        #writing into csv 
        main_df.to_csv('cryptocurrencies_df.csv', index=False)



if __name__=="__main__":
    obj=Scrap()
    obj.ScrapCsv()