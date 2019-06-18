import pandas as pd
from datetime import datetime
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

##
##  Reading in the data
##
df = pd.read_csv('sphist.csv')
df['Date'] = pd.to_datetime(df['Date'])

df.sort_values('Date', ascending=True, inplace=True)

##
## Generating indicators
##
roll_5_mean = df['Close'].rolling(window=5).mean()
df['day_5_mean'] = roll_5_mean.shift(1)
roll_30_mean = df['Close'].rolling(window=30).mean()
df['day_30_mean'] = roll_30_mean.shift(1)
roll_365_mean = df['Close'].rolling(window=250).mean()
df['day_365_mean'] = roll_365_mean.shift(1)
df['ratio_5_365_mean'] = df['day_5_mean'] / df['day_365_mean']

roll_5_std = df['Close'].rolling(window=5).std()
df['day_5_std'] = roll_5_std.shift(1)
roll_30_std = df['Close'].rolling(window=30).std()
df['day_30_std'] = roll_30_std.shift(1)
roll_365_std = df['Close'].rolling(window=250).std()
df['day_365_std'] = roll_365_std.shift(1)
df['ratio_5_365_std'] = df['day_5_std'] / df['day_365_std']

##
## Add more indicators
##
volume_r5_mean = df['Volume'].rolling(window=5).mean()
df['volume_5_mean'] = volume_r5_mean.shift(1)
volume_r365_mean = df['Volume'].rolling(window=250).mean()
df['volume_365_mean'] = volume_r365_mean.shift(1)
df['vol_rat_5_365_mean'] = df['volume_5_mean'] / df['volume_365_mean']

volume_r5_std = df['Volume'].rolling(window=5).std()
df['volume_5_std'] = volume_r5_std.shift(1)
volume_r365_std = df['Volume'].rolling(window=250).std()
df['volume_365_std'] = volume_r365_std.shift(1)
df['vol_rat_5_365_std'] = df['volume_5_std'] / df['volume_365_std']

df['year'] = df['Date'].dt.year.shift(1)
df['month'] = df['Date'].dt.month.shift(1)
df['weekday'] = df['Date'].dt.weekday.shift(1)
df['day'] = df['Date'].dt.day.shift(1)

lowest_price = df['Low'].rolling(window=250).min()
df['rat_lowest_price'] = (lowest_price.shift(1)) / (df['Close'].shift(1))

highest_price = df['High'].rolling(window=250).max()
df['rat_highest_price'] = (highest_price.shift(1)) / (df['Close'].shift(1))

##
## Splitting up the data
##
df = df[df['Date'] > datetime(year=1951, month=1, day=2)].copy()
df.dropna(axis=0, inplace=True)

train = df[df['Date'] < datetime(year=2013, month=1, day=1)].copy()
test = df[df['Date'] >= datetime(year=2013, month=1, day=1)].copy()

##
##  Making predictions
##
features = train.columns.drop(['Close', 'High', 'Low', 'Open', 'Volume', 'Adj Close', 'Date'])

model = LinearRegression()
model.fit(train[features], train['Close'])
predictions = model.predict(test[features])
error = mean_absolute_error(test['Close'], predictions)
print(error)