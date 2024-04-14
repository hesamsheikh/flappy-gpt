import time
import langchain
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    PromptTemplate
)
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from game_state_examples import *

load_dotenv(dotenv_path=".env")
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)

command = 'NEXT'

examples = [
    {"input": "COMMAND: UP \n, current state of the game: \n {INIT_STATE}", "output": {INIT_UP_STATE}},
    {"input": "COMMAND: NEXT \n, current state of the game: \n {INIT_UP_STATE}}", "output": {INIT_UP_NEXT_STATE}},
]
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a game engine that runs Flappy Bird game. \
        As a large language model you are not a game engine but I want you to act like one. \
        At each prompt i will give you the current state of the game along with a command\
        and you need to generate the next state of the game,\
        showing the bird with '>' and the pipes wih '|' and empty spaces with '0'. Every time the bird hits the pipe,\
        return 'DEAD'. Otherwise, generate the next frame. If the user prompts you 'UP' the bird\
        must go up 2 units, and if the user prompts 'NEXT', it means they don't have a specific command,\
        and you should generate the next frame with the pipes coming 1 unit to the left and\
        the bird going down 1 unit because of gravity. Obviously, the bird doesn't move in the X axis, but only the Y axis,\
        and only the pipes move to the left each time. to recap, you will only receive 2 kinds of commands:\
        'UP', 'NEXT'. You will receive them coupled with the current state of the\
        game that you can use to generate the next state."),
        few_shot_prompt,
        ("human", "COMMAND: {command} \n, current state of the game: \n {cur_state}")
    ]
)


prompt_and_model = prompt | llm
output = ''

def next_move(cur_state, user_command):
    output = prompt_and_model.invoke({"command": user_command , "cur_state":cur_state})
    cur_state = output.content[5:-5].strip()
    if output.content == 'DEAD':
        return 'DEAD'

    for row in cur_state.split("            "):
        print(row)
    print()

    return cur_state

if __name__ == "__main__":
    output = prompt_and_model.invoke({"command": 'what is my name', "cur_state": ""})
    ...
...