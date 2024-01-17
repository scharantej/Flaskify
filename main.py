 
# Import necessary libraries
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

# Define the route to handle the user's input
@app.route('/result', methods=['POST'])
def result():
    """
    Processes the user's input and generates the results.
    """
    # Get the user's input
    input_text = request.form.get('input_text')

    # Process the user's input and generate the results
    results = process_input(input_text)

    # Render the result page, passing the results as a parameter
    return render_template('result.html', results=results)

# Define the function to process the user's input
def process_input(input_text):
    """
    Processes the user's input and generates the results.

    Args:
        input_text (str): The user's input text.

    Returns:
        results (list): A list of results generated from the user's input.
    """

    # Split the user's input into words
    words = input_text.split()

    # Count the number of words in the user's input
    word_count = len(words)

    # Count the number of unique words in the user's input
    unique_words = set(words)
    unique_word_count = len(unique_words)

    # Generate the results
    results = [
        {'label': 'Word Count', 'value': word_count},
        {'label': 'Unique Word Count', 'value': unique_word_count},
    ]

    return results

# Run the app
if __name__ == '__main__':
    app.run()
