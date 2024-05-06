import time
import requests
import threading

def check_endpoint(url, test_data, available_endpoints):
    try:
        start_time = time.time()
        response = requests.post(url, json=test_data, timeout=5)
        latency = time.time() - start_time
        # 确保服务真正可用
        if response.status_code == 200 and ('data' in response.json() and len(str(response.json().get("data"))) > 0):
            available_endpoints.append((url, latency))
    except requests.exceptions.RequestException:
        pass  # 忽略错误，只关注可用接口

def test_deeplx_threads():
    # DeepLX接口列表
    deepl_urls = ['http://101.132.149.56:1188/translate', 'http://107.175.28.239:1188/translate', 'http://146.56.111.132:8180/translate', 'http://62.210.144.227:1188/translate', 'https://fanyi.yimiao.online/translate', 'https://deeplx.keyrotate.com/translate', 'http://72.18.80.51:1188/translate', 'http://168.138.34.126:1188/translate', 'http://82.157.157.107:1188/translate', 'http://20.89.253.28/translate', 'http://101.43.76.234:1188/translate', 'http://129.153.73.237:1188/translate', 'http://134.122.133.76:1188/translate', 'http://124.222.50.132:1188/translate', 'http://64.112.42.240:1188/translate', 'http://38.148.254.10:1188/translate', 'http://194.87.252.161:1188/translate', 'http://46.8.19.173:1188/translate', 'http://142.171.184.251:1188/translate', 'http://106.14.17.223:1188/translate', 'https://deepx.dumpit.top/translate', 'https://translates.me/v2/translate', 'http://162.55.35.20:1188/translate', 'http://103.152.35.2:1188/translate', 'https://deepl.aimoyu.tech/translate', 'http://152.70.117.91:1188/translate', 'http://172.98.13.238:1188/translate', 'http://49.233.41.73:1188/translate', 'http://165.22.247.82:1188/translate', 'http://148.135.107.108:1188/translate', 'http://116.204.118.161:1188/translate', 'https://deeplx.he-sb.top/translate', 'http://82.157.137.187:1188/translate', 'http://124.223.210.72:1188/translate', 'https://deeplx.ychinfo.com/translate', 'https://dlx.bitjss.com/translate', 'https://deeplx.papercar.top/translate', 'https://deep.jftkj.cyou/translate', 'http://43.154.115.62:1188/translate', 'http://43.152.203.138:1188/translate', 'http://211.227.72.101:1188/translate', 'http://91.199.209.52:1188/translate', 'https://free-deepl.speedcow.top/translate', 'http://142.171.213.4:1188/translate', 'https://deepl.coloo.org/translate', 'http://157.90.115.116:1188/translate', 'http://132.226.14.46:1188/translate', 'http://132.145.80.159:1188/translate', 'http://146.56.97.135:1188/translate', 'http://8.142.134.155:1188/translate', 'https://deeplx.vercel.app/translate', 'https://deeplxpro.vercel.app/translate', 'http://180.164.162.35:1188/translate', 'https://deepl.degbug.top/translate', 'http://45.66.217.9:1188/translate', 'http://37.123.196.26:1188/translate', 'http://77.169.34.84:1188/translate', 'http://107.173.148.148:1188/translate', 'https://deeplx.2077000.xyz:2087/translate', 'http://175.178.237.179:1188/translate', 'http://107.173.153.84:1188/translate', 'http://35.229.248.32:1188/translate', 'http://107.174.67.205:1188/translate', 'http://deeplx.hc-beijing.rhythmlian.cn/translate', 'https://5zxwvvcbqt.us.aircode.run/translate', 'http://168.138.213.1:1188/translate', 'http://hc-beijing.rhythmlian.cn:8085/translate', 'http://119.91.152.74:1188/translate', 'http://157.245.192.219:1188/translate', 'http://209.141.49.210:1188/translate', 'http://146.190.200.191:1188/translate', 'https://translate.dftianyi.com/translatehttp://1.14.71.133:1188/translate', 'http://49.232.164.78:1188/translate', 'http://103.152.34.47:1188/translate', 'http://195.154.184.125:1188/translate', 'http://152.67.208.218:8000/translate', 'http://52.253.96.13:1188/translate', 'http://134.122.133.56:1188/translate', 'https://deepl.tr1ck.cn/translate', 'http://104.234.60.178:1188/translate', 'http://49.235.73.101:1188/translate', 'http://46.148.235.162:1188/translate', 'http://43.133.208.75:1188/translate', 'https://dx-api.nosec.link/translate', 'http://47.243.180.227:1188/translate', 'https://api.deeplx.org/translate', 'http://142.171.172.172:1188/translate', 'http://130.61.194.102:1188/translate', 'https://suanh5.561379.com/translate', 'https://deepl.zhaosaipo.com/translate', 'http://123.60.157.70:8085/translate', 'http://116.203.83.80:1188/translate', 'http://deepl.wuyongx.uk/translate', 'http://152.67.211.94:1188/translate', 'http://1.12.249.244:1188/translate', 'http://149.28.220.149:1188/translate', 'http://168.138.214.221:1188/translate', 'http://82.156.36.11:1188/translate', 'https://deepl.wuyongx.uk/translate', 'http://134.122.133.65:1188/translate', 'https://deeplx.llleman.com/translate', 'http://207.148.127.142:1188/translate', 'http://192.227.178.132:1188/translate', 'http://fenghua.site:1188/translate', 'http://1.12.243.147:1188/translate', 'http://203.25.119.208:1188/translate', 'http://117.50.183.46:1188/translate', 'http://43.138.68.36:8085/translate', 'http://18.142.80.110:1188/translate', 'http://168.235.104.45:1188/translate', 'http://74.48.17.203:1188/translate', 'http://8.218.202.14:1188/translate', 'http://45.145.72.29:1188/translate', 'http://43.153.38.254:1188/translate', 'http://146.56.180.125:1188/translate', 'http://107.191.39.37:1188/translate', 'https://ghhosa.zzaning.com/translate']

    # new_url = ""
    # new_url = new_url.split(",")
    # unique_list = list(set(deepl_urls + new_url))
    # print("新增：", len(unique_list) - len(deepl_urls))
    # print("去重并打印的列表：", unique_list)
    # exit(0)

    test_data = {
        "text": "Hello, world!",
        "source_lang": "EN",
        "target_lang": "ZH"
    }
    available_endpoints = []
    threads = []
    for url in deepl_urls:
        thread = threading.Thread(target=check_endpoint, args=(url, test_data, available_endpoints))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
    return available_endpoints

def get_available_endpoints_list():
    available_endpoints = test_deeplx_threads()
    return [endpoint[0] for endpoint in available_endpoints]

if __name__ == "__main__":

    available_endpoints = test_deeplx_threads()
    available_endpoints.sort(key=lambda x: x[1])

    # 打印界面美化
    print("\nAvailable DeepLX Endpoints with Latencies:")
    print("-" * 60)
    for endpoint, delay in available_endpoints:
        print(f"🚀 ({delay:.2f}s) {endpoint}")
    print("-" * 60)

    # 打印所有可用的接口，按延迟排序，格式为"DeepLX👌：(count)"
    if available_endpoints:
        formatted_endpoints = ", ".join([endpoint[0] for endpoint in available_endpoints])
        print(f"\nDeepLX👌：({len(available_endpoints)}) {formatted_endpoints}\n")
        print([endpoint[0] for endpoint in available_endpoints])
    else:
        print("No available endpoints found.\n")