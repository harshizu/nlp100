#!/bin/bash/env python

'''
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
'''
def main():
    target_str = "パタトクカシーー"
    tmp_list = [s for s in target_str]
    answer = tmp_list[0] + tmp_list[2] + tmp_list[4] + tmp_list[6]
    print (answer)

if __name__ == "__main__":
    main()
