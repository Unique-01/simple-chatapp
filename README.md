
# Simple Chatapp

Simple chatapp using django, django-channels and websocket



## Features

- Login / Signup
- Chat with other users in the same room

## ScreenShots
![chatlogin](https://user-images.githubusercontent.com/86983696/211806079-c1274a0b-2982-4db1-ae24-93aa5d9c5a1e.png)
![chatroom](https://user-images.githubusercontent.com/86983696/211806108-e245e702-8ada-4d83-a68a-354c369f98c3.png)

## Installation
* Clone the Repository
* Create a Virtual environment
```bash
  virtualenv venv
  source venv/bin/activate
```
- Go to the project directory
```bash
    cd chatrealtime
```
- Inside the project folder
- Run the following command in the terminal 
```bash
    pip install -r requirements.txt
```  
- Open the settings file and change DEBUG to True 
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`EMAIL_HOST_USER`

`EMAIL_HOST_PASSWORD`




## Run Locally

Start the server with

```bash
    python manage.py runserver
```
or

```bash 
    daphne chatrealtime.asgi:application
```
- It will run the application on your localhost
- Open the browser with the localhost address and enjoy the application
