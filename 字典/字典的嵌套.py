wangfeng={
    "name":"汪峰",
    "age":18,
    "wife":{
        "name":"章子怡",
        "hobby":"演戏",
        "assistant":{
            "name":"樵夫",
            "age":"19",
            "hobby":"打游戏"
        }
    },
    "children":[
        {"name":"孩子1","age":13},
        {"name": "孩子2", "age":14},
        {"name": "孩子3", "age":15},
    ]
}
#查找
name=wangfeng['wife']['assistant']['name']
print(name)
wangfeng['children'][1]['age']=wangfeng['children'][1]['age']+1
print(wangfeng['children'][1]['age'])