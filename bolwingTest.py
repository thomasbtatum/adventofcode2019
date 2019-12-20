import bowling
import unittest

class BowlingGameTest(unittest.TestCase):
    g = bowling.Game()
    def setUp(self):
        self.g = bowling.Game()

    def RollMany(self, num, pins):
        for x in range(1,num+1):
            self.g.Roll(pins)

    def testGutterGame(self):
        self.RollMany(20,0)
        self.assertEqual(0,self.g.score(), "Gutter Test Fail")

    def testAllOnes(self):
        self.RollMany(20,1)
        self.assertEqual(20,self.g.score(), "All1s Test Fail")

    def testOneSpare(self):
        self.g.Roll(5)
        self.g.Roll(5)
        self.g.Roll(3)
        self.RollMany(17,0)
        sc = self.g.score()
        self.assertEqual(16,sc,"test one spare "+str(sc))

if __name__ == '__main__':
    unittest.main()

#b = BowlingGameTest()
#b.testGutterGame("Test")