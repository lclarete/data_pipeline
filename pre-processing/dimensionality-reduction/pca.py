"""
PCA stands for Principal Component Analysis.

What it does?

When apply it?

"""


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def my_pca():
    """
    Apply pca

    Input:
        Array of numbers
    Output:
        Scaled array
    """

    # instantiate the class and set its parameters
    pca = PCA(n_components=2, random_state=42)

    # train the model
    pca.fit(scaled_data)

    # transform the data
    x_pca = pca.transform(scaled_data)

    return x_pca


def plot_my_pca(pca_data, target_data):
    """
    Visualize the PCA results
    Input:
        Array of numbers
    Output:
        Scatter plot chart
    """
    plt.figure(figsize=(8,6))

    plt.scatter(x_pca[:,0],x_pca[:,1],

                # target variable

                c=target_data,
                # colormap
                cmap='plasma')

    plt.xlabel('First principal component')
    plt.ylabel('Second Principal Component')

    return plt.show()


def pcr(X,y,pc):
    ''' Principal Component Regression in Python'''
    ''' Step 1: PCA on input data'''

    # Define the PCA object
    pca = PCA()

    # Preprocessing (1): first derivative
    d1X = savgol_filter(X, 25, polyorder = 5, deriv=1)

    # Preprocess (2) Standardize features by removing the mean and scaling to unit variance
    Xstd = StandardScaler().fit_transform(d1X[:,:])

    # Run PCA producing the reduced variable Xred and select the first pc components
    Xreg = pca.fit_transform(Xstd)[:,:pc]


    ''' Step 2: regression on selected principal components'''

    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Fit
    regr.fit(Xreg, y)

    # Calibration
    y_c = regr.predict(Xreg)

    # Cross-validation
    y_cv = cross_val_predict(regr, Xreg, y, cv=10)

    # Calculate scores for calibration and cross-validation
    score_c = r2_score(y, y_c)
    score_cv = r2_score(y, y_cv)

    # Calculate mean square error for calibration and cross validation
    mse_c = mean_squared_error(y, y_c)
    mse_cv = mean_squared_error(y, y_cv)

    return(y_cv, score_c, score_cv, mse_c, mse_cv)

def pcr(X,y,pc):
    ''' Principal Component Regression in Python'''
    ''' Step 1: PCA on input data'''
 
    # Define the PCA object
    pca = PCA()
 
    # Preprocessing (1): first derivative
    d1X = savgol_filter(X, 25, polyorder = 5, deriv=1)
 
    # Preprocess (2) Standardize features by removing the mean and scaling to unit variance
    Xstd = StandardScaler().fit_transform(d1X[:,:])
 
    # Run PCA producing the reduced variable Xred and select the first pc components
    Xreg = pca.fit_transform(Xstd)[:,:pc]
 
 
    ''' Step 2: regression on selected principal components'''
 
    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Fit
    regr.fit(Xreg, y)
 
    # Calibration
    y_c = regr.predict(Xreg)
 
    # Cross-validation
    y_cv = cross_val_predict(regr, Xreg, y, cv=10)
 
    # Calculate scores for calibration and cross-validation
    score_c = r2_score(y, y_c)
    score_cv = r2_score(y, y_cv)
 
    # Calculate mean square error for calibration and cross validation
    mse_c = mean_squared_error(y, y_c)
    mse_cv = mean_squared_error(y, y_cv)
 
    return(y_cv, score_c, score_cv, mse_c, mse_cv)