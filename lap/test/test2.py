shopping_list = []

shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("apple")

print("현재 쇼핑 리스트:", shopping_list)

shopping_list.insert(0, "toilet paper")
shopping_list.insert(1, "orange juice")
shopping_list.extend(["chicken , rice"])

print("최종 쇼핑 리스트:",shopping_list)