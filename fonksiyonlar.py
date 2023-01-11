# Veriseti görüntüleneceği zaman bütün sütunları getirir. None yerine maksimum gelecek sütun sayısı yazılabilir.
pd.set_option("display.max_columns", None)

# Veriseti görüntüleneceği zaman bütün satırları getirir. None yerine maksimum gelecek satır sayısı yazılabilir.
pd.set_option("display.max_rows", None)

# Veriseti görüntüleneceği maksimum genişliği belirtir. None yerine tam sayı yazılabilir.
pd.set_option("display.width", None)

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
