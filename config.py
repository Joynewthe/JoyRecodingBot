from os import environ

class Config(object):
    API_ID = int(environ.get("API_ID" 27744634))
    API_HASH = environ.get("API_HASH", "0db310b3f4e8b07d938bcf2295bcb03d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7370621547:AAHf59KoPaU5hsnJ7nsOP5Q05-Te8Hj3xIs")
    #The bot will work only with following users
    AUTH_USERS = list(int(x) for x in environ.get("AUTH_USERS", "1885207148").split(" "))
    #Owner ID is the user id of your telegram account
    OWNER_ID = int(environ.get("OWNER_ID", "1885207148"))
    #keep default unless you know what you are doing
    DOWNLOAD_DIRECTORY = environ.get("DOWNLOAD_DIRECTORY","./downloads")
   
