# Twitter notification on discord
<p>You are free to distribute and modify the code</p>

## Pre-requisites
<p>A discord developer account to create a bot token for the discord bot</p>
<p>An account on replit</p>
<p>A twitter developer account</p>

## Installation
<p>Create a twitter app in your <a href='https://developers.twitter.com/'>twitter developer portal</a>
, remember to keep the keys as it will only be shown on the creation of the app, otherwise have to be regenerated.</p>
<p>Create a discord bot application in your <a href= 'https://discord.com/developers'>discord developer portal</a> with channel permissions and remember the bot token<p>
<p>Download the code and upload it to replit, create a .env file with the following properties</p>

<p><b>The following 4 keys are obtained in your <a href='https://developers.twitter.com/'>twitter developer portal</a></b></p>
<p>ACCESS_KEY</p>
<p>ACCESS_SECRET</p>
<p>CONSUMER_KEY</p>
<p>CONSUMER_SECRET</p>

<p>bot_token, this is the bot token generated on <a href= 'https://discord.com/developers'>discord developer portal</a></p>

## Commands
<p>Default prefix= '-'</p>
<p>follow @{username}, username is the twitter user's unique name, '@' can be ignored</p>
<p>stopfollow @{username}, unfollows a user in your followed list</p>
<p>followlist, displays a list of the users you followed in the text channel</p>

## Custom settings
<p>On the free plan of a twitter developer account, the limit is one request a second. The delay of each request in the code is 2 seconds, change it by going to main.py and manually change the async time to your desired amount.</p>
