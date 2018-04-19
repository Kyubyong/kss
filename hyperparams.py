# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/kss

Compare speech synthesis performance depending on different text processing strategies.
1: Hangul Jamo (0x01100-0x011FF)
2: Hangul Compatibility Jamo (0x03130-0x0318F)
3: Hangul Jamo (0x01100-0x011FF). Single consonants only.
4: Hangul Compatibility Jamo (0x03130-0x0318F). Single consonants only.
'''
class Hyperparams:
    '''Hyper parameters'''
    num_exp = 4

    # signal processing
    sr = 22050  # Sampling rate.
    n_fft = 2048  # fft points (samples)
    frame_shift = 0.0125  # seconds
    frame_length = 0.05  # seconds
    hop_length = int(sr * frame_shift)  # samples. =276.
    win_length = int(sr * frame_length)  # samples. =1102.
    n_mels = 80  # Number of Mel banks to generate
    power = 1.5  # Exponent for amplifying the predicted magnitude
    n_iter = 50  # Number of inversion iterations
    preemphasis = .97
    max_db = 100
    ref_db = 20

    # Model
    r = 4 # Reduction factor. Do not change this.
    dropout_rate = 0.05
    e = 128 # == embedding
    d = 256 # == hidden units of Text2Mel
    c = 512 # == hidden units of SSRN
    attention_win_size = 3

    # data
    data = "/data/private/speech/ko"
    test_data = "ko.txt"

    if num_exp == 1:
        vocab = u'''␀␃ !,.?ᄀᄁᄂᄃᄄᄅᄆᄇᄈᄉᄊᄋᄌᄍᄎᄏᄐᄑ하ᅢᅣᅤᅥᅦᅧᅨᅩᅪᅫᅬᅭᅮᅯᅰᅱᅲᅳᅴᅵᆨᆩᆪᆫᆬᆭᆮᆯᆰᆱᆲᆴᆶᆷᆸᆹᆺᆻᆼᆽᆾᆿᇀᇁᇂ'''
    elif num_exp == 2:
        vocab = u'''␀␃ !,.?ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄾㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ''' # HCJ
    elif num_exp == 3:
        vocab = u'''␀␃ !,.?ᄀᄂᄃᄅᄆᄇᄉᄋᄌᄎᄏᄐᄑ하ᅢᅣᅤᅥᅦᅧᅨᅩᅪᅫᅬᅭᅮᅯᅰᅱᅲᅳᅴᅵᆨᆫᆮᆯᆷᆸᆺᆼᆽᆾᆿᇀᇁᇂ'''
    elif num_exp == 4:
        vocab = u'''␀␃ !,.?ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ''' # HCJ. single consonants only.
    max_N, max_T = 123, 162

    # training scheme
    lr = 0.001 # Initial learning rate.
    logdir = "logdir/{}".format(num_exp)
    sampledir = 'samples/{}'.format(num_exp)
    B = 16 # batch size
    num_iterations = 400000
