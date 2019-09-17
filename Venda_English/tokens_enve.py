#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install sacremoses


# In[ ]:


import subprocess
import string
from sacremoses import MosesTokenizer

mtok = MosesTokenizer(lang='en')

# ENGLISH 
with open('data/en_ve/enve_parallel.train.tok.en', 'w') as f:
    for line in open('data/en_ve/enve_parallel.train.en'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line))) 

with open('data/en_ve/enve_parallel.dev.tok.en', 'w') as f:
    for line in open('data/en_ve/enve_parallel.dev.en'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line))) 

with open('data/en_ve/enve_parallel.test.tok.en', 'w') as f:
    for line in open('data/en_ve/enve_parallel.test.en'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line))) 

# AFRIKAANS 
with open('data/en_ve/enve_parallel.train.tok.ve', 'w') as f:
    for line in open('data/en_ve/enve_parallel.train.ve'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line))) 

with open('data/en_ve/enve_parallel.dev.tok.ve', 'w') as f:
    for line in open('data/en_ve/enve_parallel.dev.ve'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line)))

with open('data/en_ve/enve_parallel.test.tok.ve', 'w') as f:
    for line in open('data/en_ve/enve_parallel.test.ve'):
        s1 = ' '
        f.write("%s\n" % s1.join(mtok.tokenize(line))) 

# Limit sentence length to 80
subprocess.Popen(['perl','/home/explore/smt/mosesdecoder/scripts/training/clean-corpus-n.perl', 'data/en_ve/enve_parallel.train.tok', 've', 'en', 'data/en_ve/enve_parallel.train.clean', '1', '80'])
subprocess.Popen(['perl','/home/explore/smt/mosesdecoder/scripts/training/clean-corpus-n.perl', 'data/en_ve/enve_parallel.dev.tok', 've', 'en', 'data/en_ve/enve_parallel.dev.clean', '1', '80'])
subprocess.Popen(['perl','/home/explore/smt/mosesdecoder/scripts/training/clean-corpus-n.perl', 'data/en_ve/enve_parallel.test.tok', 've', 'en', 'data/en_ve/enve_parallel.test.clean', '1', '80'])

