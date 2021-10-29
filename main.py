import sys
import re
from HashST import HashST
from PIF import PIF
from utils import reservedWords, reservedOperatorsSeparators, is_constant, is_identifier


class Scanner:
    pif = PIF()
    st = HashST()

    def __init__(self):
        if len(sys.argv) != 2:
            raise Exception("analyze <input_file_name>")
        else:
            output = open(sys.argv[1][:-3] + ".out", "w")
            try:
                with open(sys.argv[1]) as f:
                    line_number = 1
                    line = f.readline()
                    while line:
                        print(line)
                        split = re.split('([^A-Za-z_0-9.,=<>-])', line)
                        split = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), split)))
                        buffer = ""

                        for token in split:
                            if token == "\'":
                                if buffer == "":
                                    buffer += token
                                    continue
                                else:
                                    buffer += token
                                    token = buffer
                                    buffer = ""
                            elif buffer != "":
                                buffer += token
                                continue

                            if token in reservedWords:
                                self.pif.add(reservedWords.index(token), None)
                            elif token in reservedOperatorsSeparators:
                                self.pif.add(reservedOperatorsSeparators.index(token) + 100, None)
                            elif is_identifier(token):
                                self.st.add(token)
                                self.pif.add('ID', self.st[token])
                            elif is_constant(token):
                                bla = is_constant(token)
                                self.st.add(token)
                                self.pif.add(bla, self.st[token])
                            else:
                                raise Exception(
                                    "Lexical error. Invalid token: '{}' on line {}".format(token, line_number))
                        if buffer != "":
                            raise Exception(
                                "Lexical error. Unclosed string: '{}' ".format(buffer))
                        line = f.readline()
                        line_number += 1

                    output.write(str(self.pif))
                    output.write("\n")
                    output.write(str(self.st))
            except Exception as e:
                output.write(str(e))


scanner = Scanner()
