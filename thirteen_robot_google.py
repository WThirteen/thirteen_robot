import pyttsx3
import speech_recognition as sr
import datetime
import os
import wave

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def save_as_wav(audio, output_file_path):
    with wave.open(output_file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)  # 单声道
        wav_file.setsampwidth(2)  # 16位PCM编码
        wav_file.setframerate(44100)  # 采样率为44.1kHz
        wav_file.writeframes(audio.frame_data)


def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour >= 0 and hour < 12:
        speak("早上好")

    elif hour >= 12 and hour < 16:
        speak("中午好")

    else:
        speak("晚上好")

    print("我是你的语音助手 Thirteen...请说出指令")
    speak("我是你的语音助手 Thirteen...请说出指令")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("识别中...")
        # google
        query = r.recognize_google(audio, language='cmn-Hans-CN')

        print(f"输入对话：{query}\n")

    except Exception as e:
        print(e)
        print("请再说一遍...")
        speak("请再说一遍...")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()
    judge = -1
    query = takeCommand().lower()
    while True:
        query = takeCommand().lower()

        # print(query)

        if "你好" in query:
            speak("你也好")

        if "今天怎么样" in query or "今天怎麽樣" in query:
            speak("我很好")

        if "十三" in query:
            speak("我在，我是thirteen")

        if "你是谁" in query or "你是誰" in query:
            speak("我是你的语音助手，thirteen")

        if "你的名字" in query or "你叫什么" in query or "你叫什麽" in query:
            speak("我的名字是thirteen.")

        if "谢谢你" in query or "謝謝你" in query:
            speak("不用谢")

        if "时间" in query or "時間" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"现在的时间是 {strTime}")

        # 退出
        if "退出" in query and judge==-1:
            speak("确定要退出吗?请说确定")
            judge = 0
        if ("确定" in query or "確定" in query) and judge == 0:
            speak("正在退出，再见!")
            exit(0)
