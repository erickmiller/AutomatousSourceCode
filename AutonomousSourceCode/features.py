#!/usr/bin/python
# coding: utf8
__author__ = 'Erick Miller for Stanford CS221'

"""

phi(x)
Feature Extractor / Encoder / Decoder for training
the generative models for code sequence learning and
code sequence generation w/ deep recurrent neural networks
also used for decoding the features back after learning

"""

from collections import OrderedDict
import cStringIO, tokenize
from timeout import timeout
import autopep8
import imp
import sys
import re
import os

# note to self: use for <eos> if/when needed for neural MT model: ¶

class Features():

    def __init__(self, code=""):
        """
        Feature vector encoder for purposes of
        sequence based machine learning using a
        variety of deep recurrent neural networks
        """
        self.source_code = ""
        self.encoder_map = {}
        self.decoder_map = {}

        self.encoder_map = {
            'abs':u'Ç',
            'divmod':u'ü',
            'input':u'é',
            'open':u'â',
            'staticmethod':u'ä',
            'all':u'à',
            'enumerate':u'å',
            'int':u'ç',
            'ord':u'ê',
            'str':u'ë',
            'any':u'è',
            'eval':u'ï',
            'isinstance':u'î',
            'pow':u'ì',
            'sum':u'Ä',
            'basestring':u'Å',
            'execfile':u'É',
            'issubclass':u'æ',
            'print':u'Æ',
            'super':u'ô',
            'bin':u'ö',
            'file':u'ò',
            'iter':u'û',
            'property':u'ù',
            'tuple':u'ÿ',
            'bool':u'Ö',
            'filter':u'Ü',
            'len':u'ø',
            'range':u'£',
            'type':u'Ø',
            'bytearray':u'×',
            'float':u'ƒ',
            'list':u'á',
            'raw_input':u'í',
            'unichr':u'ó',
            'callable':u'ú',
            'format':u'ñ',
            'locals':u'Ñ',
            'reduce':u'ª',
            'unicode':u'º',
            'chr':u'¿',
            'frozenset':u'®',
            'long':u'¬',
            'reload':u'½',
            'vars':u'¼',
            'classmethod':u'¡',
            'getattr':u'«',
            'map':u'»',
            'repr':u'░',
            'xrange':u'▒',
            'cmp':u'▓',
            'globals':u'│',
            'max':u'┤',
            'reversed':u'Á',
            'zip':u'Â',
            'compile':u'À',
            'hasattr':u'©',
            'memoryview':u'╣',
            'round':u'║',
            '__import__':u'╗',
            'complex':u'╝',
            'hash':u'¢',
            'min':u'¥',
            'set':u'┐',
            'delattr':u'└',
            'help':u'┴',
            'next':u'┬',
            'setattr':u'├',
            'dict':u'─',
            'hex':u'┼',
            'object':u'ã',
            'slice':u'Ã',
            'dir':u'╚',
            'id':u'╔',
            'oct':u'╩',
            'sorted':u'╦',
            'and':u'╠',
            'as':u'═',
            'assert':u'╬',
            'break':u'¤',
            'class':u'ð',
            'continue':u'Ð',
            'def':u'Ê',
            'del':u'Ë',
            'elif':u'È',
            'else':u'ı',
            'except':u'Í',
            'exec':u'Î',
            'finally':u'Ï',
            'for':u'┘',
            'from':u'┌',
            'global':u'█',
            'if':u'▄',
            'import':u'¦',
            'in':u'Ì',
            'is':u'▀',
            'lambda':u'Ó',
            'not':u'ß',
            'or':u'Ô',
            'pass':u'Ò',
            'raise':u'Õ',
            'return':u'µ',
            'try':u'þ',
            'while':u'Þ',
            'with':u'Ú',
            'yield':u'Û',
            '<=':u'Ù',
            '>=':u'ý',
            '==':u'≡',
            '!=':u'¯',
            '<<':u'±',
            '>>':u'‗',
        }

        for key in self.encoder_map.keys():
            self.decoder_map[ self.encoder_map[key].encode( 'utf8', 'replace' ) ] = key

        if len(code) > 1:
            if os.path.exists(code) and os.path.isfile(code):
                f = open(code)
                code = f.read()
                try:
                    unicode_code = unicode(code , errors='ignore')
                    unicode_code = unicode_code.encode('utf-8', 'ignore').strip()
                    self.source_code = unicode_code
                except:
                    pass
                    self.source_code = ""
                f.close()
            else:
                self.source_code = code

        self._latest_parsed_code_ = ""

    def indentConform(self, functionString="", useFirstLine=False):
        """
         Takes source code as an input and uses the existing presumptions
         to conform python source code comprised of function definitions
         such that it is syntactically valid since python uses indentation
         as the scope operator for it's built in loose scoping mechanism
        """
        if functionString == "":
           functionString = self.source_code
        builder = ""
        collect=False
        output = ""
        try:
            output = self.autopepIfPossible( functionString )
        except:
            pass
            output = functionString

        output = output.replace('\t', '    ')
        if output == "":
            return ""

        unindent_by=""
        linenum = 1
        unindent_amount = 0
        for line in output.split("\n"):
            if ( "def " in line or collect is True ) or (useFirstLine and linenum == 1):
                if( len(line.lstrip()) != len(line) and
                        (("def " in line) or (useFirstLine and linenum == 1)) ):
                    for char in line:
                        if char == ' ':
                            unindent_by = unindent_by+' '
                            unindent_amount = unindent_amount+1
                        else:
                            break
                    collect=True
                elif( len(line.lstrip()) == len(line) and ("def " in line) ):
                    builder = output
                    break
                unindented_line = line[unindent_amount:]
                if len(unindented_line) and unindented_line[0] != ' ' and \
                        not (("def " in line) or (useFirstLine and linenum == 1)) :
                    if not useFirstLine:
                        unindented_line = '    '+unindented_line
                builder = builder+unindented_line+"\n"
                if( " return" in line ):
                    break
            linenum = linenum+1
        return builder


    def getVariableNames(self, code_string="" ):
        """
        Given a string containing a python function
        this method will return all the local variables
        by name that were used in the function.
        It uses the compiler and filters for built in
        keywords, types and methods.
        This is an alternate method for getting variable
        names from the compiler __code__ object when
        not primarily parsing Abstract Syntax Trees
        """
        if code_string == "":
            code_string = self.source_code

        codeobj=None
        try:
            code = ""
            collect=False
            for line in code_string.split("\n"):
                if( "def " in line):
                    collect=True
                    continue
                if collect is True:
                    if( " return" not in line ):
                        code = code+line+"\n"
                    if( " return" in line ):
                        break

            preprocessed = self.indentConform( code, True )
            if len(preprocessed):
                codeobj = compile( preprocessed, "<string>", "exec")
                localNames = codeobj.co_names
                globalNames = codeobj.co_varnames
                nameTokens = localNames + globalNames
                if(len(nameTokens)):
                    local_function_variables = []
                    builtins = dir(__builtins__) + dir([]) + dir({}) + dir(set()) \
                               + dir(tuple()) + dir("") + dir(bool) + dir(float)  \
                               + dir(file) + dir(memoryview)
                    for named in nameTokens:
                        if not named in builtins:
                            try:
                                imp.find_module(named)
                            except ImportError:
                                if( not ( named+"." in preprocessed) \
                                    and not ( "."+named in preprocessed) ):

                                    local_function_variables.append( named )
                    del codeobj
                    return local_function_variables
        except:
            pass
            del codeobj
            return None
        del codeobj
        return None


    def fwdPassScanner(self, code_string=""):
        """
        Top down python code parser
        Extract python def functions defined containing return statements.
        Intentionally tears apart and collapses class methods & recursive functions
        """
        if code_string == "":
            code_string = self.source_code
        functions = []
        builder = ""
        collect=False
        for line in code_string.split("\n"):
            if( "def " in line or collect is True ):
                collect=True
                if( "def " in line ):
                    builder = line+"\n"
                else:
                    builder = builder+line+"\n"
                if( " return" in line ):
                    functions.append(builder)
                    builder=""
                    collect=False
        self._latest_parsed_code_ = "\n".join(functions)
        return functions

    def backPassScanner(self, code_string ):
        """
        Bottom up python code parser
        Extract python def functions defined containing return statements.
        Intentionally tears apart and collapses class methods & recursive functions
        """
        if code_string == "":
            code_string = self.source_code
        functions = []
        builder = ""
        collect=False
        for line in reversed(code_string.split("\n")):
            if( " return" in line or collect is True ):
                collect=True
                if " return" in line:
                    builder = "\n"+line
                else:
                    builder = "\n"+line+builder
                if( "def " in line ):
                    functions.append(builder)
                    builder=""
                    collect=False

        self._latest_parsed_code_ = "\n".join(functions)
        return functions


    def parseFunctions(self, code_string=""):
        """
        This method uses the forward pass and backward pass
        function parsers to extract and collapse all python
        functions from the given source code string.
        For now, we don't really care if the code is 100% valid
        but rather it is more important to filter out logical
        cases that are not in the scope of feature learning,
        such as recursion, class methods, etc etc .
        """
        if code_string == "":
            code_string = self.source_code

        functionsFB = self.fwdPassScanner( code_string )
        functionsFB = functionsFB + self.backPassScanner( self._latest_parsed_code_ )
        functionsList = list(OrderedDict.fromkeys(functionsFB))

        print "\nFunction extraction running...\n"
        end_val = len(functionsList)
        i=0
        bar_length=50
        # conform indentations
        functions = []
        for func in functionsList:
            # progress bar because this can take a while
            percent = float(i) / end_val
            hashes = '#' * int(round(percent * bar_length))
            spaces = ' ' * (bar_length - len(hashes))
            sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
            sys.stdout.flush()
            i=i+1

            try:
                indentedConformed = self.indentConform( func )
                functions.append( indentedConformed )
            except:
                pass

        print "\n\n"

        self._latest_parsed_code_ = "\n\n".join(functions)
        return functions


    @timeout(3)
    def autopepIfPossible(self, code="", returnOriginal=False ):
        """
        Conforms most nastiest of code to pep8 standards
        If code is too malformed, times out after 3 seconds
        and returns an empty string, as that code block is
        most certainly not going to compile into an AST
        """
        if code == "":
            code = self.source_code
        # but some code is just too malformed
        try:
            autopepped = autopep8.fix_code( code, options={'aggressive': 1} )
            self._latest_parsed_code_ = autopepped
            return autopepped
        except:
            pass
            if returnOriginal:
                return code
            else:
                return ""

    def stripEmptyTokens(self, code=""):
        """
        Helps repair malformed code after sampling, variable deletions and/or mutations
        """
        if code == "":
            code = self.source_code

        filteredCode=''
        for line in code.split("\n"):
            newCode = line
            while " =, " in newCode:
                newCode = re.sub( r' =, ', ' ', newCode )
            while "(, " in newCode:
                newCode = re.sub( r'\(, ', '(', newCode )
            while "=)" in newCode:
                newCode = re.sub( r'=\)', ')', newCode )
            while " , " in newCode:
                newCode = re.sub( r' , ', ' ', newCode )
            while ", )" in newCode:
                newCode = re.sub( r', \)', ')', newCode )
            filteredCode = filteredCode+newCode+"\n"
            self._latest_parsed_code_ = filteredCode
        return filteredCode


    def stripComments(self, code="", preserve_lines=False):
        """
        This method removes comments from python code.
        Ripping out all internal python comments from within
        the inside of functions but keeps the doc string in tact.

        TODO: Update this function to not use such crazy regular
        expressions, but this works reliably for now
        """
        if code == "":
            code = self.source_code

        LINE_PRESERVE = re.compile(r"\r?\n", re.MULTILINE)

        # such an ugly reg-ex... sorry
        #
        PY_PATTERN = re.compile(
            r"""
                  (?P<comments>
                      \s*\#(?:[^\r\n])*                 # single line comments
                  )
                | (?P<code>
                        "{3}(?:\\.|[^\\])*"{3}          # triple double quotes
                      | '{3}(?:\\.|[^\\])*'{3}          # triple single quotes
                      | "(?:\\.|[^"\\])*"               # double quotes
                      | '(?:\\.|[^'])*'                 # single quotes
                      | .[^\#"']*                       # everything else
                  )
            """,
            re.VERBOSE | re.MULTILINE | re.DOTALL
        )

        def strip_regex(pattern, text, preserve_lines):
            def remove_comments(group, preserve_lines=False):
                return ''.join([x[0] for x in LINE_PRESERVE.findall(group)]) if preserve_lines else ''
            def evaluate(m, preserve_lines):
                g = m.groupdict()
                return g["code"] if g["code"] is not None else remove_comments(g["comments"], preserve_lines)
            return ''.join(map(lambda m: evaluate(m, preserve_lines), pattern.finditer(text)))


        def removeComments(source):
            io_obj = cStringIO.StringIO(source)
            out = ""
            prev_toktype = tokenize.INDENT
            last_lineno = -1
            last_col = 0
            for tok in tokenize.generate_tokens(io_obj.readline):
                token_type = tok[0]
                token_string = tok[1]
                start_line, start_col = tok[2]
                end_line, end_col = tok[3]
                ltext = tok[4]
                if start_line > last_lineno:
                    last_col = 0
                if start_col > last_col:
                    out += (" " * (start_col - last_col))
                # Remove comments:
                if token_type == tokenize.COMMENT:
                    pass
                # This series of conditionals removes docstrings:
                elif token_type == tokenize.STRING:
                    if prev_toktype != tokenize.INDENT:
                        # Likely a docstring; double-check not in an operator:
                        if prev_toktype != tokenize.NEWLINE:
                            # Catch whole-module docstrings:
                            if start_col > 0:
                                # Unlabelled indentation, we're in an operator.
                                out += token_string
                else:
                    out += token_string
                prev_toktype = token_type
                last_col = end_col
                last_lineno = end_line
            return out

        clean = []
        for line in code.split("\n"):
            line = line.split('#', 1)[0]
            line = line.rstrip()
            clean.append(line)
        cleaned_code = "\n".join( clean )
        cleaned_code  = strip_regex( PY_PATTERN, cleaned_code, preserve_lines )
        try:
            cleaned_code = self.autopepIfPossible(cleaned_code, True)
        except:
            pass
        cleaned_code  = strip_regex( PY_PATTERN, cleaned_code, preserve_lines )
        self._latest_parsed_code_ = cleaned_code
        return cleaned_code

    def save(self, full_path, code=""):
        if code == "":
            code = self._latest_parsed_code_
        if len(code) < 2:
            raise Exception('No code to save. Use one of the Features() methods to parse first.')
        directory = os.path.dirname(full_path)
        is_directory = os.path.isdir(directory)
        path_exists = os.path.exists(directory)
        if (not is_directory) or (not path_exists):
            raise ValueError('The save function of Features() class requires the path to exist.')
        else:
            save_clean_code = open(full_path, "w")
            save_clean_code.write( code )
            save_clean_code.close()
            return full_path


