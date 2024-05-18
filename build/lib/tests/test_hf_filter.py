import pytest
import pandas as pd
import numpy as np
from hf_filter import hf_filter
import statsmodels.api as sm

def test_hf_filter():
    df = pd.DataFrame({'y': np.random.randn(100)})
    result = hf_filter(df, h=8, p=4, output=['x', 'trend', 'cycle', 'random'], family=sm.families.Gaussian())
    assert 'y' in result.columns
    assert 'y.trend' in result.columns
    assert 'y.cycle' in result.columns
    assert 'y.random' in result.columns

if __name__ == "__main__":
    pytest.main()
