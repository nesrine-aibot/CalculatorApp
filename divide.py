from flask import Flask, jsonify

@app.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify({'status': 400, 'result': 'Division by zero error'}), 400
    result = numberA / numberB
    return jsonify({'status': 200, 'result': result})