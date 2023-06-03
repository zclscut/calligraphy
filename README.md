[TOC]



# 在线学习状态分析系统操作手册



## 1.引言

### 1.1.应用开发背景

- 青少年学习时的状态是家长们密切关心的。而随着智能手机等移动通信设备的普及，通过摄像头或录制视频从而对青少年学习时的状态进行分析的可能性大大提高。同时，通过视频反馈出青少年此时的学习状态，也可以对学生起到监督作用并更好地提升学生学习的专注度。因此，本应用的开发能够很好的满足以上需求。

### 1.2.应用概述

- 本系统采`学生端-服务云端-家长端`三端式架构，`学生端`和`家长端`是基于`Windows`环境的`.exe`应用，服务云端为`mysql`数据库，提供数据存储、数据查询等功能。
- 本系统采用基于`opencv``dlib``tensorflow``pytorch``imutils`等架构开发。
  - 在观看网课或观看课程视频等应用场景中，学生端应用可以实时监测学生在使用电脑的学习状态，包括姿势是否正确，情绪是否消极，学习是否疲劳，目光是否聚焦于电脑，最后进行综合加权评分得出一个专注度分数。
  - 学生端应用在评分后，会把所有变化的学习状态更新同步到云端服务器。供家长端应用查询，家长可以实时掌握学生的学习状态，以方便及时进行个性化的解决措施。

## 2.学生端

- 运行需要`pytorch`和`tensorflow`支持，其余依赖见`requirements.txt`。
- 安装好依赖后运行`gui.py即可`。

### 2.1.注册登录

- 登录页点至`注册`即可进入注册页，输入信息后点击注册，注册成功点击`返回`返回到登录页登录。
<figure>
	<center>
    	<img src="img\学生注册.png" style="zoom:67%;" />
    	<img src="img\学生登录.png" alt="学生登录" style="zoom:67%;" />
    </center>
</figure>
<center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图1：注册登录成功</div>
</center>

- 注册可能的报错

  - 存在选项为空
  - 密码不一致或少于6位
  - 账号名已经被占用
  - 账号超过9位数字
  - 数据库连接或操作失败

- 密码无错误登录成功，即可进入主界面

### 2.2.主界面介绍
#### 2.2.1.菜单栏简介

<figure>
	<center>
    	<img src="img\菜单开始.png" style="zoom:100%;" />
    	<img src="img\菜单帮助.png"  style="zoom:89%;" />
    </center>
</figure>
<center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图2：开始选项(左)帮助选项(右)</div>
</center>

- 登录成功后默认开启摄像头，点击`开始-摄像头`可关闭摄像头，进入背景图模式，再次点击`开始-摄像头`可打开摄像头。

    <figure>
      	<center>
          	<img src="img\背景模式.png" style="zoom:67%;" />
          </center>
      </figure>
      <center>
              <div style="color:orange; border-bottom: 1px solid #d9d9d9;
          	display: inline-block;
          	color: #999;
          	padding: 2px;">图3：背景图模式</div>
      </center>
- 摄像头模式或者背景图模式下，点击`开始-文件`选择视频文件`*.mp4/*.avi`，可读取视频。视频播放完毕画面就将会停止。可选择`开始-文件`重新打开视频或`开始-摄像头`进入摄像头模式。

    <figure>
      	<center>
          	<img src="img\视频模式.png" style="zoom:40%;" />
          	<img src="img\摄像头模式.png"  style="zoom:40%;" />
          </center>
      </figure>
      <center id="img4">
              <div style="color:orange; border-bottom: 1px solid #d9d9d9;
          	display: inline-block;
          	color: #999;
          	padding: 2px;">图4：视频模式(上)摄像头模式(下)</div>
      </center>
- 点击`帮助-操作手册`可跳转至`github`仓库中的应用操作文档，点击`帮助-源码仓库`可跳转至`github-TianXiang_srp(public)`仓库，点击`帮助-联系我们`可弹出开发人员的联系方式。

     <center>
     	<img src="img\联系我们.png" style="zoom:100%;" />
     </center>
     <center>
            <div style="color:orange; border-bottom: 1px solid #d9d9d9;
         	display: inline-block;
         	color: #999;
         	padding: 2px;">图5：联系我们</div>
     </center>
#### 2.2.2.功能展示

