'''
@ created : 2023.2.12
@ author : Jenna
@ description : 배열 및 문자열 관련 문제
'''
def first_qna():
    # -1 1 3 -2 2
    # -1 -2 1 3 2
    num = input()
    n_list = num.split(" ")
    n_list = [int(x) for x in n_list]
    print(f"입력 : {n_list}")
    minus_list = []
    plus_list = []
    result = []
    for i,item in enumerate(n_list):
        if item > 0 :
            plus_list.append(item)
        else :
            minus_list.append(item)
    result.append(minus_list)
    result.append(plus_list)
    result = sum(result, [])
    print(f"결과 : {result}")


def second_qna():
    name_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
    name_list = name_str.split(",")
    # name_list = ["이유덕", "이재영", "권종표", "이재영", "박민호", "강상희", "이재영", "김지완", "최승혁", "이성연", "박영서", "박민호", "전경헌", "송정환", "김재성", "이유덕", "전경헌"]
    # (1) 김씨와 이씨는 각각 몇 명?
    kim_list = [x for x in name_list if "김" in x]
    lee_list = [x for x in name_list if "이" in x]
    print(f"김씨는 {len(kim_list)}명, 이씨는 {len(lee_list)}명입니다.")
    print("="*30)
    # (2) "이재영"이란 이름이 몇 번 반복되나?
    cnt_ljy = [x for x in name_list if x == "이재영"]
    print(f"이재영은 {len(cnt_ljy)}번 반복됩니다.")
    print("="*30)
    # (3) 중복을 제거한 이름 출력
    uniq_name = list(set(name_list))
    print(f"중복 제거 결과 : {uniq_name} \n => 총 {len(uniq_name)}명")
    print("="*30)
    # (4) 중복을 제거한 이름을 오름차순으로 정렬하여 출력
    print(f"중복 제거 및 오름차순 정렬 결과 : {sorted(uniq_name)}")
    

if __name__ == "__main__":
    print("1번 문제")
    first_qna()
    print("="*30)
    print("2번 문제")
    second_qna()