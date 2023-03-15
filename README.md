# Data_Engineer_crypto_Assignment

## Code has two version   --i)   Notebook II)   modular(oops) way .

modular(oops way project structure)

![image](https://user-images.githubusercontent.com/71961635/225427177-d2312255-9b03-496c-8659-4fdfa81207d6.png)


For better understanding prefer Notebook.I used pyspark in code ,in some system pyspark.session can throw java.gateway error. 
For that reason you can execute ipython notebook in google colab.

# Dataframe look like

![image](https://user-images.githubusercontent.com/71961635/225378918-8826b13b-ac55-42f7-85df-4ef87d9d73ac.png)


## only bitcoin
![image](https://user-images.githubusercontent.com/71961635/225386734-8a57eafb-1b7f-4998-9aba-274d4251cebe.png)

## only etherium
![image](https://user-images.githubusercontent.com/71961635/225386997-c62da3b7-85ec-4448-a20b-7f8c4610a645.png)

## TOP 5 CRYPTO 
![image](https://user-images.githubusercontent.com/71961635/225389208-b52089a1-e951-4bef-b29b-570d80db7ca0.png)

![image](https://user-images.githubusercontent.com/71961635/225389592-451b2122-6209-4538-819b-2cfd8248f218.png)

![image](https://user-images.githubusercontent.com/71961635/225389860-ec6d0262-a4af-4c72-a6cd-2d27961ff6cf.png)

## AVERAGE PRICE OF BTC IN LAST 30 DAYS
![image](https://user-images.githubusercontent.com/71961635/225408659-d5c08c06-34b2-40df-a868-13ad1b6ce2bb.png)

## MAX,MIN AND STD OF BTC IN LAST 30 DAYS
![image](https://user-images.githubusercontent.com/71961635/225408742-93b08185-aa96-4798-9a40-4b46575c5a83.png)
![image](https://user-images.githubusercontent.com/71961635/225408781-e959ec5f-1ac1-4f88-b7bb-b94f03755a54.png)


## AVERAGE PRICE OF ETH IN LAST 30 DAYS

![image](https://user-images.githubusercontent.com/71961635/225409106-929c5ebd-c6ef-4129-aa0f-2614b3794581.png)

## MAX,MIN, STD PRICE OF ETH IN LAST 30 DAYS
![image](https://user-images.githubusercontent.com/71961635/225409173-f5d2add4-654f-48e9-9dc9-697f7287a5c4.png)
![image](https://user-images.githubusercontent.com/71961635/225409220-33ff0e50-4199-4eed-a107-c8c41c1f9a79.png)

## CORRELATION BETWEEN  ETHEREUM OPEN VS BITCOIN OPEN
![image](https://user-images.githubusercontent.com/71961635/225409378-06ab0e51-d6ec-49df-b62e-00292d503902.png)

## CORRELATION HEATMAP
![image](https://user-images.githubusercontent.com/71961635/225412651-22962f66-3a74-491b-b79a-13c51f8a727f.png)
![image](https://user-images.githubusercontent.com/71961635/225412694-b0c575c5-b380-47d7-9758-d88665ab74b6.png)

## NO OUTLIERS
![image](https://user-images.githubusercontent.com/71961635/225412825-51e4232c-364b-4147-993b-df4aaa50e25a.png)
## BITCOIN MARKET OPEN PRICE VS DATE
![image](https://user-images.githubusercontent.com/71961635/225414558-7d534798-6cae-4cf3-bbc7-3e0dac7b2b8f.png)

## BITCOIN VS ETHEREUM MARKET OPEN PRICE
![image](https://user-images.githubusercontent.com/71961635/225414723-bb1256a1-8eeb-47be-aab5-a350653a329b.png)

# CONCLUSION :-> BEST CRYPTO IS BITCOIN .BEST INESTMENT WILL BE BITCOIN,THEN ETHEREUM.BITCOIN PRICE ALWAYS HIGHER THAN ANY OTHER CRYPTO.


#                                **** LOAD DATA IN S3 USIN LAMBDA****
# CREATING AN AWS LAMDA FUNCTION & WRITE DOWN PYTHON CODE TO LOAD DATA IN S3
![image](https://user-images.githubusercontent.com/71961635/225418739-8f2f4743-5623-43fe-8ce9-3e9486371dee.png)

![image](https://user-images.githubusercontent.com/71961635/225418808-9ca30003-66a3-413d-91f7-275e753b4bb6.png)
## CONFIGURE LAMBDA  FUNCTION SETTINGS AND SERVICE ROLE.
![image](https://user-images.githubusercontent.com/71961635/225419792-997f730c-92b4-4001-9d2c-ffc92e4fb9a1.png)

## CREATE A S3 BUCKET
![image](https://user-images.githubusercontent.com/71961635/225430602-21bb9193-5433-4f30-b9e6-837cb13b1030.png)

## LOAD DATA INTO S3 USING PYTHON CODE
![image](https://user-images.githubusercontent.com/71961635/225419253-38de7339-1db6-45b2-977d-4c1dc029cc3d.png)

#                         ****HOW TO RUN PROJECT****
## I)  CLONE THE PROJECT
## II) pip install -r requirements.txt 
## III) FIRST RUN webscrap.py FILE,IT WILL SCRAP  DATA FROM COINDCX API(https://docs.coindcx.com/?python#candles) AND GENERATE A cryptocurrencies_df.csv FILE
## IV)  THEN RUN crypto_analysis.py FILE to GET ANALYSIS RESULTFROM cryptocurrencies_df.csv
## V)   lambda_code.py WILL RUN PROPERLY IN AWS LAMBDA


