# pearson
# View(input1)
library("Hmisc")
library("psych")
############################################################################################ SGI75460067
path1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\type_RF_star\\tpm\\SGI75460067\\"
outputpath1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\type_RF_star\\sum\\tpm\\SGI75460067sum.txt"
# 创建一个空的dataframe,行名分别为Mt_rRNA,Mt_tRNA,lncRNA,miRNA,misc_RNA,other,protein_coding,pseudo,rRNA,scRNA,snRNA,snoRNA,tRNA
aaa <- data.frame(matrix(nrow = 13, ncol = 2))
# 将行名分别赋值为Mt_rRNA,Mt_tRNA,lncRNA,miRNA,misc_RNA,other,protein_coding,pseudo,rRNA,scRNA,snRNA,snoRNA,tRNA
rownames(aaa) <- c("Mt_rRNA", "Mt_tRNA", "lncRNA", "miRNA", "misc_RNA", "other", "protein_coding", "pseudo", "rRNA", "scRNA", "snRNA", "snoRNA", "tRNA")
# 列名分别为“rf：fr","rf:star","fr:star"
colnames(aaa) <- c("cpm_RFfr:cpm_star_r", "cpm_RFfr:cpm_star_p")
# 遍历读取D:\githubku\my_jupyter\20230206_tpm_count\final\12\SGI75460067\文件夹中的文件
for (i in list.files(path1)) {
    # 读取D:\githubku\my_jupyter\20230206_tpm_count\final\12\SGI75460067\文件夹中的文件
    input1 <- read.table(paste(path1, i, sep = ""), header = T, sep = "\t", check.names = F, stringsAsFactors = F)
    # 获得第一列的名字，去重，保存为变量rna_type
    rna_type <- unique(input1[, 1])
    # 删除input1前两列
    input1 <- input1[, -c(1:2)]
    # 分别计算input1中rf列和fr列，rf列和star列，以及fr列和star列皮尔斯相关系数，以及p值
    # print(cor.test(input1$fr,input1$rf,method = 'pearson',minlength=5),digits=10,exact=FALSE)
    rffr <- cor.test(input1$tpm_RFfr, input1$tpm_star, method = "pearson", exact = FALSE)

    # 以rna_type为索引分别将rf:fr,rf:star,fr:star的皮尔斯相关系数和p值赋值给aa
    # 获取aaa中行名为lncRNA，列名为rf:fr的值
    aaa[rna_type, "cpm_RFfr:cpm_star_r"] <- rffr$estimate
    aaa[rna_type, "cpm_RFfr:cpm_star_p"] <- rffr$p.value
}
View(aaa)
# 将aaa保存为csv文件
write.csv(aaa, file = outputpath1, row.names = T)
























############################################################################################################

# 输入文件D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\cpmSGI75460067.txt
cpm1 <- read.table("D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\sample_RF_star\\cpm\\cpmSGI75460067.txt", header = T, sep = "\t", check.names = F, stringsAsFactors = F)

View(cpm1)
cor.test(cpm1$count_RFfr, cpm1$count_star, method = "pearson")


# 遍历文件夹中的文件，获取文件名
# 创建一个空的dataframe，列名分别为RFfr:star_r,RFfr:star_p
cpm_df <- data.frame(matrix(, ncol = 2))
colnames(cpm_df) <- c("RFfr:star_r", "RFfr:star_p")
# 遍历读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
path1 <- "D:/githubku/my_jupyter/20230206_tpm_count/0215cpm_tpm_pearson/cpm_tpm/sample_RF_star/cpm/"
outputpath1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\sample_RF_star\\cpmsum.csv"
for (i in list.files(path1)) {
    # 读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
    input1 <- read.table(paste(path1, i, sep = ""), header = T, sep = "\t", check.names = F, stringsAsFactors = F)
    # 以文件名为索引分别将rf:fr,rf:star,fr:star的皮尔斯相关系数和p值赋值给aa
    # 文件名删除前面的"tpm"和后面的".txt""
    i <- substr(i, 4, nchar(i) - 4)
    pea <- cor.test(input1$cpm_RFfr, input1$cpm_star, method = "pearson", exact = FALSE)
    cpm_df[i, "RFfr:star_r"] <- pea$estimate
    cpm_df[i, "RFfr:star_p"] <- pea$p.value # nolint
}
# 将aaa保存为csv文件
# 删除第一行
cpm_df <- cpm_df[-1, ]
write.csv(cpm_df, file = outputpath1, row.names = T)

