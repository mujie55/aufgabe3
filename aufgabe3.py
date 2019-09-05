n = 1
while n <= 3:
	password = input('请输入密码:')
	if password == 'a123456':
		print('登录成功！')
		break
	else:
		print('密码错误！ 还有', 3-n, '次机会')
		n = n + 1