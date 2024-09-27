from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas


class LReg:
    def __init__(self, df_train, df_test, x_axis_name, y_axis_name):
        self.df_train = df_train
        self.df_test = df_test
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.regression = LinearRegression().fit(df_train[x_axis_name], df_train[y_axis_name])
    def predict(self, df = None):
        if df is None:
            df = self.df_test
        prediction = pandas.DataFrame(data={"Prediction": self.regression.predict(df[self.x_axis_name]), "Date": df.index})
        prediction = prediction.set_index("Date")
        df = pandas.merge(df,prediction,on="Date")
        return df
    def test_rmse(self, df_test = None):
        if df_test is None:
            df_test = self.df_test
        return mean_squared_error(df_test[self.y_axis_name], self.predict(df_test[self.x_axis_name])["Prediction"])
    def test_r_sq(self, df_test = None):
        if df_test is None:
            df_test = self.df_test
        return r2_score(df_test[self.y_axis_name], self.predict(df_test[self.x_axis_name])["Prediction"])
