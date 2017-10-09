from glob import glob 
from pandas import DataFrame 
import os
import numpy as np
import seaborn as sns

def true_ss(df, ss, at='ALL3'):
    true = df[df[at] == ss]
    pred_h = true[true['PSIPRED'] == 'H']
    pred_e = true[true['PSIPRED'] == 'E']
    pred_c = true[true['PSIPRED'] == 'C']
    return (pred_h.shape[0], pred_e.shape[0], pred_c.shape[0])

def cm(df, at='ALL3'):
    return np.array([true_ss(df,x,at) for x in ['H','E','C']]).transpose()

def do_cm(method):
    confusion_matrix = np.zeros((3,3))
    for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
        # print('teste')
        df = DataFrame.from_csv(fn)
        confusion_matrix += cm(df, at=method)
        
    print(confusion_matrix)
    print(np.sum(confusion_matrix))
    confusion_matrix = confusion_matrix/np.sum(confusion_matrix)
    fig = sns.heatmap(confusion_matrix, annot=True,fmt=".1%", xticklabels=['H','E','C'], yticklabels=['H','E','C'], cbar=False, vmin=0.0, vmax=1.0, cmap='Blues')
    fig.set_xlabel('Estrutura secundária atribuída')
    fig.set_ylabel('Estrutura secundária predita')
    fig.set_title('Matriz de confusão (PROSS x PSIPRED)')
    fig.figure.savefig("../figures/psipred_pross_confusion_matrix.pdf")

    # with open(out_file,'w') as f:
    #     f.write('PDB, CONSENSUS, DSSP, STRIDE, KAKSI, PROSS\n')
    #     for fn in glob("/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/csv_results/*"):
    #         # print(fn)
    #         df = DataFrame.from_csv(fn)
    #         id = os.path.basename(fn)
    #         f.write('{}, {}, {}, {}, {}, {}\n'.format(id, q3(df), q3(df,at='DSSP'), q3(df,at='STRIDE'), q3(df,at='KAKSI'), q3(df,at='PROSS')))
def main():
    do_cm('PROSS')

if __name__ == '__main__':
    main()