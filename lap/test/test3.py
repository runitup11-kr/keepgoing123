num = []
while True:
    menu = input("\n1: 추가 2: 조회 3: 수정 4: 삭제 5: 종료\n작업 선택:")
    if menu == "1":
        num.append(input("추가할 값: "))
        print("추가완료")
        
    elif menu == "2":
        print("\n[현재 리스트 내용]")
        for i,value in enumerate(num):
            print(f"{i}: {value}")
            
    elif menu == "3":
        index = int(input("수정할 인덱스 입력: "))
        if 0 <= index < len(num):
            new_num = input("새로운 값 입력: ")
            new_num = int(new_num)
            num[index] = new_num
            print("수정완료")
            
    elif menu == "4":
        index1 = int(input("삭제할 인덱스 입력: "))
        if 0 <= index1 < len(num):
           num.pop(index1)
           print("삭제 완료")
        else:
            print("유효하지 않은 값입니다 ")
    elif menu == "5":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력")