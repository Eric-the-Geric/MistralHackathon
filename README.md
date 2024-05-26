# MistralHackathon
Using mistral model to play monopoly


## Inspiration
We wanted to do something fun using an agentic workflow.

## What it does
Playing monopoly using mistral api. We use agents for the interface and to play the actual game. There are agents that follow different stragies, like short-term, long-term or the Trump real-estate mogul strategy.

## How it works
We use 4 agents in an agentic workflow. (all using the mistral large model api)
1. An agent to create a general strategy to play monopoly
2. An agent to retrieve possible actions given the game state (in the form of html)
3. An agent to generate an an action (which maps to a prompt)
4. An agent that generates javascript code to make an action given HTML and an action to take

## How we built it
We built it in python using Selenium for interface interaction and mistral API (mistral-large)

### Challenges we ran into
Communicating with the interface. Having a global strategy. outputing a single action took some time as well.

## Accomplishments that we're proud of
It works !

## What's next for Mono-llm-poly
- Add more features like trading property.
- Make multiple agents competing against each other.
- Using reinforcement learning. 
- Making it generic for any javascript application.
- Add the ability to trade and take 'management' actions



## Video description On the right side, we can see the monopoly.js interface playing in a Selenium Firefox instance.On the the left side, we can see some logs.
- Decide action to make
- Possible actions : It is retrieve from the html
- Action decided by the playing agent
- Javascript code to exectute the selected action
