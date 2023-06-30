# from transformers import pipeline
# qa_model = pipeline(task='table-question-answering', model='dsba-lab/koreapas-finetuned-korwikitq')
import pandas as pd
import sys
import pickle

# koreapas-finetuned-korwikitq model
with open("qa_model.pickle","rb") as fi:
    qa_model = pickle.load(fi)

inputs = sys.argv[1]

df = pd.read_csv('./python_exception.csv', encoding='cp949')
df.fillna('', inplace=True)

def make_answer(q):
    answer = qa_model(query=q, table=df)

    if answer['answer'] == '':
        return '질문에 대한 답을 찾지 못했습니다.'

    elif answer['coordinates'][0][-1] == 0:
        answer2 = answer['answer'].split(',')[0]

        return f'''질문이나 코드에서 파악한 요소는 {answer2} 입니다.
이것의 설명은 다음과 같습니다: {df[df['Error'] == answer2]['설명'].iloc[0]}'''

    else:
        answer2 = answer['cells'][0]

        return f'''질문이나 코드에서 파악한 답변은... {answer2}
이 요소의 이름은 {df[df['설명'] == answer2]['Error'].iloc[0]} 입니다.'''


if '\n' in inputs:
    inputs = inputs[:-1].split('\n')
else:
    inputs = [inputs]

f = open('./msg.txt', 'w')

for q in inputs:
    writemsg = ''
    writemsg = make_answer(q)

    f = open('./msg.txt', 'a')
    f.write(writemsg)
    f.write('\n\n')
    
f.close()
