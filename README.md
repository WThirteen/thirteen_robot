# thirteen_robot
<h4 align="center">
    <p>
        <b>中文</b> |
        <a href="https://github.com/WThirteen/thirteen_robot/blob/main/README_EN.md">English</a>
    <p>
</h4>
</div>

## 内容
根据openai的whisper以及google的开源语音api实现了一个简单的人机对话机器人  
### 原理
读取语言，通过语音识别将语言转化为文字。  
再根据判断文字中是否存在已设定的关键词来作出相应操作。  

## 初始页面
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test.jpg)


## 配置
Python == 3.10
使用命令行配置环境  
```
pip install -r requirements.txt
```
whisper的安装详见|https://github.com/openai/whisper

## 使用语音识别模型 
### 1.thirteen_robot_google
*使用Google Cloud Speech*
（国内用户使用需使用科学上网工具）
### 2.thirteen_robot_whisper
*使用OpenAI的whisper*
（初次使用需要下载whisper模型）

# 使用
运行*robot_whisper.py*或者*robot_google.py*
```
python robot_whisper.py

```
或者
```
python robot_google.py
```
## 测试页面
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test1.jpg)
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test2.jpg)
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test3.jpg)

## 拓展
* 可根据不同的语言来确定语音识别的内容
* 可自定义关键词
* 可自定义接收指令后操作或回答特定语句
