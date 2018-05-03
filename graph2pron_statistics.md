### Symbolic comparison statistics based on natural text

#### Basis of phonetic representation
The ground truth should be the acoustic measure of "typical sound" - 'average' pronunciation of all Korean speaker, which is difficult to obtain. Instead, the "standard pronunciation symbol" which is a pivot or a guideline of standard pronunciation is used as symbolic counterpart of a ground truth - Every person have different phonetic character, but at least they (usually) speak as the same way as tagged by standard pronunciation. For example, 허구연, a famous baseball caster, speaks strong dialect that pronounces 임꺽정 as [임끅쯩(이)] but still pronounces the same rule as 걱정 like [극쯩].

Note that it is debateful that the standard pronunciation symbol is equivalent to the phone, since there are several implicit phonetic rules that is not represented on the standard pronunciation symbol. For example, voicing rule of voiceless consonants (ㄱ, ㄷ, ㅂ, ㅅ, ㅈ) allows those consonants to have their voiced counterpart, but never being voiced in the front of sound cluster. Moreover, the null consonant (ㅇ) at the very start of the sound cluster sounds as glottal plosive ([ʔ]) or several exceptional cases (e. g., Roman alphabet E). All of these modification to consonants cannot be distinguished in the standard pronunciation symbol although being strictly different phonetic character.

In a usual input sequence of machine learning, whole sequences are fed into input. However, it is impossible to span whole language sequences as a probability basis, the input sequence should be splitted into a certain way to use as a statistical basis. Using the virtue of 'forced vowelization(?)',phonetic characteristics of Korean language, every fragment of a sound is assigned by a vowel. Therefore, for a given sequence of any length, number of vowels are equal for any representation under the same vowel set. A typical choice would be assigning a sound basis equivalent as a grapheme ([Consonant, Vowel, Coda]) pair. On the other hand, another basis are suggested to less suffer on the modification rule across two subsequent graphemes. A "triphone" basis spans between vowels (since vowels are less affected by modification); as [Vowel, Coda, Consonant, Vowel] pair.

Using two basis, we split a sample text into a basis sequences and compare the correpondence (or, degree of confusion) compared to corresponding pairs by standard pronunciation symbol. A degree of confusion is computed as sum of partition entropy; 0 if all of basis `$A_i$` is correponds to `$B_j$` (one-to-one correspondence). Suppose a number `$n$` of base (a [CnVoCo] or [VoCoCnVo]) is in a `$A_i$` and in standard pronunciation `$B_j$`, we connect with a network `$N_{ij} = n$`. Then the confusion of A based on B is represented as

`$C(A|B) = \sum_{i} p_{i} \sum_{j} -ln p_{j|i}$`

where `$p_{i} = \sum_j N_{ij} / \sum_{ij} N_{ij}$` and `$p_{j|i} = N_{ij}/\sum_i N_j$`. Note that this is asymmetric measure of A and B.

The confusion will be calculated in the way given by 4 experiments; but in the triphone basis only exp.1 and exp.4 are distinguished. 

#### Dataset
The sample dataset of Korean natural text was concatenation of four text sets: Korean translation of the short novel "The Black Cat" by Edgar Allan Poe, the Korean short novel "운수 좋은 날" by 현진건, kss dataset scripts and a private stt script set. Only texts and spaces are included, since only independent pronunciation is considered. Note that in this condition, phonetic modification such as liaison is ignored.

