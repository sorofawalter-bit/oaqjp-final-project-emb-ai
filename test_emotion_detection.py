from emotion_detection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase): 
    def test_emotion_detector(self):
        # Test case for Joy
        result_1 = emotion_detector('I am glad this happened') 
        self.assertEqual(result_1['dominant_emotion'], 'joy') 
        
        # Test case for Anger
        result_2 = emotion_detector('I am really mad about this') 
        self.assertEqual(result_2['dominant_emotion'], 'anger') 
        
        # Test case for Sadness
        result_3 = emotion_detector('I am so sad about this') 
        self.assertEqual(result_3['dominant_emotion'], 'sadness')
        
        # Test case for Fear
        result_4 = emotion_detector('I am really afraid that this will happen') 
        self.assertEqual(result_4['dominant_emotion'], 'fear')
        
        # Test case for Disgust
        result_5 = emotion_detector('I am so disgusted by how bad this is') 
        self.assertEqual(result_5['dominant_emotion'], 'disgust')

if __name__ == "__main__":
    unittest.main()