import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols as ols_formula

def hf_ols(x, h=8, p=4, **kwargs):
    if not isinstance(x, pd.DataFrame):
        raise ValueError(f"Argument 'x' must be a DataFrame, but {type(x)} was provided.")

    if not isinstance(h, int) or h <= 0:
        raise ValueError(f"Argument 'h' must be a positive whole number, but {h} was provided.")
    
    if not isinstance(p, int) or p <= 0:
        raise ValueError(f"Argument 'p' must be a positive whole number, but {p} was provided.")

    def lag(df, lags):
        return pd.concat(
            {f'xt_{i}': df.shift(i) for i in lags},
            axis=1
        )

    data = lag(x, [0] + list(range(h, h + p)))
    data.columns = [f'yt{h}'] + [f'xt_{i}' for i in range(p)]
    
    data = data.dropna()

    formula = f"yt{h} ~ " + " + ".join([f'xt_{i}' for i in range(p)])

    model = ols_formula(formula, data=data, **kwargs)
    result = model.fit()

    return {'fitted.values': result.fittedvalues, 'residuals': result.resid}
