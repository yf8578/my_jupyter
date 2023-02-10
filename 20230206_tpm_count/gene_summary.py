# 导入pandas库
import pandas as pd
import sys


# 传入参数input1<stringtie/.gene_abund.txt>,inpu2<result_summary/.gene_count.txt>
# output1< >,output2
ref = sys.argv[1]
input1 = sys.argv[2]
input2 = sys.argv[3]
output1 = sys.argv[4]
output2 = sys.argv[5]
# ref1 = 'C:/Users/10696/Desktop/bgi/task/06_RNAseq/gene_summary/output/merge1.txt'
# input1 = 'C:/Users/10696/Desktop/bgi/task/06_RNAseq/gene_summary/input/E-B21419995415-4.gene_abund.txt'
# input2 = "C:\\Users\\10696\\Desktop\\bgi\\task\\06_RNAseq\\gene_summary\\input\\E-B21419995415-4.gene_count.txt"
# output1 = "C:\\Users\\10696\\Desktop\\bgi\\task\\06_RNAseq\\gene_summary\\output\\E-B21419995415-4.gene_stringtieabund_add.txt"
# output2 = "C:\\Users\\10696\\Desktop\\bgi\\task\\06_RNAseq\\gene_summary\\output\\E-B21419995415-4.gene_result_summarycount_add.txt"

# 以csv格式读入ref文件，tab为分隔符,列名分别设置为id，Gene Name，type，
ref1_file = pd.read_csv(ref, sep='\t',engine='python')
# 获取ref1_file的type列，去重,保存为dataframe类型,赋值给变量type_tpm,添加四列TPM>0,TPM>1,TPM>5,TPM>10
type_tpm = pd.DataFrame(ref1_file['Gene type'].unique())
type_tpm.columns = ['Gene type']
type_tpm['TPM>0'] = 0
type_tpm['TPM>1'] = 0
type_tpm['TPM>5'] = 0
type_tpm['TPM>10'] = 0

## 挑出NAME和type
# ref1_file中删除Gene Name列重复的行，保存为变量Name_type
Name_type = ref1_file.drop_duplicates(subset=['Gene Name'], keep='first')
# delete the column Gene ID,ENST
Name_type = Name_type.drop(['Gene ID', 'ENST'], axis=1)

## 挑出ENST和type

# 保留ref1_file中ENST和Gene type列，保存为变量ENST_type
ENST_type = ref1_file[['ENST', 'Gene type']]
# 删除ENST_type中ENST列为0的数据
ENST_type = ENST_type[ENST_type['ENST'] != '0']
# 删除ENST_type中ENST列重复的数据
ENST_type = ENST_type.drop_duplicates(['ENST'])

## 挑出GeneID和type
# 保留ref1_file中Gene ID和Gene type列，保存为变量ENST_type,删除ENST_type中ENST列重复的数据
Gene_ID_type = ref1_file[['Gene ID', 'Gene type']]
Gene_ID_type = Gene_ID_type.drop_duplicates(['Gene ID'])

##挑出unassigned_type和type
# 获取ref1_file中Gene ID以unassigned开头的数据,保存为变量unassigned_type
unassigned_type = ref1_file[ref1_file['Gene ID'].str.contains('unassigned_transcript_', na=False)]
##***********PART1 START***********##

# 以csv格式读入input1文件，以tab为分隔符，不设置列名，保留第二列和最后一列数据
input1_file = pd.read_csv(input1, sep='\t', usecols=["Gene ID", "Gene Name", "TPM"],engine='python')

# 将input1_file的Gene ID列中nan的数据替换为unknown
input1_file['Gene ID'] = input1_file['Gene ID'].fillna('unknown')
# 获取input1_file的Gene ID列中ENST开头的数据
input1_ENST = input1_file[input1_file['Gene ID'].str.startswith('ENST')]
# 获取input1_file的Gene ID列中unknown开头的数据
input1_unknown = input1_file[input1_file['Gene ID'].str.startswith('unknown')]

# 获取input1_file中Gene ID列只包含数字的数据
input1_number = input1_file[input1_file['Gene ID'].str.isdigit()]
# 获取input1_file中Gene ID列不只包含纯数字和不含ENST和unknown的数据
input1_other = input1_file[~input1_file['Gene ID'].str.isdigit()]
input1_other = input1_other[~input1_other['Gene ID'].str.startswith('ENST')]
input1_other = input1_other[~input1_other['Gene ID'].str.startswith('unknown')]