cor.test(input1$tpm_RFfr, input1$tpm_star, method = "pearson", exact = FALSE)$p.value # nolint












############################################ cpm########################
# 遍历文件夹中的文件，获取文件名
# 创建一个空的dataframe，列名分别为RFfr:star_r,RFfr:star_p
cpm_df <- data.frame(matrix(, ncol = 2))
colnames(cpm_df) <- c("RFfr:star_r", "RFfr:star_p")
# 遍历读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
path1 <- "D:/githubku/my_jupyter/20230206_tpm_count/0215cpm_tpm_pearson/cpm_tpm/sample_RF_star/cpm/"
outputpath1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\sample_RF_star\\cpmsum1.csv"
for (i in list.files(path1)) {
    # 读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
    input1 <- read.table(paste(path1, i, sep = ""), header = T, sep = "\t", check.names = F, stringsAsFactors = F)
    # 以文件名为索引分别将rf:fr,rf:star,fr:star的皮尔斯相关系数和p值赋值给aa
    # 文件名删除前面的"tpm"和后面的".txt""
    i <- substr(i, 4, nchar(i) - 4)
    cpm_df[i, "RFfr:star_r"] <- cor.test(input1$cpm_RFfr, input1$cpm_star, method = "pearson", exact = FALSE)$estimate
    cpm_df[i, "RFfr:star_p"] <- cor.test(input1$cpm_RFfr, input1$cpm_star, method = "pearson", exact = FALSE)$p.value # nolint
}
# 将aaa保存为csv文件
# 删除第一行
cpm_df <- cpm_df[-1, ]
write.csv2(cpm_df, file = outputpath1, row.names = T)





# 输入文件D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\cpmSGI75460067.txt
cpm1 <- read.table("D:\\githubku\\my_jupyter\\20230206_tpm_count\\0215cpm_tpm_pearson\\cpm_tpm\\sample_RF_star\\cpm\\cpmSGI75460067.txt", header = T, sep = "\t", check.names = F, stringsAsFactors = F)

View(cpm1)
cor.test(cpm1$count_RFfr, cpm1$count_star, method = "pearson")

#########################################################################
# 遍历文件夹中的文件，获取文件名
# 创建一个空的dataframe，列名分别为RFfr:star_r,RFfr:star_p
cpm_df <- data.frame(matrix(, ncol = 6))
colnames(cpm_df) <- c("rf:fr_r", "rf:fr_p", "rf:star_r", "rf:star_p", "fr:star_r", "fr:star_p")
# 遍历读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
path1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\final\\12\\sample\\cpm\\"
outputpath1 <- "D:\\githubku\\my_jupyter\\20230206_tpm_count\\final\\12\\sample\\sum\\cpmtsum.csv"
for (i in list.files(path1)) {
    # 读取D:\githubku\my_jupyter\20230206_tpm_count\0215cpm_tpm_pearson\cpm_tpm\sample_RF_star\cpm\文件夹中的文件
    input1 <- read.table(paste(path1, i, sep = ""), header = T, sep = "\t", check.names = F, stringsAsFactors = F)
    # 以文件名为索引分别将rf:fr,rf:star,fr:star的皮尔斯相关系数和p值赋值给aa
    # 文件名删除前面的"tpm"和后面的".txt""
    rffr <- cor.test(input1$rf, input1$fr, method = "pearson", exact = FALSE)
    rfstar <- cor.test(input1$rf, input1$star, method = "pearson", exact = FALSE)
    frstar <- cor.test(input1$fr, input1$star, method = "pearson", exact = FALSE)
    cpm_df[i, "rf:fr_r"] <- rffr$estimate
    cpm_df[i, "rf:fr_p"] <- rffr$p.value # nolint
    cpm_df[i, "rf:star_r"] <- rfstar$estimate
    cpm_df[i, "rf:star_p"] <- rfstar$p.value # nolint
    cpm_df[i, "fr:star_r"] <- frstar$estimate
    cpm_df[i, "fr:star_p"] <- frstar$p.value # nolint
}
# 将aaa保存为csv文件
# 删除第一行
write.csv(cpm_df, file = outputpath1, row.names = T)
