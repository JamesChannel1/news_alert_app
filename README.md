# news_alert_app
This script checks for updates on a news website every 10mins. Note, the website name and class name are example names that can be changed to whatever website and class you want to webscrape/check for updates. 

The flow of the script:
creates database ---> webscrapes content from website ---> checks if content matches content already stored in database (from previously webscraped) ---> if content is different, then displays pop-up message notifying user that content has changed. if content is the same, then there is no pop-up message.
