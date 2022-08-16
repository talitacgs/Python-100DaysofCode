from InternetSpeedTwitterBot import InternetSpeedTwitter

PROMISED_DOWN = 500
PROMISED_UP = 50
TWITTER_EMAIL = "YOUR.EMAIL@HERE.COM"
TWITTER_PASSWORD = "YOUR_PASSWORD"


chrome_drive_path = "C:\Development\chromedriver.exe"
bot = InternetSpeedTwitter(chrome_drive_path)

bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP)
