# Bir sözlük yapısını değerleri ölçüsünde sıralamak
sorted(example.items(), key = lambda x:x[1], reverse = True)

# Datetime tipinde olmayan tarih değişkenlerini datetime olarak atar.
df["Date"] = pd.to_datetime(df["Date"])
# Datetime değişkenine çevirdiğimiz değişkenden "yıl" değerini alır.
df["Date"].dt.year
# Tarih + Saat şeklinde değişkenlerden yalnızca tarihi alabilmemizi sağlar.
df["Date"].dt.date

# Requests modülü ile API'dan alınan JSON formatındaki verileri .get fonksiyonu ile aldık. Pandas modülünün .json_normalize() fonksiyonunun içine 
# parametre olarak gönderdik. JSON formatını Pandas DataFrame yapısına çevirmiş oldu.
import requests
import pandas as pd
url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)
data = pd.json_normalize(response.json())
data.head()

# Bir veriseti değişkeni/sütunu üstünde döngü ile gezmek istediğimizde ve aynı zamanda her değerin indeks değerini istediğimizde .enumerate() fonksiyonunu kullanabiliriz.
for index, value in enumerate(dataframe[column]:
    # value = döngü ile sütundaki değerleri tek tek gezerken taşıdığımız değerler
    # index = sütun üstündeki değerlerde gezerken o değerin bulunduğu indeks değerini taşır                              

# Bir veriseti üstünde döngü ile satır satır gezmek istediğimizde .iterrows() fonksiyonunu kullanabiliriz.                              
for index, rows in dataframe.iterrows():
    # rows = döngü ile verisetinde gezerken her bir satırını taşır. rows[col] ifadesi ile seçim yapabiliriz.
    # index = her satırın indeks değerini taşır. 
                              
# Veriseti görüntüleneceği zaman bütün sütunları getirir. None yerine maksimum gelecek sütun sayısı yazılabilir.
pd.set_option("display.max_columns", None)

# Veriseti görüntüleneceği zaman bütün satırları getirir. None yerine maksimum gelecek satır sayısı yazılabilir.
pd.set_option("display.max_rows", None)

# Veriseti görüntüleneceği maksimum genişliği belirtir. None yerine tam sayı yazılabilir.
pd.set_option("display.width", None)
       
# Verisetini tek bir satır halinde göstermeye çalışır
pd.set_option("display.expand_frame_repr",  False)                              

def outliers(df, col, low_Quantile = 0.25, high_Quantile = 0.75, adjust = False):  
    Q1 = df[col].quantile(low_Quantile)
    Q3 = df[col].quantile(high_Quantile)
    IQR = Q3 - Q1
    low_Limit = Q1 - (1.5 * IQR)
    up_Limit = Q3 + (1.5 * IQR)
    
    if len(df[df[col] > up_Limit]) > 0:
        print(col, ": Higher Outlier!")
    if len(df[df[col] < low_Limit]) > 0:
        print(col, ": Lower Outlier!")
        
    if adjust:
        df.loc[(df[col] < low_Limit), col] = low_Limit
        df.loc[(df[col] > up_Limit), col] = up_Limit
        print(col, ": Done!")
