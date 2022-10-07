from instafollowerbot import InstaFollower

chrome_drive_path = "C:\Development\chromedriver.exe"

SIMILAR_ACCOUNT = "dog_agiota1"
USERNAME = "100_days_python_bootcamp"
PASSWORD = "coolpeople"

bot = InstaFollower(chrome_drive_path)

bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
