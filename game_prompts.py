
SYSTEM_PROMPT = "You should help simulate the game of Flappy Bird, where there is bird and it should \
                avoid the pipes or the bird would die. \
                At each prompt i will give you the current state of the game along with a command\
                and you need to generate the next state of the game,\
                showing the bird with '>' and the pipes wih '|' and empty spaces with '0'.\
                Only if the bird hits a pipe ('>' and '|' collide),\
                return 'DEAD'. Otherwise, generate the next frame. If the user prompts you 'UP' the bird\
                must go up 2 units, and if the user prompts 'NEXT', it means they don't have a specific command,\
                and you should generate the next frame with\
                the bird going down 1 unit because of gravity. The bird doesn't left or right,\
                but only up and down. Only the pipes move to the left each time. to recap, \
                you will only receive 2 kinds of commands:\
                'UP', 'NEXT'. You will receive them coupled with the current state of the\
                game that you can use to generate the next state.\
                Sometimes you also generate a new set of pipes coming from the rightmost part."

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

SAMPLE_STATE_1 = '\
000|0000|00\n\
000|0000|00\n\
000|0000|00\n\
00>00000|00\n\
00000000000\n\
00000000000\n\
000|0000000\n\
000|0000|00\n\
000|0000|00\n'
SAMPLE_STATE_1_OUTPUT_UP = 'DEAD'

SAMPLE_STATE_2 = '\
00000000|00\n\
00000000|00\n\
00000000|00\n\
00>00000|00\n\
00000000000\n\
00000000000\n\
00000000000\n\
00000000|00\n\
00000000|00\n'
SAMPLE_STATE_2_OUTPUT_NEXT = '\
0000000|00|\n\
0000000|00|\n\
0000000|00|\n\
0000000|000\n\
00>00000000\n\
00000000000\n\
0000000000|\n\
0000000|00|\n\
0000000|00|\n'