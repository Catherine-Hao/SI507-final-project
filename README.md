## **SI507 Final Project Submission**

### Catherine Hao  |  haorlin@umich.edu

Welcome to Movie Recommendation System! Here we recommed you a movie you want from IMDb Top 1000 Movies, and its reviews as well! Have fun!

The system will ask the users a hierarchical set of questions about if they have preferences and what their preferencess are, like:
1. What type of certificate do you want for the movie, such as PG-13, R, M?
2. What type of genre do you want for the movie, such as Drama, Sci-Fi, Comedy?
3. What year do you want for the movie?
4. What rating do you want for the movie to have at least?
5. Who do you want for the director of the movie? 
6. Who do you want to be in the cast of the movie? 
7. How long do you want for the movie to last? 

The inputs of movie requirements are sensibily designed on the web page, and users can leave blank for the fields that they have no requirements for. After the user inputs their requirements, they can click on the "submit" button. They can also click the "reset" button to input again. The system would then retrieve the link of a recommended movie that meets the users' needs the best, and provide the users with the one piece of most popular movie reviews also from IMDb so that they could be informed of the actual feedback and make further decisions based off of that. Users can always click on "switch" to change to another piece of review. There are 25 pieces of reviews for a movie at most, however, IMDb do not provide the reviews for some of the movies within their "Top 1000 Most Popular Movies" list.

The basic data structure in this system is a tree. The 1000 pieces of movie data from IMDb could be organized into a tree based on whether the film fits the users' requirements. 

This system uses Flask to accomplish interactive and presentation functions. Brief instructions for how a user would interact with your program. 
