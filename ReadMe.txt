========================
entertainment_center.py
========================
Created by Alex Rich in August 2016
utilizing code from Udacity in the "movie trailer" project

This file utilizes several other python files to generate
a website that displays favorite movies with clickable 
movie posteres that link to youtube trailers for the movie

To do so, it:
-stores the classes "Video", "Movie", and "Tv_show" in media.py
-utilizes fresh_tomatoes.py to generate the html and open the browser necessary 
	to display output.

How to use:
=================
entertainment_center.py imports media.py and fresh_tomatoes.py, 
each of which must be stored in the same directory.
Objects are created in entertainment_center.py by calling the __init__ functions
of the classes defined in media.py and inputing the required data
(for Movies: Title, duration, storyline, url to poster, and url to youtube trailer)

Saving and executing entertainment_center.py should automatically open a webbrowser
and display the information in the code.