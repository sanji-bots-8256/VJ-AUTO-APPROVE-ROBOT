# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28525384"))
    API_HASH = getenv("API_HASH", "3a1190585fe5bf1f6324be87ba5b68c6")
    BOT_TOKEN = getenv("BOT_TOKEN", "6097625674:AAEp6qhHBM9Kf4ChUoRfgVRKHAP9eWdth6E")
    FSUB = getenv("FSUB", "Straw_Hat_Bots")
    CHID = int(getenv("CHID", "-1002059817947"))
    SUDO = list(map(int, getenv("SUDO", "6727550037 7162615398").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
