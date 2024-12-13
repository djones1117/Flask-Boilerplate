from flask import Flask, render_template, jsonify, request




app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
	data = 'Hello, this is data that has been inserted from the Flask backend!!!!'
	return render_template("index.html",info = data)



@app.route('/render_form', methods=['GET', 'POST'])
def render_form():
	return render_template("form.html")

# Route to handle form submission via AJAX POST request
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
	# Retrieve JSON data sent in the request body.  parses the incoming JSON payload from the request body. The parsed data is stored in the variable data as a Python dictionary.
	data = request.get_json()
	# Print the received data to the server console for debugging
	print("I just recieved " + str(data))
	# Extract the 'message' field from the JSON data. Accesses the value associated with the key "message" in the JSON data.
	message = data["message"]
	# Prepare a response dictionary
	send_back = {}
	# Create a response message by appending a string to the received message. Adds a key "response" with a value that appends " was received" to the original message. This creates a response message acknowledging receipt of the user's message. 	 	 
	send_back["response"] = message + " was recieved"
	# Return the response as a JSON object with HTTP status code 200 (OK) Uses jsonify to convert the send_back dictionary to a JSON response. Returns this JSON response with an HTTP status code 200, indicating success.
	return jsonify(send_back), 200




if __name__ == '__main__':
	app.run(debug=True,  host='0.0.0.0', port = 5002)







