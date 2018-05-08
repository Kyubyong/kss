# -*- coding: utf-8 -*-
'''
This is mostly adapted from https://github.com/scarletcho/KoG2P.
g2p.py
~~~~~~~~~~
This script converts Korean graphemes to romanized phones and then to pronunciation.
    (1) graph2phone: convert Korean graphemes to romanized phones
    (2) phone2prono: convert romanized phones to pronunciation
    (3) graph2phone: convert Korean graphemes to pronunciation
Usage:  $ python g2p.py '스물 여덟째 사람'
        (NB. Please check 'rulebook_path' before usage.)
Yejin Cho (scarletcho@gmail.com)
Jaegu Kang (jaekoo.jk@gmail.com)
Hyungwon Yang (hyung8758@gmail.com)
Yeonjung Hong (yvonne.yj.hong@gmail.com)
Created: 2016-08-11
Last updated: 2017-02-22 Yejin Cho
* Key updates made:
    - Executable in both Python 2 and 3.
    - G2P Performance test available ($ python g2p.py test)
    - G2P verbosity control available
'''

import datetime as dt
import re
import math
import sys
import optparse

# Option
parser = optparse.OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", default="False",
                  help="This option prints the detail information of g2p process.")

(options, args) = parser.parse_args()
verbose = options.verbose

# Check Python version
ver_info = sys.version_info

if ver_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')


def readfileUTF8(fname):
    f = open(fname, 'r')
    corpus = []

    while True:
        line = f.readline()
        line = line.encode("utf-8")
        line = re.sub(u'\n', u'', line)
        if line != u'':
            corpus.append(line)
        if not line: break

    f.close()
    return corpus


def writefile(body, fname):
    out = open(fname, 'w')
    for line in body:
        out.write('{}\n'.format(line))
    out.close()


def readRules(pver, rule_book):
    if pver == 2:
        f = open(rule_book, 'r')
    elif pver == 3:
        f = open(rule_book, 'r', encoding="utf-8")

    rule_in = []
    rule_out = []

    while True:
        line = f.readline()
        if pver == 2:
            line = unicode(line.encode("utf-8"))
            line = re.sub(u'\n', u'', line)
        elif pver == 3:
            line = re.sub('\n', '', line)

        if line != u'':
            if line[0] != u'#':
                # print(line)
                IOlist = line.split('\t')
                rule_in.append(IOlist[0])
                if IOlist[1]:
                    rule_out.append(IOlist[1])
                else:  # If output is empty (i.e. deletion rule)
                    rule_out.append(u'')
        if not line: break
    f.close()

    return rule_in, rule_out


def isHangul(charint):
    hangul_init = 44032
    hangul_fin = 55203
    return charint >= hangul_init and charint <= hangul_fin


def checkCharType(var_list):
    #  1: whitespace
    #  0: hangul
    # -1: non-hangul
    checked = []
    for i in range(len(var_list)):
        if var_list[i] == 32:  # whitespace
            checked.append(1)
        elif isHangul(var_list[i]):  # Hangul character
            checked.append(0)
        else:  # Non-hangul character
            checked.append(-1)
    return checked


