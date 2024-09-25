from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

groups = []
students = []

@app.route('/api/groups', methods=['GET'])
def get_groups():
    """
    Route to get all groups
    return: Array of group objects
    """
    return jsonify(groups)

@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Route to get all students
    return: Array of student objects
    """
    return jsonify(students)

@app.route('/api/groups', methods=['POST'])
def create_group():
    """
    Route to add a new group
    param groupName: The name of the group (from request body)
    param members: Array of member names (from request body)
    return: The created group object
    """
    
    # Getting the request body (DO NOT MODIFY)
    group_data = request.json
    group_name = group_data.get("groupName")
    group_members = group_data.get("members")
    
    if not group_name:
        abort (400, "Group name required")

    new_group = {
        "id": len(groups) + 1, "groupName": group_name, "members": group_members
    }
    groups.append(new_group)

    return jsonify(new_group), 201

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """
    Route to delete a group by ID
    param group_id: The ID of the group to delete
    return: Empty response with status code 204
    """

    count = 0
    element_to_remove = -1
    for group in groups:
        if group["id"] == group_id:
            element_to_remove = count
        count += 1

    if element_to_remove != -1:
        groups.pop(element_to_remove)

    return '', 204  # Return 204 (do not modify this line)

@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    """
    Route to get a group by ID (for fetching group members)
    param group_id: The ID of the group to retrieve
    return: The group object with member details
    """

    for group in groups:
        if group["id"] == group_id:
            return jsonify(group)
            
    abort (404, "Group not found")

if __name__ == '__main__':
    app.run(port=3902, debug=True)
