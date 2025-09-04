import pandas 

try:
    dtype_optimization={
        'coloumn1': 'int32',
        'coloumn2':'catagory'
    }
    df =pandas.read_csv('sales_data.csv',dayfirst='dtype_optimization')
except Exception as e:
    print(e)
    df= pandas.read_csv('sales_data.csv')

print(df.dtypes)
print(df.head())
print(df.fd.memory_usage())
