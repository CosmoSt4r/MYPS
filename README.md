# Make your passwords safe!

> Password manager with Flask

## Functionality
__________________________

### Log In and Sign Up

![Login and Signup forms](https://github.com/CosmoSt4r/MYPS/blob/master/readme/account.jpg?raw=true)

First of all you have to **Sign up** or **Log in** if you already have an account.<br>
**Username** and **password** should be longer than 6 characters.

__________________________

### Homepage

![Homepage](https://github.com/CosmoSt4r/MYPS/blob/master/readme/home.jpg?raw=true)

On the **Homepage** you'll see all of your passwords with logins and URLs.<br>
You can **add** new password, **update** or **delete** an existing one.
__________________________

### Creating and Updating passwords

![Create and Update forms](https://github.com/CosmoSt4r/MYPS/blob/master/readme/password.jpg?raw=true)

__________________________

<br>

## How to install?


### Clone

Clone this repo to your local machine using `https://github.com/CosmoSt4r/MYPS`

### Required packages

To start the server you need the following packages: 

 - Flask
 - Flask-SQLAlchemy
 - Pypasswords
 - Cryptography
 - Zxcvbn

To install packages:

```py
cd MYPS
pip install -r requirements.txt
```

### Starting the server

```py
python main.py
```
> or just open `main.py`

### Opening app in browser

Open your browser and go to the `127.0.0.1:5000` address. You will see the login page.

### Credits

Inspired by [Flask Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=PLYqVE-1VuKv63jvgb3kvY1P63EAkfACTP) 
from [freeCodeCamp](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) YouTube channel.

App style from [Login page tutorial](https://www.youtube.com/watch?v=HV7DtH3J2PU) by 
[Dark Code's](https://www.youtube.com/channel/UCD3KVjbb7aq2OiOffuungzw) YouTube channel.
