#!/usr/bin/env python
# coding: utf-8

# __author__ = Dominika Drazyk
# __maintainer__ = Dominika Drazyk
# __email__ = dominika.a.drazyk@gmail.com
# __copyright__ = Dominika Drazyk
# __license__ = Apache License 2.0
# __version__ = 1.0.0
# __status__ = Production
# __date__ = 20/10/2025

# Required libraries and custom styles:
import os
import emoji
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

custom_params = {"font.size": 16, "axes.titlesize": 14, "axes.labelsize": 10, "legend.fontsize": 10,
                 'axes.facecolor':'white', 'figure.facecolor':'white', "grid.color": 'lightgray',
                 "axes.edgecolor": '#3D3D3D', 'xtick.color': '#3D3D3D', 'ytick.color': '#3D3D3D',
                 "grid.linewidth": 1, "axes.linewidth": 1.25, 'xtick.bottom': True,
                 'ytick.left': True, "xtick.major.size": 5, "ytick.major.size": 5,
                 "xtick.minor.size": 2, "ytick.minor.size": 2}
sns.set_theme(context = 'paper', palette = 'muted', font = "Rubik", rc = custom_params)
pd.options.display.precision = 3
plt.style.use('custom.mplstyle')

# Paths
path = os.path.dirname(os.path.dirname( __file__ ))

# Functions
def remove_using_emoji(txt):
    return emoji.replace_emoji(txt, '')

def load_datasets():
    print("---- O1.1 Loading datasets...")
    dfdat_path = os.path.join(path, 'data/googleplaystore.csv')
    df_dat = pd.read_csv(dfdat_path)
    print(f"✓ Main dataset loaded: {len(df_dat):,} records")

    dfrev_path = os.path.join(path, 'data/googleplaystore_user_reviews.csv')
    df_rev = pd.read_csv(dfrev_path)
    print(f"✓ Reviews dataset loaded: {len(df_rev):,} records\n")
    print()
    return df_dat, df_rev

