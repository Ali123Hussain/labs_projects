import pandas as pd
import numpy as np

def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    results = []
    for col in df.select_dtypes(include = np.number).columns:

        if df[col].nunique() <= 2:
            continue
        if col.lower() in ['id','index'] or col.lower().endswith('_id'):
            continue

        skewness = df[col].skew()
        minimum = df[col].min()


        if abs(skewness) >= 1:
            degree = 'Highly Skewed'
        elif abs(skewness) >= 0.5:
            degree = 'Moderately Skewed'
        else:
            degree = 'Normal'


        if skewness > 0:
            direction = 'Positive'
        else:
            direction = 'Negative'


        if degree == 'Normal':
            recommendation = 'No Recomm'
        elif minimum > 0:
            recommendation = 'Box-Cox or Yeo-Johnson'
        elif minimum == 0:
            recommendation = 'log(x+1) or Yeo-Johnson'
        else:
            recommendation = 'Yeo-Johnson'

        results.append({
            'Feature' : col,
            'Skewness' : skewness,
            'Degree' : degree,
            'Direction' : direction,
            'Recommended Transformation' : recommendation
        })
    return pd.DataFrame(results)
