#Cleans the crash data
#   1. Combine CRASH DATE and CRASH TIME into CRASH DATETIME (pandas datetime)
#   2. Fill NA values (check na_replace dict)

import pandas as pd
import numpy as np
import config as cfg

print('Reading CSV file %s ...' % cfg.filename)

crash_data = pd.read_csv(cfg.filename, 
        index_col=cfg.index_col,
        dtype=cfg.dtypes,
        parse_dates={'CRASH DATETIME' : ['CRASH DATE', 'CRASH TIME']},
        infer_datetime_format=True
    )

print('Filling NaN values ...')
for key, val in cfg.na_replace.items():
    print('\t%s' % key)
    crash_data[key] = crash_data[key].replace(np.nan, val)

print("Saving cleaned file to %s ..." % cfg.clean_filename)
crash_data.to_csv(cfg.clean_filename)
print("Cleaning complete.")