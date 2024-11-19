
import pandas as pd

df=pd.read_csv('Cleaned_Data.csv')

df['State'].value_counts()
# Good              4307    
# Not Known         4078    
# As new            2814
# To renovate        969
# To be done up      818
# Just renovated     581
# To restore          48

# Legend
# "Good" = 1
# "Not Known" = 2
# "As new" = 3
# "To renovate" = 4
# "To be done up" = 5
# "Just renovated" = 6
# "To restore" = 7



condition_mapping = {
    'Good': 1,
    'Not Known': 2,
    'As new': 3,
    'To renovate': 4,
    'To be done up': 5,
    'Just renovated': 6,
    'To restore': 7
}

df['State'] = df['State'].map(condition_mapping)

df.to_csv('Update_colState_Num_values.csv', index=False)

                  



