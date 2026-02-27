import pandas as pd

# swap the content of first and second file, then set second file to original netflix data set(for simplicity)

# Step 1: Read the contents of both files
a_content = pd.read_csv('~/Documents/Project-Netflix/netflix_titles_copy.csv')
b_content = pd.read_csv('~/Documents/Project-Netflix/netflix_titles_updating.csv')

# Step 2: Swap the contents by writing b_content to first and a_content to second
b_content.to_csv('~/Documents/Project-Netflix/netflix_titles_copy.csv', index=False)
a_content.to_csv('~/Documents/Project-Netflix/netflix_titles_updating.csv', index=False)
