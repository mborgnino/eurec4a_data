import numpy as np
from scipy import stats

# --------------
# function to compute linear regression, correlation coeff and p value
def slopes_r_p_dof(x,y,df=None):
    from scipy import stats
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    linreg = stats.linregress(x,y)
    corr_coeff, trash = stats.spearmanr(x,y)
    corr_pears, trash = stats.pearsonr(x,y)
    if df is None:
        df = len(x)-2   # degrees of freedom.
    t_value = np.abs(corr_coeff)*np.sqrt((df)/(1-corr_coeff**2))
    p_value = 2*(1 - stats.t.cdf(t_value,df=df))
    
    yhat = linreg.intercept + linreg.slope * x
    s_y = np.nansum((y - yhat)**2)
    s_x = np.nansum((x - np.mean(x))**2)
    stderr_cann = np.sqrt((1/(df))*(s_y/s_x))
    t_value_cann = linreg.slope/stderr_cann
    p_val_cann = 2*(1 - stats.t.cdf(np.abs(t_value_cann),df=df))
    
    return linreg, corr_coeff, p_value, corr_pears, p_val_cann, stderr_cann

