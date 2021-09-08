
from Twitter_Bot import TwitterBot

import undetected_chromedriver.v2 as uc
driver = uc.Chrome()
with driver:
    driver.get('https://nowsecure.nl')

twitter_bot = TwitterBot(driver=driver, username='username',password='password',message='message')
twitter_bot.run_bot()