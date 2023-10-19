from flask import Flask, request, jsonify
from core import BafLog,MasterAgent,Responder
from config import Config



# Initialize Flask app
app = Flask(__name__)

# Load configurations
try:
    app.config.from_object(Config)
    BafLog.info("Configurations loaded successfully.")
except Exception as e:
    BafLog.error(f"Error loading configurations: {str(e)}")
    raise


# Example route to check the health of the application
@app.route('/health', methods=['GET'])
def health_check():
    BafLog.info("Health check endpoint hit.")
    return jsonify({"status": "OK", "message": "Application is running!"}), 200




@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get data from the client request
        data = request.json
        # Validate the request data (you can add specific validations based on your requirements)
        if not data:
            return jsonify({"status": "Error", "message": "No data provided!"}), 400

        master_agent = MasterAgent()
        response = master_agent.process(data)
        responder = Responder()
        final_response = responder.generate(response, data['message'])

        # Return the final response
        return jsonify({"status": "OK", "message": "Processed successfully!", "data": final_response}), 200
    except Exception as e:
        BafLog.error(f"Error processing the request: {str(e)}")
        return jsonify({"status": "Error", "message": "An error occurred while processing the request!"}), 500





if __name__ == "__main__":
    try:
        port = app.config["PORT"]
        app.run(host='0.0.0.0', port=port, debug=app.config["DEBUG"])
        BafLog.info(f"App started on port {port}.")
    except Exception as e:
        BafLog.error(f"Error starting the app: {str(e)}")
        raise
