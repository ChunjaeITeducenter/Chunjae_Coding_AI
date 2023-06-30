from django.shortcuts import render

# Create your views here.

import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from urllib import parse

def home(request):
    return render(request, 'home.html')

def result(request):
    code = request.POST['code']

    f = open('./run.py', 'w')
    f.write(code)
    f.close()

    # try:
    #     subprocess.check_output('flake8 --config options.flake8 run.py', encoding='utf8')
    #
    # except subprocess.CalledProcessError as e:
    #     err = e.output
    #     subprocess.check_output(f'python qasys_main.py "{err}"', encoding='utf8')
    #     msg = open('./msg.txt')
    #     result = '\n'.join(msg.readlines())
    #
    #     return render(request, 'result.html', {'result': result})

    p = subprocess.Popen('flake8 --config options.flake8 run.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode != 0:
        output = output.decode('utf-8') #.replace('\n','')
        subprocess.check_output(f'python qasys_main.py "{output}"', encoding='utf8')
        msg = open('./msg.txt')
        result = '\n'.join(msg.readlines())

        return render(request, 'result.html', {'result': result})

    else:
        p = subprocess.Popen('python run.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()

        if p.returncode != 0:
            error = error.decode('cp949').split('\n')[-2]
            subprocess.check_output(f'python qasys_main.py "{output}"', encoding='utf8')
            msg = open('./msg.txt')
            result = '\n'.join(msg.readlines())

            return render(request, 'result.html', {'result': result})

        else:
            code = parse.urlencode(parse.parse_qs(f'code={code}'), doseq=True)
            result = f'''https://pythontutor.com/iframe-embed.html#{code}&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false'''

            return render(request, 'tutor.html', {'result': result})
#
#         try:
#             # \r\n
#             result = subprocess.check_output('python run.py', encoding='utf8')
#             result = '해당 코드를 실행하면, 아래와 같이 출력됩니다\n\n' + str(result)
#
#             return render(request, 'result.html', {'result': result})
#         except
#


    # try:
    #     result = subprocess.check_output('python run.py', encoding='utf8')
    #     result = '해당 코드를 실행하면, 아래와 같이 출력됩니다\n\n' + str(result)
    #
    #     return render(request, 'result.html', {'result': result})
    #
    # except subprocess.CalledProcessError as e:
    #     err = e.output
    #     subprocess.check_output(f'python qasys_main.py "{err}"', encoding='utf8')
    #     msg = open('./msg.txt')
    #     result = '\n'.join(msg.readlines())
    #
    #     return render(request, 'result.html', {'result': result})

def answer(request):
    code = request.POST['answer']

    subprocess.check_output(f'python qasys_main.py "{code}"', encoding='utf8')
    msg = open('./msg.txt')
    answer = '\n'.join(msg.readlines())

    return render(request, 'answer.html', {'answer': answer})
