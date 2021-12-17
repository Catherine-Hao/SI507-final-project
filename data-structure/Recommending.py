
import json
def movies_json():
    with open(r'/Users/zhhang/Desktop/si507/data/movies.json') as f:
        movies = json.load(f)
        return movies


class Node:
    def __init__(self, movies_list):
        self.parent = movies_list
        self.yes = None
        self.no = None
        self.condition = None
    def __str__(self):
        return f'{self.parent}'
    def search(self, cond):
        movies_yes, movies_no = cond.if_condition()
#         print(movies_yes)
#         print(movies_no)
        self.yes = Node(movies_yes)
        self.no = Node(movies_no)



class if_cert:
    def __init__(self, con_certificate, movies):
        self.con_certificate = con_certificate
        self.movies = movies
    def if_condition(self):
        certificate_yes = []
        certificate_no = []
        if self.con_certificate != '':
            for i in self.movies:
                if i['certificate'] == self.con_certificate:
                    certificate_yes.append(i)
                else:
                    certificate_no.append(i)
            return certificate_yes, certificate_no
        else:
            return self.movies, []


class if_genre:
    def __init__(self, con_genre1, con_genre2, con_genre3, movies):
        self.con_genre1 = con_genre1
        self.con_genre2 = con_genre2
        self.con_genre3 = con_genre3
        self.movies = movies
    def if_condition(self):
        genre_yes = []
        genre_no = []
        if self.con_genre1 != '' or self.con_genre2 != '' or self.con_genre3 != '':
            input_genres = [self.con_genre1, self.con_genre2, self.con_genre3]
            valid_genres = [vg for vg in input_genres if vg != '']
            valid_genres = set(valid_genres)
            for n in self.movies:
                n_list = n['genre'].split(', ')
                if set(valid_genres).issubset(set(n_list)):
                    genre_yes.append(n)
                else:
                    genre_no.append(n)
            return genre_yes, genre_no
        else:
            return self.movies ,[]


class if_year:
    def __init__(self, con_year_min, con_year_max, movies):
        self.con_year_min = con_year_min
        self.con_year_max = con_year_max
        self.movies = movies
    def if_condition(self):
    # if there's requirement for year
        if self.con_year_min != '' or self.con_year_max != '':
            year_yes =[]
            year_no =[]
            if self.con_year_min != '' and self.con_year_max != '':
                y_min = min(int(self.con_year_min), int(self.con_year_max))
                y_max = max(int(self.con_year_min), int(self.con_year_max))
                for y in self.movies:
                    if y_min <= int(y['year'][-5:-1]) <= y_max:
                        year_yes.append(y)
                    else: 
                        year_no.append(y)
            elif self.con_year_max == '':
                for y in self.movies:
                    if int(y['year'][-5:-1]) >= int(self.con_year_min):
                        year_yes.append(y)
                    else: 
                        year_no.append(y)
            elif self.con_year_min == '':
                for y in self.movies:
                    if int(y['year'][-5:-1]) <= int(self.con_year_max):
                        year_yes.append(y)
                    else: 
                        year_no.append(y)
            return year_yes, year_no
        else:
            return self.movies, []



class if_rating:
    def __init__(self, con_rating, movies):
        self.con_rating = con_rating
        self.movies = movies
    def if_condition(self):
        rating_yes =[]
        rating_no =[]
        # if there's requirement for rating
        if self.con_rating != '':
            for r in self.movies:
                if float(r['overview']) >= float(self.con_rating):
                    rating_yes.append(r)
                else:
                    rating_no.append(r)
            return rating_yes, rating_no
        else:
            return self.movies, []




class if_director:
    def __init__(self, con_director, movies):
        self.con_director = con_director
        self.movies = movies
    def if_condition(self):
        director_yes =[]
        director_no =[]
        # if there's requirement for director
        if self.con_director != '':
            input_director = self.con_director.lower().split(",")
            input_director = [i.strip() for i in input_director]
            for s in self.movies:
                s_list = s['director'].lower().split(', ')
                if set(input_director).issubset(set(s_list)):
                    director_yes.append(s)
                else:
                    director_no.append(s)
            return director_yes ,director_no
        else:
            return self.movies, []




