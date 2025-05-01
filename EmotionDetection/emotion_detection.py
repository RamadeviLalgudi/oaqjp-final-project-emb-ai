''' This file reads the entered text and detects its emotion'''
import json
import requests  # Import the requests library to handle HTTP requests
def emotion_detector(text_to_analyse):
    ''' Define a function named emotion_detector that takes a string input (text_to_analyse)'''
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
      # Dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
      # Headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
      # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 200, extract the scores from the response
    if response.status_code == 200:
        # Read the emotions score from the formatted response
        all_emotions = formatted_response['emotionPredictions'][0]['emotion']    
        # Assign a score to each emotion
        anger_score = all_emotions['anger']
        disgust_score = all_emotions['disgust']
        fear_score = all_emotions['fear']
        joy_score = all_emotions['joy']
        sadness_score = all_emotions['sadness']
        # Find the emotion with maximum score
        dominant_emotion = max(all_emotions, key = all_emotions.get)        
    # If the response status code is 400, set label and score to None
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None        
        dominant_emotion = None

    # Returning a dictionary containing emotion prediction results
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
        'sadness': sadness_score, 'dominant_emotion': dominant_emotion}