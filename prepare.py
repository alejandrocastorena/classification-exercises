import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split(df, target_val=None):
    
    if target_val:
        train_validate, test = train_test_split(df,
                                      test_size=.2,
                                      random_state=333,
                                      stratify=df[target_val])
        train, validate = train_test_split(train_validate,
                                           test_size=.25,
                                           random_state=333,
                                           stratify=train_validate[target_val])
    else:
        train_validate, test = train_test_split(df,
                                      test_size=.2,
                                      random_state=333,
                                      stratify=df[target_val])
        train, validate = train_test_split(train_validate,
                                           test_size=.25,
                                           random_state=333,
                                           stratify=train_validate[target_val])
        return train, validate, test
            
                                      
                    
                         
                                      