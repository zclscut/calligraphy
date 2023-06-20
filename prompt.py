from request_ChatGPT import post_GPT
import json

def short_eval(lvl, timeout=15):
    system_prompt = f"""你是一个毛笔书法老师. 用户将一个毛笔书写报告作为输入, 你输出对它的改写. 要求:
    # 1. 保持原意大致不变.
    # 2. 语言要恰当, 你的说话对象是一个正在学习书法的学生.
    # 3. 你的输出在 50 字左右, 严格控制在 80 字以内.
    """

    exp_input = f"""这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    exp_output= f"""这个字书写规范整齐，笔画技法熟练娴熟，线条质感生动传神，墨迹书写稳定且表现力强，书写节奏和韵律相对流畅自如，个人风格和创新初步显露。"""
    message = list()
    message.append({"role": "system", "content": system_prompt})
    message.append({"role": "user", "content": exp_input})
    message.append({"role": "assistant", "content": exp_output})
    if lvl == 5:
        txt = """这个字的起笔收笔行笔都非常完美，粗细得当，并且结构布局非常完美，它形成了自己独特的书法风格。"""
    elif lvl == 4:
        txt = """字体整体很好, 起笔收笔成熟, 笔画没有瑕疵。但是笔画方向不太一致，需要注重提升笔画粗细、厚度的掌控。"""
    elif lvl == 3:
        txt = """字体整体的起笔收笔成熟, 稍微有一些笔画的瑕疵, 正确笔画在80%以上，但笔画方向不太一致，稍有缺陷."""
    elif lvl == 2:
        txt = """这个字留下了一些漏洞，需要加强起笔收笔之间的控制，避免虚笔、渗墨的情况发生，需加强对笔画方向的定性和落笔的规律性。"""
    elif lvl == 1:
        txt = """这个字没有明显的起笔收笔，存在起笔收笔极多错误的情况，控制和运用毛笔能力不足，虚笔、渗墨的情况较为常见。"""
    else:
        return None
    message.append({"role": "user", "content": txt})
    try:
        res_dic = json.loads(post_GPT(message, timeout=timeout, temperature=1.2)[1])
        res = res_dic["res"]["choices"][0]["message"]["content"]
    except Exception as e:
        res = txt
    return res




def long_eval_ziti(lvl, timeout=50):
    system_prompt = f"""你是一个毛笔书法老师. 用户将一个毛笔书写报告作为输入, 你输出对它的改写. 要求:
    # 1. 保持原意大致不变.
    # 2. 语言要恰当, 你的说话对象是一个正在学习书法的学生.
    # 3. 你的输出要尽量详细.
    """

    exp_input = f"""这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    exp_output= f"""这个字书写规范整齐，笔画技法熟练娴熟，线条质感生动传神，墨迹书写稳定且表现力强，书写节奏和韵律相对流畅自如，个人风格和创新初步显露。"""
    message = list()
    message.append({"role": "system", "content": system_prompt})
    message.append({"role": "user", "content": exp_input})
    message.append({"role": "assistant", "content": exp_output})
    if lvl == 5:
        txt = """这个字的起笔收笔行笔都非常完美，粗细得当，并且结构布局非常完美，它形成了自己独特的书法风格。你需要继续保持，继续探寻更深层次的书法技艺，多学习一些艺术方面的知识，逐步提高自己的境界，求精于每一笔，更入微处。"""
    elif lvl == 4:
        txt = """字体整体很好，起笔收笔成熟，或者笔画没有瑕疵，正确笔画100%。但是笔画方向不太一致，需要更加注重横向笔画的平行和垂直于水平线方向的纵向笔画，这样可以让整个字体的结构布局更加均匀美观一些。同时还需要注重提升笔画粗细、厚度的掌控，追求自己独特的书法风格。"""
    elif lvl == 3:
        txt = """字体整体的起笔收笔成熟, 或者稍微有一些笔画的瑕疵，正确笔画在80%以上，但笔画方向不太一致，稍有缺陷，需要更加注重笔画方向的一致性和整体结构布局的均匀美观。 需要多练习自己的笔画基础技能，并通过练习不断提高自己对墨和纸的掌控能力，多去尝试不同的书法作品，进一步提升自己的艺术修养和审美水平。"""
    elif lvl == 2:
        txt = """这个字莫名其妙留下了一些漏洞，需要加强起笔收笔之间的控制，避免虚笔、渗墨的情况发生，需继续练习笔画粗细、字体大小的均匀控制，加强对笔画方向的定性和落笔的规律性。需要再次研读书法基本功相关知识，不要着急，慢慢调整、练习，等到你掌控毛笔，便是写好书法的基础。"""
    elif lvl == 1:
        txt = """这个字的起笔收笔基础存在一些问题，没有明显的起笔收笔，或存在起笔收笔极多错误的情况，控制和运用毛笔能力不足，例如虚笔、渗墨的情况较为常见，乃至笔画粗细、字体大小难以掌控，急需继续多练习，给自己更多的时间积累和实践。"""
    else:
        return None
    message.append({"role": "user", "content": txt})
    try:
        res_dic = json.loads(post_GPT(message, timeout=timeout, temperature=1.2)[1])
        res = res_dic["res"]["choices"][0]["message"]["content"]
    except Exception as e:
        res = txt
    return res


