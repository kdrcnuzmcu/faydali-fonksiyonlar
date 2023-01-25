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

# Verisetindeki aykırı değerleri baskılamak için limit belirleme.
def aykiri_limit(df, col):
  Q1 = df[col].quantile(0.01)
  Q3 = df[col].quantile(0.99)
  IQR = Q3 - Q1
  upLimit = Q3 + (1.5 * IQR)
  lowLimit = Q1 - (1.5 * IQR)
  return lowLimit, upLimit

# Verisetindeki aykırı değerleri belirlenen limitlere baskılama
def aykiri_baskilama(df, col):
  lowLimit, upLimit = aykiri_limit(df, col)
  df.loc[(df[col] < lowLimit), col] = lowLimit
  df.loc[(df[col] > upLimit), col] = upLimit