#### Result and discussions
##### Triphone, C(StdPrn|Graph), with exp.4 basis (Consonant cluster 
Overall confusion: 0.003859046558360724
Top-10 most confused base
('ㅏ', 'ㄹ', 'ㅇ', 'ㅣ') : ([(('aa', 'll', 'rr', 'ii'), 36), (('aa', ' ', 'rr', 'ii'), 666)])
('ㅏ', 'ㄱ', 'ㄱ', 'ㅏ') : ([(('aa', 'kf', 'kk', 'aa'), 48), (('aa', ' ', 'kk', 'aa'), 215)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅏ') : ([(('ii', 'nf', 'kk', 'aa'), 46), (('ii', 'nf', 'k0', 'aa'), 197)])
('ㅣ', 'ㄴ', 'ㄷ', 'ㅏ') : ([(('ii', 'nf', 'tt', 'aa'), 37), (('ii', 'nf', 't0', 'aa'), 263)])
('ㅣ', 'ㄴ', 'ㅈ', 'ㅣ') : ([(('ii', 'nf', 'c0', 'ii'), 155), (('ii', 'nf', 'cc', 'ii'), 47)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅗ') : ([(('ii', 'nf', 'kk', 'oo'), 145), (('ii', 'nf', 'k0', 'oo'), 35)])
('ㅣ', 'ㄱ', 'ㄱ', 'ㅏ') : ([(('ii', 'kf', 'kk', 'aa'), 15), (('ii', ' ', 'kk', 'aa'), 714)])
('ㅏ', 'ㄹ', 'ㄱ', 'ㅔ') : ([(('aa', 'll', 'kk', 'ee'), 131), (('aa', 'll', 'k0', 'ee'), 23)])
('ㅏ', 'ㄹ', 'ㅈ', 'ㅣ') : ([(('aa', 'll', 'cc', 'ii'), 41), (('aa', 'll', 'c0', 'ii'), 46)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅣ') : ([(('ii', 'nf', 'kk', 'ii'), 20), (('ii', 'nf', 'k0', 'ii'), 111)])

##### Triphone, C(StdPrn|Graph), with exp.1 basis
Overall confusion: 0.002684402501353149
Top-10 most confused base
('ㅏ', 'ㄹ', 'ㅇ', 'ㅣ') : ([(('aa', 'll', 'rr', 'ii'), 36), (('aa', ' ', 'rr', 'ii'), 666)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅏ') : ([(('ii', 'nf', 'kk', 'aa'), 46), (('ii', 'nf', 'k0', 'aa'), 197)])
('ㅣ', 'ㄴ', 'ㄷ', 'ㅏ') : ([(('ii', 'nf', 't0', 'aa'), 263), (('ii', 'nf', 'tt', 'aa'), 37)])
('ㅣ', 'ㄴ', 'ㅈ', 'ㅣ') : ([(('ii', 'nf', 'cc', 'ii'), 47), (('ii', 'nf', 'c0', 'ii'), 155)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅗ') : ([(('ii', 'nf', 'k0', 'oo'), 35), (('ii', 'nf', 'kk', 'oo'), 145)])
('ㅏ', 'ㄹ', 'ㄱ', 'ㅔ') : ([(('aa', 'll', 'k0', 'ee'), 23), (('aa', 'll', 'kk', 'ee'), 131)])
('ㅏ', 'ㄹ', 'ㅈ', 'ㅣ') : ([(('aa', 'll', 'cc', 'ii'), 41), (('aa', 'll', 'c0', 'ii'), 46)])
('ㅣ', 'ㄴ', 'ㄱ', 'ㅣ') : ([(('ii', 'nf', 'k0', 'ii'), 111), (('ii', 'nf', 'kk', 'ii'), 20)])
('ㅏ', 'ㄹ', 'ㄱ', 'ㅓ') : ([(('aa', 'll', 'k0', 'vv'), 22), (('aa', 'll', 'kk', 'vv'), 64)])
('ㅡ', 'ㅁ', 'ㄷ', 'ㅏ') : ([(('xx', 'mf', 't0', 'aa'), 48), (('xx', 'mf', 'tt', 'aa'), 26)])

##### Grapheme, C(StdPrn|Graph)
Overall confusion: 0.3983152605973124
top-10 most confused base
('ㅇ', 'ㅣ', ' ') : ([(('ch', 'ii', ' '), 389), (('c0', 'ii', ' '), 19), (('ss', 'ii', ' '), 157), (('rr', 'ii', ' '), 2419), (('p0', 'ii', ' '), 456), (('oh', 'ii', ' '), 11308), (('mm', 'ii', ' '), 1865), (('k0', 'ii', ' '), 1589), (('nn', 'ii', ' '), 2853), (('kk', 'ii', ' '), 29), (('s0', 'ii', ' '), 441), (('ph', 'ii', ' '), 44)])
('ㅇ', 'ㅓ', ' ') : ([(('ss', 'vv', ' '), 6860), (('k0', 'vv', ' '), 553), (('ph', 'vv', ' '), 770), (('c0', 'vv', ' '), 83), (('mm', 'vv', ' '), 98), (('t0', 'vv', ' '), 64), (('nn', 'vv', ' '), 124), (('kk', 'vv', ' '), 11), (('s0', 'vv', ' '), 62), (('rr', 'vv', ' '), 2720), (('p0', 'vv', ' '), 83), (('oh', 'vv', ' '), 4290), (('th', 'vv', ' '), 26)])
('ㅇ', 'ㅔ', ' ') : ([(('mm', 'ee', ' '), 921), (('k0', 'ee', ' '), 807), (('nn', 'ee', ' '), 1999), (('kk', 'ee', ' '), 114), (('ph', 'ee', ' '), 120), (('p0', 'ee', ' '), 405), (('c0', 'ee', ' '), 20), (('kh', 'ee', ' '), 4), (('oh', 'ee', ' '), 5356), (('th', 'ee', ' '), 56), (('ss', 'ee', ' '), 1), (('rr', 'ee', ' '), 1114), (('s0', 'ee', ' '), 95), (('ch', 'ee', ' '), 4)])
('ㅇ', 'ㅡ', 'ㄹ') : ([(('rr', 'xx', 'll'), 1278), (('oh', 'xx', 'll'), 1367), (('kk', 'xx', 'll'), 11), (('t0', 'xx', 'll'), 64), (('ph', 'xx', 'll'), 30), (('k0', 'xx', 'll'), 1044), (('nn', 'xx', 'll'), 1153), (('s0', 'xx', ' '), 1), (('th', 'xx', 'll'), 14), (('s0', 'xx', 'll'), 240), (('oh', 'xx', ' '), 60), (('c0', 'xx', 'll'), 75), (('p0', 'xx', 'll'), 344), (('ss', 'xx', 'll'), 477), (('ch', 'xx', 'll'), 11), (('mm', 'xx', 'll'), 841)])
('ㅇ', 'ㅡ', 'ㄴ') : ([(('rr', 'xx', 'nf'), 1083), (('k0', 'xx', 'nf'), 710), (('rr', 'xx', ' '), 1), (('kk', 'xx', 'nf'), 20), (('ph', 'xx', 'nf'), 206), (('nn', 'xx', ' '), 1), (('th', 'xx', 'nf'), 224), (('mm', 'xx', 'nf'), 886), (('s0', 'xx', 'nf'), 238), (('oh', 'xx', ' '), 23), (('oh', 'xx', 'nf'), 1206), (('nn', 'xx', 'nf'), 905), (('mm', 'xx', ' '), 4), (('k0', 'xx', ' '), 2), (('ch', 'xx', 'nf'), 11), (('c0', 'xx', 'nf'), 54), (('t0', 'xx', 'nf'), 33), (('ss', 'xx', 'nf'), 5), (('p0', 'xx', 'nf'), 241)])
('ㅇ', 'ㅏ', ' ') : ([(('mm', 'aa', ' '), 92), (('nn', 'aa', ' '), 878), (('rr', 'aa', ' '), 801), (('th', 'aa', ' '), 560), (('oh', 'aa', ' '), 4906), (('p0', 'aa', ' '), 94), (('c0', 'aa', ' '), 789), (('k0', 'aa', ' '), 59), (('t0', 'aa', ' '), 197), (('ch', 'aa', ' '), 5), (('kk', 'aa', ' '), 27), (('s0', 'aa', ' '), 5), (('ph', 'aa', ' '), 38)])
('ㄷ', 'ㅏ', ' ') : ([(('th', 'aa', ' '), 256), (('tt', 'aa', ' '), 3486), (('t0', 'aa', ' '), 7884)])
('ㅇ', 'ㅡ', ' ') : ([(('ch', 'xx', ' '), 3), (('th', 'xx', ' '), 36), (('ss', 'xx', ' '), 380), (('nn', 'xx', ' '), 354), (('rr', 'xx', ' '), 63), (('p0', 'xx', ' '), 130), (('s0', 'xx', ' '), 87), (('c0', 'xx', ' '), 60), (('mm', 'xx', ' '), 167), (('k0', 'xx', ' '), 717), (('oh', 'xx', ' '), 425), (('kk', 'xx', ' '), 27), (('t0', 'xx', ' '), 91), (('ph', 'xx', ' '), 75)])
('ㅇ', 'ㅣ', 'ㅆ') : ([(('k0', 'ii', 'nf'), 4), (('s0', 'ii', 'tf'), 29), (('nn', 'ii', 'nf'), 2), (('c0', 'ii', ' '), 1), (('rr', 'ii', 'nf'), 5), (('rr', 'ii', ' '), 4), (('t0', 'ii', 'tf'), 7), (('s0', 'ii', ' '), 47), (('s0', 'ii', 'nf'), 50), (('mm', 'ii', 'nf'), 5), (('nn', 'ii', ' '), 9), (('k0', 'ii', ' '), 4), (('oh', 'ii', ' '), 2238), (('oh', 'ii', 'tf'), 1139), (('oh', 'ii', 'nf'), 847), (('nn', 'ii', 'tf'), 2), (('k0', 'ii', 'tf'), 1), (('mm', 'ii', ' '), 1)])
('ㅇ', 'ㅣ', 'ㄹ') : ([(('rr', 'ii', 'll'), 105), (('oh', 'ii', 'll'), 2441), (('kk', 'ii', 'll'), 1), (('ch', 'ii', ' '), 3), (('ph', 'ii', 'll'), 1), (('k0', 'ii', 'll'), 49), (('s0', 'ii', 'll'), 10), (('rr', 'ii', ' '), 33), (('nn', 'ii', ' '), 49), (('oh', 'ii', ' '), 1184), (('nn', 'ii', 'll'), 63), (('mm', 'ii', ' '), 31), (('k0', 'ii', ' '), 13), (('mm', 'ii', 'll'), 36), (('p0', 'ii', ' '), 21), (('ch', 'ii', 'll'), 2), (('p0', 'ii', 'll'), 31)])

##### Discussion
Note that in bare grapheme basis has a lot of confusion especially in consonant ㅇ. This is largely cured by adopting triphone basis which mostly maps coda+consonant ㅇ into a single standard pronunciation. While, difference between experiment basis 1 and 4 comes from the "loss of the positional information of consonant (between coda and consonant)" which brings confusion. Separating consonant cluster with preserving positional information give almost the confusion as exp.1 (data not included).

The best case, which fully uses Hangul Jamo (0x01100-0x011FF) with consonant clusters still have some confusion; From the examples we can find out that the confusion is due to fortis-ification(?) (경음화). The same VCCV pair may pronounce either fortis(경음) or lenis(연음) due to complex rule called 경음화. Most of the 경음화 rules are defined by phonetic basis (e.g., ㅜ+ㄱ+ㅂ+ㅏ -> ㅜ+ㄱ+ㅃ+ㅏ), still a large portion of rule depends on the linguistical context. (e.g., POS, fundamental form of the word, ...) For detailed information of 경음화, please refer to [this link](https://www.korean.go.kr/front/page/pageView.do?page_id=P000102&mn_id=95
