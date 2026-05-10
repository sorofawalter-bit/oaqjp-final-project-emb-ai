import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes text for emotions and returns a formatted dictionary 
    including the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

    # 1. Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # 2. Extract the required set of emotions and their scores
    # The API returns a list of predictions; we want the first one
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 3. Code logic to find the dominant emotion
    # We find the key with the maximum value in the emotions dictionary
    dominant_emotion = max(emotions, key=emotions.get)
    
    # 4. Return the specific output format required
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }