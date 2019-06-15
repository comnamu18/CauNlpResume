# CauNlpResume
## CAU Team Project - Resume redesign with NLP
* 팀장 : 임기찬
* 팀원 : 강민수 김상헌 오준오 천영재

## How to Run
* 우분투 환경에서 하단에 기재해놓은 필요한 라이브러리들을 내려받고 `python3 pyqtui.py` 를 실행한다.
* KoNLPy 의 mecab이 Windows에선 지원하지 않아 우분투 환경에서만 실행이 가능하다.

## Enviornment
* OS : Ubuntu 18.04
* Language : Python 3.6
* OpenSource Libraries : [PANDAS](https://github.com/pandas-dev/pandas), [PyQt5](https://github.com/pyqt/python-qt5), [KoNLPy](https://github.com/konlpy/konlpy), [Selenium](https://github.com/SeleniumHQ/selenium), [XlsxWriter](https://github.com/jmcnamara/XlsxWriter)

## Code Details
* `Integraion.py` : KoNlpy와 Resources들을 통합해주는 python script
* `intention.py`  : Verb.csv 를 어근 분석한 output.csv로 변환해주는 python script
* `pyqtui.py`     : UI이자 MAIN부분이 되는 python script
* `dictionary\한국어기초사전\ExtractRelatedWords.py` : 유의어사전에서 필요한 단어들만 추출하는 python script
* `customNlp\mecab.py` : mecab을 이용하여 어근분석을 하는 python script
* `customNlp\otk.py` : otk(트위터) 모델을 이용하여 어근분석을 하는 python script
* `crawling\crawling.py` : 인터넷에서 자소서를 크롤링 해주는 python script

## Resource Folders
* resources : 프로젝트를 위해 전처리한 자료들이 들어간 폴더
* report : 발표자료를 모아둔 폴더
* corpus : 크롤링한 자소서 자료를 모아둔 폴더

## Refference
* [KoNLPy 설치] (https://yuddomack.tistory.com/entry/%EC%B2%98%EC%9D%8C%EB%B6%80%ED%84%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-EC2-konlpy-mecab-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0ubuntu)
* [Mecab 등 성능 비교] (https://iostream.tistory.com/144)
* [PyQt5] (https://shaun289.github.io/blog/2018/08/13/pyqt_on_wsl.html)