# 处理ENST开头的数据
# 以input1_ENST的Gene ID和ref1_file的ENST为键，input1_ENST为主表，合并input1_ENST和ref1_file，保存为变量ENST_tpm，并输出
ENST_tpm = pd.merge(input1_ENST, ENST_type, left_on='Gene ID', right_on='ENST', how='left')
# 获取ENST_tpm中Gene type列为nan的数据m_nan
ENST_tpm_nan = ENST_tpm[ENST_tpm['Gene type'].isnull()]
# ENST_tpm_nan保留Gene ID、Gene Name和TPM列
ENST_tpm_nan = ENST_tpm_nan[['Gene ID', 'Gene Name', 'TPM']]
# 删除ENST_tpm中Gene type列为nan的数据
ENST_tpm = ENST_tpm[ENST_tpm['Gene type'].notnull()]

ENST_tpm_df = type_tpm
# 遍历ENST_tpm_df索引，统计type_tpmTPM>0,TPM>1,TPM>5,TPM>10的数量
for i in ENST_tpm_df.index:
    ENST_tpm_type = ENST_tpm[ENST_tpm['Gene type'] == ENST_tpm_df.loc[i, 'Gene type']]
    for j in ENST_tpm_type.index:
        if ENST_tpm_type.loc[j, 'TPM'] > 0:
            ENST_tpm_df.loc[i, 'TPM>0'] += 1
        if ENST_tpm_type.loc[j, 'TPM'] > 1:
            ENST_tpm_df.loc[i, 'TPM>1'] += 1
        if ENST_tpm_type.loc[j, 'TPM'] > 5:
            ENST_tpm_df.loc[i, 'TPM>5'] += 1
        if ENST_tpm_type.loc[j, 'TPM'] > 10:
            ENST_tpm_df.loc[i, 'TPM>10'] += 1

# 以input1_number的Gene ID和ref1_file的Gene ID为键，input1_number为主表，合并input1_number和ref1_file，保存为变量Gene_ID_tpm，并输出
Gene_ID_tpm = pd.merge(input1_number, Gene_ID_type, left_on='Gene ID', right_on='Gene ID', how='left')

# 获得Gene_ID_tpm中Gene type为nan的数据，保存为变量Gene_ID_tpm_nan
Gene_ID_tpm_nan = Gene_ID_tpm[Gene_ID_tpm['Gene type'].isnull()]
# 保留Gene_ID_tpm_nan的Gene ID、Gene Name和TPM列
Gene_ID_tpm_nan = Gene_ID_tpm_nan[['Gene ID', 'Gene Name', 'TPM']]
# 删除Gene_ID_tpm中Gene type为nan的数据
Gene_ID_tpm = Gene_ID_tpm[Gene_ID_tpm['Gene type'].notnull()]

######只能通过gene name来进行比对的数据，还有一部分不能通过gene name查到
# 合并Gene_ID_tpm_nan、ENST_tpm_nan、input1_other、input1_unknown
input1_byname = pd.concat([Gene_ID_tpm_nan, ENST_tpm_nan, input1_other, input1_unknown])
# 以input1_byname的Gene Name和ref1_file的Gene Name为键，input1_byname为主表
Name_tpm = pd.merge(input1_byname, Name_type, left_on='Gene Name', right_on='Gene Name', how='left')
# 遍历NAME_tpm_df索引，统计NAME_tpm_dfTPM>0,TPM>1,TPM>5,TPM>10的数量
NAME_tpm_df = type_tpm
for i in NAME_tpm_df.index:
    # 获取Name_tpm中Gene type为NAME_tpm_df中Gene type的数据
    Name_tpm_type = Name_tpm[Name_tpm['Gene type'] == NAME_tpm_df.loc[i, 'Gene type']]
    # 遍历Name_tpm_type索引，统计TPM>0,TPM>1,TPM>5,TPM>10的数量
    for j in Name_tpm_type.index:
        if Name_tpm_type.loc[j, 'TPM'] > 0:
            NAME_tpm_df.loc[i, 'TPM>0'] += 1
        if Name_tpm_type.loc[j, 'TPM'] > 1:
            NAME_tpm_df.loc[i, 'TPM>1'] += 1
        if Name_tpm_type.loc[j, 'TPM'] > 5:
            NAME_tpm_df.loc[i, 'TPM>5'] += 1
        if Name_tpm_type.loc[j, 'TPM'] > 10:
            NAME_tpm_df.loc[i, 'TPM>10'] += 1

