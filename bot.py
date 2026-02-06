import os
import discord
from discord.ext import commands

# ===== Discord 權限設定 =====
intents = discord.Intents.default()
intents.message_content = True  # 必須在開發者後台也打開

# ===== 建立 Bot =====
bot = commands.Bot(command_prefix="!", intents=intents)

# ===== Bot 上線事件 =====
@bot.event
async def on_ready():
    print(f"✅ 機器人已上線：{bot.user}")
    print("------")

# ===== 一般指令 =====
@bot.command()
async def fuck(ctx):
    await ctx.send("永不下線掛群機器人 🤖")

@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)

# ===== 關鍵字回覆 =====
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "你好" in message.content:
        await message.channel.send("你好 👋")

    # 讓指令能正常運作（很重要）
    await bot.process_commands(message)

# ===== 關機指令（只有擁有者）=====
@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.send("機器人準備下線 👋")
    await bot.close()

# ===== 錯誤處理 =====
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("❌ 你沒有權限使用這個指令")
    elif isinstance(error, commands.CommandNotFound):
        pass  # 不顯示未知指令錯誤
    else:
        await ctx.send(f"⚠ 發生錯誤：{error}")

# ===== 啟動 Bot =====
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ 找不到 DISCORD_TOKEN，請先設定環境變數")
else:
    bot.run(TOKEN)
