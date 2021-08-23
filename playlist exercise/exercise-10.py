import pickle
import requests
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
respons=requests.get(url)
respons_text=respons.text
data=respons_text.splitlines()
red=[[i] for i in data]
fileobj=open('irisData.pkl','wb')
pickle.dump(red,fileobj)
fileobj.close()
fileobj=open('irisData.pkl','rb')
data=pickle.load(fileobj)
print(data)