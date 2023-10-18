from flask import Flask, request, jsonify
from core import load_config, framework_logger, handle_exception
import os
from agent.master import MasterAgent
from responder.llm_response import Responder
# Initialize Flask app
app = Flask(__name__)

# Load configurations
try:
    config = load_config("app_config")  # Assuming you have an app_config.py in your config directory
    app.config.from_object(config)
    framework_logger.info("Configurations loaded successfully.")
except Exception as e:
    framework_logger.error(f"Error loading configurations: {str(e)}")
    raise

# Global error handler for the Flask app
@app.errorhandler(Exception)
def global_error_handler(error):
    framework_logger.error(f"Unhandled exception: {str(error)}")
    return jsonify({"status": "Error", "message": "An unexpected error occurred!"}), 500

# Example route to check the health of the application
@app.route('/health', methods=['GET'])
def health_check():
    framework_logger.info("Health check endpoint hit.")
    return jsonify({"status": "OK", "message": "Application is running!"}), 200


@app.route('/generate', methods=['POST'])
def generate():
    """
    Route to process client requests using the master agent.
    """
    try:
        # Get data from the client request
        data = request.json

        # Validate the request data (you can add specific validations based on your requirements)
        if not data:
            return jsonify({"status": "Error", "message": "No data provided!"}), 400

        # Initialize the master agent and process the request
        master_agent = MasterAgent()
        response = master_agent.process(data)
        responder = Responder()
        final_response = responder.generate(response)

        # Return the final response
        return jsonify({"status": "OK", "message": "Processed successfully!", "data": final_response}), 200
    except Exception as e:
        framework_logger.error(f"Error processing the request: {str(e)}")
        return jsonify({"status": "Error", "message": "An error occurred while processing the request!"}), 500

# Other routes can be added here, potentially for initiating agents, handling requests, etc.

if __name__ == "__main__":
    try:
        port = app.config["PORT"]
        app.run(host='0.0.0.0', port=port, debug=app.config["DEBUG"])
        framework_logger.info(f"App started on port {port}.")
    except Exception as e:
        framework_logger.error(f"Error starting the app: {str(e)}")
        raise