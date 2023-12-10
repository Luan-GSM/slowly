#!/usr/bin/env python3

import discord
from discord import app_commands
from discord.ext import commands

from dynaconf import settings
from typing import Optional


class Letter(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name="letter",
    description="escreve uma carta."
  )

  async def letter(self, ctx: discord.Interaction, autor: Optional[discord.User], titulo: str, conteudo: str) -> None:
    if ctx.channel.id == settings.CHANNEL_ID:
      return await ctx.response.send_message(
        "você não pode usar esse comando aqui.",
        ephemeral=True
      )

    if not autor:
      autor = ctx.user

    self.bot.dispatch(
      "publish_letter", {
        "author": {
          "name": autor.name,
          "avatar": autor.avatar
        },
        "title": titulo,
        "content": conteudo
      }
    )


    await ctx.response.send_message(
      embed = discord.Embed(
        title = "<:correto:1183202781071417405> publicado.",
        description = f"vá para https://discord.com/channels/{settings.SERVER_ID}/{settings.CHANNEL_ID} e veja sua carta.",
        color = discord.Color.from_rgb(7, 13, 25)
      ), ephemeral=True
    )


async def setup(bot):
  await bot.add_cog(Letter(bot))
