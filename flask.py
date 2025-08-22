import logging
from flask import Flask, jsonify, request
from flasgger import Swagger



# Настройка логирования
logging.basicConfig(filename='api.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.before_request
def log_request_info():
    logging.info(f"Request: {request.method} {request.url}")
app = Flask(__name__)
Swagger(app)

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
    """
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