def graph2phone(graphs):
    # Encode graphemes as utf8
    try:
        graphs = graphs.decode('utf8')
    except AttributeError:
        pass

    integers = []
    for i in range(len(graphs)):
        integers.append(ord(graphs[i]))

    # Romanization (according to Korean Spontaneous Speech corpus; 성인자유발화코퍼스)
    phones = ''
    ONS = ['k0', 'kk', 'nn', 't0', 'tt', 'rr', 'mm', 'p0', 'pp',
           's0', 'ss', 'oh', 'c0', 'cc', 'ch', 'kh', 'th', 'ph', 'h0']
    NUC = ['aa', 'qq', 'ya', 'yq', 'vv', 'ee', 'yv', 'ye', 'oo', 'wa',
           'wq', 'wo', 'yo', 'uu', 'wv', 'we', 'wi', 'yu', 'xx', 'xi', 'ii']
    COD = ['', 'kf', 'kk', 'ks', 'nf', 'nc', 'nh', 'tf',
           'll', 'lk', 'lm', 'lb', 'ls', 'lt', 'lp', 'lh',
           'mf', 'pf', 'ps', 's0', 'ss', 'oh', 'c0', 'ch',
           'kh', 'th', 'ph', 'h0']

    # Pronunciation
    idx = checkCharType(integers)
    iElement = 0
    while iElement < len(integers):
        if idx[iElement] == 0:  # not space characters
            base = 44032
            df = int(integers[iElement]) - base
            iONS = int(math.floor(df / 588)) + 1
            iNUC = int(math.floor((df % 588) / 28)) + 1
            iCOD = int((df % 588) % 28) + 1

            s1 = '@' + ONS[iONS - 1]  # onset
            s2 = NUC[iNUC - 1]  # nucleus

            if COD[iCOD - 1]:  # coda
                s3 = COD[iCOD - 1]
            else:
                s3 = ''
            tmp = "`" + s1 + "`" + s2 + "`" + s3 + "`"
            phones = phones + tmp

        elif idx[iElement] == 1:  # space character
            tmp = '`#`'
            phones = phones + tmp

        else:  # non-Hangul
            phones += "`" + unichr(integers[iElement]) + "`"

        iElement += 1
        tmp = ''

    # Collapse syllable delimiters (`).
    phones = re.sub("`+", "`", phones)

    # 초성 이응 삭제
    phones = phones.replace("`@oh`", "`@")

    # 받침 이응 'ng'으로 처리 (Velar nasal in coda position)
    # print(phones)
    phones = phones.replace("oh`@", "ng`@")
    # print(phones,"===")
    phones = phones.replace("oh`#", "ng`#")
    phones = re.sub('oh`$', 'ng`', phones)


    return phones


def phone2prono(phones, rule_in, rule_out):
    # Apply g2p rules
    for pattern, replacement in zip(rule_in, rule_out):
        _phones = phones
        phones = re.sub(pattern, replacement, phones)
        # if _phones != phones:
        #     print(_phones, "->", phones)
        #     print("::", pattern, "->", replacement)
        prono = phones
    return prono


def graph2prono(graphs, rule_in, rule_out):
    romanized = graph2phone(graphs)
    prono = phone2prono(romanized, rule_in, rule_out)

    prono = re.sub(u'`', u' ', prono)
    prono = re.sub(u' $', u'', prono)
    # prono = re.sub(u'#', u'@', prono)
    prono = re.sub(u'@+', u'@', prono)

    prono_prev = prono
    identical = False
    loop_cnt = 1

    # if verbose == True:
    # print('=> Romanized: ' + romanized)
    # print('=> Initial output: ' + prono)

    while not identical:
        prono_new = phone2prono(re.sub(u' ', u'`', prono_prev + u'`'), rule_in, rule_out)
        prono_new = re.sub(u'`', u' ', prono_new)
        prono_new = re.sub(u' $', u'', prono_new)

        if re.sub(u'@', u'', prono_prev) == re.sub(u'@', u'', prono_new):
            identical = True
            prono_new = re.sub(u'@', u'', prono_new)
            # if verbose == True:
            # print('\n=> Exhaustive rule application completed!')
            # print('=> Total loop count: ' + str(loop_cnt))
            # print('=> Output: ' + prono_new)
        else:
            # if verbose == True:
            # print('\n=> Rule applied for more than once')
            # print('cmp1: ' + re.sub(u'@', u'', prono_prev))
            # print('cmp2: ' + re.sub(u'@', u'', prono_new))
            loop_cnt += 1
            prono_prev = prono_new

    # prono_new = prono_new.replace("@", "")
    # prono_new = prono_new.strip("`")
    # prono_new = prono_new.replace("`#`", " ")
    # print("prnono_new::", prono_new)
    prono_new = prono_new.strip()

    return prono_new


def runKoG2P(graph, rulebook):
    [rule_in, rule_out] = readRules(ver_info[0], rulebook)
    if ver_info[0] == 2:
        prono = graph2prono(unicode(graph), rule_in, rule_out)
    elif ver_info[0] == 3:
        prono = graph2prono(graph, rule_in, rule_out)

    phones = [phone.replace("#", " ") for phone in prono.split()]

    return phones


# Usage:
if __name__ == '__main__':
    graph = args[0]
    phonemes = runKoG2P(graph, 'rulebook.txt')
    # print(phonemes)

