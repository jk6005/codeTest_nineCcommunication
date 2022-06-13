import csv
import json
import os

if __name__ == '__main__':
    '''
        순수 Python 으로 백엔드 과제 구현
        
        파이썬 인터 프리터 버전 : python 3.9
        작업 IDE : IntelliJ PHPStorm
        
        구현일 : 2022-06-13
        작성자 : 이태영
        Git : jk6005, eae8633@naver.com
    '''
    # 경로 설정
    CSV_PATH = 'data/top20.csv'
    JSON_DIR = 'result/'

    # csv 파일 불러오기
    with open(CSV_PATH, 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        # csv 파일 읽기 및 json 변환
        json_data_list = []
        for line in reader:
            # Id 가 str 이기 떄문에 int 로 변경
            line['id'] = int(line['id'])
            json_data_list.append(line)
        json.dumps(json_data_list)

    # 경로 유효성 검사 없으면 경로 생성
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)
    # JSON 으로 저장
    with open(JSON_DIR + 'top20.json', encoding='utf-8', mode='w') as json_file:
        json_file.write(json.dumps(json_data_list, ensure_ascii=False, indent=2))

    # 저장된 JSON 경로 검사 및 불러오기
    if os.path.exists(JSON_DIR + 'top20.json'):
        with open(JSON_DIR + 'top20.json', encoding='utf-8', mode='r') as json_file:
            new_json_data_list = json.load(json_file)
            # 만 출력
            for line in new_json_data_list:
                print(line['licenseOrgan'])
    else:
        print('※ 경고 - {} 을(를) 찾을 수 없습니다.'.format(JSON_DIR + 'top20.json'))
