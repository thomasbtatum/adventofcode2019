class Game:
    rolls = [0]*21
    currentRoll = 0

    def Roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll+=1


    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(0, 10):
            if(self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10):
                score += 10 + score[frameIndex+2]
            else:
                score += self.rolls[frameIndex] + self.rolls[frameIndex+1]
            frameIndex += 2
        return score