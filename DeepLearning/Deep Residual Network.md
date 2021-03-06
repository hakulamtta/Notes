# Deep Residual Network

-----

1. **理解**
将一串训练分成一个个block训练，让每一个block的误差最小，达到整体误差最小的目的，避免梯度弥散。

    对于常规网络（plain network），实验发现，随着网络层级不断增加，模型精度先是不断提升，然后回迅速下降。说明网络很深之后，深度网络就变得难以训练了。

2. **原因：梯度消失现象**
神经网络再反向传播过程中需要不断传播梯度（由链式求导法则决定），当网络层数加深时，梯度会在传播过程中逐渐消失。例如如果使用Sigmoid函数，对于幅度为1的信号，每向后传递一层，梯度就衰减为原来的0.25，层数越多，衰减越厉害，导致无法对前面网络层的权重进行有效调节。

    ![f40c633b-62d3-4c44-b5b0-22f225fac649.png](.assets/f40c633b-62d3-4c44-b5b0-22f225fac649.png)

   由于梯度消失现象的存在，我们引入深度残差网络，达到加深网络层数的同时避免梯度消失的目的。

3. **解决**
假设现在有一个较浅的网络，已经达到了接近饱和的准确率，在它后面加上几个恒等映射层（Identity Mapping：y=x），这样就增加了网络的深度，也不会代来误差上的增加。这就是ResNet的主要思想。

4. **ResNet**
   ![6d94688a-38b3-4924-96a2-2abfeb11496a.png](.assets/6d94688a-38b3-4924-96a2-2abfeb11496a.png)
   残差网络借鉴了高速网络跨层连接的思想，将带有权重的残差改为恒等映射。
   假设某段神经网络的输入为x，期望输出为H(x)，直接进行这样的学习，训练难度较大。
   
   所以在残差网络中，当大仙学习到较为饱和的准确率或者下层误差变大时，就将学习目标转变为恒等映射的学习，也就是使输入x近似于输出H(x)。
   
   由上图，通过捷径连接，我们的输出变成H(x)=F(x)+x，当F(x)=0时，即变为恒等映射。此时我们的学习目标转变为学习目标值H(x)与x的差值，即残差F(x)=H(x)-x。
   
   由此神经网络能够超越之前的约束，达到几十层甚至上千层，为高级语义特征提取和分类提供了可能。

5. **改进**

   《Identity Mappings in Deep Residual Networks》论文中提出了ResNet V2，将捷径连接中的非线性激活函数如ReLu替换为Identity Mappings，并在每一层中添加Batch Normalization，这样处理后的残差学习单元较之前更容易训练，拥有更强的泛化能力。
   
   
   