# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com
import unittest
from testfilter import runIf, Filter


# 设置执行环境 执行级别
Filter.env = 'test'  # test uat prod/production 不区分大小写
Filter.level = 'p2'  # smoke/p1 p2 p3 p4 不区分大小写


class Demo(unittest.TestCase, metaclass=Filter.Meta):  # 添加 metaclass 参数
    @runIf.env.NOT_PROD  # 非正式环境下执行
    def test_001(self):
        self.assertEqual(1, 1)

    @runIf.env.TEST  # 仅在测试环境下执行
    def test_002(self):
        self.assertEqual(1, 1)

    @runIf.env.UAT
    @runIf.env.TEST
    @runIf.level_in.P3   # 测试环境和 UAT 环境下，且用例优先级在 P3 以上执行
    def test_003(self):
        self.assertEqual(1, 1)

    @runIf.level_in.SMOKE
    def test_004(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
