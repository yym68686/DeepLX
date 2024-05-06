import requests
from deeplx import get_available_endpoints_list
from itertools import cycle
from flask import Flask, request, jsonify

app = Flask(__name__)

# 提供的翻译 API URL 列表
urls = get_available_endpoints_list()
print(f"\nDeepLX👌：({len(urls)}) {urls}\n")

# 创建一个循环迭代器
url_cycle = cycle(urls)

@app.after_request
def after_request(response):
    # 设置 CORS 头部
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/translate', methods=['POST'])
def translate():
    # 从迭代器中获取下一个 URL
    url = next(url_cycle)
    print(url)
    # 获取传入的 JSON 数据
    data = request.get_json()
    # 将请求转发到选定的翻译 API
    try:
        response = requests.post(url + "?token=your_access_token", json=data, timeout=5)
        # 如果请求成功，返回响应内容
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Remote server error", "status_code": response.status_code}), 502
    except requests.exceptions.RequestException as e:
        # 如果请求失败，返回错误信息
        return jsonify({"error": str(e)}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1188)