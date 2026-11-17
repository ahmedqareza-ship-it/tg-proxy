import os

PORT = int(os.environ.get("PORT", 4433))

# Secret يمكن تغييره من environment variable
_secret = os.environ.get("SECRET", "6a9a13d526dd99b5e513664451d8d1e6")

USERS = {
    "user1": _secret
}

USE_MIDDLE_PROXY = False
