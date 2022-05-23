from toolbox.toolbox import test_train_split_func
import pandas as pd

def test_type_df():
    assert type(test_train_split_func()) == type(pd.Dataframe)
