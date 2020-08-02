from func1 import *
from query1 import *
from sklearn.preprocessing import MinMaxScaler

df = data1(10)
print(df.shape)
df.index = df['datetime']
df.index = df.index.astype('datetime64[ns]')
df.sort_index(inplace=True)
df.dropna(inplace=True)
df['datetime'] = pd.to_datetime(df['datetime'])

dtat0 = df.iloc[-1:,0:1].values[0][0]
dti = pd.date_range(dtat0, periods=7).shift(1, freq='D')
dfdt = dti.to_frame(index=False, name='datims')

df.drop(('datetime'), axis=1, inplace=True)


y_scaler = MinMaxScaler()
y_scaler.fit(df[['stor']])
X_scaler = MinMaxScaler()

df[['fore24', 'tail24', 'tail24_avg', 'evap', 'infl', 'losses',
       'rel1', 'rel2', 'rel3', 'rel_tol', 'engr1', 'engr2', 'engr3', 'cond1',
       'cond2', 'cond3', 'str1', 'str2', 'str3', 'run_g1', 'run_g2', 'run_g3',
       'run_c1', 'run_c2', 'run_c3', 'spillway', 'irr', 'camp', 'demand',
       'derate', 'outage', 'stor']] = X_scaler.fit_transform(df)

dfval = df.values[:,:-1]

n_steps_in, n_steps_out = 10, 7
X_test = dfval.reshape(1,10,31).transpose(0,1,2)

n_features = X_test.shape[2]

model_2 = ShallowConvNet(n_steps_in=n_steps_in, n_steps_out=n_steps_out, n_features=n_features)
model_2.summary()
model_2.load_weights("models/model1.hdf5")
model_2.compile(optimizer='adam', loss='mse')
Y_pred = model_2.predict(X_test)
yp = y_scaler.inverse_transform(Y_pred)

from sqlalchemy import create_engine
user='root'
pwd='opt#565784'
dbname='predictive'
host='10.211.1.25'
port=3306
con = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}')

df = pd.DataFrame(yp).T
df.columns = ['stor']
com = pd.concat([dfdt, df], axis=1, join='inner')
com.to_sql('lwweekly', con, if_exists='append', index=False)