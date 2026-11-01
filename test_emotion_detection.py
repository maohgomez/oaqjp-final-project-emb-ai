import json
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        casos = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for texto, esperada in casos.items():
            respuesta = json.loads(emotion_detector(texto))
            emociones = respuesta['emotionPredictions'][0]['emotion']
            dominante = max(emociones, key=emociones.get)
            self.assertEqual(dominante, esperada)


if __name__ == '__main__':
    unittest.main()