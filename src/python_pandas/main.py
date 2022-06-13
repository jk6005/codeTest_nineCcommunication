import pandas as pd
import json
import os

if __name__ == '__main__':
    '''
        Python Pandas 를 사용힌 백엔드 과제 구현

        파이썬 인터 프리터 버전 : python 3.9
        작업 IDE : IntelliJ PHPStorm

        구현일 : 2022-06-13
        작성자 : 이태영
        Git : jk6005, eae8633@naver.com
    '''
    CSV_PATH = 'data/top20.csv'
    JSON_DIR = 'result/'

    top_20_df = pd.read_csv(CSV_PATH)
    # 경로 유효성 검사 없으면 경로 생성
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)
    # df -> json 바로 저장
    top_20_df.to_json(path_or_buf=JSON_DIR + 'top20.json', orient='records', force_ascii=False, indent=2)

    # 저장된 JSON 경로 검사 및 불러오기
    if os.path.exists(JSON_DIR + 'top20.json'):
        with open(JSON_DIR + 'top20.json', encoding='utf-8', mode='r') as json_file:
            new_json_data_list = json.load(json_file)
            # 만 출력
            for line in new_json_data_list:
                print(line['licenseOrgan'])
    else:
        print('※ 경고 - {} 을(를) 찾을 수 없습니다.'.format(JSON_DIR + 'top20.json'))
