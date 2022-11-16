import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)
        self.resetContents = self.contents.copy()

    def reset(self):
        self.contents = self.resetContents.copy()

    def draw(self, nDraw):
        rList = []
        
        if nDraw >= len(self.contents):
            copyContents = self.contents.copy()
            self.contents.clear()
            return copyContents
        for n in range(nDraw):
            randIndex = random.randrange(len(self.contents))
            newBall = self.contents.pop(randIndex)
            rList.append(newBall)
        return rList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    nCorrect = 0
    nTries = 0
    # hatOriginalContents = hat.contents
    # print(num_experiments)
    for _ in range(num_experiments):
        hat.reset()
        nTries += 1
        expectedBalls = []
        flag = True
        for k, v in expected_balls.items():
            for _ in range(v):
                expectedBalls.append(k)
        pulledBalls = hat.draw(num_balls_drawn)
        # print("expected: ",expectedBalls, "     pulled:", pulledBalls)
        for item in expectedBalls:
            if item in pulledBalls:
                pulledBalls.remove(item)
            else: 
                flag = False
        if flag:
            nCorrect += 1
    probability = nCorrect/nTries
    print(probability)
    return probability

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print("Probability:", experiment)
