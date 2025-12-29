# Astral Discord Bot

## Overview
A Discord bot that matches users in private threads for anonymous conversations. Users can join a queue with `/match` and get paired up randomly to chat in their own private portal.

## Features
- `/match` - Join the matching queue or pair with a waiting user
- `/leave` - Close the current match thread

## Technical Stack
- Python 3.11
- discord.py library

## Setup
1. Add your Discord bot token as `DISCORD_TOKEN` in the Replit Secrets (padlock icon)
2. The bot will sync slash commands and go online automatically

## Project Structure
- `bot.py` - Main bot file with all commands and logic
