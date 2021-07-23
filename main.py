import discord
from discord.ext import commands
from discord.ext import tasks
from get_tweet_v2 import get_tweet_id
import manage_list
import os
import asyncio
from running import running
from replit import db


bot = commands.Bot(command_prefix = "-")


@bot.event
async def on_ready():
    print("{0.user} is in ".format(bot) + str(len(bot.guilds)) + " server(s)")
    print("{0.user} is fking online".format(bot))
    get_ID.start()

@tasks.loop(seconds=0)
async def get_ID():

    user_list = db["users"].value

    for user in user_list:
        channel_list = manage_list.get_channel_id(user)
        if len(channel_list) != 0:
            ids, username = get_tweet_id(user)
            if ids != None:
                # manage_list.clear_notif_hist(username)
                for channel in channel_list:
                    if channel != "":
                      try:
                          value = db["channel_" + str(channel)].value
                          if len(value) != 0:
                            role = discord.utils.get(bot.get_guild(value[0]).roles, id = value[1])
                            msg = bot.get_channel(int(channel))
                            await msg.send("{} \n".format(role.mention) + username + " just tweeted: https://twitter.com/" + username + "/status/" + str(ids))
                      except KeyError:
                          msg = bot.get_channel(int(channel))
                          await msg.send(username + " just tweeted: https://twitter.com/" + username + "/status/" + str(ids))
            await asyncio.sleep(2)
                    
@bot.command()
async def follow(ctx, arg = "@"):
    username = arg.strip("@")
    await ctx.send("Follow this channel? [Y/N]: https://twitter.com/" + username)
    
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
            await ctx.send("Start getting new tweets from @" + username)

        elif msg.content.lower() == "n":
            await ctx.send("Following cancelled")
        else:
            await ctx.send("Following cancelled")
    except:
        await ctx.send("Following cancelled")

@bot.command()
async def stopfollow(ctx, arg = "@"):
    username = arg.strip("@")
    await ctx.send("Stop follow this channel? [Y/N]: https://twitter.com/" + username)

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

                await ctx.send("Stop getting new tweets from @" + username)
            else:
                await ctx.send("Already stopped getting new tweets from @" + username)

        elif msg.content.lower() == "n":
            await ctx.send("Cancelled")
        else:
            await ctx.send("Cancelled")
    except:
        await ctx.send("Cancelled")

@bot.command()
async def followlist(ctx):
    followlist = manage_list.get_followlist(ctx.message.channel.id)
    
    print_follow = ""
    for follow in sorted(followlist):
        print_follow += follow
        print_follow += "\n"

    embed = discord.Embed(title = "#" + str(ctx.message.channel), url = "", description = print_follow, color = discord.Color.blue())

    await ctx.send(embed = embed)

@bot.command()
async def mention(ctx, arg : discord.Role):
    serverID = ctx.guild.id
    roleID = arg.id
    db["channel_" + str(ctx.message.channel.id)] = [serverID, roleID]
    value = db["channel_" + str(ctx.message.channel.id)].value
    role = discord.utils.get(bot.get_guild(value[0]).roles, id = value[1])
    await ctx.send("mention updated {}".format(role.mention)) 

@bot.command()
async def removemention(ctx):
    db["channel_" + str(ctx.message.channel.id)] = []

running()
bot.run(os.environ['bot_token'])
