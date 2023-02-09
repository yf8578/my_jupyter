# input1="C:/Users/10696/Desktop/hisat280_082.non_rRNa_id.r1.txt"
# #逐行读取input1，将每行内容拆分，只删除第一个@前的内容，输出到新文件中时还原@符号
# with open(input1) as f:
#     lines = f.readlines()
#     with open("C:/Users/10696/Desktop/hisat280_082.non_rRNa_id.r1_1.txt", "w") as f1:
#         for line in lines:
#             line = line.split("@")[1] ##    #删除@前的内容
#             f1.write("@" + line)    ##    #还原@符号


import sys
input=sys.argv[1]
output=sys.argv[2]
#逐行读取input1，以|为分隔符，只保留第一部分，随后只删除@SYN_前的内容，输出到新文件中时还原@SYN_符号
with open(str(input)) as f:
    lines = f.readlines()
    with open(str(output), "w") as f1:
        for line in lines:
            line = line.split("_1_.")[0] ##    #以|为分隔符，只保留第一部分
            line1=line.split("@SYN_")[1] ##    #删除@SYN_前的内容
            f1.write("@SYN_"+line1+"\n")    ##    #还原@SYN_符号
            
            
    
    
    
            