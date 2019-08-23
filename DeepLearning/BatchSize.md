# 关于BatchSize


-----


### 直观的理解： 
Batch Size定义：一次训练所选取的样本数。 
Batch Size的大小影响模型的优化程度和速度。同时其直接影响到GPU内存的使用情况，假如你GPU内存不大，该数值最好设置小一点。

在小样本数的数据库中，不使用Batch Size是可行的，而且效果也很好。但是一旦是大型的数据库，一次性把所有数据输进网络，肯定会引起内存的爆炸。所以就提出Batch Size的概念。

### Batch Size从小到大的变化对网络影响 
1、没有Batch Size，梯度准确，只适用于小样本数据库 
2、Batch Size=1，梯度变来变去，非常不准确，网络很难收敛。 
3、Batch Size增大，梯度变准确， 
4、Batch Size增大，梯度已经非常准确，再增加Batch Size也没有用

**注意：Batch Size增大了，要到达相同的准确度，必须要增大epoch。**

参考文档《神经网络中Batch Size的理解》 [https://blog.csdn.net/qq_34886403/article/details/82558399](http://)

**iterations**
iterations（迭代）：每一次迭代都是一次权重更新，每一次权重更新需要batch_size个数据进行Forward运算得到损失函数，再BP算法更新参数。1个iteration等于使用batchsize个样本训练一次。

**epochs**
epochs被定义为向前和向后传播中所有批次的单次训练迭代。这意味着1个周期是整个输入数据的单次向前和向后传递。简单说，epochs指的就是训练过程中数据将被“轮”多少次，就这样。

训练集有1000个样本，batchsize=10，那么：
训练完整个样本集需要：
100次iteration，1次epoch。

具体的计算公式为：
> one epoch = numbers of iterations = N = 训练样本的数量/batch_size
> 
在LSTM中我们还会遇到一个seq_length,其实
> batch_size = num_steps * seq_length
