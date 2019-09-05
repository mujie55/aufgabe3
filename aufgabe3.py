password = 'a123456'
n = 3
while n > 0:
	n = n - 1
	pwd = input('请输入密码:')
	if pwd == password:
		print('登录成功！')
		break
	else:
		print('密码错误! ')
		if n > 0:
			print('还有', n, '次机会')
		else:
			print('没有机会了 账号已锁')