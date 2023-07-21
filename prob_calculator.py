import copy
import random

class Hat:
    # Class hat that can take any number of arguments
    def __init__(self, **kwargs):
        self.contents = []
        
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
        
    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        drawn_balls = random.sample(self.contents, num_balls)
        
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    # Creating a loop to iterate over the number of experiments and the copy of the balls inside the hat
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        success = True

        # Creating a loop to iterate over the expected balls input and if the drawn balls are less than the expected, the loop breaks as the it is unsuccessful. If it is successful, then we add 1 to the 'successful_experiments' variable so that we can calculate the probability in the end
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
            
    probability = successful_experiments / num_experiments
    
    return probability

