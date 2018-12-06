# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:22:42 2018

@author: navi_
"""
import nltk
import matplotlib.pyplot as plt

#build a dictionary with the sequence (String)
def build_dict(sequence):
    ref = None
    dict_seq = {} 
    #tokenize to get the diferent numbers (string type) of the sequence
    nums = nltk.word_tokenize(sequence.replace(',',' ')) 
    #build a list with the numbers (int type) 
    for i in range(len(nums)):
        #find the number with de references (*) to get the reference
        if '*' in nums[i]:
            nums[i] = nums[i].replace('*','')
            ref = i
        nums[i] = float(nums[i])
        i += 1
   #built the dictionary with the position and value of the numbers in the seq
    aux = ref * -1 
    for n in nums:
        dict_seq[aux] = n
        aux += 1      
    return dict_seq

#complete seq1 and seq2, so that are in the same interval (dictionaries)
#to operate the sequences
def complete_seqs(seq1, seq2):
    seq1aux = {}
    seq2aux = {}
    #create a copy of the dictionaries for keep intact the originals
    for k1 in seq1:
        seq1aux[k1] = seq1[k1]
    for k2 in seq2:
        seq2aux[k2] = seq2[k2]
    #add the missed values    
    keys1 = seq1.keys()
    keys2 = seq2.keys()
    for k in keys1:
        if not k in keys2:
           seq2aux[k] = 0
    for k in keys2:
        if not k in keys1:
           seq1aux[k] = 0      
    return seq1aux, seq2aux

#build a sequence in (val1, val2, val3...) style (list of strings)
#to show in screen
def build_seq(seq1):
    sequence = []
    keys = sorted(seq1.keys())
    for k in keys:
        if k == 0:
            sequence.append(str(seq1[k])+'*') #the reference
        else:
            sequence.append(str(seq1[k]))
    return sequence

#add/substract/multiplication of sequences (dictionaries)
def basic_operation_seq(seq1, seq2, op):
    keys = sorted(seq1.keys())
    seq_result = {}
    for k in keys:
        if op == 'sub':
            seq_result[k] = seq1[k] - seq2[k]
        elif op == 'mult':
            seq_result[k] = seq1[k] * seq2[k]
        else:
            seq_result[k] = seq1[k] + seq2[k]
    return seq_result

#plot a sequence (dictionary)
def plot_sequence(seq):
    keys = sorted(seq.keys())
    index = [] 
    values = []
    #get the positions and values of the elements in the sequence
    for k in keys:
        index.append(k)
        values.append(seq[k])
    #get the limits of the axis plot    
    plt.axvline(x=0, color='r')
    markerline, stemlines, baseline = plt.stem(index,values, 'b-.', 'bo')
    plt.axhline(y=0, color='r')
    ymax = max(values)+2
    ymin = min(values)-2
    xmax = max(index)+1
    xmin = min(index)-1
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid(True)

    plt.show()

#plot two sequences (dictionary)
def plot_two_sequences(seq, seq2):
    keys = sorted(seq.keys())
    index = [] 
    values = []
    #get the positions and values of the elements in the sequence
    for k in keys:
        index.append(k)
        values.append(seq[k])
    #get the limits of the axis plot
    fig,subplots=plt.subplots()

    #subplots.plot(index, values, 'ro', alpha=0.5)
    plt.axvline(x=0, color='r')
    markerline, stemlines, baseline = subplots.stem(index,values, 'b-.', 'bo')
    ymax = max(values)+2
    ymin = min(values)-2
    xmax = max(index)+1
    xmin = min(index)-1
    
	#getting data from the second sequence 
    keys2 = sorted(seq2.keys())
    index2 = [] 
    values2 = []
    #get the positions and values of the elements in the sequence
    for k2 in keys2:
        index2.append(k2)
        values2.append(seq2[k2])
    #get the limits of the axis plot
    #subplots.plot(index2, values2, 'go', alpha=0.5)
    markerline, stemlines, baseline = subplots.stem(index2,values2, 'g-.', 'go')
    #subplots.set_aspect('equal')
    fig.tight_layout()
    #adjusting the max and min values of the plot
    ymax = max(values+values2)+2
    ymin = min(values+values2)-2
    xmax = max(index+index2)+1
    xmin = min(index+index2)-1

    subplots.axis([xmin, xmax, ymin, ymax])
    plt.grid(True)
    plt.axhline(y=0, color='r')
    plt.show()

#reflection of a sequence (dictionary) 
def reflection_seq(seq):
    refl_seq = {}
    keys = seq.keys()
    for k in keys:
        refl_seq[k*(-1)] = seq[k]
    return refl_seq

#amplitude or attenuation of a sequence (dictionary)
def ampl_seq(seq, a):
    new_seq = {}
    keys = seq.keys()
    for k in keys:
        new_seq[k] = seq[k] * a
    return new_seq

#displacement of a sequence (dictionary)
def shift_seq(seq, n0):
    displ_seq = {}
    keys = seq.keys()
    for k in keys:
        displ_seq[k-n0]	= seq[k]
	return displ_seq

#decimated "diezmacion" of a sequence (dictionary), quit samples
def decim_seq(seq, n):
	decim_seq = {}
	seqa = {}
	keys = seq.keys()
	#print(type(keys))
	#print(keys)
	#get places of the sequence "jumping" over the n (n is the position), ignoring the left places
	for k in keys:
		#print seq[k]
		if k%n==0:
			seqa[k] = seq[k]

	#now is needed to "adjust" the value of the references
	#sort the keys to loop them, taking first the values after zero
	keys = sorted(seqa.keys())
	j=0
	for i in range(len(keys)):
		if(keys[i]>0):
			j=j+1
			decim_seq[j]=seqa[keys[i]]
		else:
			if(keys[i]==0):
				decim_seq[0]=seqa[keys[i]]

	#now invert the order of the keys, to adjust the values before zero
	j=0
	keys = keys[::-1]
	
	for i in range(len(keys)):
		if(keys[i]<0):
			j=j-1
			decim_seq[j]=seqa[keys[i]]
		else:
			if(keys[i]==0):
				decim_seq[0]=seqa[keys[i]]

	return decim_seq

#interpolation of a sequence (dictionary), add samples
def interp_seq(seq, n):
    inter_seq = {}
    seqa = {}
    keys = seq.keys()

	#get the values all the values of the sequence but "jumping" over the new sequence, lefting 'n-1' places 
    for k in keys:
        seqa[n*k] = seq[k]

    keys = sorted(seqa.keys())
    j=0
        #add the left spaces of the sequence
    #first, get the start and end to calculate the values of the left spaces
    for i in range(len(keys)):
        start=seqa[keys[i]]
        if i+1 < len(keys):
            end=seqa[keys[i+1]]
        else:
            end=0

        j=j+1

        for pp in range(1, n):
            if(end>start):
                seqa[keys[i] + pp] = start + ((abs((end-start)/n))*pp)

            if(end<start):
                seqa[keys[i] + pp] = start - ((abs((end-start)/n))*pp) 

            if(end==start):
                seqa[keys[i] + pp] = start + ((abs((end-start)/n))*pp)    
    
    return seqa

#ordinary convolution of two sequences (dictionaries) (sequences are not periodic)
def convolve(seq1, seq2):
    seq_result={}

    #reflect 'any' of the sequences, in this case, we selected the first
    seq1a, seq2a = complete_seqs(reflection_seq(seq1), seq2)

    #get the max and mins references of each sequence to do the loops (useful for the limits)
    n_max_seq1=max(seq1.keys())
    n_min_seq1=min(seq1.keys())

    n_max_seq2=max(seq2.keys())
    n_min_seq2=min(seq2.keys())

    seq1Keys=seq1a.keys()
    seq2Keys=seq2a.keys()    

    #sort the keys in order to multiply 'pair to pair' the values of the
    keys1 = sorted(seq1Keys)
    keys2 = sorted(seq2Keys)
    #this variable saves '0' if in the given index there is no value for the sequence, or simply the value if exists
    valorAux=0
    #'carry' for the sumatory
    saveAdd = 0
  
    #get the values fo the other side of the zero
    for mm in range(0, abs(n_min_seq1+n_min_seq2)+1):
        saveAdd=0
        for i in range(len(keys1)):
            if(i+mm < len(keys1)):
                if(keys1[i+mm] in seq1a):
                    valorAux = seq1a[keys1[i+mm]]
            else:
                valorAux = 0
            saveAdd = saveAdd + (valorAux*seq2a[keys2[i]])

        seq_result[mm]=saveAdd

    #the reflected sequence must be 'displaced' without changing its references
    for mm in range(0, (n_max_seq1+n_max_seq2)+1):
        saveAdd=0
        for i in range(len(keys1)):
            if(i-mm >= 0):
                if(keys1[i-mm] in seq1a):
                    valorAux = seq1a[keys1[i-mm]]
            else:
                valorAux = 0
            saveAdd = saveAdd + (valorAux*seq2a[keys2[i]])

        seq_result[(-1)*mm]=saveAdd

    return reflection_seq(seq_result)

    #convolution of a periodic sequence with a simple sequence.
    #Note: the periodic sequence must be only one period (not contains "repeated" or periodic values), including in it the value for n=0
def periodic_convolve(per_seq, seq2):
    seq_result = {}
    lenPerSeq = len(per_seq.keys())
    lenSeq2 = len(seq2.keys())

    rows = lenPerSeq
    cols = lenSeq2+lenPerSeq-1

    #bidimentional list to save the multiplication "element by element" of the sequences
    a = [[0 for col in range(cols)] for row in range(rows)]

    seqPerSortedK = sorted(per_seq.keys())
    seq2SortedK = sorted(seq2.keys())
    
    for i in range(len(seqPerSortedK)):
        for j in range(len(seq2SortedK)):
            a[i][j+i]=per_seq[seqPerSortedK[i]]*seq2[seq2SortedK[j]]

    for(i) in range(rows):
        print a[i]

    colsAdd=[]
    addByColumn=0
    for j in range(cols):
        for i in range(rows):
            addByColumn+=a[i][j]
        colsAdd.append(addByColumn)
        addByColumn=0

    finalValues=[0]*len(seqPerSortedK)

    for i in range(len(colsAdd)):
        finalValues[i%len(seqPerSortedK)] += colsAdd[i]

    for i in range(min(seqPerSortedK) + min (seq2SortedK), min(seqPerSortedK) + min (seq2SortedK)+ len(finalValues)):
        seq_result[i]=finalValues[i%len(finalValues)]

    return seq_result

    #convolution of a pair of periodic sequences.
    #Note: the sequence must be only one period (not contains "repeated" or periodic values), including in it the value for n=0
def circular_convolve(per_seq, seq2):
    seq_result = {}

    lenPerSeq = len(per_seq.keys())
    lenSeq2 = len(seq2.keys())

    rows = lenPerSeq
    cols = lenSeq2+lenPerSeq-1

    #bidimentional list to save the multiplication "element by element" of the sequences
    a = [[0 for col in range(cols)] for row in range(rows)]

    seqPerSortedK = sorted(per_seq.keys())
    seq2SortedK = sorted(seq2.keys())
    
    for i in range(len(seqPerSortedK)):
        for j in range(len(seq2SortedK)):
            a[i][j+i]=per_seq[seqPerSortedK[i]]*seq2[seq2SortedK[j]]
            print 'per_seq[seqPerSortedK[i]]', per_seq[seqPerSortedK[i]]
            print 'seq2[seq2SortedK[j]]', seq2[seq2SortedK[j]]
    for(i) in range(rows):
        print a[i]

    colsAdd=[]
    addByColumn=0
    for j in range(cols):
        for i in range(rows):
            addByColumn+=a[i][j]
        colsAdd.append(addByColumn)
        addByColumn=0

    maxPeriod=max(len(per_seq.keys()), len(seq2.keys()))
    print '..',colsAdd

    finalValues=[0]*(len(seqPerSortedK) + maxPeriod%len(seqPerSortedK))

    for i in range(len(colsAdd)):
        finalValues[i%maxPeriod] += colsAdd[i]

    print 'fVals=',finalValues

    for i in range(min(seqPerSortedK) + min (seq2SortedK), min(seqPerSortedK) + min (seq2SortedK)+ len(finalValues)):
        seq_result[i]=finalValues[i%len(finalValues)]


    return seq_result

if __name__=='__main__':  
    seq1 = build_dict('3*, 6, 2')
    seq2 = build_dict('-1*, 4')
    #seq1 = build_dict('1, 0, -4*, 3')
    #seq2 = build_dict('1*, 2, 3')
    #auxiliary sequences for operate 
    seq1a, seq2a = complete_seqs(seq1, seq2)
    
    """
    #sequence1
    #plot_sequence(seq1)
    print('sequence1 =', build_seq(seq1a))
    #reflection of sequence1
    refl_seq = reflection_seq(seq1)
    #plot_sequence(refl_seq)
    print('seq1(-n) =', build_seq(refl_seq))
    #sequence2
    #plot_sequence(seq2)
    print('sequence2 =', build_seq(seq2))
    #operations with sequence1 and sequence2
    result = basic_operation_seq(seq1a, seq2a, 'mult')
    #plot_sequence(result)
    print('seq1 * seq2 =', build_seq(result))

    #operations with sequence1 and sequence2
    result = basic_operation_seq(seq1a, seq2a, 'add')
    #plot_sequence(result)
    print('seq1 + seq2 =', build_seq(result))
	"""
	#displacement of a sequence
    print 'seq1(n)=', build_seq((seq1))
    #displacement of a sequence
    print build_seq(circular_convolve(seq1, seq2))
    #plot_two_sequences(seq1,interp_seq(seq1, 1))
