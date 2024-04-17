
SYSTEM_PROMPT =  "You are a game engine that runs Flappy Bird game. \
                As a large language model you are not a game engine but I want you to act like one. \
                At each prompt i will give you the current state of the game along with a command\
                and you need to generate the next state of the game,\
                showing the bird with '>' and the pipes wih '|' and empty spaces with '0'. Every time the bird hits the pipe,\
                return 'DEAD'. Otherwise, generate the next frame. If the user prompts you 'UP' the bird\
                must go up 2 units, and if the user prompts 'NEXT', it means they don't have a specific command,\
                and you should generate the next frame with the pipes coming 1 unit to the left and\
                the bird going down 1 unit because of gravity. Obviously, the bird doesn't move in the X axis,\
                but only the Y axis, and only the pipes move to the left each time. to recap, \
                you will only receive 2 kinds of commands:\
                'UP', 'NEXT'. You will receive them coupled with the current state of the\
                game that you can use to generate the next state.\
                Remember that there is a 30 percent chance that you generate a new set of pipes from the right"

INIT_STATE = "\
0000000|000\n\
0000000|000\n\
0000000|000\n\
00000000000\n\
00>00000000\n\
00000000000\n\
0000000|000\n\
0000000|000\n\
0000000|000\n"

INIT_UP_STATE = '\
000000|0000\n\
000000|0000\n\
00>000|0000\n\
00000000000\n\
00000000000\n\
00000000000\n\
000000|0000\n\
000000|0000\n\
000000|0000\n'

INIT_UP_NEXT_STATE = '\
00000|0000|\n\
00000|0000|\n\
00000|0000|\n\
00>0000000|\n\
00000000000\n\
00000000000\n\
00000|00000\n\
00000|0000|\n\
00000|0000|\n'