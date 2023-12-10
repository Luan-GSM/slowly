#!/usr/bin/env python3

import discord, aiohttp
from discord.ext import commands

from dynaconf import settings


class PublishLetter(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @commands.Cog.listener()
  async def on_publish_letter(self, dataObj):
    await self.bot.wait_until_ready()

    embed = discord.Embed(
      title=dataObj.get("title"),
      description=dataObj.get("content"),
      color=discord.Color(14423100)
    )

    embed.set_author(
      name=dataObj["author"]["name"],
      icon_url=dataObj["author"]["avatar"]
    )

    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(settings.WEBHOOK, session=session)
      await webhook.send(embeds=[embed])


async def setup(bot):
  await bot.add_cog(PublishLetter(bot))
