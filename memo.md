<!-- インタラクティブでの処理 -->

# 文頭・文末一致の判定方法

```
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```

# 単語をつなげるときにメゾットと単語を切るときのメゾット

```
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

```
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container
in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not
drink it.', 'Sincerely,', 'Bob']
```

1. import re で正規表現モジュールをインポートする。
2. re.compile()関数を呼び出し Regex オブジェクトを生成する（raw 文字列を使
   う）。
3. Regex オブジェクトの search()メソッドに、検索対象の文字列を渡すと、
   Match オブジェクトを返す。
4. Match オブジェクトの group()メソッドを呼び出し、実際にマッチした文字列を
   取得する。

