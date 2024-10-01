import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "10658015")

API_HASH = os.environ.get("API_HASH", "a0087bca748f86698c53d291c9e5b3af")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7927233081:AAHP8rlBz8Q8ngUCxuOZdPAKuL4N670j9RU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Renamechannel4") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://helphm9:MO7vlO8DtXqezh3i@cluster0.mom8p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://i.imgur.com/U8vcDOf.jpeg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6170962395').split()]

PORT = os.environ.get("PORT", "8080")
