''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the emotion_detector function from the package created: TODO
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Function to receive text and return emotion analysis
    """
	# Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

	# Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    return response

	# Extract the label and score from the response
#    label = response['label']
 #   score = response['score']

		# Check if the label is None, indicating an error or invalid input
 #   if label is None:
        return "Invalid input! Try again."
 #   else:
        # Return a formatted string with the sentiment label and score
 #   return f"The given text has been identified as {label} with a score of {score}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
