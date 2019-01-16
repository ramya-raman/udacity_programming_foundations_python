import webbrowser
import time

def initiate_break(break_video_url="https://www.youtube.com/watch?v=v10jDT7SJsw",
                   period=300) :
    i = 0
    while i<3 :
        time.sleep(period)
        webbrowser.open(break_video_url)
        i = i + 1

initiate_break("https://www.youtube.com/watch?v=v10jDT7SJsw", 10)
