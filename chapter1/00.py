#!/bin/bash/env python
# coding: UTF-8
'''
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''

def main():
    target_str = "stressed"
    tmp_list = [s for s in target_str][::-1]
    answer = "".join(tmp_list)
    print (answer)

if __name__ == "__main__":
    main()
