#!/bin/bash/env python

'''
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''
def main():
    str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    terms = str1.split(" ")
    for term in terms:
        print(len(term.rstrip(",.")))

if __name__ == "__main__":
    main()