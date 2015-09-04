DEBUG = True

# Database settings.
MONGODB_SETTINGS = {
  "db": "tavili",
  "host": "localhost",
  "port": 27017,
}

# Web URL settings.
WEB_SHORT_DOMAIN = "localhost:5000"
WEB_FULL_DOMAIN = "http://localhost/"
WEB_USE_HTTPS = False
WEB_USE_SUBDOMAINS = False

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

MANDRILL_API_KEY = "HShwAStG1GP76vMiLLxpzg"
MANDRILL_UPDATE_INTERVAL_SECONDS = 60