status_code = int(input("请输入状态码: "))
match status_code:
    case 200 | 300|400 :
        print("请求成功")
    case 404:
        print("请求失败")
    case 500:
        print("服务器错误")
    case _:
        print("未知状态码")