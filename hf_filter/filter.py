import pandas as pd
from .ols import hf_ols

def hf_filter(x, h=8, p=4, output=['x', 'trend', 'cycle', 'random'], **kwargs):
    output_args = ['x', 'trend', 'cycle', 'random']
    
    if not all(elem in output_args for elem in output):
        incorrect_args = [elem for elem in output if elem not in output_args]
        raise ValueError(f"Incorrect argument(s) {incorrect_args} present in 'output' argument. Must be a list containing 'x', 'trend', 'cycle', or 'random'.")
    
    if x.columns is None or any(x.columns.str.strip() == ''):
        warning_msg = ("Your DataFrame doesn't have column names, assigning default name 'y'.")
        print(warning_msg)
        x.columns = ['y']
    
    neverHP = hf_ols(x, h, p, **kwargs)
    
    trend = neverHP['fitted.values']
    trend = pd.DataFrame(trend)
    trend.columns = [col + '.trend' for col in x.columns]
    
    if len(output) == 1 and output[0] == 'trend':
        return trend
    
    cycle = neverHP['residuals']
    cycle = pd.DataFrame(cycle)
    cycle.columns = [col + '.cycle' for col in x.columns]
    
    if len(output) == 1 and output[0] == 'cycle':
        return cycle
    
    random = x - x.shift(h)
    random.columns = [col + '.random' for col in x.columns]
    
    if len(output) == 1 and output[0] == 'random':
        return random
    
    all_data = pd.concat([x, trend, cycle, random], axis=1)
    all_data.columns = list(x.columns) + [col + '.' + suffix for col in x.columns for suffix in ['trend', 'cycle', 'random']]
    
    if 'x' in output:
        index = [i for i, col in enumerate(all_data.columns) if any(suffix in col for suffix in output)]
        return all_data.iloc[:, [0] + index]
    else:
        index = [i for i, col in enumerate(all_data.columns) if any(suffix in col for suffix in output)]
        return all_data.iloc[:, index]
