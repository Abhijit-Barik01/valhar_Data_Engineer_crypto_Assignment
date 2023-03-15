# Import Libraries
#THIS CODE FOR AWS LAMBDA .U HAVE TO COPY PASTE THERE
import json
import numpy as np
import requests
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import boto3
def lambda_handler(event, context):
    try:
        coin_list = ['BTC', 'ETH', 'XRP', 'ADA', 'USDT', 'DOGE', 'XLM', 'DOT', 'UNI', 'LINK', 'USDC', 'BCH', 'LTC', 'GRT', 'ETC', 'FIL', 'AAVE', 'ALGO', 'EOS']

    #defining the dataframe
        main_df = pd.DataFrame()

        for coin in coin_list:
            coin_df = pd.DataFrame()
            df = pd.DataFrame(index=[0])
    
    # Defining the Start Date and End Date
            datetime_end = datetime(2023, 3,14, 0, 0)
            datetime_check = datetime(2023, 3, 10, 0, 0)
    
            while len(df) > 0:
                if datetime_end == datetime_check:
                    break
        
                datetime_start = datetime_end - relativedelta(hours = 12)
        
        #Api for the scrapping
                url = 'https://production.api.coindesk.com/v2/price/values/'+ coin +'?start_date='+datetime_start.strftime("%Y-%m-%dT%H:%M") + '&end_date=' + datetime_end.strftime("%Y-%m-%dT%H:%M") + '&ohlc=true'
        
        #we are using the request to fetch the data from the api in the json format and then storing it into the dataframe.
                temp_data = requests.get(url).json()
                current_epoch_time = datetime.now().timestamp()
                BUCKET_NAME="bucketi123"
                print("Start Data Write in S3")
                s3 = boto3.resource('s3')
                s3object = s3.Object(BUCKET_NAME, f"inbox/{str(current_epoch_time)}_crypto_data.json")
                s3object.put(Body=(bytes(json.dumps( temp_data ).encode('UTF-8'))))
                print("Data Write Successfull in S3")
                
    except Exception as err:
        print(err)
 