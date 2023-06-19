from request_ChatGPT import post_GPT
import json

def short_eval(lvl, timeout=15):
    system_prompt = f"""你是一个毛笔书法老师. 用户将一个毛笔书写报告作为输入, 你输出对它的改写. 要求:
    # 1. 保持原意大致不变.
    # 2. 语言要恰当, 你的说话对象是一个正在学习书法的学生.
    # 3. 你的输出在 100 字左右.
    # 4. 对于同样的输入, 你的两次输出应当是不同的.
    """

    exp_input = f"""这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    exp_output= f"""这个字书写规范整齐，笔画技法熟练娴熟，线条质感生动传神，墨迹书写稳定且表现力强，书写节奏和韵律相对流畅自如，个人风格和创新初步显露。"""
    message = list()
    message.append({"role": "system", "content": system_prompt})
    message.append({"role": "user", "content": exp_input})
    message.append({"role": "assistant", "content": exp_output})
    if lvl == "优秀":
        txt = """这个字结构与形态讲究，笔画技法细腻，线条质感自然，墨迹稳定，书写节奏与韵律流畅，个人风格与创新得以充分展现。"""
    elif lvl == "良好":
        txt = """这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    elif lvl == "合格":
        txt = """这个字总体规范，但仍需进一步加强结构与形态、笔画技法、线条质感、墨迹稳定及书写节奏与韵律的掌握和表现，个人风格与创新有待进一步挖掘与发挥。"""
    elif lvl == "差":
        txt = """这个字存在结构与形态、笔画技法、线条质感、墨迹稳定及书写节奏与韵律等多方面的问题，个人风格与创新不足，需要下功夫反复实践、练习。"""
    else:
        return None
    message.append({"role": "user", "content": txt})
    try:
        res_dic = json.loads(post_GPT(message, timeout=timeout)[1])
        res = res_dic["res"]["choices"][0]["message"]["content"]
    except Exception as e:
        res = txt
    return res


if __name__ == '__main__':
    print("test: prompy.py")
    print("author: Sijin Yu")
    print("优秀: " + short_eval("优秀"))
    print("良好: " + short_eval("良好"))
    print("合格: " + short_eval("合格"))
    print("差: " + short_eval("差"))