# thirteen_robot
## 内容
根据openai的whisper以及google的开源语音api实现了一个简单的人机对话机器人  
### 原理
读取语言，通过语音识别将语言转化为文字。  
再根据判断文字中是否存在已设定的关键词来作出相应操作。  


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
## 拓展
* 可根据不同的语言来确定语音识别的内容
* 可自定义关键词
* 可自定义接收指令后操作或回答特定语句
