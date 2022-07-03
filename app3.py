from pyexpat import model
from flask import Flask, jsonify, render_template, request
import pickle
import model2 as md2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
@app.route('/getFinalPrediction',methods=['GET', 'POST'])
def index():
    html_text = requests.get('https://www.healthline.com/health/how-to-stop-a-panic-attack').text
    soup = BeautifulSoup(html_text, 'lxml')
    stepsToDo = soup.find_all('h3')
    df = pd.DataFrame(columns = 
            ['steps'])
        
    soup = BeautifulSoup(html_text, 'lxml')
    stepsToDo = soup.find_all('h3')
    for steps in stepsToDo:
        try:
            one= steps.text[3:]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    n = 3
    df.drop(df.tail(n).index,
            inplace = True)
    

    html_text2 = requests.get('https://www.medicalnewstoday.com/articles/321510#methods').text




    soup = BeautifulSoup(html_text2, 'lxml')
    stepsToDo = soup.find_all('h3')




    soup = BeautifulSoup(html_text2, 'lxml')
    stepsToDo = soup.find_all('h3')
    for steps in stepsToDo:
        try:
            one= steps.text[3:]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    n = 1
    df.drop(df.tail(n).index,
            inplace = True)
    


    html_text3 = requests.get('https://www.priorygroup.com/blog/what-to-do-during-a-panic-attack').text




    soup = BeautifulSoup(html_text3, 'lxml')
    stepsToDo = soup.find_all('strong')




    soup = BeautifulSoup(html_text3, 'lxml')
    stepsToDo = soup.find_all('strong')
    for steps in stepsToDo:
        try:
            one= steps.text
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    n = 6
    df.drop(df.tail(n).index,
            inplace = True)
    df.drop(25,inplace=True)



    html_text4 = requests.get('https://www.priorygroup.com/blog/5-top-tips-for-coping-with-panic-attacks').text




    soup = BeautifulSoup(html_text4, 'lxml')
    stepsToDo = soup.find_all('strong')




    soup = BeautifulSoup(html_text4, 'lxml')
    stepsToDo = soup.find_all('strong')
    for steps in stepsToDo:
        try:
            one= steps.text[3:]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    n = 5
    df.drop(df.tail(n).index,
            inplace = True)
    df.drop(34,inplace=True)
    df.drop(35,inplace=True)
    df.drop(36,inplace=True)
    df.drop(37,inplace=True)
    df.drop(38,inplace=True)
    df.drop(39,inplace=True)



    html_text5 = requests.get('https://www.verywellmind.com/what-to-do-after-a-panic-attack-2584267').text




    soup = BeautifulSoup(html_text5, 'lxml')
    stepsToDo = soup.find_all('h3')




    soup = BeautifulSoup(html_text5, 'lxml')
    stepsToDo = soup.find_all('h3')
    for steps in stepsToDo:
        try:
            one= steps.text[:-2]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)

    


    html_text6 = requests.get('https://www.verywellhealth.com/how-to-stop-a-panic-attack-5202930').text




    soup = BeautifulSoup(html_text6, 'lxml')
    stepsToDo = soup.find_all('strong')




    soup = BeautifulSoup(html_text6, 'lxml')
    stepsToDo = soup.find_all('strong')
    for steps in stepsToDo:
        try:
            one= steps.text
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    df.drop(59,inplace=True)
    df.drop(57,inplace=True)
    df.drop(55,inplace=True)
    df.drop(52,inplace=True)
    df.drop(50,inplace=True)
    df.drop(49,inplace=True)
    df.drop(48,inplace=True)
    df.drop(47,inplace=True)
    df.drop(46,inplace=True)
    df.drop(45,inplace=True)
    df.drop(44,inplace=True)
    df.drop(43,inplace=True)




    html_text7 = requests.get('https://www.nbcnews.com/better/health/7-steps-getting-through-anxiety-attack-ncna801081').text





    soup = BeautifulSoup(html_text7, 'lxml')
    stepsToDo = soup.find_all('h2')




    soup = BeautifulSoup(html_text7, 'lxml')
    stepsToDo = soup.find_all('h2')
    for steps in stepsToDo:
        try:
            one= steps.text[8:]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)
        
    df.drop(56,inplace=True)



    html_text8 = requests.get('https://www.healthline.com/health/anxiety/panic-attack-self-care-strategies').text




    soup = BeautifulSoup(html_text8, 'lxml')
    stepsToDo = soup.find_all('h2')




    soup = BeautifulSoup(html_text8, 'lxml')
    stepsToDo = soup.find_all('h2')
    for steps in stepsToDo:
        try:
            one= steps.text[3:]
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)

    



    html_text9 = requests.get('https://firstaidforlife.org.uk/how-to-help-someone-having-a-panic-attack/').text




    soup = BeautifulSoup(html_text9, 'lxml') 
    stepsToDo = soup.find_all("a", {"href":"https://firstaidforlife.org.uk/999when-to-call-for-an-ambulance-and-when-not-to/"})




    soup = BeautifulSoup(html_text9, 'lxml')
    stepsToDo = soup.find_all("a", {"href":"https://firstaidforlife.org.uk/999when-to-call-for-an-ambulance-and-when-not-to/"})
    for steps in stepsToDo:
        try:
            one= steps.text
        except:
            one= None
        df = df.append({'steps': one}, ignore_index=True)

    



    df = df.sample(frac=1).reset_index(drop=True)



    df['steps_no_contract'] = df['steps'].apply(lambda x: [contractions.fix(word) for word in x.split()])



    df['steps_str'] = [' '.join(map(str, l)) for l in df['steps_no_contract']]



    import nltk
    nltk.download('punkt')
    df['tokenized_steps'] = df['steps_str'].apply(word_tokenize)



    df['lower_steps'] = df['tokenized_steps'].apply(lambda x: [word.lower() for word in x])



    df['steps_lower_str'] = [' '.join(map(str, l)) for l in df['lower_steps']]



    m = df['steps_lower_str']

    df['med1'] = m.map(lambda x: True if 'medications' in x else False)
    df['med2'] = m.map(lambda x: True if 'prescribed' in x else False)
    df['med3'] = m.map(lambda x: True if 'medicine' in x else False)



    df['exc1'] = m.map(lambda x: True if 'muscle' in x else False)
    df['exc2'] = m.map(lambda x: True if 'physical' in x else False)
    df['exc3'] = m.map(lambda x: True if 'exercise' in x else False)
    df['exc4'] = m.map(lambda x: True if 'activities' in x else False)




    df['bre1'] = m.map(lambda x: True if 'breathing' in x else False)
    df['bre2'] = m.map(lambda x: True if 'breaths' in x else False)
    df['bre3'] = m.map(lambda x: True if 'meditate' in x else False)
    df['bre4'] = m.map(lambda x: True if 'breath' in x else False)
    df['bre5'] = m.map(lambda x: True if 'meditation' in x else False)




    df['happy1'] = m.map(lambda x: True if 'happy' in x else False)
    df['happy2'] = m.map(lambda x: True if 'place' in x else False)




    df['fuc1'] = m.map(lambda x: True if 'focus' in x else False)
    df['fuc2'] = m.map(lambda x: True if 're-focus' in x else False)
    df['fuc3'] = m.map(lambda x: True if 'object' in x else False)
    df['fuc4'] = m.map(lambda x: True if 'objects' in x else False)
    df['fuc5'] = m.map(lambda x: True if 'notice' in x else False)
    df['fuc6'] = m.map(lambda x: True if 'name' in x else False)
    df['fuc7'] = m.map(lambda x: True if 'naming' in x else False)




    df['cal1'] = m.map(lambda x: True if 'mindfulness' in x else False)
    df['cal2'] = m.map(lambda x: True if 'lavender' in x else False)
    df['cal3'] = m.map(lambda x: True if 'peaceful' in x else False)
    df['cal4'] = m.map(lambda x: True if 'positive' in x else False)




    df['er1'] = m.map(lambda x: True if 'medical' in x else False)
    df['er2'] = m.map(lambda x: True if 'consult' in x else False)
    df['er3'] = m.map(lambda x: True if 'doctor' in x else False)
    df['er4'] = m.map(lambda x: True if 'hospital' in x else False)




    df['obRea1'] = m.map(lambda x: True if 'recognize' in x else False)
    df['obRea2'] = m.map(lambda x: True if 'remember' in x else False)
    df['obRea3'] = m.map(lambda x: True if 'remind' in x else False)




    df['matr'] = m.map(lambda x: True if 'mantra' in x else False)



    conditions = [
    (df['med1'] == True) | (df['med2'] == True) | (df['med3'] == True),
    (df['exc1'] == True) | (df['exc2'] == True) | (df['exc3'] == True) | (df['exc4'] == True),
    (df['bre1'] == True) | (df['bre2'] == True) | (df['bre3'] == True) | (df['bre4'] == True) | (df['bre5'] == True),
    (df['happy1'] == True) | (df['happy2'] == True),
    (df['fuc1'] == True) | (df['fuc2'] == True) | (df['fuc3'] == True) | (df['fuc4'] == True) | (df['fuc5'] == True) | (df['fuc6'] == True) | (df['fuc7'] == True),
    (df['cal1'] == True) | (df['cal2'] == True) | (df['cal3'] == True) | (df['cal4'] == True),
    (df['er1'] == True) | (df['er2'] == True) | (df['er3'] == True) | (df['er4'] == True),
    (df['obRea1'] == True) | (df['obRea2'] == True) | (df['obRea3'] == True),
    (df['matr'] == True),
    (df['med1'] == False) & (df['med2'] == False) & (df['med3'] == False) & (df['exc1'] == False) & (df['exc2'] == False) & (df['exc3'] == False) 
    & (df['exc4'] == False) & (df['bre1'] == False) & (df['bre2'] == False) & (df['bre3'] == False) & (df['bre4'] == False) 
    & (df['bre5'] == False) & (df['happy1'] == False) & (df['happy2'] == False) & (df['fuc1'] == False) & (df['fuc2'] == False) 
    & (df['fuc3'] == False) & (df['fuc4'] == False) & (df['fuc5'] == False) & (df['fuc6'] == False) & (df['fuc7'] == False) 
    & (df['cal1'] == False) & (df['cal2'] == False) & (df['cal3'] == False) & (df['cal4'] == False) & (df['obRea1'] == False) 
    & (df['obRea2'] == False) & (df['obRea3'] == False) & (df['matr'] == False)
    ]



    values = ['medicine', 'exce', 'breathingEx', 'happyPl', 'fucus', 'calm', 'emgRoom', 'reality', 'mantra', 'other']



    df['category'] = np.select(conditions, values)








    if request.method == 'POST' :
        model = pickle.load(open("model.pkl", "rb"))
        print("sdsfcdsf")

        swt = request.json.get('swt')
        diffBr = request.json.get('diffBr')
        chestPn = request.json.get('chestPn')
        abCramp = request.json.get('abCramp')
        headache = request.json.get('headache')
        dizz = request.json.get('dizz')
        fear = request.json.get('fear')
        depres = request.json.get('depres')
        flashbk = request.json.get('flashbk')
        trem = request.json.get('trem')
        bluVi = request.json.get('bluVi')
        tunVi = request.json.get('tunVi')
        senTer = request.json.get('senTer')
        firstYes = request.json.get('firstYes')
        lastYes = request.json.get('lastYes')

        swt = int(swt)
        diffBr = int(diffBr)
        chestPn = int(chestPn)
        abCramp = int(abCramp)
        headache = int(headache)
        dizz = int(dizz)
        fear = int(fear)
        depres = int(depres)
        flashbk = int(flashbk)
        trem = int(trem)
        bluVi = int(bluVi)
        tunVi = int(tunVi)
        senTer = int(senTer)
        firstYes = int(firstYes)
        lastYes = int(lastYes)
        

        data_to_predict = {'swt': [swt], 'diffBr': [diffBr], 'chestPn': [chestPn], 'abCramp': [abCramp], 'headache': [headache], 'dizz': [dizz], 'fear': [
        fear], 'depres': [depres], 'flashbk': [flashbk], 'trem': [trem], 'bluVi': [bluVi], 'tunVi': [tunVi], 'senTer': [senTer], 'firstYes': [firstYes], 'lastYes': [lastYes]}
        print(data_to_predict)
        data_to_predict = md2.prototype(data_to_predict)


        if(data_to_predict == 'high'):
            conditions = [(df['category'] == 'medicine'), (df['category'] == 'breathingEx'), (df['category'] == 'happyPl'), (df['category'] == 'fucus'), (df['category'] == 'calm'), (df['category'] == 'emgRoom'), (df['category'] == 'exce'), (df['category'] == 'reality'), (df['category'] == 'mantra'), (df['category'] == 'other')]
            values = ['2', '3', '6', '5', '4', '1', '6', '6', '6', '6']
            df['value'] = np.select(conditions, values)

        elif(data_to_predict == 'mid'):
            conditions = [(df['category'] == 'medicine'), (df['category'] == 'breathingEx'), (df['category'] == 'happyPl'), (df['category'] == 'fucus'), (df['category'] == 'calm'), (df['category'] == 'emgRoom'), (df['category'] == 'exce'), (df['category'] == 'reality'), (df['category'] == 'mantra'), (df['category'] == 'other')]
            values = ['2', '1', '6', '3', '6', '6', '4', '6', '5', '6']
            df['value'] = np.select(conditions, values)

        else:
            conditions = [(df['category'] == 'medicine'), (df['category'] == 'breathingEx'), (df['category'] == 'happyPl'), (df['category'] == 'fucus'), (df['category'] == 'calm'), (df['category'] == 'emgRoom'), (df['category'] == 'exce'), (df['category'] == 'reality'), (df['category'] == 'mantra'), (df['category'] == 'other')]
            values = ['6', '1', '5', '3', '4', '6', '6', '2', '6', '6']
            df['value'] = np.select(conditions, values)

        df.sort_values("value", inplace = True)

        df = df[~df.duplicated('value') | (df['value'] == '6')]

        stepsUi = df['steps_lower_str'].head(7).to_json(orient = 'values')

        returnObject = {"prediction":data_to_predict, "stepsUi":stepsUi}
    return jsonify(returnObject)
app.run()

if __name__ == "_main_":
    app.run(debug=True)