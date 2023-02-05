'''
@ created : 2023.2.2
@ author : Jenna
@ description : 컴퓨터와 대결하는 업앤다운 게임
'''
import random


def main():
    print(" ==== 업앤다운 게임 시작 ==== ")
    print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.\n이 숫자를 맞춰주세요.")
    # 정답 랜덤숫자
    answer = random.randrange(1, 101)
    # n번째 입력
    cnt = 0
    # 계속 진행
    go = True
    while go:
        user_num = int(input("1~100 숫자 입력:"))
        cnt += 1
        if user_num < answer:
            print("UP!!")
        elif user_num > answer:
            print("DOWN!")
        else:
            go = False
            print(f"정답입니다! {cnt}회 만에 맞췄어요.")


if __name__ == "__main__":
    main()
