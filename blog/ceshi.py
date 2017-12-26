from django.test import TestCase

# Create your tests here.


# 可变数据类型  [] {}
# 不可变数据类型 数字 字符串  元组

# s="hello".upper()
# print(s)


# l=[1,2,3]
#
# c=[4,5]
#
# l.append(c)
# c.append(7)
#
# print(c)  #
# print(l)




# d1={"name":"yuan"}
# d2={"age":12}
# d1["xxx"]=d2
#
# d2["height"]="180cm"
#
# print(d1)   # {"name":"yuan","xxx":{"age":12,"height":"180cm"}}




# d1={1:{"xxx":[12,34]},2:{"xxx":[34,56]}}
# d2={"xxx":[777,888,999]}
# d3={"xxx":[11,8238,99]}
# d1[2]["xxx"].append(d2["xxx"])
# d2["xxx"].append(d3["xxx"])
#
# print(d1)   #  {1:{"xxx":[12,34]},2:{"xxx":[34,56,[777,888,999,[11,8238,99]]]}}
# print(d2)   #  {"xxx":[777,888,999,[11,8238,99]]}
# print(d3)   #  d3={"xxx":[11,8238,99]}




# =========================================================================

comment_list = [

    {"id": 1, "content": "...", "Pid": None},
    {"id": 2, "content": "...", "Pid": None},
    {"id": 3, "content": "...", "Pid": None},
    {"id": 4, "content": "...", "Pid": 1},
    {"id": 5, "content": "...", "Pid": 1},
    {"id": 6, "content": "...", "Pid": 4},
    {"id": 7, "content": "...", "Pid": 3},
    {"id": 8, "content": "...", "Pid": 7},
    {"id": 9, "content": "...", "Pid": None},

]

for comment in comment_list:
    comment["chidren_commentList"] = []

# print(comment_list)

'''
[
  {'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}, 
  {'id': 2, 'content': '...', 'Pid': None, 'chidren_commentList': []},
  {'id': 3, 'content': '...', 'Pid': None, 'chidren_commentList': []},
  {'id': 4, 'content': '...', 'Pid': 3, 'chidren_commentList': []}, 
  {'id': 5, 'content': '...', 'Pid': 1, 'chidren_commentList': []}, 
  {'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []}, 
  {'id': 7, 'content': '...', 'Pid': 3, 'chidren_commentList': []},
  {'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}, 
  {'id': 9, 'content': '...', 'Pid': None, 'chidren_commentList': []}

 ]


{
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"2":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"3":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
"1":{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': []}
}

'''
for comment in comment_list:
    comment["chidren_commentList"] = []
comment_tree=[]
for comment in comment_list:
    if comment["Pid"]:
        pid = comment["Pid"]
        # print(comment)
        for i in comment_list:
            if i["id"] == pid:
                i["chidren_commentList"].append(comment)
    else:
        comment_tree.append(comment)
print(comment_tree)

# print(comment_list)
# for item in comment_list:
#     if not item['Pid']:
#         print(item)

'''
[{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': 
    [{'id': 4, 'content': '...', 'Pid': 1, 'chidren_commentList': 
        [{'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []}]},
    {'id': 5, 'content': '...', 'Pid': 1, 'chidren_commentList': []}]}, 
 {'id': 2, 'content': '...', 'Pid': None, 'chidren_commentList': []}, 
 {'id': 3, 'content': '...', 'Pid': None, 'chidren_commentList': 
    [{'id': 7, 'content': '...', 'Pid': 3, 'chidren_commentList': 
        [{'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}]}]}, 
{'id': 9, 'content': '...', 'Pid': None, 'chidren_commentList': []}]

'''

'''

{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': 
    [{'id': 4, 'content': '...', 'Pid': 1, 'chidren_commentList': 
        [{'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []}]},
    {'id': 5, 'content': '...', 'Pid': 1, 'chidren_commentList': []}]}
{'id': 2, 'content': '...', 'Pid': None, 'chidren_commentList': []}
{'id': 3, 'content': '...', 'Pid': None, 'chidren_commentList': 
    [{'id': 7, 'content': '...', 'Pid': 3, 'chidren_commentList': 
        [{'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}]}]}
{'id': 9, 'content': '...', 'Pid': None, 'chidren_commentList': []}

'''
'''
[
{'id': 1, 'content': '...', 'Pid': None, 'chidren_commentList': [{'id': 4, 'content': '...', 'Pid': 1, 'chidren_commentList': [{'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []}]},
{'id': 5, 'content': '...', 'Pid': 1, 'chidren_commentList': []}]},
{'id': 2, 'content': '...', 'Pid': None, 'chidren_commentList': []}, 
{'id': 3, 'content': '...', 'Pid': None, 'chidren_commentList': [{'id': 7, 'content': '...', 'Pid': 3, 'chidren_commentList': [{'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}]}]}, 
{'id': 4, 'content': '...', 'Pid': 1, 'chidren_commentList': [{'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []}]}, {'id': 5, 'content': '...', 'Pid': 1, 'chidren_commentList': []}, 
{'id': 6, 'content': '...', 'Pid': 4, 'chidren_commentList': []},
{'id': 7, 'content': '...', 'Pid': 3, 'chidren_commentList': [{'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}]}, 
{'id': 8, 'content': '...', 'Pid': 7, 'chidren_commentList': []}, 
{'id': 9, 'content': '...', 'Pid': None, 'chidren_commentList': []}]

'''



