from pandas import DataFrame
import xlsxwriter
import xlrd
import pandas as pd
import os
import numpy as np
import sys
count_path = r"C:\Users\zhangyifan1\Desktop\work\0217\type_count"  # count文件夹路径
tpm_path = r"C:\Users\zhangyifan1\Desktop\work\0217\tpm_count"  # tpm文件夹路径
output_count = r"C:\Users\zhangyifan1\Desktop\work\0217\count.xlsx"  # '.xlsx'，合并后的count文件
output_tpm = r"C:\Users\zhangyifan1\Desktop\work\0217\tpm.xlsx"  # '.xlsx'，合并后的tpm文件
# '.xlsx'，合并成一个excel表，包含tpm和count两个sheet"  # count文件夹路径
final_output = r"C:\Users\zhangyifan1\Desktop\work\0217\final.xlsx"
# count_path = sys.argv[1]  # count文件夹路径
# tpm_path = sys.argv[2]  # tpm文件夹路径
# output_count = sys.argv[3]  # '.xlsx'，合并后的count文件
# output_tpm = sys.argv[4]  # '.xlsx'，合并后的tpm文件
# final_output = sys.argv[5]  # '.xlsx'，合并成一个excel表，包含tpm和count两个sheet
file_listcount = os.listdir(count_path)
# 删除文件名中的.gene_tpm.txt，赋值给变量file_tpmname
file_countname = [file.split('.')[0] for file in file_listcount]
# 创建一个空的dataframe，以file_name作为索引，列名分别为all_mapped_reads，lncRNA，lncRNA-ratio，miRNA，miRNA-ratio，	other，other-ratio，protein_coding，protein_coding-ratio，pseudo，pseudo-ratio，rRNA，rRNA-ratio，scRNA，scRNA-ratio，snoRNA。snoRNA-ratio，snRNA，snRNA-ratio，tRNA，tRNA-ratio，Mt_tRNA，Mt_tRNA-ratio，Mt_rRNA，Mt_rRNA-ratio，misc_RNA，misc_RNA-ratio
df = pd.DataFrame(index=file_countname, columns=['all_mapped_reads', 'lncRNA', 'lncRNA-ratio', 'miRNA', 'miRNA-ratio', 'other', 'other-ratio', 'protein_coding', 'protein_coding-ratio', 'pseudo', 'pseudo-ratio',
                  'rRNA', 'rRNA-ratio', 'scRNA', 'scRNA-ratio', 'snoRNA', 'snoRNA-ratio', 'snRNA', 'snRNA-ratio', 'tRNA', 'tRNA-ratio', 'Mt_tRNA', 'Mt_tRNA-ratio', 'Mt_rRNA', 'Mt_rRNA-ratio', 'misc_RNA', 'misc_RNA-ratio'])
# 遍历file_list中的文件名，保存为变量file，读取文件，赋值给变量df1，将df1中的索引对应的值查找到df对应的列名中
for file in file_listcount:
    df1 = pd.read_csv(count_path+'/'+file, index_col=0)
    df.loc[file.split('.')[0], 'all_mapped_reads'] = df1.sum()[0]
    df.loc[file.split('.')[0], 'lncRNA'] = df1.loc['lncRNA'][0]
    df.loc[file.split('.')[0], 'miRNA'] = df1.loc['miRNA'][0]
    df.loc[file.split('.')[0], 'other'] = df1.loc['other'][0]
    df.loc[file.split('.')[0], 'protein_coding'] = df1.loc['protein_coding'][0]
    df.loc[file.split('.')[0], 'pseudo'] = df1.loc['pseudo'][0]
    df.loc[file.split('.')[0], 'rRNA'] = df1.loc['rRNA'][0]
    df.loc[file.split('.')[0], 'scRNA'] = df1.loc['scRNA'][0]
    df.loc[file.split('.')[0], 'snoRNA'] = df1.loc['snoRNA'][0]
    df.loc[file.split('.')[0], 'snRNA'] = df1.loc['snRNA'][0]
    df.loc[file.split('.')[0], 'tRNA'] = df1.loc['tRNA'][0]
    df.loc[file.split('.')[0], 'Mt_tRNA'] = df1.loc['Mt_tRNA'][0]
    df.loc[file.split('.')[0], 'Mt_rRNA'] = df1.loc['Mt_rRNA'][0]
    df.loc[file.split('.')[0], 'misc_RNA'] = df1.loc['misc_RNA'][0]
    # 计算比例
    df.loc[file.split('.')[0],
           'lncRNA-ratio'] = df1.loc['lncRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'miRNA-ratio'] = df1.loc['miRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'other-ratio'] = df1.loc['other'][0]/df1.sum()[0]
    df.loc[file.split(
        '.')[0], 'protein_coding-ratio'] = df1.loc['protein_coding'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'pseudo-ratio'] = df1.loc['pseudo'][0]/df1.sum()[0]
    df.loc[file.split('.')[0], 'rRNA-ratio'] = df1.loc['rRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'scRNA-ratio'] = df1.loc['scRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'snoRNA-ratio'] = df1.loc['snoRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'snRNA-ratio'] = df1.loc['snRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0], 'tRNA-ratio'] = df1.loc['tRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'Mt_tRNA-ratio'] = df1.loc['Mt_tRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'Mt_rRNA-ratio'] = df1.loc['Mt_rRNA'][0]/df1.sum()[0]
    df.loc[file.split('.')[0],
           'misc_RNA-ratio'] = df1.loc['misc_RNA'][0]/df1.sum()[0]
    # 计算总数
