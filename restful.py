### **Repository 2: RESTful API with Flask**
```python
# Repository: python-flask-api
# Description: A RESTful API for managing users.

from flask import Flask, jsonify, request

app = Flask(__name__)
users = []

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user.get('id') == user_id:
            user.update(data)
            return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    global users
    users = [user for user in users if user.get('id') != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
