"""
Network of Words - Ian Billett

ibillett2@gmail.com 

This program tracks the assocations between different words from inputted textual media.

The idea is that with enough data input, we will be able to see quantifiable differences 
between different media sources and begin to understand how media sources shape our 
perceptions of certain ideas, people or objects.

Assocations are measured by the frequency with which words appear in the same sentence. 
Frequencies are stored as weights on a Networkx graph with the nodes representing each word.
Incredibly common words are omitted to increase clarity of analysis and save processing.

Weight ranked file of all edges is outputted by default at the end. 

To see the assocations of a certain word from the input file, change the argument 
in the output_word_ranked_connections() function at the bottom.

To specify the name of the input file, simply change the file_name variable beneath. 

"""

import networkx as nx
import re 
import itertools
import os.path

file_name = 'eu'
source = open('{}.txt'.format(file_name)).read()

common_words = ['the', 'i','my','thy', 'such', 'who','whose','every', 'our', 'mr', 'most', 'de', 'me','him','thee', 'hath', 'o','th', 'of', 'and', 'sq', 'mi', 'da', 'just', 'km2', 'per', 'km', 'also', 'than', 'more', 'apart', 'including', 'being', 'off', 'into', 'during', 'since', 'only', 'has', 'its', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I', 'at', 'be', 'this', 'have', 'from', 'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would']

def intial_text_clean(source):
	"""
	Function to do preliminary processing on the input text file, discards any sentences of length 1. 
	"""
	source = source.lower()
	source = re.sub('[^A-Za-z0-9\s\.]+','', source)
	source = source.split('.')
	if len(source) >=2:
		return source
	else:
		return

def clean_sentence(text):
	"""
	Returns a list of all words from the sentence.
	"""
	text = text.split()
	for word in text:
		if word in common_words:
			text.remove(word)
	#print text  
	#print "Sentence length:", len(text) 
	return text

def create_edges(word_list):
	"""
	Returns a list of all of the combinations of words within the sentence.
	"""
	edges = itertools.combinations(word_list,2)
	edges = list(edges)
	#print edges
	#print "No of Edges:", len(edges)
	return edges

def add_to_network(edges):
	"""
	Adds the edges created to the existing network.
	"""
	global network
	for edge in edges: 
		if network.has_edge(edge[0],edge[1]):
			network[edge[0]][edge[1]]['weight'] += 1
		else: 
			network.add_edge(edge[0],edge[1],weight=1)

def process_and_add(text):
	"""
	Function that takes the raw text as an input.
	Processes the text, creates the edges then adds them to the network.
	"""
	for sentence in text: 
		text = clean_sentence(sentence)
		edges = create_edges(text)
		add_to_network(edges)
	pass

def clean_network():
	"""
	Double checks that all of the common words have been removed from the network
	"""
	for node in network.nodes():
		if node in common_words:
			network.remove_node(node)
	for edge in network.edges():
		if edge[0] == edge[1]:
			network.remove_edge(edge[0],edge[1])
	pass

def open_network():
	"""
	Opens the network if it already exists otherwise creates a new networkx graph.
	"""
	global network 
	if os.path.isfile("{}_network_of_words_raw.txt".format(file_name)):
		network = nx.read_edgelist("{}_network_of_words_raw.txt".format(file_name), 'rb')
		return
	else: 
		network = nx.Graph()
		return
def write_network():
	"""
	Writes the network to a .txt edgelist file that could be read on another machine.
	"""
	nx.write_edgelist(network,"{}_network_of_words_raw.txt".format(file_name), data=True)
	pass

def output_weight_ranked_file():
	"""
	Outputs all word associations from the source text by descending frequency.
	"""
	output = open('{}_weight_ranked_network_edges.txt'.format(file_name),'w')
	for a, b, dct in sorted(network.edges(data = True), key = lambda (a, b, dct): dct, reverse=True):
		output.write('{a:<15} {b:<15} {dct} \n'.format(a = a, b = b, dct = dct))
	pass

def output_word_ranked_connections(word):
	"""
	Takes a word and outputs the associated words from the text in descending order of frequency in a .txt file.
	"""
	output = open('{0}_{1}_weight_ranked_network_edges.txt'.format(file_name, word),'w')
	for a, b, dct in sorted(network.edges(data = True), key = lambda (a, b, dct): dct, reverse=True):
		if a == word:
			output.write('{a} {b:<15} {dct}\n'.format(a=a,b=b,dct=dct))
		elif b == word: 
			output.write('{b} {a:<15} {dct}\n'.format(a=a,b=b,dct=dct)) 
	
def get_closest_neighbors(node):
    """
    Prints to the console the neighbors of the specified node in descending order of strength of association.
    """
    for w in sorted(network[node], key=network[node].get, reverse=True):
        print w, network[node][w]

open_network()

text = intial_text_clean(source)
process_and_add(text)

clean_network()
write_network()

output_weight_ranked_file()
output_word_ranked_connections('religion')

#nx.write_gml(network,'{}_network_of_words.gml'.format(file_name))

print "Edges:", network.number_of_edges()
print "Nodes:", network.number_of_nodes()




