# [剑指 Offer II 040. 矩阵中最大的矩形](https://leetcode.cn/problems/PLYXKQ)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定一个由&nbsp;<code>0</code> 和 <code>1</code>&nbsp;组成的矩阵 <code>matrix</code>&nbsp;，找出只包含 <code>1</code> 的最大矩形，并返回其面积。</p>

<p><strong>注意：</strong>此题 <code>matrix</code>&nbsp;输入格式为一维 <code>01</code> 字符串数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/lcof2/%E5%89%91%E6%8C%87%20Offer%20II%20040.%20%E7%9F%A9%E9%98%B5%E4%B8%AD%E6%9C%80%E5%A4%A7%E7%9A%84%E7%9F%A9%E5%BD%A2/images/maximal.jpg" style="width: 402px; height: 322px;" /></p>

<pre>
<strong>输入：</strong>matrix = ["10100","10111","11111","10010"]
<strong>输出：</strong>6
<strong>解释：</strong>最大矩形如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["0"]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["1"]
<strong>输出：</strong>1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["00"]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[0].length</code></li>
	<li><code>0 &lt;= row, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 85 题相同（输入参数格式不同）：&nbsp;<a href="https://leetcode.cn/problems/maximal-rectangle/">https://leetcode.cn/problems/maximal-rectangle/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python

```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java

```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if(matrix.length==0){
            return 0;
        }
        int[] heights = new int[matrix[0].length];
        int max_res = 0;
        for(int ii=0;ii<matrix.length;ii++){
            //遍历String 加到heights上 并计算最大面积
            for(int jj=0;jj<heights.length;jj++){
                // if(matrix[ii].charAt(jj)=='1'){
                if(matrix[ii][jj]=='1'){
                    heights[jj] += 1;
                }
                else{
                    //断掉--清零
                    heights[jj] = 0;
                }
            }
            //计算
            max_res = Math.max(max_res,largestRectangleArea(heights));
        }
        return max_res;
    }

    //使用上一题的一维数组计算方法
    public int largestRectangleArea(int[] heights) {
        //类似盛水最多的容器  但不同
        //https://leetcode-cn.com/problems/container-with-most-water/

        //利用栈实现
        Deque<Integer> stack1 = new ArrayDeque<>();
        stack1.addLast(-1);

        int res = 0;
        for(int ii=0;ii<heights.length;ii++){
            while(stack1.peekLast()!=-1 && heights[stack1.peekLast()]>=heights[ii]){
                //退栈并比较
                int temp_height = heights[stack1.pollLast()];
                int temp_width = ii - 1 - stack1.peekLast();
                
                res = Math.max(res,temp_height*temp_width);
            }
            //入栈 每次都要入
            stack1.addLast(ii);
        }

        //最后清空
        while(stack1.peekLast()!=-1){
            //退栈并比较
            int temp_height = heights[stack1.pollLast()];
            int temp_width = heights.length - 1 - stack1.peekLast();
            res = Math.max(res,temp_height*temp_width);
        }
        return res;
    }
}
```

<!-- tabs:end -->
