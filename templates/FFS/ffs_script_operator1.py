import math
import random
import pandas as pd


def main():
    vals = [ random.randint(1,100) for i in range(100) ]

    df = pd.DataFrame({'Raw':vals})

    filtered = df.rolling(11,center=True).median()
    filtered.columns=['Filt']

    #df.join(filtered)

    all_df = pd.merge(df, filtered,right_index=True, left_index=True)

    the_file = r"C:\Users\Simon\Documents\test.csv"
    all_df.to_csv(the_file)




if __name__ == "__main__":
    main()