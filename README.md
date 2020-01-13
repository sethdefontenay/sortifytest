# sortifytest
## Contains a docker container which has very basic python API
### How to run:
* ```docker build -t sortifytest:latest .```
* ```docker run -d -p 5000:5000 sortifytest:latest```
* Then send a GET request via postman (or whatever you like)
* ```http://localhost:5000?input=teststring```


