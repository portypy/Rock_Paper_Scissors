import random
import pdb


def str_generator():
        random_in = random.randint(1,3)
        if random_in == 1:
            random_out = "rock"
        elif random_in == 2:
            random_out = "scissors"
        else:
            random_out = "paper"

        return random_out
