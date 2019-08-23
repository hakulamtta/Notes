# Deep Residual Network for Steganalysis of Digital Images
-----
## 深度残差网络在数字图像隐写中的应用

深度残差网络在之前已经学习过，这篇论文主要讨论其在隐写中的应用。

### 关于激活函数的选择
   常见的激活函数：
   sigmoid: y = 1/(1 + e-x)
   tanh: y = (ex - e-x)/(ex + e-x)
   relu: y = max(0, x)
   ![627fa846-d132-42f7-a6f6-7f34e2daa784.png](.assets/627fa846-d132-42f7-a6f6-7f34e2daa784.png)
   相较而言，在隐藏层，tanh函数要优于sigmoid函数，可以认为是sigmoid的平移版本，优势在于其取值范围介于-1 ~ 1之间，数据的平均值为0，而不像sigmoid为0.5，有类似数据中心化的效果。

　　在输出层，sigmoid也许会优于tanh函数，原因在于你希望输出结果的概率落在0 ~ 1 之间，比如二元分类，sigmoid可作为输出层的激活函数。

　　实际应用中，特别是深层网络在训练时，tanh和sigmoid会在端值趋于饱和，造成训练速度减慢，故深层网络的激活函数默认大多采用relu函数，浅层网络可以采用sigmoid和tanh函数。
