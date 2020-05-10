# CoronaStat
This is a whatsapp bot, that replies on basis of user input.

#1. Install required Python Packages:

flask

  pip install flask
twilio

  pip install twilio
  
#######################################################

2. Create a Flask App (app.py)


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import DataParse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    data = DataParse.resp(msg)
    # Create reply
    resp = MessagingResponse()
    #resp.message("You said: {}".format(msg))
    resp.message(data)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
###############################################    
3. Run the flask app
python app.py

###############################################
4. For local testing: Generate Public URL for Webhook using ngrok.io

ngrok is a free tool that allows us to tunnel from a public URL to our application running locally.

Download ngrok.

Unzip it.

Run ngrok from command line (from the location where executable is stored)

  ./ngrok http 5000
Copy the HTTPS Forwarding URL

Paste it as the webhook URL for incoming messages in your sandbox configuration.

################################################
