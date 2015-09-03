DEBUG = True

# Database settings.
MONGODB_SETTINGS = {
  "db": "tavili",
  "host": "mongodb://tavili:tavilitavili99@ds035563.mongolab.com:35563/heroku_t2vv4d0p",
  "port": 35563,
}

# Web URL settings.
WEB_SHORT_DOMAIN = "intense-badlands-1277.herokuapp.com"
WEB_FULL_DOMAIN = "https://intense-badlands-1277.herokuapp.com/"
WEB_USE_HTTPS = True
WEB_USE_SUBDOMAINS = True

# User authentication settings.
SECRET_KEY = "I'M A SECRET KEY! REALLY!!"
REMEMBER_COOKIE_NAME = "tavili"
REMEMBER_COOKIE_DOMAIN = "." + WEB_SHORT_DOMAIN
TOKEN_TIMEOUT = 30*24*60*60  # 1 month.
TOKEN_ROLE_SETTINGS = {
  "USER": {
    "COOKIE_TIMEOUT": 24*60*60,  # 1 day.
    "SESSION_TIMEOUT": 30*60,  # 30 minutes.
  },
}

