
const Kahoot = require("kahoot.js-updated");
const sleep = require("system-sleep");
const kahootCode = 9888902;
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

