import requests
import time
import hashlib

# Author: Sijin Yu
# 实现了访问 OpenAI 的 API 功能.



def get_s(k, t):
    _s = k + t
    hash_object = hashlib.sha256()
    hash_object.update(_s.encode())
    return hash_object.hexdigest()

def log(info):
    print(info)


def post_GPT(
                messages,  # 对话内容
                model="gpt-3.5-turbo",  # 使用的模型
                max_tokens=2048,  # 最大回复token
                timeout=120,  # 最长等待时间
                retry=3,  # 重试次数
                proxy=None,  # 代理
                temperature=1.0
            ):
    k = "GR0J69bhDtn8g1c5LQXaSYKjxpvMWPykwIsZNUuB7VefFEmzH4dAoOTCq2lVi3"
    t = time.time()
    s = get_s(k, str(t))
    data = {
        'k': k,
        't': t,
        's': s,
        'messages': messages,
        'model': model,
        'max_tokens': max_tokens,
        'temperature': temperature,
    }
    u = "http://103.143.248.145:1314/api/ChatGPT_post/"
    for _ in range(retry):
        try:
            res = requests.post(u, json=data, proxies=proxy, timeout=timeout)
            return True, res.text
        except Exception as e:
            log("[ERROR]" + str(e))
            return False, str(e)

def test():
    print("==========POST========")
    flag, res = post_GPT(messages=[{'role': 'user', 'content': 'What\'s your name?'}], max_tokens=256)
    print(flag)
    print(res)


if __name__ == "__main__":
    print("test: request_ChatGPT")
    test()
