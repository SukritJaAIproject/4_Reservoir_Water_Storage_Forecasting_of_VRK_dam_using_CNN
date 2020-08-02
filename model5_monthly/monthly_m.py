from numpy import split
from numpy import array


from query1 import *
from Func_Paper1 import *

df = data1(30)

df.index = df['datetime']
df.index = df.index.astype('datetime64[ns]')
df.sort_index(inplace=True)
df.dropna(inplace=True)
df['datetime'] = pd.to_datetime(df['datetime'])
print("shape ", df.shape)

df.tail(1)

dtat0 = df.iloc[-1:,0:1].values[0][0]
dti = pd.date_range(dtat0, periods=30).shift(1, freq='D')
dfdt = dti.to_frame(index=False, name='datims')

df.drop(('datetime'), axis=1, inplace=True)

from sklearn.preprocessing import MinMaxScaler
y_scaler = MinMaxScaler()
y_scaler.fit(df[['fore24']])
X_scaler = MinMaxScaler()

df[['tail24', 'tail24_avg', 'evap', 'infl', 'losses',
       'rel1', 'rel2', 'rel3', 'rel_tol', 'engr1', 'engr2', 'engr3', 'cond1',
       'cond2', 'cond3', 'str1', 'str2', 'str3', 'run_g1', 'run_g2', 'run_g3',
       'run_c1', 'run_c2', 'run_c3', 'spillway', 'irr', 'camp', 'demand',
       'derate', 'outage', 'stor','fore24']] = X_scaler.fit_transform(df)

dfval = df.values[:,:-1]

def split_dataset(data):
    test = data
    test = array(split(test, len(test)/30))
    return test

test = split_dataset(df.values)

n_input = 14

def forecast(model, history, n_input):
    data = array(history)
    data = data.reshape((data.shape[0] * data.shape[1], data.shape[2]))
    input_x = data[-n_input:, :]
    input_x = [input_x[:, i].reshape((1, input_x.shape[0], 1)) for i in range(input_x.shape[1])]
    yhat = model.predict(input_x, verbose=1)
    yhat = yhat[0]
    return yhat

#เป็น list ที่สมาชิกแต่ละตัวเป็น samples (windows, n-feature)
history = [x for x in test]

model = ShallowConvNet(test, n_input)
model.load_weights("models/weights73.hdf5")
model.compile(loss='mse', optimizer='adam')

predictions = list()
for i in range(len(test)):
    yhat_sequence = forecast(model, history, n_input)
    predictions.append(yhat_sequence)
predictions = array(predictions)

yp = y_scaler.inverse_transform(predictions)

from sqlalchemy import create_engine
user='root'
pwd='opt#565784'
dbname='predictive'
host='10.211.1.25'
port=3306
con = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}')

df = pd.DataFrame(yp).T
df.columns = ['stor30D']
com = pd.concat([dfdt, df], axis=1, join='inner')
com.to_sql('monthly_m', con, if_exists='replace', index=False)