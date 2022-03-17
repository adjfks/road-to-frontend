"""
问题描述
　　Tom教授正在给研究生讲授一门关于基因的课程，有一件事情让他颇为头疼：一条染色体上有成千上万个碱基对，它们从0开始编号，到几百万，几千万，甚至上亿。
　　比如说，在对学生讲解第1234567009号位置上的碱基时，光看着数字是很难准确的念出来的。
　　所以，他迫切地需要一个系统，然后当他输入12 3456 7009时，会给出相应的念法：
　　十二亿三千四百五十六万七千零九
　　用汉语拼音表示为
　　shi er yi san qian si bai wu shi liu wan qi qian ling jiu
　　这样他只需要照着念就可以了。
　　你的任务是帮他设计这样一个系统：给定一个阿拉伯数字串，你帮他按照中文读写的规范转为汉语拼音字串，相邻的两个音节用一个空格符格开。
　　注意必须严格按照规范，比如说“10010”读作“yi wan ling yi shi”而不是“yi wan ling shi”，“100000”读作“shi wan”而不是“yi shi wan”，“2000”读作“er qian”而不是“liang qian”。
输入格式
　　有一个数字串，数值大小不超过2,000,000,000。
输出格式
　　是一个由小写英文字母，逗号和空格组成的字符串，表示该数的英文读法。
样例输入
1234567009
样例输出
shi er yi san qian si bai wu shi liu wan qi qian ling jiu
 """
num = list(map(int, input()))
wei = {1: 'shi', 2: 'bai', 3: 'qian', 4: 'wan',
       5: 'shi', 6: 'bai', 7: 'qian', 8: 'yi', 9: 'shi'}
yin = {1: 'yi', 2: 'er', 3: 'san', 4: 'si',
       5: 'wu', 6: 'liu', 7: 'qi', 8: 'ba', 9: 'jiu'}
res = []
for i in range(len(num)):
    # 中间连0的最后一个0发音
    if num[i] == 0 and i < len(num) - 1:
        if num[i+1] != 0:
            res.append('ling')
        continue
    # 获取当前数字的位
    w = len(num) - 1 - i
    if num[i] == 1 and (w == 5 or w == 9):
        res.append('shi')
    else:
        if num[i] in yin:
            res.append(yin[num[i]])
        if w in wei:
            res.append(wei[w])

print(" ".join(res))
