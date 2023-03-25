import sys

KM=sys.argv[1]
OUTPUT=sys.argv[2]
a=0
kmer={}
s288c=0
for line in open(KM,'r'):
	l=line.strip().split()
	if a==0:spel=l[1:];a+=1
	if l[1:].count('0')>0:kmer[l[0]]=l[1:];print(len(l[1:]))

fout = open(OUTPUT, 'w')
fout.write("##fileformat='VCFv4" + '\n')
fout.write('##FORMAT=<ID=GT, Number=1, Type=String, Description="Genotype"' + '\n')
fout.write('##contig=<ID=1, Description="Virtual chromosome for VCF"' + '\n')
fout.write('#' + '\t'.join(['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'] + spel)+'\n')
pos=0
for key,freq in kmer.items():
#    print(len(freq));input()
	pos+=1
	context = ['1', str(pos), key, 'G', 'T', '.', '.', '.', 'GT']
	bifreq=[]
	for i in freq:
		if i=='0':bifreq.append('0')
		else:bifreq.append('1')
	fout.write('\t'.join(context + bifreq) + '\n')
fout.close()
################################################################################
print('Done')
