#!/bin/bash/env python

'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
def main():
    str1 = "パトカー"
    str2 = "タクシー"

    tmp_list1 = [s for s in str1]
    tmp_list2 = [s for s in str2]
    answer = ""
    for s1, s2 in zip(tmp_list1, tmp_list2):
        answer += s1 + s2
    print (answer)

if __name__ == "__main__":
    main()
