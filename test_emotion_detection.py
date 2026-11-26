import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        res1= emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(res1,"joy")
        
        res2= emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(res2,"anger")

        res3= emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(res3,"disgust")

        res4= emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(res4,"sadness")

        res5= emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(res5,"fear")


unittest.main()
