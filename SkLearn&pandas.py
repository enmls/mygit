####################本知识点纯手打,python3.7.9环境,2021######################################################
data = {'size':['XL','L','M',np.NaN,'M','M'],
        'color':['red','green','blue','green','red','green'],
        'gender':['female','male',np.NaN,'female','female','male'],
        'price':[199.0,89.0,np.NaN,129.0,79.0,89.0],
        'weight':[500,450,300,np.nan,410,np.nan],
        'bought':['yes','no','yes','no','yes','no']
        }
#############################################################一,##每列缺失值的比例##########################################

df = pd.DataFrame(data).isnull().sum()  #显示每列缺失值个数
f1 = np.round(df/len(df),2)              #每一列空值比例

#############################################################二,填充weight列缺失值######################################

#nan值用均值来填充
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

#@二维数组所以两个[[]]
df[['weight']] = imputer.fit_transform(df[['weight']])
"""
fit() ：用于从训练数据生成学习模型参数

transform()：从fit()方法生成的参数，应用于模型以生成转换数据集。

fit_transform()：在同一数据集上组合fit()和transform()api
"""
####已经使用了SimpleImputer填充了缺失值,怎么知道填充了那个数值?
list_1=imputer.statistics_
print(list_1)

#############################################################三,使用常量99.0填充price一列的缺失值#####################
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,
                        strategy='constant',
                        fill_value=99.0)
df[['price']] = imputer.fit_transform(df[['price']])

print(df)

list_2 = imputer.statistics_
print(list_2) #打印填充值

#############################################################四,使用一列中最频繁出现的值填充缺失值#####################
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,
                        strategy="most_frequent")
df[['size']] = imputer.fit_transform(df[['size']])

print(df)

list_2 = imputer.statistics_
print(list_2)

##-----------------------------------------------------------五,1,过滤掉weight不为空值得行------------------------
print(df[-df["weight"].isnull()])
##-----------------------------------------------------------五,2,筛选出数字类型得列------------------------
print(df[-df["weight"].isnull()].select_dtypes(include=['float']))
##-----------------------------------------------------------五,3,计算这些列的均值------------------------
print(df[-df["weight"].isnull()].select_dtypes(include=['float']).mean())


##-----------------------------------------------------------六,1,筛选出字符类型得列(object类型)------------------------
from sklearn.impute import SimpleImputer


imputer = SimpleImputer(missing_values=np.nan,
                        strategy="constant",
                        fill_value="empty")

columns = df.select_dtypes(include=['object']).columns  #拿出字符串行

##-----------------------------------------------------------六,2,使用常量字符串empty进行填充---------------------------

# column = imputer.fit_transform(df[columns])             #空字符替换成empty
# print(column)

df.loc[: ,columns] = imputer.fit_transform(df[columns])    #将替换后得列表形式变为展示全部Dataframe形式
print(df)
















