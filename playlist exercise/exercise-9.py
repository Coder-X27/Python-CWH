import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch('SAPI.SpVoice')
    speak.Speak(str)

if __name__ == '__main__':
    url='https://newsapi.org/v2/everything?q=tesla&from=2021-07-08&sortBy=publishedAt&apiKey=1683095536524a658954f761329188b6'
    data=requests.get(url).text
    conv=json.loads(data)
    for item in conv['articles']:
        s=item['title']
        speak(s)
        speak('Going to speak next news ! Listen Carefully')