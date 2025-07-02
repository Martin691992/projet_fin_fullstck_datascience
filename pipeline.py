import pandas as pd

chunksize = 100_000  # 100 000 lignes par bloc

for index, chunk in enumerate(pd.read_csv('C:/Users/bonna/Downloads/StockUniteLegale_utf8/StockUniteLegale_utf8.csv', chunksize=chunksize)):
    if index == 1 :
        break
    tri = chunk[['etatAdministratifUniteLegale','']]
    print(chunk)
