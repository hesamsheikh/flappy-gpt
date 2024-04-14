import time
import langchain
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    PromptTemplate
)
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.document_loaders import json_loader
# from langchain.prompts import load_prompt


load_dotenv(dotenv_path=".env")
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)

cur_state = "\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
            000>00000000000000000000000\n\
            000000000000000000000000000\n\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
            00000000000000000000000|000\n\
"
command = 'NEXT'

human_prompt_template = PromptTemplate(
    template="COMMAND: {command} \n, current state of the game: \n {cur_state}",
    input_variables=["command", "cur_state"],
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
        'UP', 'NEXT'. You will recieve them coupled with the current state of the game that you can use to \
        generate the next state.")
        ,
        ("human", "COMMAND: {command} \n, current state of the game: \n {cur_state}")
    ]
)


prompt_and_model = prompt | llm
output = ''
steps = 0

while(True):
    output = prompt_and_model.invoke({"command": command , "cur_state":cur_state})
    cur_state = output.content[5:-5].strip()
    steps += 1
    for row in cur_state.split("            "):
        print(row)
    print()
    if output.content == 'DEAD':
        break
    time.sleep(1)

...