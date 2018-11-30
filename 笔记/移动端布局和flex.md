## 移动端布局的步骤：

1. 修改视口

   ```html
   <meta name="viewport" content="width=device-width">
   ```

2. 引入rem.js    em为当前字体的倍率

   ```html
   <script src="js/rem.js"></script>
   ```

3. 修改rem.js中设计稿的宽度

   100px=1rem

   ​

   ## 背景图片

   ```
   先为盒子设大小
   //引入背景图片   禁止重复  位置（top left right bottom）
   background:url() no-repeat left bottom
   //设置背景图片的大小
   background-size:100% 100%;
   background-size:contain;  //按照宽高中的较大者进行缩放
   background-size:cover;  //按照宽高中的较小者进行缩放
   ```

   ## 线性渐变：

   ```css
   background:linear-gradient(top,颜色，颜色，..);
   参数意义：第一个参数：渐变开始的方向top.left.bottom.right.25deg
    		颜色：渐变的颜色变化。
   ```

   ## 浏览器内核：

   ```css
   /* 谷歌内核 */
   	background: url('../img/screen.png') no-repeat bottom/contain,-webkit-linear-gradient(top,#3bbcff,#47eaff); 
   	/* 火狐内核 */
   	background: -moz-linear-gradient(top,#3bbcff,#47eaff); 
   	/* ie内核 */
   	background:-ms- linear-gradient(top,#3bbcff,#47eaff);
   ```

   ## flex弹性布局

   #### 容器属性（在父元素中设置）

   1. flex-direction属性    `flex-direction`属性决定主轴的方向（即项目的排列方向）

      ```css
      .box {
        flex-direction: row | row-reverse | column | column-reverse;
      }
      row（默认值）：主轴为水平方向，起点在左端。
      row-reverse：主轴为水平方向，起点在右端。
      column：主轴为垂直方向，起点在上沿。
      column-reverse：主轴为垂直方向，起点在下沿
      ```

   2. justify-content属性  `justify-content`属性定义了项目在主轴上的对齐方式。

      ```css
      .box {
        justify-content: flex-start | flex-end | center | space-between | space-around;
      }
      它可能取5个值，具体对齐方式与轴的方向有关。下面假设主轴为从左到右。
      flex-start（默认值）：左对齐
      flex-end：右对齐
      center： 居中
      space-between：两端对齐，项目之间的间隔都相等。
      space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一
      ```

   3. flex-wrap属性  决定项目换行（默认为不换行）

      ```css
      .box{
        flex-wrap: nowrap | wrap | wrap-reverse;
      }
      （1）nowrap（默认）：不换行。
      （2）wrap：换行，第一行在上方。
      （3）wrap-reverse：换行，第一行在下方。
      ```

   4. justify-content属性  定义了项目在主轴上的对齐方式。

      ```css
      .box {
        justify-content: flex-start | flex-end | center | space-between | space-around;
      }
      flex-start（默认值）：左对齐  主轴的起点
      flex-end：右对齐   主轴的终点
      center： 居中     主轴的中心
      space-between：两端对齐，项目之间的间隔都相等。
      space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍.
      ```

   5.align-items:定义项目在交叉轴上的对齐方式（适用于一根轴线与多根轴线）

   ```css
   .box {
     align-items: flex-start | flex-end | center | baseline | stretch;
   }
   ```

   ​

   - flex-start  交叉轴的起点
   - flex-end   交叉轴的终点
   - center     交叉轴的中心
   - baseline  基线对齐（文本底部对齐）

   6.`align-content`属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。

   ```css
   .box {
     align-content: flex-start | flex-end | center | space-between | space-around | stretch;
   }
   ```

   ​

   - `flex-start`：与交叉轴的起点对齐。

   - `flex-end`：与交叉轴的终点对齐。

   - `center`：与交叉轴的中点对齐。

   - `space-between`：与交叉轴两端对齐，轴线之间的间隔平均分布。

   - `space-around`：每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。

   - `stretch`（默认值）：轴线占满整个交叉轴。

     #### 项目属性（在子元素中定义）

     1. order属性：定义项目的排列顺序，数值越小越靠前，默认值为0.

        ```css
        item {
          order: <integer>;
        }
        可为负值
        ```

     2. `flex-grow`属性定义项目的放大比例，默认为`0`，即如果存在剩余空间，也不放大。

        ```csss
        .item {
          flex-grow: <number>; /* default 0 */
        }
        如果所有项目的flex-grow属性都为1，则它们将等分剩余空间（如果有的话）。如果一个项目的flex-grow属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。
        ```

        3.`flex-shrink`属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。

     ```css
     .item {
       flex-shrink: <number>; /* default 1 */
     }
     如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。
     负值对该属性无效。
     flex-shrink:0;  项目不缩小
     ```

     ​    4.align-self:定义单个项目在交叉轴上的对齐方式     `align-self`属性允许单个项目有与其他项目不一样的对齐方式，可覆盖`align-items`属性。默认值为`auto`，表示继承父元素的`align-items`属性，如果没有父元素，则等同于`stretch`。

     ```css
     .item {
       align-self: auto | flex-start | flex-end | center | baseline | stretch;
     }
     	flex-start  交叉轴起点

     	flex-end   交叉轴终点

     	center   中心

     ```

     5.`flex-basis`属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为`auto`，即项目的本来大小。

     ```css
     item {
       flex-basis: <length> | auto; /* default auto */
     }
     它可以设为跟width或height属性一样的值（比如350px），则项目将占据固定空间。
     ```


​              display:flex;为父元素指定弹性布局（当子元素宽度不够是默认令子元素缩小）在父元素中命令
​		flex-shrink：0;即使空间不足，子元素也不缩小   在子元素中命令
​		overflow-x:auto;超出部分在x方向的表现形式/auto：自动。如果超出自动以滚动条的形式显示。  在父										    元素中命令
​		.recent-hours::-webkit-scrollbar{height: 0;}去掉滚动条

iscroll移动端上拉刷新插件

草料二维码生成器，测试移动端

手机浏览器全为-wedkit-内核

图片格式：jpg：有损压缩（大图一般采用）

​			png：无损压缩（小图一般采用，支持透明通道）

​		gif：有损压缩（支持帧动画，但压缩不如jpg）

微信浏览器：x4内核 