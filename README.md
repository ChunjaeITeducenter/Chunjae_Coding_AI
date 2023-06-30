## Chunjae Python code AI
---
* 파이썬 코드의 실행 정보와 질의응답 서비스를 제공하는 웹앱

* License info.
    * Django(www.djangoproject.com/ BSD-3)
    * OnlinePythonTutor(https://github.com/hcientist/OnlinePythonTutor, GPL v3, Copyright (C) 2010 Philip J. Guo (philip@pgbovine.net))
    * flake8(https://pypi.org/project/flake8/, MIT)
    * koreapas-finetuned-korwikitq(https://huggingface.co/dsba-lab/koreapas-finetuned-korwikitq, TAPAS based(https://github.com/google-research/tapas), Apache-2.0 license)


* 사용법 `python manage.py runserver`
* 실행 후 localhost:8000 으로 접속해 이용

* 기능
    1. 파이썬 코드 리뷰: 파이썬 코드를 입력한 경우, 아래 두 가지 시나리오에 따라 지정된 값을 리턴한다
        * 올바른 파이썬 코드: PythonTutor API를 이용해 실행 결과를 시각적으로 보여준다
        * 잘못된 파이썬 코드: flake8을 이용한 linting 후 에러 코드에 따라 확보된 데이터 테이블을 검색한다
    1. 파이썬 질의응답: 자연어 질문에 대해 확보된 데이터 테이블을 검색해 답변한다

* 이용 라이브러리 및 버전: requirements.txt 참조
    * Model pipeline: HuggingFace Transformers
    * Code linting: flake8
    * Table Question Answering model: koreapas-finetuned-korwikitq(https://huggingface.co/dsba-lab/koreapas-finetuned-korwikitq)