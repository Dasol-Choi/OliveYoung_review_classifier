# !pip install kss
# !pip install emoji==1.2.0

import time, re
import pandas as pd
import emoji
from kss import split_sentences 
import warnings
warnings.filterwarnings(action='ignore') 

def remove_multispaces(input_str) :
    len_prev = len(input_str)
    
    while True :
        input_str = re.sub('[ ]+', ' ', input_str)
        len_cur = len(input_str)

        if len_prev >= len_cur :
            break
        else :
            len_prev = len_cur
    
    return input_str.strip()

def remove_emoji(input_str):
    input_str = emoji.get_emoji_regexp().sub(u'', input_str)
    return remove_multispaces(input_str)

def remove_chars(input_str, pattern): 
    input_str = re.sub(pattern, '', input_str)
    return remove_multispaces(input_str)

def replace_chars(input_str, pattern, replace_str):
    input_str = re.sub(pattern, replace_str, input_str)
    return remove_multispaces(input_str)

def remove_bracket_edge(input_str) :
    if len(input_str) >= 2 :
        if input_str[0] =='(' and input_str[-1] ==')':
            input_str = input_str[1:-1]
    return input_str.strip()


patterns = [':-\)', '\([^)]*\)', '\[[^)]*\]', '\<[^)]*\>','[^:]*:',
           '.\)', '[0-9]+[\. ]', ':D', ':\(', '[,.]*',
            '[!_ㅠㅜㅎㅋ^\[\]<>\'\"“‘;★☆♤♡♥※♧♣♤♠■□◇◆◈▣△▲▽▼◁◀▷▶○●⊙◐◑◎]*']

def remove_patterns(sent) :
    for pattern in patterns :
        sent = remove_chars(sent, pattern)
    
    return sent        


start_words = ["BUT", "그런데", "그런대", "그리고", "근데", "근대", "그래도", "그런만큼", "그래서", "구래서", "그렇다고",
               "그리구", "글고", "그치만", "그러다가", "그러고", "그렇지만", "그랬더니", "그러데", "아니면", "그런지", "일단"
               "그만큼", "그러나", "때문에", "앞에 언급했던것 것처럼", "그래두", "즉,", "되려", "덧붙여", "더불어", "이것도",
               "그러니", "그러다", "그것빼곤", "그러고", "그래가지고", "그렇다보니", "그렇다 보니", "그럼에도", "그러므로", 
               "따라서", "그런 점에서", "그러면", "그러니까", "그래서인지", "그만큼", "다만", "대신", "결론은", "대신에", "인지 ",
               "암튼간에", "아무튼", "암튼", "여튼", "무튼", "하지만", "오히려", "물론", "게다가", "또 ", "특히", "이게", "이번에",
               "특히나", "이래서", "단 ", "단," "우선", "이 외에도", "뭐근데", "그러다가", "덕분에", "그 덕에", "결국은",  
               "결국", "결론적으로", "결과적으로", "참고로", "심지어", "왜냐하면",  "이외에도", "반대로","더구나", "반면에", 
               "즉 ", "마지막으로", "혹은", "아무쪼록", "일단", "일단은"," 거기에" "먼저", "어쨌든", "쨌든", "어쨋든", "쨋든", 
               "또는", "앞서 말했듯이", "더더군다나", "거기다", "거기다가", "그것 외에는", "그밖에는", "그 밖에는", "참고로", 
               "왜냐", "그에 반해", "그 외엔", "그외엔", "그외에", "그 외에", "지금처럼", "대신에", "더불어", "오히려",  "물론", 
               "다만", "오우", "아 ", "오 ", "와 ", "헐 ", "어 ", "음 ", "으음", "옹 ", "->", "→", "☆", "\+", "@", "#", 
               "•", "\)", "\ㅣ","✓", "0", "○", "\.", "," "=" , "=>", "&", "/", "➡", "➤", "⇨", "☞", " ☛", ":", "-", "~", 
               "#", "\*", "•", "…"]

def remove_start_words(sent) :
    for start_word in start_words :
        len_prev = len(sent)
        
        while True :
            sent = re.sub(pattern=f'^{start_word}', repl='', string=sent).strip()
            len_cur = len(sent)
            
            if len_prev >= len_cur :
                break
            else :
                len_prev = len_cur
    
    return sent.strip()


def preprocessing(review) :
    result = []
    
    # 하나의 문장으로 연결되어 있는 리뷰 전체를 문장 분할
    sents = split_sentences(review)
    
    # 문장 분할 후, 문장 단위로 텍스트 전처리 수행
    for idx, sent in enumerate(sents) :
        sent = remove_emoji(sent) # 이모지 제거
        sent = remove_bracket_edge(sent) # 문장 전체가 괄호라면, 괄호 기호만 삭제
        sent = remove_patterns(sent) # 정규 표현식 패턴을 이용한 일괄 제거
        sent = remove_start_words(sent) # 시작 불용어 제거 x 3 
        sent = remove_start_words(sent) 
        sent = remove_start_words(sent) 
        sent = replace_chars(sent, '&', ', ')
        
        if len(sent) > 4 :
            result.append(sent)
    return result


def reviews_prepro(reviews_list):  # 리뷰 리스트에 대한 최종 전처리 함수
    sents_all = []
    for review in reviews_list :
        review = review.strip()
        if len(review) == 0 :
            continue

        sents = preprocessing(review)
        sents_all.extend(sents)

    return list(set(sents_all))