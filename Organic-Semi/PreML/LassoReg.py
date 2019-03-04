
# coding: utf-8

# In[ ]:


#import all package
import pandas as pd
import numpy as np
from sklearn import linear_model
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
get_ipython().run_line_magic('matplotlib', 'inline')

def lassoreg(Descriptors):
    """This function is used to plot RR coef and error vs lamdas throughs Lasso Regression method"""
    train,test = train_test_split(Descriptors, test_size=0.05, random_state=123)
    scaler = StandardScaler().fit(train)
    train_normalized = pd.DataFrame(data=scaler.transform(train), columns=train.columns)
    test_normalized = pd.DataFrame(data=scaler.transform(test), columns=test.columns)
    coefs = []
    trainerror = []
    testerror = []

    lambdas = np.logspace(-8,1,200)
    model=linear_model.Lasso()

    # loop over lambda values (strength of regularization)
    for k in lambdas:
        model.set_params(alpha=k,max_iter=1e6)
        model.fit(train_normalized[train.columns.values[2:16]],train_normalized[train.columns.values[1]])
        coefs.append(model.coef_)
        trainerror.append(mean_squared_error(train_normalized[train.columns.values[1]],model.predict(
        train_normalized[train.columns.values[2:16]])))
        testerror.append(mean_squared_error(test_normalized[train.columns.values[1]],model.predict(
        test_normalized[train.columns.values[2:16]])))
    fig = plt.figure(figsize=(10,3))
    RR_coefs = fig.add_subplot(121)
    plt.plot(lambdas,coefs)
    RR_coef.set_xscale('log')
    RR_coef.set_xlabel('$\lambda$')
    RR_coef.set_ylabel('$coefs$')
    RR_coef.set_title('RR coefs vs $\lambda$')
    error = fig.add_subplot(122)
    plt.plot(lambdas,trainerror,label='train error')
    plt.plot(lambdas,testerror,label='test error')
    error.set_xscale('log')
    error.set_xlabel('$\lambda$')
    error.set_ylabel('error')
    error.set_legend(loc=1)
    error.set_title('error vs $\lambda$')
return fig

