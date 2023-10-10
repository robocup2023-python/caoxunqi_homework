
import sys
import argparse
import pathlib
import os

print(sys.argv)

parser = argparse.ArgumentParser()

parser.add_argument('--a',type=int, help='operator A')


parser.add_argument('--path',type=str,help='path_of_csv')
parser.add_argument('--number',type=str,help='number_of_delete')
args =parser.parse_args()
print(args)

import pandas as pd

df = pd.DataFrame(pd.read_csv(args.path,header=0))
print('original:\n',df)
df=df.drop(args.number,axis=1)
print('after_delete:\n',df)
