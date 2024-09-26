import pandas
import PythonTableConsole as PTC
import matplotlib.pyplot as plt

df_raw = pandas.read_csv('data/saveecobot_16181.csv', on_bad_lines='warn')  # open file, ignore all rows with errors

print("Raw table height:", df_raw.size)

df_raw = df_raw.dropna(axis=0, subset='value')  # drop all NAN values in column 'values'
df_raw = df_raw.drop("value_text", axis = 1)

print("Table height after dropping nan values:", df_raw.size)

print('Group by phenomenon to get all phenomenon names:')
print(pandas.DataFrame(df_raw.groupby('phenomenon')))
print()

df_pm1 = df_raw.loc[df_raw['phenomenon'] == 'pm1'].set_index("logged_at")
df_pm1 = df_pm1.rename(columns={'value': 'pm_1'}).drop(['device_id','phenomenon'], axis=1)

df_pm25 = df_raw.loc[df_raw['phenomenon'] == 'pm25'].set_index("logged_at")
df_pm25 = df_pm25.rename(columns={'value': 'pm_25'}).drop(['device_id','phenomenon'], axis=1)

df_pm10 = df_raw.loc[df_raw['phenomenon'] == 'pm10'].set_index("logged_at")
df_pm10 = df_pm10.rename(columns={'value': 'pm_10'}).drop(['device_id','phenomenon'], axis=1)

df_pressure_pa = df_raw.loc[df_raw['phenomenon'] == 'pressure_pa'].set_index("logged_at")
df_pressure_pa = df_pressure_pa.rename(columns={'value': 'pressure_pa'}).drop(['device_id','phenomenon'], axis=1)

df_temperature = df_raw.loc[df_raw['phenomenon'] == 'temperature'].set_index("logged_at")
df_temperature = df_temperature.rename(columns={'value': 'temperature'}).drop(['device_id','phenomenon'], axis=1)

df_humidity = df_raw.loc[df_raw['phenomenon'] == 'humidity'].set_index("logged_at")
df_humidity = df_humidity.rename(columns={'value': 'humidity'}).drop(['device_id','phenomenon'], axis=1)

list_length = [['phenomenon', 'pm1', 'pm10', 'pm25', 'humidity', 'pressure_pa', 'temperature'],
               ['size', df_pm1.size, df_pm25.size, df_pm10.size, df_humidity.size, df_pressure_pa.size,
                df_temperature.size]]

table_length = PTC.PythonTableConsole(list_length)
print(table_length)

# merge all sub-dfs in one df
df_cooked = pandas.merge(df_pm1, df_pm10,on="logged_at")
df_cooked = pandas.merge(df_cooked, df_pm25,on="logged_at")
df_cooked = pandas.merge(df_cooked, df_pressure_pa,on="logged_at")
df_cooked = pandas.merge(df_cooked, df_temperature,on="logged_at")
df_cooked = pandas.merge(df_cooked, df_humidity,on="logged_at")

df_norm=(df_cooked-df_cooked.mean())/df_cooked.std()

print(df_cooked.size)
df_cooked = df_cooked.dropna()
print(df_cooked.size)

df_norm.plot()
plt.show()