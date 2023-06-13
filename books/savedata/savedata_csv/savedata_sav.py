from geturlcocument.get_single_docuemnt import get_single
import pandas as pd
# 获取字典类型的数据
data=get_single.get_single()
# 用pandas的DataFrame类型存储数据
df=pd.DataFrame(data)
df.to_csv('./books.csv',encoding='utf-8')
print('ending of data')