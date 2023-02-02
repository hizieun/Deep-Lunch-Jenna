'''
@ created : 2023.1.31
@ author : Jenna
@ description : 컴퓨터와 대결하는 배스킨라빈스31 게임
'''
import random
'''
TODO
# 31을 외치게 되면 바로 끝내고 승자 결정되는것으로
# 입력 잘못했을때 다시 입력할수있도록
# 사용자 시작, 컴퓨터 시작 제대로 되는지 확인
'''


# 컴퓨터,사용자 나누지 않고 하나의 함수에서 처리
def call_number(round, last_num, first):
    # 컴퓨터면 랜덤으로 값 생성, 사용자면 입력개수 입력받기
    odd = "사용자" if (round % 2 == first) else "컴퓨터"
    print(f"{odd} 차례입니다.")

    if odd == "사용자":
        cnt_num = int(input("입력할 숫자의 개수를 입력하세요(범위 : 1~3): "))
        for num, idx in enumerate(range(cnt_num)):
            num = int(input("숫자를 입력하세요: "))
            if idx == cnt_num - 1:
                fin_num = num
    else:
        cnt_num = random.randrange(1, 4)
        for num, idx in enumerate(range(cnt_num)):
            print(f"숫자를 입력하세요: {last_num + (idx+1)}")
            if idx == cnt_num - 1:
                fin_num = num
    return fin_num


def main():
    print("=" * 5 + " Baskin 31 Game " + "=" * 5)
    # 최종 숫자
    fin_num = 31
    # 누가 먼저 공격할지 정하기
    first = int(input("올바른 숫자를 입력하세요.\n(0. 사용자 선공격, 1. 컴퓨터 선공격): "))

    # first가 0이면 사용자가 round이 홀수번째마다, 1이면 컴퓨터가 round이 홀수번째마다 진행
    # 이외의 숫자를 입력하면 assert 에러 발생시키기
    # assert first == 0 | first == 1, "0 또는 1을 입력"
    # 끝?
    isFinished = True
    # 몇회차?
    round = 0
    # 마지막으로 부른 숫자만 저장
    last_num = 0
    while isFinished:
        print(f"===== {round+1}번째 =====")
        # 공격
        last_num = call_number(round, last_num, first)
        # 횟수 증가
        round += 1
        # 마지막 체크
        if last_num == fin_num:
            isFinished = False
    print("=" * 20)
    print(f"승자 : {round}")  # TODO 바꿔야함
    print(f"{round} 회차에 끝났습니다.")
    return


if __name__ == "__main__":
    main()
