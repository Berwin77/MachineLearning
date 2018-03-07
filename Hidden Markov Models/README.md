### 用HMM(隐形马尔科夫模型)对诗歌进行分词

*TrainHMM.py* ：是通过已经切分好词的文件pku_training.utf8来得到HMM的初始概率矩阵pi 转移矩阵A 和 发射矩阵B

*Segmentation.py* ：是一个例子：给定了一段朱自清的《春》，是通过1.py求出的pi A B 进行分词。

*Spring.txt* ：朱自清的散文《春》。