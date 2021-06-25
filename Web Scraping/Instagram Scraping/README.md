# InstagramScraping

This project focuses on getting user, hastag, posts related information from Instagram. 

## Requirements
**pip install Instagramy** to access the Instagramy library.<br/> **SessionId** is required for interacting with Instagram API.

## How to get Credentials(SessionId) to interact with Instagram API

For Login into Instagram via instagramy, session id is required. No username or password is needed. You must be login into Instagram via Browser to get session id

- Login into Instagram in default webbrowser
- Move to Inspect option
- Go to Application and then to Storage and then to Cookies and copy the sessionid

## Steps
- Getting the SessionId for authorization. 
- Extracting details of an Instagram user(name, no_of_followers, no_of_following, no_of_posts etc.) - **from instagramy import InstagramUser**
  - Analyzing user popularity (usernames,followers, following, no of posts) - **from instagramy.plugins.analysis import analyze_users_popularity**
- Extracting Instagram Hashtag details - **from instagramy import InstagramHashTag**
- Extracting Instagram Post details - **from instagramy import InstagramPost**
  - Getting posts location details - **from instagramy import InstagramLocation**
- Plugins for Downloading posts, profile pic,hastags - **from instagramy.plugins.download import* \**

## Process
The detailed steps are described in the [python file](https://github.com/HarshineeRoopakula/Web-Scraping-Project/blob/main/Instagram%20Scraping/Instagram_Webscraping.ipynb) attached. 
