list1 = ["turkey","shanghai","paris","miami"]
print("原始数据---------------")
print(list1)
print("不修改正序排列---------")
print(sorted(list1))
print("数据没变---------------")
print(list1)
print("不修改倒序排列---------")
print(sorted(list1,reverse = True))
print("数据没变---------------")
print(list1)
print("反转列表---------------")
list1.reverse()
print(list1)
print("再次反转---------------")
list1.reverse()
print(list1)
print("用sort修改列表---------")
list1.sort()
print(list1)
print("用sort倒序修改列表-----")
list1.sort(reverse = True)
print(list1)