- 选择左边栏`分析模式`栏中按钮可进入不同模式，综合分析即为专注度分析，包含其它三种`姿势/情绪/疲劳`分析。
- 在分析状态中，按下`分析模式`的任意按键，将退出分析模式进入纯摄像或纯视频模式。再次按下`分析模式`的任意按键，会进入对应模式进行识别。
- 选择左边栏`标志栏`中按钮可更改视频帧上的辅助标志线/点，默认全部勾选。
- 分数说明
  - 姿势分析
    
    | 分数 |    评级     |
    | :--: | :---------: |
    |  20  |  倾斜>20°   |
    |  40  | 倾斜15°~20° |
    |  70  | 倾斜10°~15° |
    |  90  |  倾斜<10°   |
    
  - 情绪分析
    
    |  分数  | 评级 |
    | :----: | :--: |
    |  0~40  | 积极 |
    | 40~60  | 中性 |
    | 60~100 | 消极 |
  - 疲劳分析
    | 分数  |   评级   |
    | :---: | :------: |
    | 0~15  |   清醒   |
    | 15~35 |   一般   |
    | 35~50 | 轻度疲劳 |
    | 50~60 | 中度疲劳 |
    |  60~  | 重度疲劳 |
    
  - 综合分析
    |  分数  | 评级 |
    | :----: | :--: |
    |  0~45  | 专注 |
    | 45~60  | 正常 |
    | 60~70  | 欠佳 |
    | 70~100 | 分心 |
##### 2.2.2.1.姿势分析

- 按下`分析模式-姿势`时，标识***仅仅***使能`姿势线`，右边`信息`栏***仅仅***使能`姿势分析`框，且不使能`分数`。

  <center>
  	<img src="img\姿势分析.png" style="zoom:70%;" />
  </center>
  <center>
         <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图6：学习姿势错误，可以正常识别(侧倾)</div>
  </center>

##### 2.2.2.2.情绪分析

- 按下`分析模式-情绪`时，标识***仅仅***使能`人脸框`，右边`信息`栏***仅仅***使能`情绪分析`框`细分`，且不使能`大类`和`分数`。

<center>
	<img src="img\情绪分析.png" style="zoom:70%;" />
</center>
<center>
       <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图7：上网课接受到新知识后感到惊奇,，可以正常识别</div>
</center>



##### 2.2.2.3.疲劳分析

- 按下`分析模式-疲劳`时，标识***仅仅***使能`人脸框`和`人脸点`，右边`信息`栏***仅仅***使能`疲劳分析`框。在一个帧计时周期内，更新一次`疲劳分析`框中的`分数`。

  <center>
  	<img src="img\疲劳分析.png" style="zoom:70%;" />
  </center>
  <center>
         <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图8：连续检测1000帧，统计判断疲劳程度。</div>
  </center>

##### 2.2.2.4.专注度分析

- 按下`分析模式-综合`时，标识框内选项***全部***使能，右边`信息`栏***全部***使能。在一个帧计时周期内，更新一次四种分析的`分数`和专注度的`等级`。

  <center>
  	<img src="img\综合分析.png" style="zoom:70%;" />
  </center>
  <center>
         <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图9：连续检测1000帧，统计判断疲劳程度。</div>
  </center>
