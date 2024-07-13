import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv

urls = {
    "action": "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=num_votes,desc",
    "drama": "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=num_votes,asc",
    "romance": "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=romance&sort=num_votes,desc",
    "sci-fi": "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sci-fi&sort=num_votes,desc",
    "comedy": "https://www.imdb.com/search/title/?title_type=feature&genres=comedy&sort=num_votes,desc",
    "animation": "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=num_votes,desc"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_movies(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')

def extract_movies(soup):
    movies = soup.find_all('div', class_="sc-b189961a-0 hBZnfJ") 
    data = []
    
    for movie in movies:
        name = movie.find('div', class_="ipc-title").h3.text.split('.')[1].strip()
        rank = movie.find('div', class_="ipc-title").h3.text.split('.')[0].strip()
        year = movie.find('div', class_="sc-b189961a-7").span.text.strip()
        rating = float(movie.find('div', class_="sc-e2dbc1a3-0").span.text.split('.')[0].strip())
        data.append([rank, name, rating, year])
    
    return data

def save_to_csv(data, genre):
    df = pd.DataFrame(data, columns=['Rank', 'Name', 'Rating', 'Year'])
    filename = f'imdbmovies_{genre}.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    
    print(f"Data has been written to the {genre} CSV file: {filename}")
    print(df)

def main():
    while True:
        try:
            user_input = input("Enter genre (action, drama, romance, comedy, animation, sci-fi) or 'exit' to quit: ").strip().lower()
            if user_input == 'exit':
                break
            
            if user_input in urls:
                print(f"Fetching movies for genre: {user_input}")
                soup = fetch_movies(urls[user_input])
                movies_data = extract_movies(soup)
                save_to_csv(movies_data, user_input)
            else:
                print("Invalid genre. Please try again.")
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()