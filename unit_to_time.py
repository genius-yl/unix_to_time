import time
import datetime
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def unix_to_datetime():
    while True:
        # 1. 터미널 출력을 깔끔하게 유지하기 위해서 clear_screen() 함수도 추가해주었다.
        clear_screen()
        print("============================")
        print("  유닉스 시간 변환기  ")
        print("============================")
        # 2. 'exit'를 입력하면 프로그램이 종료된다.
        try:
        # 3. 주 간단하게 변환할 유닉스 시간 값을 input으로 입력받고, 이를 datetime.datetime.fromtimestamp(unix_time)를 통해서 유닉스 시간을 시간으로 변환할 수 있도록 구현했다.
            unix_time = input("\n변환할 유닉스 시간 (초 단위, 'exit' 입력 시 종료): ")
            if unix_time.lower() == 'exit':
                break
            
            unix_time = int(unix_time)
            human_time = datetime.datetime.fromtimestamp(unix_time)
        # 4. 엔터키를 누르면 화면이 clear되고 새로운 입력 화면이 뜬다.
            print("\n============================")
            print(f" 변환된 시간: {human_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("============================\n")
            input("엔터 키를 눌러 계속...")
        # 5. 물론 유닉스 시간이 잘못 입력될 시 오류 메세지가 뜨는 예외처리도 진행했다.
        except ValueError:
            print("\n올바른 숫자를 입력하세요.")
            input("엔터 키를 눌러 계속...")
        except OverflowError:
            print("\n입력한 유닉스 시간이 너무 큽니다.")
            input("엔터 키를 눌러 계속...")

if __name__ == "__main__":
    unix_to_datetime()
