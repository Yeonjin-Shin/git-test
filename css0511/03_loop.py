"""
상자안에 물건을 전부 까서
사과는 냉장실에
아이스크림은 냉동실에 넣어 주시고,
나머지는 폐기처분 해주세요.
"""

상자 = ["사과", "아이스크림", "콩", "콩", "아이스크림"]

for 물건 in 상자:
    if 물건 == "사과":
        print(f"'{물건}' 냉장실에 넣기")
    elif 물건 == "아이스크림":
        print(f"'{물건}' 냉동실에 넣기")
    else:
        print(f"'{물건}' 폐기처분")


#f-string
#문자와 변수를 혼재해서 문자열로 바꾸고 싶을 떄!