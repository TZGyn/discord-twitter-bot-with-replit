import asyncio
import os

import discord
from discord.ext import commands, tasks
from replit import db

import manage_list
from get_tweet_v2 import get_tweet_id
from running import running

bot = commands.Bot(command_prefix = "-")

# Note:
# The function name is the command name, change it to your likings

discordcmd_names = ['follow', 'stopfollow', 'followlist', 'mention', 'removemention', 'help']

# Startup message
@bot.event
async def on_ready():
	print("{0.user} is in ".format(bot) + str(len(bot.guilds)) + " server(s)")
	print("{0.user} is online".format(bot))
	get_ID.start()


# Getting and sending new tweets
@tasks.loop(seconds=0)
async def get_ID():

	user_list = db["users"].value

	for user in user_list:
		channel_list = manage_list.get_channel_id(user)
		if len(channel_list) != 0:
			ids, username = get_tweet_id(user)
			if ids != None:
				for channel in channel_list:
					if channel != "":
						try:
							value = db[f"channel_{str(channel)}"].value
							if len(value) != 0:
								role = discord.utils.get(bot.get_guild(value[0]).roles, id = value[1])
								msg = bot.get_channel(int(channel))
								await msg.send(
									f"{role.mention} \n{username} just tweeted: https://twitter.com/{username}/status/{str(ids)}"
								)

						except KeyError:
							msg = bot.get_channel(int(channel))
							await msg.send(
								f"{username} just tweeted: https://twitter.com/{username}/status/{str(ids)}"
							)

			# Change the delay (in seconds) in the bracket
			await asyncio.sleep(2)


# Command in discord to follow a user
@bot.command()
async def follow(ctx, arg = "@"):
	username = arg.strip("@")
	await ctx.send(f"Follow this user? [Y/N]: https://twitter.com/{username}")

	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n"]

	try:
		msg = await bot.wait_for('message', check=check, timeout=30)
		if msg.content.lower() == "y":
			user_list = db["users"].value

			if user_list.__contains__(username) == False:
				value = db["users"].value
				value.append(username)
				db["users"] = value

				manage_list.set_key(username)

			channelID = ctx.message.channel.id
			manage_list.add_channel(channelID, username)
			await ctx.send(f"Start getting new tweets from @{username}")

		elif msg.content.lower() == "n":
			await ctx.send("Following cancelled")
		else:
			await ctx.send("Following cancelled")
	except:
		await ctx.send("Following cancelled")


# Command in discord to unfollow a user
@bot.command()
async def stopfollow(ctx, arg = "@"):
	username = arg.strip("@")
	await ctx.send(
		f"Stop follow this channel? [Y/N]: https://twitter.com/{username}"
	)


	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel and \
		msg.content.lower() in ["y", "n"]

	try:
		msg = await bot.wait_for('message', check=check, timeout=30)
		if msg.content.lower() == "y":
			user_list = db["users"].value

			if user_list.__contains__(username):
				user_list.remove(username)
				db["users"] = user_list

				await ctx.send(f"Stop getting new tweets from @{username}")
			else:
				await ctx.send(f"Already stopped getting new tweets from @{username}")

		elif msg.content.lower() == "n":
			await ctx.send("Cancelled")
		else:
			await ctx.send("Cancelled")
	except:
		await ctx.send("Cancelled")


# Command in discord to display the user followed (each channel is different)
@bot.command()
async def followlist(ctx):
	followlist = manage_list.get_followlist(ctx.message.channel.id)

	print_follow = ""
	for follow in sorted(followlist):
		print_follow += follow
		print_follow += "\n"

	embed = discord.Embed(
		title=f"#{str(ctx.message.channel)}",
		url="",
		description=print_follow,
		color=discord.Color.blue(),
	)


	await ctx.send(embed = embed)

# Command in discord to display all commands
# discord already has a built-in help command
# @bot.command()
# async def help(ctx):
#     help_list = discordcmd_names

#     print_help = ""
#     for cmd in sorted(help_list):
#         print_help += cmd
#         print_help += "\n"

#     embed = discord.Embed(title = "#" + str(ctx.message.channel), url = "", description = print_help, color = discord.Color.blue())

#     await ctx.send(embed = embed)


# Command in discord to include mentioning when displaying new tweets, ex. (-mention @NotificationGroup)
# Note: default roles such as @everyone may not work, create a new role to avoid that
@bot.command()
async def mention(ctx, arg : discord.Role):
	serverID = ctx.guild.id
	roleID = arg.id
	db[f"channel_{str(ctx.message.channel.id)}"] = [serverID, roleID]
	value = db[f"channel_{str(ctx.message.channel.id)}"].value
	role = discord.utils.get(bot.get_guild(value[0]).roles, id = value[1])
	await ctx.send(f"mention updated {role.mention}")


# Command in discord to remove the mentioning
@bot.command()
async def removemention(ctx):
	db[f"channel_{str(ctx.message.channel.id)}"] = []


# Starts the bot
running()
bot.run(os.environ['bot_token'])