def long_eval_zishi(lvl, timeout=50):
    system_prompt = f"""你是一个毛笔书法老师. 用户将一个毛笔书写报告作为输入, 你输出对它的改写. 要求:
    # 1. 保持原意大致不变.
    # 2. 语言要恰当, 你的说话对象是一个正在学习书法的学生.
    # 3. 你的输出要尽量详细.
    """

    exp_input = f"""这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    exp_output= f"""这个字书写规范整齐，笔画技法熟练娴熟，线条质感生动传神，墨迹书写稳定且表现力强，书写节奏和韵律相对流畅自如，个人风格和创新初步显露。"""
    message = list()
    message.append({"role": "system", "content": system_prompt})
    message.append({"role": "user", "content": exp_input})
    message.append({"role": "assistant", "content": exp_output})
    if lvl == 5:
        txt = """学生的笔画有力而准确，使用笔杆的能力很强，呼吸和身体姿态得到很好地改进，足以让观众感受到一定的艺术魅力，需要继续探索和加强书写技巧和练习。"""
    elif lvl == 4:
        txt = """学生笔握持姿势规范，身体站、坐姿正确，纸张和桌面的位置摆放合适，书写角度正确，笔画流畅，呈现出一定的艺术感染力，需要加强对笔画和字符结构的练习，更好地表现书写的优美性。"""
    elif lvl == 3:
        txt = """学生的姿势正确，姿态端正，但写字时缺乏正确的呼吸节奏和身体节奏，导致笔画有些生硬，需要注意呼吸和身体的配合。"""
    elif lvl == 2:
        txt = """学生的笔握持姿势和身体姿势还比较正确，但书写时所选的桌椅高度和纸张位置存在不足之处，无法保证书写时的舒适度和稳定性，需要注意作出调整。"""
    elif lvl == 1:
        txt = """学生的笔握持姿势存在一些问题，使用的握笔力度不足，笔画不流畅、生硬，身体和笔的角度不够稳定，需要加强对书写姿势的练习与修正。"""
    else:
        return None
    message.append({"role": "user", "content": txt})
    try:
        res_dic = json.loads(post_GPT(message, timeout=timeout, temperature=1.2)[1])
        res = res_dic["res"]["choices"][0]["message"]["content"]
    except Exception as e:
        res = txt
    return res


def long_eval_lidu(lvl, timeout=50):
    system_prompt = f"""你是一个毛笔书法老师. 用户将一个毛笔书写报告作为输入, 你输出对它的改写. 要求:
    # 1. 保持原意大致不变.
    # 2. 语言要恰当, 你的说话对象是一个正在学习书法的学生.
    # 3. 你的输出要尽量详细.
    """

    exp_input = f"""这个字整体规范，笔画技法掌握较好，线条质感生动，墨迹稳定度不容置疑，书写节奏与韵律相对流畅，个人风格与创新能够初见端倪。"""
    exp_output= f"""这个字书写规范整齐，笔画技法熟练娴熟，线条质感生动传神，墨迹书写稳定且表现力强，书写节奏和韵律相对流畅自如，个人风格和创新初步显露。"""
    message = list()
    message.append({"role": "system", "content": system_prompt})
    message.append({"role": "user", "content": exp_input})
    message.append({"role": "assistant", "content": exp_output})
    if lvl == 5:
        txt = """学生的笔画线条清晰、流畅，掌握了毛笔字的描摹技巧，自由控制着笔画的重心及使笔画灵活多样，形成协调的笔画效果，自然不做作。在要素运用方面更加得心应手，并能够丰富工整地明确表现毛笔字的独特风格和特色。"""
    elif lvl == 4:
        txt = """学生的笔画线条比较清晰、流畅，有很好的点画控制能力，用笔相当老道，在毛笔描绘过程中把能体现作品气质的各种技巧都运用其中，但仍可以更加准确摆放笔画，使其更好的体现毛笔字书写特色。"""
    elif lvl == 3:
        txt = """学生的毛笔字写法笔画掌握有在一定程度上的提升，但仍存在一些缺点，如笔画线条略显急促，轻重不太匀称等。需要继续加强练习，提高笔画的准确性和匀称度。"""
    elif lvl == 2:
        txt = """学生在写字时，有一定程度的掌握毛笔的重心和力度控制，但仍需注意笔画重心匀称问题，有时笔画线条太过粗重，有时太过轻易，需要改进笔画书写的准确度。"""
    elif lvl == 1:
        txt = """学生在书写时，无法保持笔画线条清晰且流畅，线条有时过于细，有时过于粗，重心掌握十分不当，不符合毛笔字的基本规律."""
    else:
        return None
    message.append({"role": "user", "content": txt})
    try:
        res_dic = json.loads(post_GPT(message, timeout=timeout, temperature=1.2)[1])
        res = res_dic["res"]["choices"][0]["message"]["content"]
    except Exception as e:
        res = txt
    return res



if __name__ == '__main__':
    print("test: prompy.py")
    print("author: Sijin Yu")
    test = long_eval_lidu
    print("5: " + test(5))
    print("4: " + test(4))
    print("3: " + test(3))
    print("2: " + test(2))
    print("1: " + test(1))