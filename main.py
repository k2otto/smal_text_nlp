################ PERFORMING PREPROCESSING OF INPUT TEXT ###################
def preprocess_text(df, column):
    import re
    for i in range(len(df)):
        ######  REMOVING SPECIAL CHARACTERS
        df.loc[i, column] = re.sub(r'\W', ' ', str(df.loc[i, column]))

        ######  REMOVING ALL SINGLE CHARACTERS
        df.loc[i, column] = re.sub(r'\s+[a-zA-Z]\s+', ' ', str(df.loc[i, column]))

        ######  REMOVING MULTIPLE SPACES WITH SINGLE SPACE
        df.loc[i, column] = re.sub(r'\s+', ' ', str(df.loc[i, column]))

    return df