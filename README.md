# 智能书法评分系统

## 1.文件目录

- 主函数文件。
  - 包含`main.py`，`gui.py `。读取摄像头数据，获取原始帧，调用库函数文件，对原始帧进行处理，显示必要的文字、点线框标注，将两个摄像头的修饰帧拼接后，显示在界面上。`main.py`为`opencv`默认界面；`gui.py `为基于`py2side`的`exe`应用界面
- 库函数文件。
  - `penhold.py`，`penforce.py`，`grade.py`，`sitpos.py`，输入原始帧，完成识别，然后将识别结果，在原帧上标注文字/点/线/框，返回标注后的修饰帧。
  - `segment.py`，输入原始帧，返回所有单字的坐标四元组`(x,y,w,h)`，供`grade.py`调用
  - `audio.py`，播报以上识别结果
- 资源文件。
  - 包括但不限于`.xml/.dat/.h5/.py/.pkl/.pth`等非`python`源码资源文件.

```
│ 
├─main.py - 主程序，同时运行所有功能，同时展示两个摄像头画面
├─gui.py - 基于py2side的exe界面，同时运行所有功能，同时展示两个摄像头画面
├─penhold.py - 封装持笔手势识别函数，龚圣杰负责
├─penforce.py - 封装书写力度检测函数，钟晋负责
├─segment.py - 封装yolo文字分割函数，单泽昱负责
├─grade.py - 封装单字评分函数，钟楚龙负责
├─sitpos.py - 封装坐姿检测函数
├─audio.py  - 封装文字转语音函数，余思进负责
├─requests_ChatGPT.py  - 调用OpenAI的API函数，余思进负责
├─database.py - 封装读写mysql数据库函数
├─lib - 放置资源文件
│  ├─
│  └─
├─img - 放置测试图片或视频
```

## 2. 对话系统的API
- 生成评价
```python
import prompt

lvl = 1  # 评分, 取值范围 [1, 2, 3, 4, 5]
prompt.short_eval(lvl)       # 生成短评, 大概5秒一条结果
prompt.long_eval_ziti(lvl)   # 生成字体详细评价
prompt.long_eval_zishi(lvl)  # 生成姿势详细评价
prompt.long_eval_lidu(lvl)   # 生成力度详细评价
```

- 文本语音互转
```python
from audio2text import audio2text
from text2audio import text2audio

text = "需要转换成语音的文字"
text2audio(text)  # 将输出为: ./audio/text2audio.mp3

audio2text()      # 读取 ./audio/audio2text.mp3 并转为文字, 存储为 audio2text.txt
```