# 保存为xlsx文件
df.to_excel(output_count)

# 打开文件夹，读取文件名
file_listtpm = os.listdir(tpm_path)
# 删除文件名中的.gene_tpm.txt，前缀赋值给变量file_tpmname
file_tpmname = [file.split('.')[0] for file in file_listtpm]
# 创建一个空的dataframe，列名分别为lncRNA_TPM>0	lncRNA_TPM>1	lncRNA_TPM>5	lncRNA_TPM>10	miRNA_TPM>0	miRNA_TPM>1	miRNA_TPM>5	miRNA_TPM>10	other_TPM>0	other_TPM>1	other_TPM>5	other_TPM>10	protein_coding_TPM>0	protein_coding_TPM>1	protein_coding_TPM>5	protein_coding_TPM>10	pseudo_TPM>0	pseudo_TPM>1	pseudo_TPM>5	pseudo_TPM>10	rRNA_TPM>0	rRNA_TPM>1	rRNA_TPM>5	rRNA_TPM>10	scRNA_TPM>0	scRNA_TPM>1	scRNA_TPM>5	scRNA_TPM>10	snoRNA_TPM>0	snoRNA_TPM>1	snoRNA_TPM>5	snoRNA_TPM>10	snRNA_TPM>0	snRNA_TPM>1	snRNA_TPM>5	snRNA_TPM>10	tRNA_TPM>0	tRNA_TPM>1	tRNA_TPM>5	tRNA_TPM>10		Mt_rRNA_TPM>0 	Mt_rRNA_TPM>1 	Mt_rRNA_TPM>5 	Mt_rRNA_TPM>10 Mt_tRNA_TPM>0	Mt_tRNA_TPM>1	Mt_tRNA_TPM>5	Mt_tRNA_TPM>10 misc_RNA_TPM>0	misc_RNA_TPM>1	misc_RNA_TPM>5	misc_RNA_TPM>10
df2 = pd.DataFrame(index=file_tpmname, columns=['lncRNA_TPM>0', 'lncRNA_TPM>1', 'lncRNA_TPM>5', 'lncRNA_TPM>10', 'miRNA_TPM>0', 'miRNA_TPM>1', 'miRNA_TPM>5', 'miRNA_TPM>10', 'other_TPM>0', 'other_TPM>1', 'other_TPM>5', 'other_TPM>10', 'protein_coding_TPM>0', 'protein_coding_TPM>1', 'protein_coding_TPM>5', 'protein_coding_TPM>10', 'pseudo_TPM>0', 'pseudo_TPM>1', 'pseudo_TPM>5', 'pseudo_TPM>10', 'rRNA_TPM>0', 'rRNA_TPM>1', 'rRNA_TPM>5', 'rRNA_TPM>10',
                   'scRNA_TPM>0', 'scRNA_TPM>1', 'scRNA_TPM>5', 'scRNA_TPM>10', 'snoRNA_TPM>0', 'snoRNA_TPM>1', 'snoRNA_TPM>5', 'snoRNA_TPM>10', 'snRNA_TPM>0', 'snRNA_TPM>1', 'snRNA_TPM>5', 'snRNA_TPM>10', 'tRNA_TPM>0', 'tRNA_TPM>1', 'tRNA_TPM>5', 'tRNA_TPM>10', 'Mt_rRNA_TPM>0', 'Mt_rRNA_TPM>1', 'Mt_rRNA_TPM>5', 'Mt_rRNA_TPM>10', 'Mt_tRNA_TPM>0', 'Mt_tRNA_TPM>1', 'Mt_tRNA_TPM>5', 'Mt_tRNA_TPM>10', 'misc_RNA_TPM>0', 'misc_RNA_TPM>1', 'misc_RNA_TPM>5', 'misc_RNA_TPM>10'])
