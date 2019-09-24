# testfilter
unittest 用例执行过滤， 可选择用例级别或用例级别进行过滤

### 如何使用它?

```shell
>>> pip install testfilter
```


```python

import unittest
from testfilter import runIf, Filter

# 设置执行环境 执行级别
Filter.env = 'test'
Filter.level = 'p2'


class Demo(unittest.TestCase, metaclass=Filter.Meta):
    @runIf.env.NOT_PROD  # 非正式环境下执行
    def test_001(self):
        self.assertEqual(1, 1)

    @runIf.env.TEST  # 仅在测试环境下执行
    def test_002(self):
        self.assertEqual(1, 1)

    @runIf.env.UAT
    @runIf.env.TEST
    @runIf.level_in.P3   # 测试环境和 UAT 环境下，且用例级别在 P3 以上执行
    def test_003(self):
        self.assertEqual(1, 1)

    @runIf.level_in.SMOKE
    def test_004(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':

    unittest.main()

```
![image](http://mocobk.test.upcdn.net/image/2019-04-14-112321.jpg)

### 用例环境

| Tag |  英文 | 中文 |
|:----|:------|:-----|
|TEST|Testing|测试|
|UAT|User Acceptance Test|用户验收测试|
|PROD|Production|正式/生产|


### 用例级别
**Level:** 

|SMOKE/P1|P2|P3|P4|
|----|----|----|-----|

[用例级别参考](https://www.jianshu.com/p/4903856cd6c5)

