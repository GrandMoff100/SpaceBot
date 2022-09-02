# SpaceBot

A discord bot that sends a wall of outspace emoji text to a discord channel.

## Example

![Example Screenshot of Discord](./images/example.png)

## Usage

> Pre-requisites: Docker, Python 3, pip, and a discord bot token for a bot in a server of your choice.

Clone the repository and install the requirements:

    git clone https://github.com/GrandMoff100/spacebot.git && cd spacebot

Build the docker image:

    docker build -t spacebot .

Run the docker image:

    docker run -d \
        -e TOKEN=<your discord bot token> \
        -e GUILD_IDS=<comma sepparated guilds for running your commands> \
        spacebot
