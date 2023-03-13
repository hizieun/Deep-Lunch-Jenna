import os
import cv2
import argparse

def main(args):
    # 이미지 불러오기
    img = cv2.imread(args.img_path) # 원본
    smile = cv2.imread(args.img_path.replace("jieun.jpg", "smile.png")) # 스마일
    # 이미지 흑백 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 이미지 크기 조정
    resized_img = cv2.resize(gray_img, (100, 100))
    # TODO : 이미지에 스마일 부착
    cv2.copyTo()
    # 결과 저장
    res_img = cv2.imwrite(args.img_path.replace("jieun.jpg", "result.jpg"), resized_img)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='이미지를 활용한 OpenCV 실습')
    parser.add_argument("--img_path", type=str,
                        default='./img/jieun.jpg', help='테이블 셀별 이미지 폴더 경로')
    args = parser.parse_args()
    main(args)