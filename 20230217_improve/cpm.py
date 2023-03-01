import pandas as pd
import sys
# 改输入
input_count_path = sys.argv[1]+''
# 读取，删除第一行
#####################
genes_counts = pd.read_csv(
    'D:\\githubku\\my_jupyter\\20230217_improve\\SGI75460067.gene_count.txt', sep=',', header=None)
genes_counts = genes_counts.drop(0, axis=0)
genes_counts_count = genes_counts.iloc[:, 1:].astype('int')
# 读取D:\githubku\my_jupyter\20230217_improve\nan_name_id.txt,列名设置为
# ['GeneID','id','Gene Name','type']
nan_name_id = pd.read_csv(
    'D:\\githubku\\my_jupyter\\20230217_improve\\nan_name_id.txt', sep='\t', header=None)
nan_name_id.columns = ['Gene ID', 'id', 'Gene Name', 'type']
nan_name_id.index = nan_name_id['Gene ID']
# genes_counts的0列按照|分割，变成三列
genes_counts = genes_counts[0].str.split('|', expand=True)
genes_counts = pd.concat([genes_counts, genes_counts_count], axis=1)
genes_counts.columns = ['Gene ID', 'Gene Name', 'count']
genes_counts_nan = genes_counts[genes_counts.isnull().values == True]
genes_counts_nan.index = genes_counts_nan['Gene ID']
# 遍历genes_counts_nan的GeneID列，获得nan_name_id中对应的Gene Name
for nan_id in genes_counts_nan['Gene ID']:
    genes_counts_nan.loc[nan_id,
                         'Gene Name'] = nan_name_id.loc[nan_id, 'Gene Name']
    # 删除genes_counts中包含nan的行
genes_counts = genes_counts.dropna(axis=0)
# 删除genes_counts_nan中的索引
genes_counts_nan = genes_counts_nan.reset_index(drop=True)
genes_counts = pd.concat([genes_counts, genes_counts_nan], axis=0)
# 将相同的Gene Name的count相加
genes_counts = genes_counts.groupby('Gene Name',).mean(numeric_only=True)
# 计算cpm
genes_counts['cpm'] = genes_counts['count']/genes_counts['count'].sum()*1000000
name_cpm = genes_counts[['cpm']]
name_cpm.to_csv('D:\\githubku\\my_jupyter\\20230217_improve\\name_cpm.txt',
                sep='\t', index=True, header=True)
