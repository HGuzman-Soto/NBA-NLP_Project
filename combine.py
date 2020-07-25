import os, glob
import pandas as pd

def main():
    all_files = glob.glob(os.path.join(path, "reddit_posts*.csv"))
    all_csv = (pd.read_csv(f, sep=',') for f in all_files)

    df_merged   = pd.concat(all_csv, ignore_index=True)
    df_merged.to_csv( "reddit_posts.csv")


if __name__ == "__main__":
    path = "../NBA-NLP_Project"
    main()