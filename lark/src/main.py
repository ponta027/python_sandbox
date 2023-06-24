#!/usr/bin/env python3


from lark import Lark
from transformer.sm_transformer import SMTransformer


def main(grammar_file ,model_file ):
    with open( grammar_file ) as f:
        grammar =  f.read()
        parser = Lark(grammar, parser='lalr' , transformer=SMTransformer())

        text = open( model_file ).read()
        print(parser.parse(text).pretty())

#        print(parser.parse(text))

if __name__ == '__main__':
    grammar_file = "grammer/sm_grammar.lark"
    model_file = "models/sample.sm"
    main(grammar_file,model_file)