def quality_check_and_var_transform(df_dat, df_rev):
    print("---- O1.2 Performing data quality checks and variable transformations...\n")
    print()
    print("Main dataset variable anomalies:")
    print(f"• Categories: {len(df_dat.Category.unique())} unique values")
    print("• Found anomaly in Category column: '1.9'")
    print("• For abnormal row all values were shifted left between columns.")
    df_dat[df_dat.columns[1:]] = df_dat[df_dat.columns[1:]].astype('object')
    df_dat.loc[df_dat['Category'] == '1.9', df_dat.columns[1:]] = (
        df_dat.loc[df_dat['Category'] == '1.9', df_dat.columns[1:]].shift(1, axis=1))
    print("✓ Anomaly corrected\n")
    print()

    print("Main dataset variable processing:")
    df_dat['App'] = df_dat['App'].map(lambda x: remove_using_emoji(x))
    print(f"• App names: {len(df_dat.App.unique()):,} unique (emoji removed)")
    print(f"• Categories: {len(df_dat.Category.unique())} unique")
    print(f"• App types: {df_dat.Type.unique()}")
    print(f"• Content Rating: {df_dat['Content Rating'].unique()}")
    print(f"• Genres: {len(df_dat.Genres.unique())} unique")
    print(f"• Installs: {df_dat.Installs.unique()}")

    df_dat['Rating Value'] = pd.to_numeric(df_dat['Rating'], errors = 'coerce')
    nan_pct = df_dat['Rating Value'].isnull().sum()*100/len(df_dat['Rating Value'])
    print(f"• Rating Value → numeric: {nan_pct:.1f}% values converted to NaN")
    print(f"• Rating Value range: {df_dat['Rating Value'].min():.1f} - {df_dat['Rating Value'].max():.1f}")
    
    df_dat['Last Updated'] = pd.to_datetime(df_dat['Last Updated'],
                                            format = '%B %d, %Y', errors = 'coerce')
    nan_pct = df_dat['Last Updated'].isnull().sum()*100/len(df_dat['Last Updated'])
    print(f"• Last Updated → datetime: {nan_pct:.1f}% values converted to NaT")
    
    df_dat['Ratings Count'] = pd.to_numeric(df_dat['Reviews'], errors = 'coerce')
    nan_pct = df_dat['Ratings Count'].isnull().sum()*100/len(df_dat['Ratings Count'])
    print(f"• Ratings Count → numeric: {nan_pct:.1f}% values converted to NaN")
    print(f"• Ratings Count range: {df_dat['Ratings Count'].min():,} - {df_dat['Ratings Count'].max():,}")
    df_dat_sum = df_dat.drop(['Reviews', 'Rating'], axis = 1)
    print()

    print("Main dataset structure anomalies:")
    count_df_dat = df_dat['App'].value_counts()
    roblox_entries = df_dat[df_dat['App'] == 'ROBLOX'].nunique()
    print(f"• Duplicate apps detected: {roblox_entries} unique combinations for 'ROBLOX'")
    print("• Issue 1: Same app assigned to multiple categories (will not be modified).")
    print("• Issue 2: Multiple duplicate entries with different review counts")
    
    df_dat_sum = df_dat.groupby(['App', 'Category', 'Rating Value', 'Size', 'Installs', 'Type', 'Price',
                                 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']).agg({'Ratings Count': 'sum'}).reset_index()
    print("✓ Rating Number aggregated by App-Category combination (Issue 2)")
    print()

    print("Main dataset size conversion (Size → Size KB):")
    df_dat_sum['Size num'] = df_dat_sum['Size'].str.replace(r'[kM]', '', regex=True)
    df_dat_sum['Size num'] = pd.to_numeric(df_dat_sum['Size num'], errors = 'coerce')
    df_dat_sum['Size KB'] = df_dat_sum.apply(lambda x: x['Size num'] * 1024 if 'M' in str(x['Size'])
                             else x['Size num'] if 'k' in str(x['Size'])
                             else float('nan'), axis=1)
    nan_pct = df_dat_sum['Size KB'].isnull().sum()*100/len(df_dat_sum['Size KB'])
    print(f"• Size → Size KB: {nan_pct:.0f}% values converted to NaN")
    print(f"• Size KB range: {df_dat_sum['Size KB'].min():.0f} - {df_dat_sum['Size KB'].max():.0f} KB")
    print()

    print("Main dataset price Conversion (Price → Price USD):")
    df_dat_sum['Price USD'] = df_dat_sum['Price'].str.replace(r'[$]', '', regex = True)
    df_dat_sum['Price USD'] = pd.to_numeric(df_dat_sum['Price USD'], errors = 'coerce')
    nan_pct = df_dat_sum['Price USD'].isnull().sum()*100/len(df_dat_sum['Price USD'])
    print(f"• Price → Price USD: {nan_pct:.0f}% values converted to NaN")
    print(f"• Price USD range: ${df_dat_sum['Price USD'].min():.2f} - ${df_dat_sum['Price USD'].max():.2f}")
    df_dat_sum = df_dat_sum.drop(['Size num', 'Price'], axis = 1)
    print()

    print("Reviews dataset variables:")
    print(f"• Translated reviews: {len(df_rev)} text entries")
    print(f"• Sentiment categories: {df_rev.Sentiment.unique()}")
    df_rev['App'] = df_rev['App'].map(lambda x: remove_using_emoji(x))

    df_rev['Sentiment Polar'] = pd.to_numeric(df_rev['Sentiment_Polarity'], errors = 'coerce')
    nan_pct = df_rev['Sentiment Polar'].isnull().sum()*100/len(df_rev['Sentiment Polar'])
    print(f"• Sentiment Polarity → numeric: {nan_pct:.0f}% values converted to NaN")
    print(f"• Sentiment Polarity range: {df_rev['Sentiment Polar'].min():.2f} - {df_rev['Sentiment Polar'].max():.2f}")
    
    df_rev['Sentiment Subject'] = pd.to_numeric(df_rev['Sentiment_Subjectivity'], errors = 'coerce')
    nan_pct = df_rev['Sentiment Subject'].isnull().sum()*100/len(df_rev['Sentiment Subject'])
    print(f"• Sentiment Subjectivity → numeric: {nan_pct:.0f}% values converted to NaN")
    print(f"• Sentiment Subjectivity range: {df_rev['Sentiment Subject'].min():.2f} - {df_rev['Sentiment Subject'].max():.2f}")
    df_rev = df_rev.drop(['Sentiment_Subjectivity', 'Sentiment_Polarity', 'Translated_Review'], axis = 1)
    print()
    return df_dat_sum, df_rev

def merge_datasets(df_dat_sum, df_rev):
    print("---- O1.3 Merging datasets:")

    dat_set = set(df_dat_sum.App.unique())
    rev_set = set(df_rev.App.unique())
    non_matching = len(list(rev_set - dat_set))
    print(f"• Apps reviewed but not in the main dataset: {non_matching}")
    print("• Non-matching apps will be excluded from main dataset analysis")
    df = pd.merge(df_dat_sum, df_rev, on = ['App'], how = 'left')
    df['App_id'] = df['App'].astype('category').cat.codes + 1
    df = df[['App_id', 'App', 'Category', 'Genres', 'Content Rating', 'Type', 'Installs', 'Last Updated',
             'Current Ver', 'Android Ver', 'Size', 'Size KB', 'Price USD', 'Ratings Count', 'Rating Value',
             'Sentiment', 'Sentiment Polar', 'Sentiment Subject']]
    print(f"✓ Datasets merged successfully")
    print(f"• Final dataset shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"• Columns: {', '.join(df.columns.tolist())}")
    print("Merged Dataset Summary:")
    print(df.info())
    print()
    return df

def review_missing_data(df):
    print("---- O1.4 Missing data analysis:")

    nan_count = df.isna().sum()
    all_count = df.iloc[:,0].count()
    prc = (nan_count * 100)/all_count
    for col, pct in prc.items():
        if pct > 0:
            print(f"• {col}: {pct:.0f}% missing")
    print("• Size KB: 31% missing (due to 'varies with device' entries)")
    print("• Review variables: 47% missing (apps without text reviews)")
    print()
    df_norev = df[(df['Sentiment'].isna()) &
                 (df['Sentiment Polar'].isna()) &
                 (df['Sentiment Subject'].isna())]

    print(f"Apps Without Text Reviews ({len(df_norev.App.unique()):,} apps):")
    print(f"• Categories: {len(df_norev.Category.unique())} unique")
    print(f"• Types: {df_norev.Type.unique()}")
    print(f"• Content Ratings: {df_norev['Content Rating'].unique()}")
    print(f"• Install ranges: {df_norev.Installs.unique()}")
    print(f"• Rating Value range: {df_norev['Rating Value'].min():.1f} - {df_norev['Rating Value'].max():.1f}")
    print(f"• Ratings Count range: {df_norev['Ratings Count'].min():,} - {df_norev['Ratings Count'].max():,}")
    print(f"• Size KB range: {df_norev['Size KB'].min():.0f} - {df_norev['Size KB'].max():.0f} KB")
    print(f"• Price USD range: ${df_norev['Price USD'].min():.2f} - ${df_norev['Price USD'].max():.2f}")
    print("• No clear pattern distinguishes non-reviewed apps")
    print()
    return df

# def create_new_variables(df):
#     print("---- O1.5 Creating new variables:")
#
#     print("• Creating Text Review flag (Yes/No for text review availability)")
#     df['Text Review'] = np.where((df['Sentiment'].isna()) &
#                                (df['Sentiment Polar'].isna()) &
#                                (df['Sentiment Subject'].isna()), 'No', 'Yes')
#
#     print("• Creating sentiment analysis variables")
#     df['Sent_Pos'] = (df['Sentiment'] == 'Positive').astype(int)
#     df['Sent_Neut'] = (df['Sentiment'] == 'Neutral').astype(int)
#     df['Sent_Neg'] = (df['Sentiment'] == 'Negative').astype(int)
#     df['Sent_NaN'] = (df['Sentiment'].isna()).astype(int)
#     df['TxtReview_count'] = (df['TxtReview'] == 'Yes').astype(int)
#
#     print("• Aggregating data by App-Category combination")
#     agg_rules = {'Sentiment_Polarity': 'mean', 'Sentiment_Subjectivity': 'mean',
#         'Sent_Pos': lambda x: (x.sum() / len(x)) * 100 if len(x) > 0 else 0,
#         'Sent_Neut': lambda x: (x.sum() / len(x)) * 100 if len(x) > 0 else 0,
#         'Sent_Neg': lambda x: (x.sum() / len(x)) * 100 if len(x) > 0 else 0,
#         'Sent_NaN': lambda x: (x.sum() / len(x)) * 100 if len(x) > 0 else 0,
#         'TxtReview_count': lambda x: x.sum(),
#         'Rating': 'first', 'Type': 'first', 'Content Rating': 'first', 'Genres': 'first', 'Size_KB': 'first',
#         'Installs': 'first', 'Price_USD': 'first', 'Last Updated': 'first', 'Current Ver': 'first',
#         'Android Ver': 'first', 'Reviews': 'first'}
#     df_agg = df.drop(['Translated_Review'], axis=1).groupby(['App', 'Category']).agg(agg_rules).reset_index()
#     print()
#     print(f"✓ Aggregated dataset created: {df_agg.shape[0]:,} rows × {df_agg.shape[1]} columns")
#     print()
#     return df, df_agg

def save_preprocessed_datasets(df):
    print("---- O1.6 Saving preprocessed dataset:")

    df.to_csv('../data/prep_fact_data.csv', encoding='utf-8', index = False)
    print(f"✓ Fact dataset saved: ../data/prep_fact_data.csv ({df.shape[0]:,} rows)")

def main():
    print("=" * 60)
    print("GOOGLE APPS PERFORMANCE - CONSULTANT DASHBOARD")
    print("Data Preprocessing Pipeline")
    print("=" * 60)
    print()
    
    df_dat, df_rev = load_datasets()
    
    df_dat_sum, df_rev = quality_check_and_var_transform(df_dat, df_rev)

    df = merge_datasets(df_dat_sum, df_rev)

    df = review_missing_data(df)
    
    #df, df_agg = create_new_variables(df)
    
    save_preprocessed_datasets(df)

if __name__ == "__main__":
    main()