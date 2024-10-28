"""


Refs:
- https://huggingface.co/learn/nlp-course/chapter6/5

"""

from transformers import AutoTokenizer
from collections import defaultdict
from functools import reduce


class BPETokenizer:
    def __init__(self, corpus, vocab_size):
        vocab = None
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

        word_freq = defaultdict(int)
        for text in corpus:
            words_with_offsets = (
                self.tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
            )
            for word, offset in words_with_offsets:
                word_freq[word] += 1

        alphabet = reduce(
            lambda x, y: x.union(y), [set(list(w)) for w in word_freq.keys()], set()
        )
        alphabet = list(sorted(alphabet))
        vocab = ["<|endoftext|>"] + alphabet

        splits = {word: [c for c in word] for word in word_freq.keys()}

        def calc_pairs_freq(splits):
            pairs_freq = defaultdict(int)
            for word, freq in word_freq.items():
                for i in range(len(splits[word]) - 1):
                    pairs_freq[(splits[word][i], splits[word][i + 1])] += freq
            return pairs_freq

        def merge_pair(splits, left, right):
            for word, split in splits.items():
                i = 0
                while i < len(split) - 1:
                    if split[i] == left and split[i+1] == right:
                        split = split[:i] + [left + right] + split[i+2:]
                    else:
                        i += 1
                splits[word] = split

        merges = {}
        while len(vocab) < vocab_size:
            pairs_freq = calc_pairs_freq(splits)
            pair, most_freq = None, 0
            for k, v in pairs_freq.items():
                if most_freq < v:
                    most_freq = v
                    pair = k
            vocab.append(pair[0] + pair[1])
            merges[pair] = pair[0] + pair[1] 
            merge_pair(splits, *pair)
        self.vocab = vocab
        self.merges = merges

    def tokenize(self, text):
        splits = [
            [e for e in word] for (word, offset) 
            in self.tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
        ]
        for (m_left, m_right), m_word in self.merges.items():
            for w_inx, word in enumerate(splits):
                i = 0
                while i < len(word) - 1:
                    if word[i] == m_left and word[i+1] == m_right:
                        word = word[:i] + [m_word] + word[i+2:]
                    else:
                        i += 1
                splits[w_inx] = word
        return sum(splits, [])
        



def test_simple():
    corpus = [
        "This is the Hugging Face Course.",
        "This chapter is about tokenization.",
        "This section shows several tokenizer algorithms.",
        "Hopefully, you will be able to understand how they are trained and generate tokens.",
    ]
    tokenizer = BPETokenizer(corpus, 50)
    print(f"{tokenizer.vocab=}")
    print(f"{tokenizer.merges=}")
    assert tuple(tokenizer.vocab) == ( "<|endoftext|>", ",", ".", "C", "F", "H", "T", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "Ġ", "Ġt", "is", "er", "Ġa", "Ġto", "en", "Th", "This", "ou", "se", "Ġtok", "Ġtoken", "nd", "Ġis", "Ġth", "Ġthe", "in", "Ġab", "Ġtokeni",)
    res = tokenizer.tokenize("This is not a token.")
    print(f"{res=}")
    assert res == [ "This", "Ġis", "Ġ", "n", "o", "t", "Ġa", "Ġtoken", ".", ]


test_simple()
