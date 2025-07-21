import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('netflix_titles.csv')

# Data Cleaning
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')
df['year_added'] = df['date_added'].dt.year


# Total Movies vs TV Shows
type_count = df['type'].value_counts()
plt.style.use('dark_background')
plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color=['skyblue', 'orange'])
plt.title('Total Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.legend(title = 'netflix')
plt.tight_layout() 
plt.grid(True)
plt.savefig('movies_vs_tvshows.png')
plt.close()

# Content Added Each Year
yearly_content = df['year_added'].value_counts().sort_index()
plt.style.use('dark_background')
plt.figure(figsize=(10,5))
plt.bar(yearly_content.index.astype(str), yearly_content.values, color='lightgreen')
plt.title('Content Added Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles Added')
plt.xticks(rotation=45)
plt.legend(title = 'netflix')
plt.tight_layout() 
plt.grid(True)
plt.savefig('content_by_year.png')
plt.close()

# Top 10 Genres
genres = df['listed_in'].value_counts().head(10)
plt.style.use('dark_background')
plt.figure(figsize=(10,5))
plt.bar(genres.index, genres.values, color='coral')
plt.title('Top 10 Genres')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45, ha='right')
plt.legend(title = 'netflix' )
plt.tight_layout() 
plt.grid(True)
plt.savefig('top_genres.png')
plt.close()

# Top 10 Countries
countries = df['country'].value_counts().head(10)
plt.style.use('dark_background')
plt.figure(figsize=(10,5))
plt.bar(countries.index, countries.values, color='violet')
plt.title('Top 10 Countries by Content')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45, ha='right')
plt.legend(title = 'netflix' )
plt.tight_layout() 
plt.grid(True)
plt.savefig('top_countries.png')
plt.close()


top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.bar(top_directors.index, top_directors.values, color='gold')
plt.title('Top 10 Directors on Netflix')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(True)
plt.savefig('top_directors.png')
plt.close()

plt.figure(figsize=(10,5))
plt.plot(yearly_content.index, yearly_content.values, marker='o', color='cyan')
plt.title('Netflix Content Added Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.savefig('yearly_trend_lineplot.png')
plt.close()



india_movies = df[(df['country'].str.contains('India')) & (df['type'] == 'Movie')]
india_movies_by_year = india_movies['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.bar(india_movies_by_year.index.astype(str), india_movies_by_year.values, color='lime')
plt.title('Number of Indian Movies Added Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Indian Movies')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('indian_movies_by_year.png')
plt.close()

print("Analysis Completed.Graphs saved successfully.")