class if_star:
    def __init__(self, con_star, movies):
        self.con_star = con_star
        self.movies = movies
    def if_condition(self):
        star_yes =[]
        star_no =[]
        # if there's requirement for star
        if self.con_star != '':
            input_stars = self.con_star.lower().split(",")
            input_stars = [i.strip() for i in input_stars]
            for s in self.movies:
                s_list = s['stars'].lower().split(', ')
                if set(input_stars).issubset(set(s_list)):
                    star_yes.append(s)
                else:
                    star_no.append(s)
            return star_yes, star_no
        else:
            return self.movies, []



class if_runtime:
    def __init__(self, con_runtime_min, con_runtime_max, movies):
        self.con_runtime_min = con_runtime_min
        self.con_runtime_max = con_runtime_max
        self.movies = movies
    def if_condition(self):
    # if there's requirement for runtime
        if self.con_runtime_min != '' or self.con_runtime_max != '':
            runtime_yes =[]
            runtime_no =[]
            if self.con_runtime_min != '' and self.con_runtime_max != '':
                y_min = min(int(self.con_runtime_min), int(self.con_runtime_max))
                y_max = max(int(self.con_runtime_min), int(self.con_runtime_max))
                for y in self.movies:
                    if y_min <= int(y['runtime'][0:-4]) <= y_max:
                        runtime_yes.append(y)
                    else: 
                        runtime_no.append(y)
            elif self.con_runtime_min == '':
                for y in self.movies():
                    if int(y['runtime'][0:-4]) <= int(self.con_runtime_max):
                        runtime_yes.append(y)
                    else: 
                        runtime_no.append(y)
            elif self.con_runtime_max == '':
                for y in self.movies:
                    if int(y['runtime'][0:-4]) >= int(self.con_runtime_min):
                        runtime_yes.append(y)
                    else: 
                        runtime_no.append(y)
            return runtime_yes, runtime_no
        else:
            return self.movies, []


def recommending_classes(movies, con_certificate, con_genre1, con_genre2, con_genre3, con_year_min, con_year_max,
                         con_rating, con_director, con_cast, con_runtime_min, con_runtime_max):
    ms_total = Node(movies)
    ms_list = []
    ms_list.append(ms_total)

    cond1 = if_cert(con_certificate, ms_total.parent)
    ms_total.search(cond1)
    ms_certificate = ms_total.yes
    ms_list.append(ms_certificate)

    cond2 = if_genre(con_genre1, con_genre2, con_genre3, ms_certificate.parent)
    ms_certificate.search(cond2)
    ms_genre = ms_certificate.yes
    ms_list.append(ms_genre)

    cond3 = if_year(con_year_min, con_year_max, ms_genre.parent)
    ms_genre.search(cond3)
    ms_year = ms_genre.yes
    ms_list.append(ms_year)

    cond4 = if_rating(con_rating, ms_year.parent)
    ms_year.search(cond4)
    ms_rating = ms_year.yes
    ms_list.append(ms_rating)

    cond5 = if_director(con_director, ms_rating.parent)
    ms_rating.search(cond5)
    ms_director = ms_rating.yes
    ms_list.append(ms_director)

    cond6 = if_star(con_cast, ms_director.parent)
    ms_director.search(cond6)
    ms_star = ms_director.yes
    ms_list.append(ms_star)

    cond7 = if_runtime(con_runtime_min, con_runtime_max, ms_star.parent)
    ms_star.search(cond7)
    ms_runtime = ms_star.yes
    ms_list.append(ms_runtime)

    ms_list.reverse()
    for j in ms_list:
        if j.parent:
            recommended_ms = j.parent
            break
    # if not ms_certificate.parent:
    #     if not ms_genre.parent:
    #         if not ms_year.parent:
    #             if not ms_rating.parent:
    #                 if not ms_director.parent:
    #                     if not ms_star.parent:
    #                         if not ms_runtime.parent:
    #                             recommend_ms = ms_runtime.parent
    #                         else:
    #                             recommend_ms = ms_star.parent
    #                     else:
    #                         recommend_ms = ms_director.parent
    #                 else:
    #                     recommend_ms = ms_rating.parent
    #             else:
    #                 recommend_ms = ms_year.parent
    #         else:
    #             recommend_ms = ms_genre.parent
    #     else:
    #         recommend_ms = ms_certificate.parent
    # else:
    #     recommend_ms = movies
    return recommended_ms
movies = movies_json()
ms_list = recommending_classes(movies, 'PG-13', 'Crime', '', '', '', '',
                             '', '', '', '', '')


