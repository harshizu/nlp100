#!/bin/bash/env python

'''
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''
def main():
    str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    terms = str1.split(" ")
    word_count = 0
    answer = {}
    for term in terms:
        word_count += 1
        term = term.rstrip(",.")
        # 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字
        if word_count in (1, 5, 6, 7, 8, 9, 15, 16, 19):
            answer[term[0]] = word_count
        # それ以外の単語は先頭に2文字
        else:
            answer[term[0:2]] = word_count

    print(answer)

if __name__ == "__main__":
    main()
