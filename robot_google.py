import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from thirteen_robot_google import * 
from robot_ui import Ui_Form


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        


    def run1(self):
        query = takeCommand().lower()
        self.textBrowser.setText(query)
        
        response = echo(query)
        self.textBrowser_2.setText(response)


    
def echo(query):
    response = ''
    if "你好" in query:
        speak("你也好")
        response = "你也好"

    if "今天怎么样" in query or "今天怎麽樣" in query:
        speak("我很好")
        response = "我很好"

    if "十三" in query:
        speak("我在，我是thirteen")
        response = "我在，我是thirteen"

    if "你是谁" in query or "你是誰" in query:
        speak("我是你的语音助手，thirteen")
        response = "我是你的语音助手，thirteen"

    if "你的名字" in query or "你叫什么" in query or "你叫什麽" in query:
        speak("我的名字是thirteen.")
        response = "我的名字是thirteen."

    if "谢谢你" in query or "謝謝你" in query:
        speak("不用谢")
        response = "不用谢"

    if "时间" in query or "時間" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"现在的时间是 {strTime}")
        response = f"现在的时间是 {strTime}"

    return response

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    wishMe()
    sys.exit(app.exec_())
    