if __name__ == "__main__":

    # path = '/home/emill/CODE/project/data/raw/sort/'
    # filename = 'ALL_SORT_TRAINING_DATA.txt'

    path = "/home/emill/CODE/project/data/raw/squareroot/"
    filename = "ALL_SQUARE_ROOT_TRAINING_DATA.txt"

    phi = Features(path+filename)
    cleaned_code = phi.stripComments()
    functions = phi.parseFunctions( cleaned_code )

    phi.save( path+"CLEANED__"+filename )





###
#
# Playing with tokenizer - TBD, it works great but need to apply it better
# check out more later for possibly POS tagging for feature extraction:
#
#
#     tokens = tokenize.generate_tokens( cStringIO.StringIO(code).readline )   # tokenize the string
#     print "\nCODE TOKENS: \n"
#     for tok in tokens:
#         print tok

    # result = []
    # g = tokenize.generate_tokens(StringIO(s).readline)   # tokenize the string
    # for toknum, tokval, _, _, _  in g:
    #     if toknum == NUMBER and '.' in tokval:  # replace NUMBER tokens
    #         result.extend([
    #             (NAME, 'Decimal'),
    #             (OP, '('),
    #             (STRING, repr(tokval)),
    #             (OP, ')')
    #         ])
    #     else:
    #         result.append((toknum, tokval))
    #
    # untokenize(result)
    #









