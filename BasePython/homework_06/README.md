### Assignment "Containers Interactions"
#### Problem
- create docker-compose file, set connection between the database and web application
- add models for database
- add support for adding new records
- create a webpage displaying all added records
- database should be running in a separate container
- Flask web app should be running in a production-ready mode (uwsgi, nginx, unicorn)

### Result

![hw06_preview](https://user-images.githubusercontent.com/23639048/160006797-2ab4a2fc-90d6-4ed6-b92f-f3097702b62d.png)

- `User` model added 
- `localhost:5000` page displays list of all added users
- `localhost:5000/add` page is for adding new user to the database
- Flask web app is set for production-mode regime 
