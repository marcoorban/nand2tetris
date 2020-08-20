class Tokenizer():

    symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '_', '~']
    keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']

    def __init__(self, input_file):
        self.current_file = input_file
        self.tokens = self.get_tokens(self.remove_comments(input_file))
        self.current_token = ''
        self.idx = -1
        
    def hasMoreTokens(self):
        while self.idx + 1 < len(self.tokens):
            return True

    def advance(self):
        self.idx += 1
        self.current_token  = self.tokens[self.idx]

    def remove_comments(self, input_file):
        token_string = ''
        with open(input_file, 'r') as f:
            multiline_comment = False
            lines = f.readlines()
            for line in lines:
                if multiline_comment == True:
                    if '*/' in line:
                        line = line.split('*/')[-1]
                        multiline_comment = False
                    else:
                        continue

                if '//' in line:
                    line = line.split('//')[0]
                elif '/**' and '*/' in line:
                    line = line.split('/**')[1].split('*/')[-1]
                elif '/**' in line:
                    multiline_comment = True
                    continue
                    
                line = line.strip()
                if line == '':
                    continue
                else:
                    token_string += ' ' + line

        return token_string.strip()

    def get_tokens(self, token_string):
        tokens_list = []
        is_string = False
        token = ""
        for char in token_string:
            if not is_string:
                if char != " " and char !='"' and char not in Tokenizer.symbols:
                    token += char
                elif char == " ":
                    if len(token) > 0:
                        tokens_list.append(token)
                        token = ""
                elif char in Tokenizer.symbols:
                    # remove the char that was just added and add to the list, but only if its length is greater than one
                    if len(token) > 0:
                        tokens_list.append(token)
                    # also add char to token list
                    tokens_list.append(char)
                    # reset token
                    token = ""
                elif char == '"':
                    token += char
                    is_string = True
            else:
                if char != '"':
                    token += char
                else:
                    token += char
                    tokens_list.append(token)
                    token = ""
                    is_string = False
        return tokens_list

    def tokenType(self):
        if self.current_token in Tokenizer.symbols:
            return "SYMBOL"
        elif self.current_token in Tokenizer.keywords:
            return "KEYWORD"
        elif (self.current_token).isnumeric():
            return "INT_CONST"
        elif self.current_token[0] == '"' and self.current_token[-1] == '"':
            return "STRING_CONST"
        else:
            return "IDENTIFIER"