# 读取tpm文件夹中的文件
for file in file_listtpm:
    # 读取文件
    df2_tpm = pd.read_csv(tpm_path+'/' + file, sep=',', index_col=0)
    # 获取每个文件中的TPM>0的数量
    df2.loc[file.split('.')[0],
            'lncRNA_TPM>0'] = df2_tpm.loc['lncRNA', 'TPM>0']
    df2.loc[file.split('.')[0], 'miRNA_TPM>0'] = df2_tpm.loc['miRNA', 'TPM>0']
    df2.loc[file.split('.')[0], 'other_TPM>0'] = df2_tpm.loc['other', 'TPM>0']
    df2.loc[file.split(
        '.')[0], 'protein_coding_TPM>0'] = df2_tpm.loc['protein_coding', 'TPM>0']
    df2.loc[file.split('.')[0],
            'pseudo_TPM>0'] = df2_tpm.loc['pseudo', 'TPM>0']
    df2.loc[file.split('.')[0], 'rRNA_TPM>0'] = df2_tpm.loc['rRNA', 'TPM>0']
    df2.loc[file.split('.')[0], 'scRNA_TPM>0'] = df2_tpm.loc['scRNA', 'TPM>0']
    df2.loc[file.split('.')[0],
            'snoRNA_TPM>0'] = df2_tpm.loc['snoRNA', 'TPM>0']
    df2.loc[file.split('.')[0], 'snRNA_TPM>0'] = df2_tpm.loc['snRNA', 'TPM>0']
    df2.loc[file.split('.')[0], 'tRNA_TPM>0'] = df2_tpm.loc['tRNA', 'TPM>0']
    df2.loc[file.split('.')[0],
            'Mt_rRNA_TPM>0'] = df2_tpm.loc['Mt_rRNA', 'TPM>0']
    df2.loc[file.split('.')[0],
            'Mt_tRNA_TPM>0'] = df2_tpm.loc['Mt_tRNA', 'TPM>0']
    df2.loc[file.split('.')[0],
            'misc_RNA_TPM>0'] = df2_tpm.loc['misc_RNA', 'TPM>0']
    # 获取每个文件中的TPM>1的数量
    df2.loc[file.split('.')[0],
            'lncRNA_TPM>1'] = df2_tpm.loc['lncRNA', 'TPM>1']
    df2.loc[file.split('.')[0], 'miRNA_TPM>1'] = df2_tpm.loc['miRNA', 'TPM>1']
    df2.loc[file.split('.')[0], 'other_TPM>1'] = df2_tpm.loc['other', 'TPM>1']
    df2.loc[file.split(
        '.')[0], 'protein_coding_TPM>1'] = df2_tpm.loc['protein_coding', 'TPM>1']
    df2.loc[file.split('.')[0],
            'pseudo_TPM>1'] = df2_tpm.loc['pseudo', 'TPM>1']
    df2.loc[file.split('.')[0], 'rRNA_TPM>1'] = df2_tpm.loc['rRNA', 'TPM>1']
    df2.loc[file.split('.')[0], 'scRNA_TPM>1'] = df2_tpm.loc['scRNA', 'TPM>1']
    df2.loc[file.split('.')[0],
            'snoRNA_TPM>1'] = df2_tpm.loc['snoRNA', 'TPM>1']
    df2.loc[file.split('.')[0], 'snRNA_TPM>1'] = df2_tpm.loc['snRNA', 'TPM>1']
    df2.loc[file.split('.')[0], 'tRNA_TPM>1'] = df2_tpm.loc['tRNA', 'TPM>1']
    df2.loc[file.split('.')[0],
            'Mt_rRNA_TPM>1'] = df2_tpm.loc['Mt_rRNA', 'TPM>1']
    df2.loc[file.split('.')[0],
            'Mt_tRNA_TPM>1'] = df2_tpm.loc['Mt_tRNA', 'TPM>1']
    df2.loc[file.split('.')[0],
            'misc_RNA_TPM>1'] = df2_tpm.loc['misc_RNA', 'TPM>1']
    # 获取每个文件中的TPM>5的数量
    df2.loc[file.split('.')[0],
            'lncRNA_TPM>5'] = df2_tpm.loc['lncRNA', 'TPM>5']
    df2.loc[file.split('.')[0], 'miRNA_TPM>5'] = df2_tpm.loc['miRNA', 'TPM>5']
    df2.loc[file.split('.')[0], 'other_TPM>5'] = df2_tpm.loc['other', 'TPM>5']
    df2.loc[file.split(
        '.')[0], 'protein_coding_TPM>5'] = df2_tpm.loc['protein_coding', 'TPM>5']
    df2.loc[file.split('.')[0],
            'pseudo_TPM>5'] = df2_tpm.loc['pseudo', 'TPM>5']
    df2.loc[file.split('.')[0], 'rRNA_TPM>5'] = df2_tpm.loc['rRNA', 'TPM>5']
    df2.loc[file.split('.')[0], 'scRNA_TPM>5'] = df2_tpm.loc['scRNA', 'TPM>5']
    df2.loc[file.split('.')[0],
            'snoRNA_TPM>5'] = df2_tpm.loc['snoRNA', 'TPM>5']
    df2.loc[file.split('.')[0], 'snRNA_TPM>5'] = df2_tpm.loc['snRNA', 'TPM>5']
    df2.loc[file.split('.')[0], 'tRNA_TPM>5'] = df2_tpm.loc['tRNA', 'TPM>5']
    df2.loc[file.split('.')[0],
            'Mt_rRNA_TPM>5'] = df2_tpm.loc['Mt_rRNA', 'TPM>5']
    df2.loc[file.split('.')[0],
            'Mt_tRNA_TPM>5'] = df2_tpm.loc['Mt_tRNA', 'TPM>5']
    df2.loc[file.split('.')[0],
            'misc_RNA_TPM>5'] = df2_tpm.loc['misc_RNA', 'TPM>5']
    # 获取每个文件中的TPM>10的数量
    df2.loc[file.split('.')[0],
            'lncRNA_TPM>10'] = df2_tpm.loc['lncRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'miRNA_TPM>10'] = df2_tpm.loc['miRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'other_TPM>10'] = df2_tpm.loc['other', 'TPM>10']
    df2.loc[file.split(
        '.')[0], 'protein_coding_TPM>10'] = df2_tpm.loc['protein_coding', 'TPM>10']
    df2.loc[file.split('.')[0],
            'pseudo_TPM>10'] = df2_tpm.loc['pseudo', 'TPM>10']
    df2.loc[file.split('.')[0], 'rRNA_TPM>10'] = df2_tpm.loc['rRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'scRNA_TPM>10'] = df2_tpm.loc['scRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'snoRNA_TPM>10'] = df2_tpm.loc['snoRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'snRNA_TPM>10'] = df2_tpm.loc['snRNA', 'TPM>10']
    df2.loc[file.split('.')[0], 'tRNA_TPM>10'] = df2_tpm.loc['tRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'Mt_rRNA_TPM>10'] = df2_tpm.loc['Mt_rRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'Mt_tRNA_TPM>10'] = df2_tpm.loc['Mt_tRNA', 'TPM>10']
    df2.loc[file.split('.')[0],
            'misc_RNA_TPM>10'] = df2_tpm.loc['misc_RNA', 'TPM>10']
# 保存结果为excel文件
df2.to_excel(output_tpm)

# output_tpm、output_count两个文件合并到一个excel文件的不同sheet中
# 读取文件
df1 = pd.read_excel(output_tpm)
df2 = pd.read_excel(output_count)
# 创建一个excel文件
writer = pd.ExcelWriter(final_output, engine='xlsxwriter')
# 将df1写入excel文件的第一个sheet中
df1.to_excel(writer, sheet_name='TPM', index=False)
# 将df2写入excel文件的第二个sheet中
df2.to_excel(writer, sheet_name='RNA-type', index=False)
# 保存文件
writer.save()
