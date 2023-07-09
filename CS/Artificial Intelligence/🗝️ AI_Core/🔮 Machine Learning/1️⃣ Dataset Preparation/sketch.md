
### 任务说明
1. 有很多标记工具可以选，我选择的是 Colabeler: http://www.colabeler.com
> 教程 https://blog.csdn.net/m0_43505377/article/details/101677346

2. 标记软件里使用位置标记，先在标记软件上标记完之后导出成xml文件，然后用python脚本把xml文件转换成yolo使用的txt文件，最后大家汇总到群里的时候只交txt文件，不用xml文件。软件默认会使用原图片的文件名来命名xml文件，所以最后提交的txt文件的文件名也是和图片文件名是相同的。

3. 需要提交的文件：（假设对Persian进行标记）
	1. [x] ～`Persian_train.txt`: 记录了Persian训练集的每个文件名，不用写出文件路径，一行一个文件名，类似下图～
	![](https://img-blog.csdnimg.cn/20210101010102119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L29KaVd1WHVhbg==,size_16,color_FFFFFF,t_70#pic_center)
	3. [x] `Persian_vali.txt`: 记录了Persian测试集的每个文件名。格式同上
	4. `Label/Persian/train`: 文件夹内包含了Persian每个训练集照片对应的txt标签文件
	5. `Label/Persian/vali`: 文件夹内包含了Persian每个测试集照片对应的txt标签文件

4. 如何转换？
参考这篇文章 🔗 https://blog.csdn.net/oJiWuXuan/article/details/107558286


### 任务分工
1. Persian, Ragdoll, 孙
2. Scottish fold, Singapur， 罗
3. Sphynx，林




4. 文件目录
```
├── data
│   ├── Annotations  进行 detection 任务时的标签文件，xml 形式，文件名与图片名一一对应
│   ├── images  存放 .jpg 格式的图片文件
│   ├── ImageSets  存放的是分类和检测的数据集分割文件，包含train.txt, val.txt,trainval.txt,test.txt

│   ├── labels  存放label标注信息的txt文件，与图片一一对应
```


