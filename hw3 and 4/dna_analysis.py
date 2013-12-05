# Name: Maggie Aaron
# Evergreen Login: aarmag22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)
# Homework 4: DNA analysis (Part 2)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###


# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0

# Number of A nucleotides seen so far.
a_count = 0
# Number of C nucleotides seen so far.
c_count = 0
# Number of G nucleotides seen so far.
g_count = 0
# Number of T nucleotides seen so far.
t_count = 0

# For each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1
        
    # if the nucleotide is an A
    if bp == 'A':
        # increment the count of a
        a_count = a_count + 1
    # if the nucleotide is a C
    if bp == 'C':
        # increment the count of c
        c_count = c_count + 1
    # if the nucleotide is a G
    if bp == 'G':
        # increment the count of g
        g_count = g_count + 1
    # if the nucleotide is a T
    if bp == 'T':
        # increment the count of t
        t_count = t_count + 1

gc_count = g_count + c_count
at_count = a_count + t_count

# Total count of A, C, G, and T nucleotides
sum_count = a_count + c_count + g_count + t_count        
# Sequence length 
seq_length = len(seq)


# Divide the gc_count by the sum_count
gc_content = float(gc_count) / sum_count
# Divide the at_count by the sum_count
at_content = float(at_count) / sum_count

# Compute the AT/GC ratio
atgc_ratio = float(at_count)/(gc_count)

# Categorize organisms
if (gc_content > .60):
    gc_class = 'high GC content'
elif (gc_content < .40):
    gc_class = 'low GC content'
else:
    gc_class = 'moderate GC content'

# Print the answers
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A-count:', a_count
print 'C-count:', c_count
print 'G-count:', g_count
print 'T-count:', t_count
print 'Sum count:', sum_count
print 'Total count:', total_count
print 'seq length:', seq_length
print 'AT/GC Ratio:', atgc_ratio
print 'GC Classification:', gc_class
