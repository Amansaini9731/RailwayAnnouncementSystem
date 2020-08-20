import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
#pip install pyaudio
#pip install pydub
#pip install pandas
#pip install gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudio(audio):
    combined=AudioSegment.empty()
    for audios in audio:
        combined +=AudioSegment.from_mp3(audios)
    return combined
def generateSkeleton():
    audio=AudioSegment.from_mp3('train.mp3')
    #1 -Generating Kripya dhyan dijiye
    start=22000
    finish=25700
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format("mp3"))
    # 2 -Generating Greeating in hindi
    start = 38600
    finish = 43900
    audioProcessed = audio[start:finish]
    audioProcessed.export('10_hindi.mp3', format("mp3"))
    # 3 -Generating ke ratse in hindi
    start = 32600
    finish = 33300
    audioProcessed = audio[start:finish]
    audioProcessed.export('4_hindi.mp3', format("mp3"))
    # 4 -Generating Platform no in hindi
    start = 35000
    finish = 36000
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format("mp3"))
    # 5 -Generating ready to go in hindi
    start = 36400
    finish = 38300
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3', format("mp3"))
    # 6 -Generating ko jane wali in hindi
    start = 34000
    finish = 35100
    audioProcessed = audio[start:finish]
    audioProcessed.export('6_hindi.mp3', format("mp3"))
def generateAnnouncement():
    df=pd.read_excel("train_chart.xlsx")
    print(df)
    for index,item in df.iterrows():
         textToSpeech(item["train_no"]+" "+item["train_name"],"2_hindi.mp3")
         textToSpeech(item["from"]+" "+item["via"],"3_hindi.mp3")
         textToSpeech(item["to"], "5_hindi.mp3")
         textToSpeech(item["platform"], "8_hindi.mp3")
         audios=[f"{i}_hindi.mp3" for i in range(1,11)]
         announcement=mergeAudio(audios)
         announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")
if __name__=="__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now genrating announcement")
    generateAnnouncement()
