import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import webbrowser
import requests
import flask
from flask import Flask
import json

# Data Source 1:
# url: https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv
# Scraping 20  IMDb pages.

url_50 = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
urls=[url_50]
for i in range(1,20):
    start=1+50*i
    url_tmp='https://www.imdb.com/search/title/?groups=top_1000&start='+ str(start) + '&ref_=adv_nxt'
    urls.append(url_tmp)

titles = []
years = []
time = []
genres=[]
certificates=[]
overviews=[]
imdb_ratings = []
metascores = []
votes = []
us_gross = []
directors=[]
stars=[]
ids=[]
imdb_urls=[]

# scraping data with Beautiful Soup
for url in urls:
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')
    for container in movie_div:

            #name
            name = container.h3.a.text
            titles.append(name)
            
            #imdb_id
            imdb_id = container.h3.a.get('href').replace('/title/','')[:-1]
            ids.append(imdb_id)
            
            #imdb_url
            imdb_url = "https://www.imdb.com" + container.h3.a.get('href')
            imdb_urls.append(imdb_url)

            #year
            year = container.h3.find('span', class_='lister-item-year').text
            years.append(year)

            #certificate
            try:
                certificate = container.p.find('span', class_='certificate').text 
            except:
                certificate = '-'
            certificates.append(certificate)

            #runtime
            runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
            time.append(runtime)

            #genre
            genre = container.p.find('span', class_='genre').text[1:] if container.p.find('span', class_='genre').text[1:] else '-'
            genre = genre.rstrip()
            genres.append(genre)


            #overview
            overview = container.find_all(class_="text-muted")[2].text[1:] if container.find_all(class_="text-muted")[2].text[1:] else '-'
            overviews.append(overview)

            #director & stars
            director = ' '.join(container.find_all('p')[2].text.split()).split(' | ')[0].replace('Director: ', '') if ' '.join(container.find_all('p')[2].text.split()).split(' | ')[0].replace('Director: ', '') else '-'
            director = director.replace('Directors: ', '')
            directors.append(director)

            #star
            star = ' '.join(container.find_all('p')[2].text.split()).split(' | ')[1].replace('Stars: ', '') if ' '.join(container.find_all('p')[2].text.split()).split(' | ')[1].replace('Stars: ', '') else '-'
            stars.append(star)

            #IMDB rating
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)

            #metascore
            m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
            m_score = m_score.rstrip()
            metascores.append(m_score)

            #There are two NV containers, grab both of them as they hold both the votes and the grosses
            nv = container.find_all('span', attrs={'name': 'nv'})

            #filter nv for votes
            vote = nv[0].text
            votes.append(vote)

            #filter nv for gross
            grosses = nv[1].text if len(nv) > 1 else '-'
            us_gross.append(grosses)
            
            
            
#building our Pandas dataframe         
movies = pd.DataFrame({
'title': titles,
'imdb_id':ids,
'imdb_url':imdb_urls,
'year': years,
'certificate':certificates,
'runtime': time,
'genre':genres,
'director':directors,
'stars':stars,
'overview':overviews, 
'rating': imdb_ratings,
'metascore': metascores,
'votes': votes,
'us_gross': us_gross,
})

#cleaning data with Pandas
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['runtime'] = movies['runtime'].str.extract('(\d+)').astype(int)
try:
    movies['metascore'] = movies['metascore'].astype(int)
except:
    movies['metascore'] = movies['metascore']
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['us_gross'] = movies['us_gross'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_gross'] = pd.to_numeric(movies['us_gross'], errors='coerce')

movies.to_csv(r'D:\U-M\SI_507\final_project\movies.csv')


# writing json file
import json
movies_list=[]

for i in range(len(movies)):
    movies_dict = {}
    movies_dict['title'] = titles[i]
    movies_dict['imdb_id'] = ids[i]
    movies_dict['imdb_url'] = imdb_urls[i]
    movies_dict['year'] = years[i]
    movies_dict['certificate'] = certificates[i]
    movies_dict['runtime'] = time[i]
    movies_dict['genre'] = genres[i]
    movies_dict['director'] = directors[i]
    movies_dict['stars'] = stars[i]
    movies_dict['overview'] = imdb_ratings[i]
    movies_dict['metascore'] = metascores[i]
    movies_dict['votes'] = votes[i]
    movies_dict['us_gross'] = us_gross[i]
    movies_list.append(movies_dict)

with open(r'D:\U-M\SI_507\final_project\movies.json', "w") as jsonw:
    movies_json = json.dumps(movies_list, indent=4)
    jsonw.write(movies_json)
    jsonw.close()



# Data Source 2: 
# url: https://imdb-api.com/en/API/Reviews/
# The IMDb Web API requires API key. 
# My IMDb API key is 'k_nm384tne'.

# accessing IMDb reviews using API keY
import requests
IMDb_API_KEY = 'k_nm384tne'
url_review= ['https://imdb-api.com/en/API/Reviews/'+IMDb_API_KEY+'/'+i for i in movies['imdb_id']]
# base_url = 'https://imdb-api.com/en/API/Reviews/'+IMDb_API_KEY+'/tt1375666'
response = requests.get(url_review[0])
review = response.json()
review_json= json.dumps(review, indent=4)
print(review_json)

# writing json file
with open(r'D:\U-M\SI_507\final_project\reviews_example.json', "w") as jsonw:
    jsonw.write(result_json)
    jsonw.close()