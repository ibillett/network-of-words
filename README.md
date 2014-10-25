#Network of Words 

This python programme conducts sentiment analysis by analysing the strength of associations between words in an input .txt file. 

##But... *why*?

The idea is that with enough data input we will be able to see quantifiable differences in the word associations made between media sources. Then we can see how media sources affect our perceptions of certain ideas, people or objects. For example, the words most heavily associated with the word 'immigrant' in the Daily Mail and The Guardian will be very different. The Network of Words provides a framework for this analysis.

##How does it work?

Assocations between words are measured by the frequency with which words appear in the same sentence. Words are stored as nodes in the graph then frequencies are stored as weights between nodes, being increased everytime an association is made. Incredibly common words are omitted to increase clarity of analysis and save processing.

The programme then outputs 3 files: i) the raw network, ii) associations ranked highest to lowest, iii) associations from a user defined word ranked highest to lowest. 

##Usage notes

To specify the name of the input file, simply change the file_name string variable.

To see the assocations of a certain word from the input file, change the argument in the output_word_ranked_connections() function at the bottom.

Examples of outputs are given in this repo.



