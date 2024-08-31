"""
Emotion Detector Flask Application
This application detects emotions from a text input using an external emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Handle the emotion detection request.
    Returns a message with the detected emotions and the dominant emotion.
    It returns an error if it is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)

    if not text_to_analyze:
        return "Invalid input! Text to analyze cannot be empty. Please try again."
    
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return f"For the given statement, the system response is " \
           f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
           f"'joy': {joy}, and 'sadness': {sadness}.\n" \
           f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Render the index page for the Emotion Detector application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
