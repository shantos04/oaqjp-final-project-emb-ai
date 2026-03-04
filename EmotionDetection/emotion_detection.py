import requests     # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to send a POST request to the Watson Emotion Predict API.
    Args:
        text_to_analyze( str): The input text to be analyzed for emotions.
    Returns:
        str: The raw text response from the API.
    """

    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom header specifying the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=headers)

    # Check if the request status code is 400
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting sentiment anger, disgust, fear, joy, sadness
    emotions = formatted_response["emotionPredictions"][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': emotions['anger'], 
        'disgust': emotions['disgust'], 
        'fear':  emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
        }

    # Return the text attribute of the response object
    return result