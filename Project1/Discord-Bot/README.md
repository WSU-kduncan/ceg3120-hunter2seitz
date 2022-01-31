# Hunter Seitz 
## Part 3- R&D

### Setup
- How to get an API token? 
    - To get an API token, most of the websites, apps, and more will have the developer section to generate an API token. For example in Discord, we can go into their Developer Portal and create a bot. Next, click on the bot pane and the token is as provided in hidden. Copy the token for appropriate place. If there's a problem, you can regenerate the token. 
- Where to put it to work with the code? 
    - First, we can create a .env file and put the token in: 'DISCORD_TOKEN' handler. 
- Dependencies (what packages need to be installed to run the code?)
    - Some of the dependencies required are pip3 and pythondotenv.
### Usage
- Describe
        - I made a simple change in the discord.py code where I put couple quotes from another TV show.
- Commands
   - One command is '!xavier' can be typed on my Discord server.
   - What response provided by from the bot? 
        - The bot will randomize a quote from the list of qoutes as provided.
            - For example, "What doth life" will be entered by the bot.  
### Research
- The problem is that the bot turns off when the AWS service shuts down rendering unusuable. The only solution is the bot is Python-based and rather have the server which the bot is hosted on stays on perpetually. 
