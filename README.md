# api_NY

website : https://developer.nytimes.com/apis


To build the container and run the app:

docker build -t nytimes-app .
docker run -p 8080:8080 --name nytimes-container nytimes-app
