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
    data = request.get_json()
    for _ in range(len(urls)):  # 尝试每个URL一次
        url = next(url_cycle)
        print(url)
        try:
            response = requests.post(url + "?token=your_access_token", json=data, timeout=5)
            print(response.json())
            if response.status_code == 200 and len(response.json()["data"]) > 0:
                return jsonify(response.json()), 200
            else:
                print(f"请求 {url} 失败：{str(e)}")
                continue  # 如果不是200，尝试下一个URL
        except requests.exceptions.RequestException as e:
            print(f"请求 {url} 失败：{str(e)}")
            continue  # 发生异常，尝试下一个URL

    return jsonify({"error": "所有翻译服务不可用"}), 503  # 所有URL尝试后仍然失败

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1188)