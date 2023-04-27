# Zaman serileri ile çalışırken zamana bağlı olarak bir pencere yapısında ilerleyerek değerler üzerinde işlem yapabilmeyi sağlayan fonksiyon
df.sales.rolling(window=10).mean() # Birbirini takip eden 10 değeri seçer ve ortalamalarını alır. Bir pandas.series geri döner.

# DataFrame içinde zaman/tarih değişkeni datetime kütüphanesi ile de düzenlenebiliyor.
import datetime
df.date = df.date.apply(lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"))

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

def plot_importance(model, features, num = 3):
    feature_imp = pd.DataFrame({"Value": model.feature_importances_, "Feature": features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value", ascending=False)[0:num])
    plt.title("Features")
    plt.tight_layout()
    plt.show()                              
                                                       
# Kategorik değişken analizi                              
def categorical_value_counts(df, col, target):   
    print(df.groupby(col).agg(Count = (col, lambda x:x.count()), \
                          Ratio = (col, lambda x:x.count() / len(df)), \
                          Target_Ratio = (target, lambda x:x.sum() / df[target].sum())) \
                          .sort_values("Count", ascending = False), "\n")

# Verisetinin değişkenlerini tespit etme                                                                                     
def grab_col_names(df, cat_th=10, car_th=20):

    # Categorical Columns
    cat_cols = [col for col in df.columns if df[col].dtypes == "O"]
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes != "O"]
    cat_but_car = [col for col in df.columns if df[col].nunique() > car_th and df[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Numerical Columns
    num_cols = [col for col in df.columns if df[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    # Results
    print(f"Observations: {df.shape[0]}")
    print(f"Variables: {df.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, cat_but_car, num_cols                                                           
                              
# Sayısal değişkenlerin aykırı değerleri tespit etme ve düzeltme
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
