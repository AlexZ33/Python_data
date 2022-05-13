- [3blue1brown的视频 : 《线性代数的本质》](https://www.bilibili.com/video/BV1ys411472E?spm_id_from=333.788.b_636f6d6d656e74.78)
- [3Blue1Brown的数学基础](https://space.bilibili.com/88461692)
- B站线性代数视频教程 [MIT线性代数【全】](https://www.bilibili.com/video/BV1Kt411y7jN/)
    - [麻省理工公开课：线性代数](https://open.163.com/newview/movie/courseintro?newurl=%2Fspecial%2Fopencourse%2Fdaishu.html&utm_source=weibolife)
    - [mit官网上的exam、assignments、教材和答案的pdf文档]()
    - [MIT线性代数课程笔记](./MIT线性代数公开课笔记.pdf)
    - 
- [B站最强学习资源汇总](https://www.jiqizhixin.com/articles/2020-04-14-3)
- 吴恩达机器学习：https://www.bilibili.com/video/BV164411b7dx
- 《程序员数学：用Python学透线性代数和微积分》
  - 
- 吴恩达深度学习：https://www.bilibili.com/video/BV164411m79z
- Pytorch实战：
- Tensorflow实战：https://www.bilibili.com/video/BV1Zt411T7zE

- 毕设项目推荐https://www.zhihu.com/question/325011850/answer/1915328146
# 情感分析
- 基于机器学习的商品评论情感分析，使用 Selenium 模拟真实登录行为，爬取数据。使用 jieba 分词，分类模型采用机器学习算法SVM 和深度学习算法 LSTM。
- https://github.com/20100507/emotional_analysis

# 舆情分析
- 利用微博热点话题舆情聚类分析，主要功能包括爬取微博数据，微博数据文本处理，特征向量提取，Kmeans 聚类。
- https://github.com/pengLP/sina_analysis

这个项目只是使用了简单的聚类算法 Kmeans，如果大家那这个项目作为自己的毕业设计，我觉得可以调研深度学习相关的算法，看几篇 Paper，有能力复现一下再进行改进，只要有了数据你就能搞很多事情，按照我的思路应付本科毕业设计足够了，硕士就算了，估计开题都过不了。

如果这个项目爬取的数据没办法满足你的需求，你可以去这个库看看，一个非常好用的微博爬虫。

https://github.com/dataabc/weiboSpider

# 图片分类
这个 GitHub 项目就很多了，你可以直接 GitHub 搜索关键字「Pytorch 图片分类」或者「TensorFlow 图片分类」，比如有猫狗分类等等。如果你做图片分类，技术路线大体是一样的，都是基于卷积神经网络来做。但是你需要改一改，怎么改呢 ? 我举个栗子：你可以做疾病分类，网上有很多的开源数据集，判断一张图片是猫还是狗和判断一张图片有没有病本质上是一样的。如果你想搞一些花里胡哨的东西，可以借助注意力机制把病灶找出来，最终的效果就是：输入一张医疗图片，会输出这张图片患病概率，而且把这张图片上的病灶高亮出来。
