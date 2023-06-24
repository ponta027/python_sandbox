# README

## 目的

構文解析を簡易的に実装してみようと思い、ツールを探していた。
ANTLRなどがあることを知っていたが、Pythonで簡易的に作れるツールがないか
探していた。
Larkというパッケージがあるらしいので、簡単なサンプルを作って見る。

## install 

以下コマンドで必要なパッケージをインストール

<!-- -->
```
pip install  -r requirement.txt
```
<!-- -->


## 実装方法

実行するときに以下を用意する。

* grammar
    * EBNFによる構造定義
* Transformer
    * データ変換時に使用するクラス
* 解析文字列


以下簡易サンプル。

<!-- -->
```python
from lark import Lark

l = Lark('''start: WORD "," WORD "!"

            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
         ''')

print( l.parse("Hello, World!") )
```
<!-- -->


これだけだとあまりおもしろくないので、
[State Machine Compilerで定義されているEBNF](https://smc.sourceforge.net/SmcManAppendixA.htm)
をlarkで動かしてみる。

1. :=を : に変換
1. ' を " に変換
1. | の位置を変更
1. import , ignoreを追加する
1. word,raw_code_line,raw_codeを変更


これだけだとTransision Argumentが足りていないので、解析エラーが発生する。
今後修正を行っていく予定。



## reference

### Lark 

* [lark Document](https://lark-parser.readthedocs.io/en/latest/)
* [lark IDE](https://www.lark-parser.org/ide/)
* [CheatSheet](https://github.com/lark-parser/lark/blob/master/docs/_static/lark_cheatsheet.pdf)

### State Machine Compiler

https://smc.sourceforge.net/SmcManual.htm


