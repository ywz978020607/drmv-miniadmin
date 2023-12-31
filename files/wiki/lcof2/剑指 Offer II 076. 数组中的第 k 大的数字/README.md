# [剑指 Offer II 076. 数组中的第 k 大的数字](https://leetcode.cn/problems/xx4gT2)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定整数数组 <code>nums</code> 和整数 <code>k</code>，请返回数组中第 <code><strong>k</strong></code> 个最大的元素。</p>

<p>请注意，你需要找的是数组排序后的第 <code>k</code> 个最大的元素，而不是第 <code>k</code> 个不同的元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,1,5,6,4] 和</code> k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6] 和</code> k = 4
<strong>输出:</strong> 4</pre>

<p>&nbsp;</p>

<p><strong>提示： </strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 215&nbsp;题相同：&nbsp;<a href="https://leetcode.cn/problems/kth-largest-element-in-an-array/">https://leetcode.cn/problems/kth-largest-element-in-an-array/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

快速排序 partition 实现。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(left, right, k):
            if left == right:
                return nums[left]
            i, j = left - 1, right + 1
            x = nums[(left + right) >> 1]
            while i < j:
                while 1:
                    i += 1
                    if nums[i] >= x:
                        break
                while 1:
                    j -= 1
                    if nums[j] <= x:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if j < k:
                return quick_sort(j + 1, right, k)
            return quick_sort(left, j, k)

        n = len(nums)
        return quick_sort(0, n - 1, n - k)
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        return quickSort(nums, 0, n - 1, n - k);
    }

    private int quickSort(int[] nums, int left, int right, int k) {
        if (left == right) {
            return nums[left];
        }
        int i = left - 1, j = right + 1;
        int x = nums[(left + right) >>> 1];
        while (i < j) {
            while (nums[++i] < x);
            while (nums[--j] > x);
            if (i < j) {
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
            }
        }
        if (j < k) {
            return quickSort(nums, j + 1, right, k);
        }
        return quickSort(nums, left, j, k);

    }
}
```

### **C++**

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        return quickSort(nums, 0, n - 1, n - k);
    }

    int quickSort(vector<int>& nums, int left, int right, int k) {
        if (left == right) return nums[left];
        int i = left - 1, j = right + 1;
        int x = nums[left + right >> 1];
        while (i < j)
        {
            while (nums[++i] < x);
            while (nums[--j] > x);
            if (i < j) swap(nums[i], nums[j]);
        }
        return j < k ? quickSort(nums, j + 1, right, k) : quickSort(nums, left, j, k);
    }
};
```

### **Go**

```go
func findKthLargest(nums []int, k int) int {
	n := len(nums)
	return quickSort(nums, 0, n-1, n-k)
}

func quickSort(nums []int, left, right, k int) int {
	if left == right {
		return nums[left]
	}
	i, j := left-1, right+1
	x := nums[(left+right)>>1]
	for i < j {
		for {
			i++
			if nums[i] >= x {
				break
			}
		}
		for {
			j--
			if nums[j] <= x {
				break
			}
		}
		if i < j {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	if j < k {
		return quickSort(nums, j+1, right, k)
	}
	return quickSort(nums, left, j, k)
}
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    private static final Random rand = new Random();
    public int findKthLargest(int[] nums, int k) {
        // 堆排序 改
        PriorityQueue<Integer> pri = new PriorityQueue<>(k, (a,b)->(a-b)); //使用默认的最小堆
        for(int ii=0;ii<nums.length;ii++){
            if(ii < k){
                pri.add(nums[ii]);
            }
            else if(ii >= k && nums[ii] > pri.peek()){
                pri.remove();
                pri.add(nums[ii]);
            }   
        }
        return pri.peek();
    }
}
```

### **ywz_1**

```java
class Solution {
    private static final Random rand = new Random();
    public int findKthLargest(int[] nums, int k) {
        // 快排 改
        k -= 1; // 从0开始
        int left = 0, right = nums.length - 1;
        int ret_idx = quicksort(nums, left, right);
        while(ret_idx!=k){
            if(ret_idx<k){
                left = ret_idx + 1;
            }
            else{
                right = ret_idx - 1;
            }
            ret_idx = quicksort(nums, left, right);
        }
        return nums[ret_idx];
    }

    public int quicksort(int[] nums, int left, int right){
        int temp_start = left;
        int sel = rand.nextInt(right - left + 1) + left;
        //exchange
        swap(nums, sel, right);
        for(int ii=left;ii<right;ii++){
            if(nums[ii] > nums[right]){ //> 降序
                //exchange
                swap(nums, ii, temp_start);
                //move temp_start
                temp_start++;
            }
        }
        //exchange
        swap(nums, temp_start, right);
        return temp_start; //一轮排序后的标定的索引位置
    }

    public void swap(int[] nums, int index1, int index2){
        if(index1 == index2){
            return;
        }
        nums[index1] += nums[index2];
        nums[index2] = nums[index1] - nums[index2];
        nums[index1] = nums[index1] - nums[index2];
    }
}
```

<!-- tabs:end -->
