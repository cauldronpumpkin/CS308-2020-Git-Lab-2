import re
from gensim.parsing.preprocessing import remove_stopwords

num_of_lines, num_of_sentences, num_of_words = 0, 0, 0

def file_open(path):
	global num_of_lines
	file = open(path,"r")
	text = file.read()
	num_of_lines = text.count('\n') + 1
	return (text.splitlines(), num_of_lines)

def remove_punctuations(line):
	return re.sub(r'[^\w\s]', '',line)


def list_of_sentences(text):
	global num_of_sentences
	num_of_sentences = 0
	lists = []
	for line in text:
		sentences = list(filter(lambda s: len(s) != 1,line.split('.')))
		sentences = [sentence.strip() for sentence in sentences]
		lists += sentences
	num_of_sentences = len(lists)
	return (lists, num_of_sentences)


def split_and_store(list):
	dict = {}
	global num_of_words
	num_of_words = 0
	for line in list:
		words = remove_stopwords(remove_punctuations(line).lower()).split(' ')
		num_of_words += len(words)
		for word in words:
			if word.isnumeric() or word == '':
				continue
			if word not in dict:
				dict[word] = 1
			else:
				dict[word] += 1
	return (dict, num_of_words)

def get_max_occuring_word(dict):
	return max(dict, key=dict.get)

def get_min_occuring_word(dict):
	return min(dict, key=dict.get)

def get_keyword_set(filepath):
	file = open(filepath,'r')
	return set(file.read().splitlines()) 

def get_keyword_sentences(list,set):
	keyword_sentences = []
	for sentence in list:
		words = remove_punctuations(sentence).split(' ')
		for word in words:
			if word in set:
				keyword_sentences.append(sentence)
				break
	return keyword_sentences
