# connecta-api
This is API for android app Connecta, where you can create and store you business cards

# Installation
1. Clone git repository
2. Create a virtual enviroment and activate it
```
python -m venv venv
```
If you have Windows to activate this you need run this command:
```
venv\Scripts\activate
```
3. Install all dependencies 
```
pip3 install -r requirements.txt
```

# Configuring
1. Open bash terminal and enter this command:
```
openssl rand -hex 32
```
Then you'll be given a secret key

2. Create .env file(MAKE .env FILE, NOT .env.txt)
3. Write options in .env like this:
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=password of your postgres
DATABASE_NAME=connecta
DATABASE_USERNAME=postgres username
SECRET_KEY=secret key, that you get in 1 step
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
## ALERT!!! YOU NEED TO CREATE A DB IN POSTGRES WITH NAME "connecta"
4. Run this command in terminal VS Code, Powershell, Bash or else:
```
alembic upgrade 616c3a64bd42
```
This will migrate all database tables in PostgreSQL

# Running a local server
1. Run this command in the terminal:
```
uvicorn app.main:app --reload
```
This command will run the local server
If you get messages in terminal like this:
```
INFO:     Will watch for changes in these directories: [path to your repository]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7428] using WatchFiles
INFO:     Started server process [12476]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Congrats! You run the API!
