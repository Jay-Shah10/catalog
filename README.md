# catalog
Django version of Flask app catalog

## Summary
This applicatin is a remake of the Flask application created from Full Stack Nano-Degree Program.
This application displays genres and movies, when a user clicks on a genre they can view all movies related 
to that genre. When the user clicks on a movie's view button it will display movie's information. 

### Requirements
```
* python3
```

## How to
Clone the repository.
You will need to create a python environment. 
```
python3 -m venv venv
(linux/mac) source venv/bin/activate
(windows) .\venv\Scripts\activate
```
Install from requirements.txt
```
pip install -r requirements.txt
```
You should have django at this point and you should be able to run runserver. 
Make sure you are in the same directory as ```manage.py ``` and run the following command. 
```
python manage.py runserver
```
This will boot the django server. ```localhost:8000```. You should see Catalog UI. 

This is still under-development.



### Resources
* [Django Context Processors](https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi)


### Disclaimer 
All movie poster images are not owned by me. These have been taken from google and IMDB. 
Including the movie descriptions. [Example](https://www.imdb.com/title/tt0120338/?ref_=fn_al_tt_1)