# 遍历ID_tpm_df索引，统计ID_tpm_dfTPM>0,TPM>1,TPM>5,TPM>10的数量
ID_tpm_df = type_tpm
for i in ID_tpm_df.index:
    ID_tpm_type = Gene_ID_tpm[Gene_ID_tpm['Gene type'] == ID_tpm_df.loc[i, 'Gene type']]
    for j in ID_tpm_type.index:
        if ID_tpm_type.loc[j, 'TPM'] > 0:
            ID_tpm_df.loc[i, 'TPM>0'] += 1
        if ID_tpm_type.loc[j, 'TPM'] > 1:
            ID_tpm_df.loc[i, 'TPM>1'] += 1
        if ID_tpm_type.loc[j, 'TPM'] > 5:
            ID_tpm_df.loc[i, 'TPM>5'] += 1
        if ID_tpm_type.loc[j, 'TPM'] > 10:
            ID_tpm_df.loc[i, 'TPM>10'] += 1

type_tpm.to_csv(output1, index=False)
print('finished'+str(output1))
# *********************************PART1 END*********************************#

# *********************************PART2 START*********************************#
# 以csv格式读入input2文件，以,分隔，不设置列名，删除第一行
input2_file = pd.read_csv(input2, sep=',', header=None, skiprows=1,engine='python')
# 第一列按照|分隔，保存为变量input2_file1
input2_file1 = input2_file[0].str.split('|', expand=True)
# 将input2_file1和input2_file合并，保存为变量input2_file
input2_file = pd.concat([input2_file1, input2_file[1]], axis=1)
input2_file.columns = ['Gene ID', 'Gene Name', 'count']
input2_file = input2_file.reset_index(drop=True)

# 获取input2_file中Gene ID以ENST开头的数据
input2_ENST = input2_file[input2_file['Gene ID'].str.contains('ENST')]
# 获取input2_file中Gene ID中纯数字的数据
input2_ID = input2_file[input2_file['Gene ID'].str.contains('^[0-9]+$')]
# 获得input2_file中Gene ID包含unassigned的数据
input2_unassigned = input2_file[input2_file['Gene ID'].str.contains('unassigned')]
# 获得input2_file中Gene ID不是纯数字，也不是以ENST开头的数据
input2_other = input2_file[~input2_file['Gene ID'].str.contains('^[0-9]+$')]
input2_other = input2_other[~input2_other['Gene ID'].str.contains('ENST')]
input2_other = input2_other[~input2_other['Gene ID'].str.contains('unassigned')]

# 将input2_ENST和ENST_type合并，以Gene ID为键，以input2_ENST为主表，保存为变量input2_ENST_type
input2_ENST_type = pd.merge(input2_ENST, ENST_type, right_on='ENST', left_on='Gene ID', how='left')
# 将input2_ID和ID_type合并，以Gene ID为键，保存为变量input2_ID_type
input2_ID_type = pd.merge(input2_ID, Gene_ID_type, on='Gene ID', how='left')
# 将input2_unassigned和unassigned_type合并，以Gene ID为键，保存为变量input2_unassigned_type
input2_unassigned_type = pd.merge(input2_unassigned, unassigned_type, on='Gene ID', how='left')

# 将input2_ENST_type中Gene type为nan的数据
input2_ENST_type_nan = input2_ENST_type[input2_ENST_type['Gene type'].isnull()]
# 获取input2_ID_type中Gene type为nan的数据
input2_ID_type_nan = input2_ID_type[input2_ID_type['Gene type'].isnull()]
# 将input2_ID_type_nan前三列和input2_other合并
input2_other = pd.concat([input2_ID_type_nan.iloc[:, :3], input2_other], axis=0)
# 将input2_other和Name_type合并，以Gene Name为键，保存为变量input2_other_type
input2_other_type = pd.merge(input2_other, Name_type, on='Gene Name', how='left')

# 统计input2_ENST_type、input2_ID_type、input2_unassigned_type、input2_other_type中每个Gene type对应的count
input2_ENST_type_count = input2_ENST_type.groupby('Gene type')['count'].sum()
input2_ID_type_count = input2_ID_type.groupby('Gene type')['count'].sum()
input2_unassigned_type_count = input2_unassigned_type.groupby('Gene type')['count'].sum()
input2_other_type_count = input2_other_type.groupby('Gene type')['count'].sum()

# 将input2_ENST_type_count、input2_ID_type_count、input2_unassigned_type_count、input2_other_type_count合并，以Gene
# type为键，保存为变量input2_type_count
input2_type_count = pd.concat([input2_ENST_type_count, input2_ID_type_count, input2_unassigned_type_count, input2_other_type_count], axis=0)
input2_type_count = input2_type_count.reset_index()
input2_type_count.columns = ['Gene type', 'count']
input2_type_count = input2_type_count.groupby('Gene type')['count'].sum()
input2_type_count = input2_type_count.reset_index()
input2_type_count.to_csv(output2, index=False)
print('finished'+str(output2))
