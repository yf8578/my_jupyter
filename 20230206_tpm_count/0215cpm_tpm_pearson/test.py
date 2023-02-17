
import pandas as pd
import os
# 合并同一批样本的tpm
inputfilefolder = "D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\RFfr\\tpm"
# 遍历文件夹的文件，将文件名保存到file_list中
file_list = os.listdir(inputfilefolder)
# 创建空dataframe
tpm_1 = pd.DataFrame()
# 遍历读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\RFfr\tpm中的文件,按照Gene Name合并
for i in file_list:
    file = pd.read_csv(inputfilefolder+"\\"+i, sep=",")
    # 按照Gene Name升序排列
    file = file.sort_values(by="Gene Name")
    # 文件名替换TPM作为列名
    i = i.replace("Name_tPM.csv", "")
    file.columns = ["Gene Name", i]
    # 将file合并到tpm_1中
    tpm_1 = pd.merge(tpm_1, file, left_on=None, right_on=None,
                     left_index=False, right_index=False)
# 输出tpm_1
print(tpm_1)
