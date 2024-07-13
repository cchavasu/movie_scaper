import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv

url_action="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=num_votes,desc"
url2_drama="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=num_votes,asc"
url3_romance="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=romance&sort=num_votes,desc"
url4_sci = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sci-fi&sort=num_votes,desc"
url5_comedy = "https://www.imdb.com/search/title/?title_type=feature&genres=comedy&sort=num_votes,desc"
url6_animation = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=num_votes,desc"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#genres = ["action", "drama", "romance", "comedy", "sci-fi", "animation"]
#selected_genre = input(f"Select genre from {', '.join(genres)}: ").strip().lower()
#print("i am all good")
actionurl= requests.get(url_action, headers=headers)#ACTION soup
actionurl.raise_for_status()
soup_action = BeautifulSoup(actionurl.content, 'html.parser')
#print(soup_action.prettify())
     
dramaurl= requests.get(url2_drama, headers=headers) #DRAMA Soup
dramaurl.raise_for_status()
soup_drama = BeautifulSoup(dramaurl.content, 'html.parser')
#print(soup_drama.prettify())
     
romanceurl= requests.get(url3_romance, headers=headers) #DRAMA soup
romanceurl.raise_for_status()
soup_romance = BeautifulSoup(romanceurl.content, 'html.parser')
#print(soup_romance.prettify())
     
sciencefictionurl= requests.get(url4_sci, headers=headers) #science fiction soup
sciencefictionurl.raise_for_status()
soup_sci = BeautifulSoup(sciencefictionurl.content, 'html.parser')
#print(soup_sci.prettify())
     
comedyurl= requests.get(url5_comedy, headers=headers) #comedy soup
comedyurl.raise_for_status()
soup_comedy = BeautifulSoup(comedyurl.content, 'html.parser')
#print(soup_comedy.prettify()) 
     
animationurl= requests.get(url6_animation, headers=headers) #animation soup
animationurl.raise_for_status()
soup_animation = BeautifulSoup(animationurl.content, 'html.parser')
#print(soup_animation.prettify())
movies_action = soup_action.find_all('li', class_="ipc-metadata-list-summary-item")
movies_drama = soup_drama.find_all('div', class_="sc-b189961a-0 hBZnfJ")
movies_comedy = soup_comedy.find_all('div', class_="sc-74bf520e-3 klvfeN dli-parent")
movies_animation = soup_animation.find_all('div', class_="sc-b189961a-0 hBZnfJ")
movies_romance = soup_romance.find_all('div', class_="sc-b189961a-0 hBZnfJ")
movies_sci_fic = soup_sci.find_all('div', class_="sc-b189961a-0 hBZnfJ")
print(len(movies_action))

def main():
    try:
        user_input = str(input("Enter genre (action, drama, romance, comedy, animation, sci-fic): ").strip().lower())
        
        if user_input == "action":

            print("inside action_if")
            csv_filename_action ='movies_action.csv'
            with open(csv_filename_action, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for action in movies_action:
                    name = action.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = action.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = action.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(action.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    print(name)
                    # print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the action csv file", csv_filename_action)
            with open(csv_filename_action, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)   
                                       
        elif user_input == "drama":
            
            print("inside drama_if")
            csv_filename_drama ='movies_drama.csv'
            with open(csv_filename_drama, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for drama in movies_drama:
                    name = drama.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = drama.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = drama.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(drama.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    #print(name)
                    # #print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the drama csv file", csv_filename_drama)
            with open(csv_filename_drama, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                    
        elif user_input == "comedy":
            
            print("inside comedy_if")
            csv_filename_comedy ='movies_comedy.csv'
            with open(csv_filename_comedy, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for comedy in movies_comedy:
                    name = comedy.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = comedy.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = comedy.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(comedy.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    #print(name)
                    # #print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the drama csv file", csv_filename_comedy)
            with open(csv_filename_comedy, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                    
        elif user_input == "animation":
            
            print("inside animation_if")
            csv_filename_animation ='movies_animation.csv'
            with open(csv_filename_animation, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for animation in movies_animation:
                    name = animation.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = animation.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = animation.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(animation.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    #rating = animation.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text
                    #print(name)
                    # #print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the drama csv file", csv_filename_animation)
            with open(csv_filename_animation, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                    
        elif user_input == "romance":
            
            print("inside romance_if")
            csv_filename_romance ='movies_romance.csv'
            with open(csv_filename_romance, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for romance in movies_romance:
                    name = romance.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = romance.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = romance.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(romance.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    #print(name)
                    # #print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the drama csv file", csv_filename_romance)
            with open(csv_filename_romance, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        elif user_input == "sci-fic":
            
            print("inside action_if")
            csv_filename_sci_fic ='movies_romance.csv'
            with open(csv_filename_sci_fic, mode ='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                header =['Rank','Name','rating','Year']
                writer.writerow(header)
                for sci_fic in movies_sci_fic:
                    name = sci_fic.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[1]
                    rank = sci_fic.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").h3.text.split('.')[0]
                    year = sci_fic.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                    rating = float(sci_fic.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split('.')[0])
                    #print(name)
                    # #print(rank)
                    # #print(year)
                    # #print(rating)
                    writer.writerow([rank, name, rating, year])     
            print("data has been written to the drama csv file", csv_filename_sci_fic)
            with open(csv_filename_sci_fic, mode ='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        else: 
            print("entered in correct Genre")
            
    except requests.exceptions.RequestException as e:
        print(e)
        
if __name__ == "__main__":
    main()
    