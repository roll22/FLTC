import sys
import re
from HashST import HashST
from PIF import PIF


class Scanner:
    pif = PIF()
    st = HashST()

    def __init__(self):
        if len(sys.argv) != 2:
            raise Exception("analyze <input_file_name>")
        else:
            output = open(sys.argv[1][:-2] + ".out", "w")
            try:
                with open(sys.argv[1]) as f:
                    line_number = 1
                    line = f.readline()
                    while line:
                        print(line)
                        split = re.split('([^A-Za-z_0-9&.,|-])', line)
                        split = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), split)))
                        print(split)
                        buffer = ""

                        for token in split:
                            if token == '"':
                                if buffer == "":
                                    buffer += token + " "
                                else:
                                    token = buffer[2:]
                                    buffer = ""
                            elif buffer != "":
                                buffer += token + " "
                                continue

                            if token in reservedWords or token in operatorsSeparators:
                                self.pif[token] = -1
                            elif is_identifier(token):
                                index = self.st.add(token)
                                self.pif[token] = index
                            else:
                                raise Exception(
                                    "Lexical error. Invalid token: '{}' on line {}".format(token, line_number))
                        line = f.readline()
                        line_number += 1

                    output.write(str(self.pif))
                    output.write("\n")
                    output.write(str(self.st))
            except Exception as e:
                output.write(str(e))


scanner = Scanner()
