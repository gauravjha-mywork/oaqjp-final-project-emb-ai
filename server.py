from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def controller_emotion_detector():
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    if response["dominant_emotion"] is None:
        return {"message":"Invalid text! Please try again!"}

    return response

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)