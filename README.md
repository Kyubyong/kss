# Korean TTS Model: what is the best Hangul processing strategy for Korean speech synthesis?

Hangul is a unique script designed mostly for Korean. It is phonetic in principle like Latin letters, but you need to know much more pronunciation rules in order to pronounce it correctly than you do for German or Spanish. Hangul is syllable-based like Kana,
the Japanese script, but Hangul is also different from Kana in that Hangul syllables can be decomposed
into their constitutional consonants and vowels.
Putting together, these are quite handy for readability in practice, but often they embarrass Korean computational linguists.
Do I have to convert graphmes into phonemes first? Is it better to decompose Hangul syllables for TTS?
 Or do I have to take syllables without decomposition?
 If you know the scene behind the Hangul unicode, you will find things are even
 more complicated. There are two kinds of unicode blocks for contemporary Hangul consonants and vowels (called __jamo__ in Korean): Hangul Jamo (0x01100-0x011FF) and
 Hangul Compatibility Jamo (0x03130-0x0318F). In Hangul Compatibility Jamo the first consonant (onset) and the final consonant (code) are given the same unicode point,
 wherase in Hangul Jamo they are treated as independent letters. (Figuratively, if you follow the Hangul Jamo system in English, you have to distinguish the two l's in law and cool)
On the other hand, those two regard consonant clusters such as ㄲ, ㄱㅅ as a single letter. Some claim that they should be understood as a sequence of single consonants. Are they right in the computational practice? These questions motivate this project.

I run four different experiements depending on the Hangul processing strategies below.

* Exp.0: Hangul Jamo (0x01100-0x011FF) with consonant clusters. Graphemes are converted into phonemes.
* Exp.1: Hangul Jamo (0x01100-0x011FF) with consonant clusters.
* Exp.2: Hangul Compatibility Jamo (0x03130-0x0318F) with consonant clusters
* Exp.3: Hangul Jamo (0x01100-0x011FF). Single consonants only.
* Exp.4: Hangul Compatibility Jamo (0x03130-0x0318F). Single consonants only.

## Requirements
  * python >= 2.7
  * NumPy >= 1.11.1
  * TensorFlow >= 1.3
  * librosa
  * tqdm
  * matplotlib
  * scipy

## Data

[KSS Dataset](https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset/version/2), a Korean single speaker speech dataset, is used.

## Model
DCTTS, introudced in [Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](https://arxiv.org/abs/1710.08969), is implemented for this project.
You can refer to my other repo to see the original implementation. This repo focuses on the comparison among the four different experiment conditions.

## Training
  * STEP 0. Download [KSS Dataset](https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset).
  * STEP 1. Adjust `num_exp` in `hyperparams.py`.
  * STEP 2. Run `python prepro.py` for model inputs and targets.
  * STEP 3. Run `python train.py 1` for training Text2Mel.
  * STEP 4. Run `python train.py 2` for training SSRN.

You can do STEP 3 and 4 at the same time, if you have more than one gpu card.


## Sample Synthesis
  * Run `synthesize.py` and check the files in `samples`.

## Generated Samples

| Num Experiment       | Samples |
| :----- |:-------------|
| 0      | [400k](https://soundcloud.com/kyubyong-park/sets/kss_exp0)|
| 1      | [400k](https://soundcloud.com/kyubyong-park/sets/kss_exp1)|
| 2      | [400k](https://soundcloud.com/kyubyong-park/sets/kss_exp2)|
| 3| [400k](https://soundcloud.com/kyubyong-park/sets/kss_ex3)|
|4 | [400k](https://soundcloud.com/kyubyong-park/sets/kss_exp4)|

## Pretrained Models

| Num Experiment       | Models |
| :----- |:-------------|
| 0      | [400k](https://www.dropbox.com/s/ipt17hoo4lj56xg/exp0.zip?dl=0)|
| 1      | [400k](https://www.dropbox.com/s/q133hrwyyvudl65/exp1.zip?dl=0)|
| 2      | [400k](https://www.dropbox.com/s/vaz0tb5l8gwfvd0/exp2.zip?dl=0)|
| 3| [400k](https://www.dropbox.com/s/iy7v2zzqguw1q18/exp3.zip?dl=0)|
|4 | [400k](https://www.dropbox.com/s/qtxiss3jk0hjbap/exp4.zip?dl=0)|

## Notes

  * Refer to [this](https://github.com/Kyubyong/kss/blob/master/graph2pron_statistics.md), which is provided by Hyungjun So.
