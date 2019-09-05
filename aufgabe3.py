password = 'a123456'
n = 1
while n <= 3:
	pwd = input('请输入密码:')
	if pwd == password:
		print('登录成功！')
		break
	else:
		print('密码错误！ 还有', 3-n, '次机会')
		n = n + 1