const Kahoot = require("kahoot.js-updated");
const settings = require('./settings.json');
const Chance = require('chance');
const chance = new Chance();
const readline = require("readline");
const readlines = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
readlines.question("KahootID: ", (answer) => {
    var splits = answer.split(",");
    const pin = splits[0];
    const bots = [...Array(200).keys()].map((i) => {
        const client = new Kahoot();
        const name = settings.random_name ? chance.name() : settings.bot_name+i;
        client.join(pin, name);
        console.log(`I have logged in as ${name}`);
        client.on("questionStart", (question) => {
            question.answer(Math.floor(Math.random() * 4));
        });
        return client;
    });
});
