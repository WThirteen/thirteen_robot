# thirteen_robot
<h4 align="center">
     <p>
      <a href="https://github.com/WThirteen/thirteen_robot/blob/main/README.md">中文</a> |
    <b> English</b>
    <p>
</h4>
</div>

## Content
A simple human-computer conversation robot based on openai's whisper and google's open source voice api
### Principle
Read the language and convert it into text through speech recognition.
Then make the corresponding operation according to whether there is a set keyword in the text.

## Initial page
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test.jpg)


## Configuration
Python == 3.10
Configure the environment using the command line
```
pip install -r requirements.txt
```
The installation of whisper see|[https://github.com/openai/whisper](https://github.com/openai/whisper)

## Use speech recognition models
### 1.thirteen_robot_google
* Use Google Cloud Speech*

### 2.thirteen_robot_whisper
* whisper using OpenAI *
(You need to download the whisper model for your first use)

# Use
Run *robot_whisper.py* or *robot_google.py*
```
python robot_whisper.py

```
perhaps
```
python robot_google.py
```
## Test page
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test1.jpg)
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test2.jpg)
![image](https://github.com/WThirteen/thirteen_robot/blob/main/test_jpg/test3.jpg)

## Expand
* The content of speech recognition can be determined according to different languages
* Customizable keywords
* You can customize to operate or answer specific statements after receiving instructions
