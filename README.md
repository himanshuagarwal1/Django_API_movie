# AccentDesign Django Tech Test Backend

## Running with Docker

- A sample Dockerfile and a docker-compose is provided to run the application in an isolated environment
- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build and run the container: `docker-compose up`
- Start making some requests: `curl http://localhost:8000/movies/`

## Running with a virtual environment

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment for 3.9.6
- Check you have the pyenv version you need: `pyenv versions`
- You should see 3.9.6
- If you do not have the correct version of Python, install it like this: `pyenv install 3.9.6`
- On command line do this: `~/.pyenv/versions/3.9.6/bin/python -m venv env`
- This creates a folder called env. Then do this to activate the virtual environment: `source env/bin/activate`
- Lastly do this to check that you are now on the correct Python version: `python --version`
- You can install the dependencies with `pip install -r requirements.txt`

- You can then run the app with `python manage.py runserver 0.0.0.0:8000` in the root directory

## Running with a on CMD without any virtualization


- Clone repository.
- install Python
- You can install the dependencies with `pip install -r requirements.txt`

- You can then run the app with `python manage.py runserver ` in the root directory
## Project Structure Notes

- There are two django apps installed `movies` and `comments`
- Django is used as a RESTful API, no html rendering is required
- Marshmallow is used to serialize and deserialize django object instances

Project structure:
```
.
├── README.md
├── manage.py
├── requirements.txt
|── test.py
└── techtest(App Folder)
```
POST http://127.0.0.1:8000/movies/

REQUEST
```json
{
	"t": "300"
}
```
RESPONSE
```json
   
{
    "Title": "300", "Year": "2006", 
"Rated": "R", "Released": "09 Mar 2007", "id":1,
"Runtime": "117 min", "Genre": "Action, Drama", 
"Director": "Zack Snyder", "Writer": "Zack Snyder, Kurt Johnstad, Michael B. Gordon", 
"Actors": "Gerard Butler, Lena Headey, David Wenham", "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
"Language": "English", "Country": "United States, Canada, Bulgaria", "Awards": "19 wins & 55 nominations", 
"Poster": "https://m.media-amazon.com/images/M/MV5BNWMxYTZlOTUtZDExMi00YzZmLTkwYTMtZmM2MmRjZmQ3OGY4XkEyXkFqcGdeQXVyMTAwMzUyMzUy._V1_SX300.jpg", 
"Metascore": "52", "imdbRating": "7.6", "imdbVotes": "801,393", "imdbID": "tt0416449", "Type": "movie", 
"DVD": "31 Jul 2007", "BoxOffice": "$210,629,101", "Production": "N/A", "Website": "N/A", "Response": "True"
}
PUT http://127.0.0.1:5000/users/1

REQUEST
```json
{
	"Title": "change_name"
}
```
RESPONSE
```json
{
   "Title": "change_name", "Year": "2006","id":1, 
"Rated": "R", "Released": "09 Mar 2007", 
"Runtime": "117 min", "Genre": "Action, Drama", 
"Director": "Zack Snyder", "Writer": "Zack Snyder, Kurt Johnstad, Michael B. Gordon", 
"Actors": "Gerard Butler, Lena Headey, David Wenham", "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
"Language": "English", "Country": "United States, Canada, Bulgaria", "Awards": "19 wins & 55 nominations", 
"Poster": "https://m.media-amazon.com/images/M/MV5BNWMxYTZlOTUtZDExMi00YzZmLTkwYTMtZmM2MmRjZmQ3OGY4XkEyXkFqcGdeQXVyMTAwMzUyMzUy._V1_SX300.jpg", 
"Metascore": "52", "imdbRating": "7.6", "imdbVotes": "801,393", "imdbID": "tt0416449", "Type": "movie", 
"DVD": "31 Jul 2007", "BoxOffice": "$210,629,101", "Production": "N/A", "Website": "N/A", "Response": "True"
}
```

GET http://127.0.0.1:5000/movies

RESPONSE
```json
{
   "Title": "change_name", "Year": "2006","id":1, 
"Rated": "R", "Released": "09 Mar 2007", 
"Runtime": "117 min", "Genre": "Action, Drama", 
"Director": "Zack Snyder", "Writer": "Zack Snyder, Kurt Johnstad, Michael B. Gordon", 
"Actors": "Gerard Butler, Lena Headey, David Wenham", "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
"Language": "English", "Country": "United States, Canada, Bulgaria", "Awards": "19 wins & 55 nominations", 
"Poster": "https://m.media-amazon.com/images/M/MV5BNWMxYTZlOTUtZDExMi00YzZmLTkwYTMtZmM2MmRjZmQ3OGY4XkEyXkFqcGdeQXVyMTAwMzUyMzUy._V1_SX300.jpg", 
"Metascore": "52", "imdbRating": "7.6", "imdbVotes": "801,393", "imdbID": "tt0416449", "Type": "movie", 
"DVD": "31 Jul 2007", "BoxOffice": "$210,629,101", "Production": "N/A", "Website": "N/A", "Response": "True"
}
GET http://127.0.0.1:5000/api/movies/1
```json
{
   "Title": "change_name", "Year": "2006","id":1, 
"Rated": "R", "Released": "09 Mar 2007", 
"Runtime": "117 min", "Genre": "Action, Drama", 
"Director": "Zack Snyder", "Writer": "Zack Snyder, Kurt Johnstad, Michael B. Gordon", 
"Actors": "Gerard Butler, Lena Headey, David Wenham", "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
"Language": "English", "Country": "United States, Canada, Bulgaria", "Awards": "19 wins & 55 nominations", 
"Poster": "https://m.media-amazon.com/images/M/MV5BNWMxYTZlOTUtZDExMi00YzZmLTkwYTMtZmM2MmRjZmQ3OGY4XkEyXkFqcGdeQXVyMTAwMzUyMzUy._V1_SX300.jpg", 
"Metascore": "52", "imdbRating": "7.6", "imdbVotes": "801,393", "imdbID": "tt0416449", "Type": "movie", 
"DVD": "31 Jul 2007", "BoxOffice": "$210,629,101", "Production": "N/A", "Website": "N/A", "Response": "True"
}
```



Comments endpoint is similar to movies endpoint you just need to pass valid movie if while making a POST request.

ex:- data = {"id": 1, "Comments": "this is a comment "}


run python manage.py test for unitest of the endpoints
