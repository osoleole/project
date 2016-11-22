import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--vocab_file', default='vocab.txt', type=str)
parser.add_argument('--vectors_file', default='vectors.txt', type=str)
parser.add_argument('-important_file', default='important.txt', type=str)
args = parser.parse_args()
print(args)
print(args.vocab_file)
print(args.vectors_file)
print(args.important_file)
