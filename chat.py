from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from prompts import *
import langchain
langchain.verbose = True
langchain.debug = True

load_dotenv(dotenv_path=".env")
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.5)

command = 'NEXT'

examples = [
    {"input": f"COMMAND: UP \n, current state of the game: \n {INIT_STATE}", "output": {INIT_UP_STATE}},
    {"input": f"COMMAND: NEXT \n, current state of the game: \n {INIT_UP_STATE}", "output": {INIT_UP_NEXT_STATE}},
    {"input": f"COMMAND: UP \n , current state of the game: \n {SAMPLE_STATE_1}", "output": {SAMPLE_STATE_1_OUTPUT_UP}},
    {"input": f"COMMAND: UP \n , current state of the game: \n {SAMPLE_STATE_2}", "output": {SAMPLE_STATE_2}}
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
        ("system", SYSTEM_PROMPT),
        few_shot_prompt,
        ("human", "COMMAND: {command} \n, current state of the game: \n {cur_state}")
    ]
)


prompt_and_model = prompt | llm

output = ''
def next_move(cur_state, user_command):
    output = prompt_and_model.invoke({
        "command": user_command,
        "cur_state":cur_state})
    
    cur_state = output.content.strip()
    if output.content == 'DEAD':
        return 'DEAD'

    return cur_state