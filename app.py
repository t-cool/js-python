from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    action = data.get('action')
    timestamp = data.get('timestamp')

    # ここで通信内容を分析する
    result = analyze_data(action, timestamp)

    return jsonify(result)

def analyze_data(action, timestamp):
    # 通信内容に基づいて結果を返す
    if action == "button_click":
        return {"message": "ボタンがクリックされました", "timestamp": timestamp}
    else:
        return {"message": "未知のアクション", "timestamp": timestamp}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

