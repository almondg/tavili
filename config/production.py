
# Database settings.
MONGODB_SETTINGS = {
  "db": "heroku_t2vv4d0p",
  "host": "mongodb://tavili:tavilitavili99@ds035563.mongolab.com:35563/heroku_t2vv4d0p",
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
  "CLIENT": {
    "COOKIE_TIMEOUT": 30*24*60*60,  # 1 month.
  },
  "ADMIN": {
    "COOKIE_TIMEOUT": 24*60*60,  # 1 day.
  },
}


MANDRILL_API_KEY = "HShwAStG1GP76vMiLLxpzg"
MANDRILL_UPDATE_INTERVAL_SECONDS = 60