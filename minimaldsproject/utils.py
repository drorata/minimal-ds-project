import pandas as pd

def my_foo(ser):
    print("XXX")
    value_counts = ser.value_counts()
    value_count_norm = ser.value_counts(normalize=True)
    return pd.concat([value_counts, value_count_norm], axis=1, keys=['count', 'ratio'])
