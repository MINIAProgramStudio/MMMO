from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class LReg:
    def __init__(self, df_train, df_test, x_axis_name, y_axis_name):
        self.df_train = df_train
        self.df_test = df_test
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.regression = LinearRegression().fit(df_train[x_axis_name], df_train[y_axis_name])
    def predict(self, x_values = None):
        if x_values is None:
            x_values = self.df_test[self.x_axis_name]
        return self.regression.predict(x_values)
    def test_rmse(self, df_test = None):
        if df_test is None:
            df_test = self.df_test
        return mean_squared_error(df_test[self.y_axis_name], self.predict(df_test[self.x_axis_name]))
    def test_r_sq(self, df_test = None):
        if df_test is None:
            df_test = self.df_test
        return r2_score(df_test[self.y_axis_name], self.predict(df_test[self.x_axis_name]))
