# Twitter notification on discord
<p>A discord bot that gets the latest tweets and display it in the text channel</p>
<p><b>__How to use the bot__</b></p>
<p>Add the bot to your server, add users to follow by typing '-follow {the tweet account id (start with @)}'</p>
<p>The bot will start getting new tweets from the user and display it in the channel where the command is executed</p>

## Requirements
<p>A discord developer account to create a bot token for the discord bot</p>
<p>An account on replit</p>
<p>A twitter developer account</p>

## Installation
<p>Create a twitter app in your <a href='https://developers.twitter.com/'>twitter developer portal</a>
, remember to keep the keys as it will only be shown on the creation of the app, otherwise have to be regenerated.</p>
<p>Create a discord bot application in your <a href= 'https://discord.com/developers'>discord developer portal</a> with channel permissions and remember the bot token<p>
<p>Download the code and upload it to replit, create a .env file with the following properties</p>

<p><b><u>The following 4 keys are obtained in your</u> <a href='https://developers.twitter.com/'>twitter developer portal</a></b></p>
<ul>
<li>ACCESS_KEY</li>
<li>ACCESS_SECRET</li>
<li>CONSUMER_KEY</li>
<li>CONSUMER_SECRET</li>
<li>bot_token, this is the bot token generated on <a href= 'https://discord.com/developers'>discord developer portal</a></li>
</ul>

## Commands
<p>Default prefix= '-'</p>
<p>follow @{username}, username is the twitter user's unique name, '@' can be ignored</p>
<p>stopfollow @{username}, unfollows a user in your followed list</p>
<p>followlist, displays a list of the users you followed in the text channel</p>

## Custom settings
<p>On the free plan of a twitter developer account, the limit is one request a second. The delay of each request in the code is 2 seconds, change it by going to main.py and manually change the async time to your desired amount.</p>

## How to keep the bot active?
<p>The code will run prefectly on replit but if the session is closed for more than an hour, replit will push the code into a idle state. The bot will enter a sleep mode and can be re-activate by logging back the replit account and open the code.</p>
<p><b><u>To prevent the bot to enter sleep mode</u></b></p>
<p>Constantly ping your bot, I recommend using <a href=https://uptimerobot.com/>UptimeRobot</a></p>
<p><b><u>How to use UptimeRobot</u></b></p>
<p>When running the bot, you will find a box appeared on top of your console/shell showing "running" with a link on top. Copy the link.</p>
<p>Log into your UptimeRobot account and click on "Add New Monitor" and enter the following.</p>
<p>Monitor Type: HTTP(s)</p>
<p>Friendly Name: {Put whatever name your want here}</p>
<p>URL (or IP): {Put the link mentioned above here}</p>
<p>Monitoring Interval: under 15 minutes</p>
<p>Change the rest of the setting to your likings or keep it default</p>
<p>Click "Create Monitor" and you're done, add the bot to your discord server and start using it.</p>
