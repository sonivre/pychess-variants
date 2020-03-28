import base64
import os
import json
import logging
import string

logging.basicConfig(level=logging.DEBUG)

URI = os.getenv("URI", "http://127.0.0.1:8080")

REDIRECT_PATH = "/oauth"  # path of oauth callback in app
# lichess.org OAuth Apps Callback URL: https://pychess-variants.herokuapp.com/oauth
REDIRECT_URI = URI + REDIRECT_PATH

# lichess tokens for local dev users login
DEV_TOKEN1 = os.getenv("DEV_TOKEN1")
DEV_TOKEN2 = os.getenv("DEV_TOKEN2")

# client app id and secret from lichess.org
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# secret_key for session encryption
# key must be 32 url-safe base64-encoded bytes
FERNET_KEY = os.getenv("FERNET_KEY", string.ascii_letters[:42] + "_=")
SECRET_KEY = base64.urlsafe_b64decode(FERNET_KEY)
MAX_AGE = 3600 * 24 * 365

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb://127.0.0.1:27017")
MONGO_DB_NAME = "heroku_hdfj8qcd"

BOT_TOKENS = json.loads(os.getenv("BOT_TOKENS", "{}"))
FISHNET_KEYS = json.loads(os.getenv("FISHNET_KEYS", "{}"))
