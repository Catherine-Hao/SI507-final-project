## **SI507 Final Project**

### Catherine Hao  |  haorlin@umich.edu

Welcome to Movie Recommendation System! Here we recommed you a movie you want from IMDb Top 1000 Movies, and its reviews as well! Have fun! You can check the [demo](https://youtu.be/m7d1o3C2U7o) for further information.

The system will ask the users a hierarchical set of questions about what their preferences are, like:
- What type of certificate do you want for the movie, such as PG-13, R, M?
- What type of genre do you want for the movie, such as Drama, Sci-Fi, Comedy?
- What year do you want for the movie?
- What rating do you want for the movie to have at least?
- Who do you want for the director of the movie? 
- Who do you want to be in the cast of the movie? 
- How long do you want for the movie to last? 

<b>Instructions: </b> </br>
The inputs of movie preferences are sensibily designed on the web page, and users can leave blank for the fields that they have no preferences for. After the user inputs their preferences, they can click on the "submit" button. They can also click the "reset" button to input again. The system would then retrieve the link of a recommended movie that meets the users' needs the best, and provide the users with the one piece of most popular movie reviews also from IMDb so that they could be informed of the actual feedback and make further decisions based off of that. Users can always click on "switch" to change to another piece of review. On most occasions, there are 25 pieces of reviews for a movie at most. However, IMDb do not provide the reviews for some of the movies within their "Top 1000 Most Popular Movies" list, and the system would output a "Sorry! There's no review for this movie!"

<b>Perferences Specifications:</b> </br>
- Certificate: Users are given a list of selections for all certificate types for all 1000 movies. 
- Genre: Users are given a list of selections for all certificate types for all 1000 movies, and can select three types of genres.
- Year: Users can input the first blank representing for the earliest year when the movie has been released while the second blank for the lastest year. If both blanks have inputs, the system would automatically recognize the smaller number of the two as the earliest year and the other one as the latest year.
- Rating: Users can input a integer or decimal on the scale of 1-10 representing for the rating they would like the movie to have at least.
- Director: Users can input the name of a director, or names of multiple directors with "," in between. This input is not case sensitive.
- Cast: Users can input the name of an actor, or names of multiple actors with "," in between. This input is not case sensitive.
- Runtime: Users can input the first blank representing for the shortest runtime while the second blank for the longest runtime. If both blanks have inputs, the system would automatically recognize the smaller number of the two as the shortest runtime and the other one as the longest runtime. The unit of this input is minute.

<b>Data Structure: </b> </br> 
The basic data structure in this system is a tree. The 1000 pieces of movie data from IMDb could be organized into a tree based on whether the film fits the users' requirements. Following the order of the hierarchical set of questions, the movie data which doesn't meet the users' preferences would be abondoned. However, if there's no movie that exactly fit the users' needs, the system would return to the last node of the tree which has values to retrieve a movie that fits the user' needs.

<b>Packages: </b></br>
The python packages for this system to work besides the built in packages include requests, flask, BeautifulSoup, webbrowser, pandas, etc.

<b>Codes: </b> </br>
In data-source repository: 
- data_source.py: to implement data scraping for IMDb movies and accessing data using API Key for IMDb reviews;
- movies.csv: the .csv file storing the [IMDB movies](https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv) data;
- movies.json: the .json file storing the [IMDB movies](https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv) data;
- reviews_example.json: an example of the .json file storing the [IMDB reviews](https://imdb-api.com/en/API/Reviews/k_nm384tne/tt1160419) for Dune.
  
In data-structure repository: 
- main.py: the main .py file ruuning the movie recommendation system;
- Recommending.py: the .py file that reads the json of the movie tree.
  - In templates repository:
  - -movie_recommendation.html: the html template for the front page of the movie recommendation system;
  - -movie_response.html: the html template for the result page of the movie recommendation.
  
  
  
  
  
