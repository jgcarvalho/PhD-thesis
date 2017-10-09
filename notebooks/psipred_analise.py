from glob import glob 
from pandas import DataFrame 
import os

def q3(df,at='ALL3'):
    eq = df[df[at] == df['PSIPRED']]
    valid = df[df[at] != '?']
    return eq.shape[0]/valid.shape[0]

def qh(df,at='ALL3'):
    eq = df[(df[at] == df['PSIPRED']) & (df['PSIPRED'] == 'H') ]
    valid = df[df[at] == 'H']
    if valid.shape[0] == 0:
        return 
    else:
        return eq.shape[0]/valid.shape[0]

def qe(df,at='ALL3'):
    eq = df[(df[at] == df['PSIPRED']) & (df['PSIPRED'] == 'E') ]
    valid = df[df[at] == 'E']
    if valid.shape[0] == 0:
        return 
    else:
        return eq.shape[0]/valid.shape[0]

def qc(df,at='ALL3'):
    eq = df[(df[at] == df['PSIPRED']) & (df['PSIPRED'] == 'C') ]
    valid = df[df[at] == 'C']
    if valid.shape[0] == 0:
        return 
    else:
        return eq.shape[0]/valid.shape[0]

def save_q3(out_file):
    with open(out_file,'w') as f:
        f.write('PDB, CONSENSUS, DSSP, STRIDE, KAKSI, PROSS\n')
        for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
            # print(fn)
            df = DataFrame.from_csv(fn)
            id = os.path.basename(fn)
            f.write('{}, {}, {}, {}, {}, {}\n'.format(id, q3(df), q3(df,at='DSSP'), q3(df,at='STRIDE'), q3(df,at='KAKSI'), q3(df,at='PROSS')))
    
def save_qh(out_file):
    with open(out_file,'w') as f:
        f.write('PDB, CONSENSUS, DSSP, STRIDE, KAKSI, PROSS\n')
        for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
            # print(fn)
            df = DataFrame.from_csv(fn)
            id = os.path.basename(fn)
            f.write('{}, {}, {}, {}, {}, {}\n'.format(id, qh(df), qh(df,at='DSSP'), qh(df,at='STRIDE'), qh(df,at='KAKSI'), qh(df,at='PROSS')))

def save_qe(out_file):
    with open(out_file,'w') as f:
        f.write('PDB, CONSENSUS, DSSP, STRIDE, KAKSI, PROSS\n')
        for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
            # print(fn)
            df = DataFrame.from_csv(fn)
            id = os.path.basename(fn)
            f.write('{}, {}, {}, {}, {}, {}\n'.format(id, qe(df), qe(df,at='DSSP'), qe(df,at='STRIDE'), qe(df,at='KAKSI'), qe(df,at='PROSS')))

def save_qc(out_file):
    with open(out_file,'w') as f:
        f.write('PDB, CONSENSUS, DSSP, STRIDE, KAKSI, PROSS\n')
        for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
            # print(fn)
            df = DataFrame.from_csv(fn)
            id = os.path.basename(fn)
            f.write('{}, {}, {}, {}, {}, {}\n'.format(id, qc(df), qc(df,at='DSSP'), qc(df,at='STRIDE'), qc(df,at='KAKSI'), qc(df,at='PROSS')))

def main():
    # save_q3('psipred_results_q3.csv')
    # save_qh('psipred_results_qh.csv')
    save_qe('psipred_results_qe.csv')
    save_qc('psipred_results_qc.csv')
        

if __name__ == '__main__':
    main()