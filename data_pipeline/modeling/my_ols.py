"""
Linear Regresson

"""

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
mse = cross_val_score(estimator=lr, 
                      X=X, 
                      y=y, 
                      scoring='neg_mean_squared_error',
                     cv=5)
mean_mse = np.mean(mse)
mean_mse


# ridge regression

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge = Ridge()
parameters = {'alpha':[1e-15, 1e-10, 1e-8, 1e-3, 1e-2, 1, 5, 10, 20, 30, 35, 40, 45, 50, 55, 100]}
ridge_regressor = GridSearchCV(estimator=ridge,
                  param_grid=parameters,
                  scoring='neg_mean_squared_error',
                  cv=5
                 )
ridge_regressor.fit(X,y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)

# lasso regression
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso()
lasso_regression = GridSearchCV(estimator=lasso,
                                param_grid=parameters,
                                scoring='neg_mean_squared_error',
                                cv=5
                               )

lasso_regression.fit(X,y)

print(lasso_regression.best_params_)
print(lasso_regression.best_score_)

# Best model

