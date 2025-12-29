# Astral Discord Bot

## Overview
A Discord bot that matches users in private threads for anonymous conversations. Users can join a queue with `/match` and get paired up randomly to chat in their own private portal. Includes a Flask keep-alive server to ensure the bot stays online.

## Features
- `/match` - Join the matching queue or pair with a waiting user
- `/leave` - Close the current match thread
- Keep-alive server on port 8080

## Technical Stack
- Python 3.11
- discord.py library
- Flask (for keep-alive server)

## Project Files
- `main.py` - Main bot file with all commands, bot logic, and Flask server
- `bot.py` - (Legacy) Contains the same code as main.py

## Setup
1. Add your Discord bot token as `DISCORD_TOKEN` in the Replit Secrets (padlock icon)
2. The bot will sync slash commands and go online automatically

## How It Works
- When a user runs `/match`, they're added to the waiting queue
- When a second user runs `/match`, both are paired and a private thread is created
- Both users can chat in the private thread
- Either user can run `/leave` to close the match thread
