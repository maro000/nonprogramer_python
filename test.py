def What_your_name():
  print('名前を入れてください')
  name = input()
  print('パスワードを入れてください')
  password =input()
  if name == "Mary":
    print('Marysさん、こんにちわ。')
    if password == 'swordfish':
      print('success')
    else:
      print('false')