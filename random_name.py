from tqdm.notebook import tqdm
import time
from IPython.display import display, clear_output
from random import shuffle

def draw_name(textfile, total_seconds):

    with open(textfile, encoding="utf-8") as f:
        lines = f.read().splitlines()

    rand_index = [i for i in range(len(lines))]
    shuffle(rand_index)

    for rand_id in rand_index:
    
        name = lines[rand_id]
   
        print("The next person to introduce herself/himself is: --> " + name + " <--")
    
        input('Press any key to start the countdown!\n')
    
        for sec in tqdm(range(total_seconds)):
        
            time.sleep(1)

        input('Draw the next person!\n')
    
        clear_output()

    print("That's it! We've heard everyone and can now continue with the course :-)")