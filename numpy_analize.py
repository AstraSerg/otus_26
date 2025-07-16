#!/usr/bin/env python

# analize dataset with numpy

import pandas as pd
import numpy as np

def sep():
	print("-" * 80)


dataset_file = "Netflix TV Shows and Movies.csv"
df = pd.read_csv(dataset_file, sep=',')

# print(df.shape)

sep()
print("Columns in dataset:")
print(df.columns)

sep()
print("Sample of data:")
print(df.head())

sep()
unvoted = df['imdb_votes'].isna()
print("Unvoted shows:")
for _, row in df[unvoted][['id', 'title']].iterrows():
    print(f"ID: {row['id']}, Title: {row['title']}")
print(f"Count: {unvoted.sum()}")

sep()
print("Top voted shows:")
top_movies = df.sort_values(
    by=['imdb_score', 'imdb_votes'],
    ascending=[False, False]
).head(20)
for _, row in top_movies.iterrows():
    print(
        f"ID: {row['id']}, "
        f"Title: {row['title']}, "
        f"IMDb Score: {row['imdb_score']}, "
        f"Votes: {row['imdb_votes']}"
    )

sep()
print("Top 10 shows by type:")
top_combined = (
    df.sort_values(['imdb_score', 'imdb_votes'], ascending=[False, False])
    .groupby('type')
    .head(10)
)
for type_name, group in top_combined.groupby('type'):
    print(f"\n--- Top 10 {type_name}s by IMDb Score and Votes ---")
    print(group[['id', 'title', 'imdb_score', 'imdb_votes']].to_string(index=False))

sep()
print("The most productiev years:")
top_years = df['release_year'].value_counts().head(10).reset_index()
top_years.columns = ['Year', 'Count of Releases']  # Rename columns for clarity

print("\n--- Top 10 Years by Number of Releases ---")
print(top_years.to_string(index=False))
