## **SI507 Final Project Submission**

### Catherine Hao  |  haorlin@umich.edu

"Welcome to Movie Recommendation System! Here we recommed you a movie you want from IMDb Top 1000 Movies, and its reviews as well! Have fun!"

The system will ask the users a set of questions about if they have preferences and what their preferencess are, like these:

1. Do you have preference for the movie's cerificate?
What type of certificate do you want for the movie, such as PG-13, R, M?
2. Do you have preference for the movie's genre?
What type of genre do you want for the movie, such as Drama, Sci-Fi, Comedy? (You can input multiple genres with " " in between)
3. Do you have preference for the released year of the movie?
What year do you want for the movie? (you can input a time period like "1990-2000", or one certain year like "1995")
4. Do you have preference for the movie's rating?
What rating do you want for the movie to have at least?
5. Do you have preference for the movie's director?
Who do you want for the director of the movie? (You can input multiple names with " " in between)
6. Do you have preference for the movie's cast?
Who do you want to be in the cast of the movie? (You can input multiple names with " " in between)
7. Do you have preference for the movie's runtime?
How long do you want for the movie to last? (you can input a time range like \"80-120\")
This system uses Flask to conduct interactive and presentation functions. Brief instructions for how a user would interact with your program. First, for every attribute the movie, the system would first ask whether they have requirement for that certain attribute, and then would be more specific about what their requirement is. Then, after this is done, the system would randomly select a movie that meet the users’ need. If there is not a movie that would satisfy the user, the system would recommend the user to try again. Lastly, the system would inform the user about the recommended movie’s title and would jump to the movie’s IMDb web page for further information. It would also provide with a list of 25 reviews of the movie.