### 2.3.性能说明
- 参考各模块性能，***不包含***写数据库，在CPU`i7-1065G7`,内存`16G`的`Windows11`，电脑基于`720×1280`的摄像头***不调用***GPU的环境中测试而得。**注意：**不同穿搭(眼镜/帽子)、背景、明暗环境会影响检测人脸时间，从而影响帧率，本数据测试环境参考[图4：摄像头模式](#img4)。

|       模块       | 帧率 |     测试     |
| :--------------: | :--: | :----------: |
|     坐姿分析     |  21  | 1000帧/47秒  |
|     情绪分析     |  10  | 1000帧/101秒 |
|     疲劳分析     |  15  | 1000帧/65秒  |
| 综合(专注度)分析 |  5   | 1000帧/191秒 |

- 在`420×720`的测试视频中[expressions_2.mp4](https://github.com/zcl-scut/TianXiang_srp/tree/main/images)，***不调用***GPU，***不包含***写数据库，情绪分析帧率可达12帧(500帧/42秒)。

- 在`720×1280`的测试视频中[expressions.mp4](https://github.com/zcl-scut/TianXiang_srp/tree/main/images)，***不调用***GPU，***不包含***写数据库，情绪分析帧率可达12帧(1000帧/83秒)。

  <figure>
  	<center>
      	<img src="img\GUI运行时间.png" style="zoom:100%;" />
      </center>
  </figure>
  <center>
          <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图10：单次测试综合分析执行一帧时间(未取平均)。综合测试中，把人脸检测从情绪模块和疲劳模块中分离出来，供两者调用。故单独运行情绪分析模块时，参考单帧运行时间应该为0.032+0.042=0.074秒</div>
  </center>

- 实测单次写数据库时间约为`170ms`，故应用`.exe`包含写数据库功能时，帧率被限制到6帧以下。

### 2.4.数据库配置文件(db.ini)

- 若云服务器IP端口，或者数据库登录账号密码发生变更，请修改`[mysql]`字段。如，在本地数据库调试中，更改为`host=127.0.0.1`。

  <center>
  	<img src="img\db.mysql.png" style="zoom:70%;" />
  </center>
  <center>
         <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图11：[mysql]字段默认设置</div>
  </center>

- 若在仅仅本地识别信息，识别状态无需写入数据库的应用场景，请修改`[write]`字段，`is_insert=0`为不写入数据库，其中帧率也会更高；`is_insert=1`为写入数据库，帧率会更低。

- 若分析状态数据表的键值定义发生变化，或者需要修改UI界面中文状态描述，请修改`[posture]`或`[emotion]`或`[concentration]`字段。以下为`db.ini`配置和云端数据表定义的对应关系。

  <figure>
  	<center>
      	<img src="img\db.posture.png" style="zoom:100%;" />
      	<img src="img\db.posture.key.png"  style="zoom:89%;" />
      </center>
  </figure>
  <center>
          <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图12：本地配置和云端配置需一致。如此配置时，UI界面姿势识别结果为正常/前倾/低头/侧倾</div>
  </center>

### 2.5.菜单栏配置文件(menu.ini)

- 如需更改或增加支持的读取视频格式，可更改`[start]`字段。

  <figure>
  	<center>
      	<img src="img\menu.start.png" style="zoom:80%;" />
      	<img src="img\menu.start.windows.png"  style="zoom:90%;" />
      </center>
  </figure>
  <center>
          <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图13：“Windows文件管理器”显示的即为filetype对应的键值</div>
  </center>

- 如`github`仓库/帮助文档/联系的地址发生改变，请更改`[help]`字段。其中链接为UI界面跳转打开的网址。

  <figure>
  	<center>
      	<img src="img\menu.help.png" style="zoom:60%;" />
      	<img src="img\联系我们.png"  style="zoom:120%;" />
      </center>
  </figure>
  <center>
          <div style="color:orange; border-bottom: 1px solid #d9d9d9;
      	display: inline-block;
      	color: #999;
      	padding: 2px;">图14：按下“联系我们”，弹出信息框中显示的的即为contact_us对应的键值</div>
  </center>

## 3.家长端

### 3.1.安装

#### 3.1.1.安装环境

- 需要`Windows xp`及以上系统。

- `Windows xp`需要安装`.net framework 3.5`及以上版本。

- `Windows 7/8/10/11`不需要额外安装。

#### 3.1.2.安装步骤

- 下载压缩包，并自行选择路径解压。

  <img src="img\家长端解压.png" alt="image-20230312104727284" style="zoom: 67%;" />

  <center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图15：解压目录</div>
  </center>


- 在解压路径找到`.exe`可执行文件，双击成功打开家长端。

  <img src="img\解压登录.png" alt="解压登录" style="zoom:67%;" />
<center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图16：家长端登录页</div>
</center>


### 3.2.注册登录

- 若未注册，单击`注册`按钮可进行注册。按照提示填写相关信息，学生ID为学生注册时分配的ID，***请在学生端查看***。若误触则可按`返回`返回登录界面。

  - 注册
    - 姓名填写家长姓名
    - 手机号为11位纯数字
    - 密码为6位及以上字母和数字组合
    - 确认密码需与密码一致
    - 学生ID为纯数字
<figure>
	<center>
    	<img src="img\注册.png" alt="注册" style="zoom:67%;" />
    	<img src="img\登录.png" style="zoom:72%;" />
    </center>
</figure>
<center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图17：家长端注册登录示例</div>
</center>


- 注册登录成功后进入主页面

### 3.3.查询学生状态

- 单击![img](img\时间按钮.png)选择查询的起始时间和终止时间。查询内容可自由选择打勾或去勾，打勾则正常查询，去勾则不查询该类数据。

  <img src="img\家长查询.png" style="zoom: 67%;" />

  <center>
        <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    	display: inline-block;
    	color: #999;
    	padding: 2px;">图18：查询界面</div>
  </center>

- 查询事件分类和查询值。详细信息请查看`/img/数据库表设计.xls`。

| 数据库标签 |      坐姿分析      | 情绪分析 | 疲劳分析 | 专注度分析 |
| :--------: | :----------------: | :------: | :------: | :--------: |
|     1      |      坐态正常      |   积极   |   清醒   |  极其专注  |
|     2      | 脸部朝前的颈部前倾 |   中性   | 临界状态 |    专注    |
|     3      | 脸部朝下的颈部前倾 |   消极   | 轻度疲劳 |   不专注   |
|     4      |    脊椎左右倾斜    |          | 中度疲劳 |  极不专注  |
|     5      |                    |          | 重度疲劳 |            |

