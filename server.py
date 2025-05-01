''' Executing this function initiates the application of emotion deection to be executed 
    over the Flask channel and deployed on localhost:5000.'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, request, render_template
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app :
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and runs Emotion Predictions over it 
        using emotion_detector()function. The output returned shows the score of each emotion 
        for a given text along with a dominant emotion.'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the score for each emotion and the final dominant score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    # Return the predicted emotion scores and the dominant emotion
    return f'''For the given statement, the system reponse is 'anger': {anger_score},
     'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 
     'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}.'''

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
