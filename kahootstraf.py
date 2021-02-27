# -*- coding: utf-8 -*-
import colorama
import sys
import requests
import os
import webbrowser
import pyperclip

os.system('clear')
os.system('sudo apt install npm')
os.system('sudo apt install node')
os.system('npm install kahoot.js-updated')
os.system('npm install system-sleep')

print("""

  \033[31m╦╔═╔═╗╦ ╦╔═╗╔═╗╔╦╗  \033[34m┬┌─┐  \033[31m╔═╗╔═╗╦ ╦╔═╗╔═╗╦   \033[34m┌─┐┌┬┐┬─┐┌─┐┌─┐
  \033[31m╠╩╗╠═╣╠═╣║ ║║ ║ ║   \033[34m│└─┐  \033[31m╚═╗║  ╠═╣║ ║║ ║║   \033[34m└─┐ │ ├┬┘├─┤├┤ 
  \033[31m╩ ╩╩ ╩╩ ╩╚═╝╚═╝ ╩   \033[34m┴└─┘  \033[31m╚═╝╚═╝╩ ╩╚═╝╚═╝╩═╝ \033[34m└─┘ ┴ ┴└─┴ ┴└  

    \033[34m╔═════════════════════════════════════════════════════╗\033[34m
    \033[34m║\033[34m \033[31mRemastered & Power Set by [DEV] z3ntl3 root (EFDAL)\033[31m \033[34m║\033[34m
    \033[34m╚═════════════════════════════════════════════════════╝\033[34m

""")

kahootCODE = input("\033[1m\033[36m\033[34m╔═\033[34m\033[31m[\033[31m\033[33m~\033[33m\033[31m]\033[31m\033[36mr00t\033[36m\033[33m@\033[33m\033[35mEfdal\033[35m\033[33m[\033[33m\033[36m\033[36m\033[36mGeef > Kahoot > Code\033[33m]\033[33m\033[32m$\033[32m\033[36m\033[1m\033[0m\n\033[1m\033[34m╚═══════►\033[34m\033[1m\033[0m")


botnanoCODE = """
const Kahoot = require("kahoot.js-updated");
const sleep = require("system-sleep");
"""

botnanoCODE3 =f"""const kahootCode = {kahootCODE};"""

botnanoCODE2 ="""
const kahootBotPrefix = 'kbot';
const kahootBotNumberSeperator = ' #';
const numberOfBots = 51;



for (var i = 0; i < numberOfBots; i++) {
    console.log('joining bot ' + i + '/' + numberOfBots);
    let client = new Kahoot;
    client.setMaxListeners(Number.POSITIVE_INFINITY);
    client.join(kahootCode, kahootBotPrefix + kahootBotNumberSeperator + i);
    client.on("QuestionStart", question => {
        console.log('choosing the first answer..');
        question.answer(0);
        console.log('---------------------------');
    });
    console.log('joined bot ' + i + '/' + numberOfBots);
    sleep(250);
}
"""
print("""
\033[31m--\033[31m\033[34m>\033[34m \033[34mBestand wordt geopent. Wanneer het geopent is, klik a.u.b op CTRL + S + Enter | Vervolgens CTRL + X

""")
doorgaan = input("\033[31m--\033[34m>\033[34m \033[31mKlik ENTER om door te gaan")



filename = input("\033[31m--\033[34m>\033[31m Kies uw bestand naam (bijv: hallo.js!\n\033[35m[>] LET OP : .js erachter is verplicht: ")

akkoort = input("\033[0m\nLET OP:\n\nNa alle stappen sluit programma. Typ wanneer het sluit: node "+filename)

os.system('node spam.js')

