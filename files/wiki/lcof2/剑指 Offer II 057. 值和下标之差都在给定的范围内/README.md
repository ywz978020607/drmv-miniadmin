# [剑指 Offer II 057. 值和下标之差都在给定的范围内](https://leetcode.cn/problems/7WqeDu)

## 题目描述

<!-- 这里写题目描述 -->

<p>给你一个整数数组 <code>nums</code> 和两个整数&nbsp;<code>k</code> 和 <code>t</code> 。请你判断是否存在 <b>两个不同下标</b> <code>i</code> 和 <code>j</code>，使得&nbsp;<code>abs(nums[i] - nums[j]) &lt;= t</code> ，同时又满足 <code>abs(i - j) &lt;= k</code><em> </em>。</p>

<p>如果存在则返回 <code>true</code>，不存在返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], k<em> </em>= 3, t = 0
<strong>输出：</strong>true</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,1], k<em> </em>=<em> </em>1, t = 2
<strong>输出：</strong>true</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,9,1,5,9], k = 2, t = 3
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= t &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 220&nbsp;题相同：&nbsp;<a href="https://leetcode.cn/problems/contains-duplicate-iii/">https://leetcode.cn/problems/contains-duplicate-iii/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

“滑动窗口 + 有序集合”实现。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        s = SortedSet()
        for i, num in enumerate(nums):
            idx = s.bisect_left(num - t)
            if 0 <= idx < len(s) and s[idx] <= num + t:
                return True
            s.add(num)
            if i >= k:
                s.remove(nums[i - k])
        return False
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> ts = new TreeSet<>();
        for (int i = 0; i < nums.length; ++i) {
            Long x = ts.ceiling((long) nums[i] - (long) t);
            if (x != null && x <= (long) nums[i] + (long) t) {
                return true;
            }
            ts.add((long) nums[i]);
            if (i >= k) {
                ts.remove((long) nums[i - k]);
            }
        }
        return false;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<long> s;
        for (int i = 0; i < nums.size(); ++i)
        {
            auto it = s.lower_bound((long) nums[i] - t);
            if (it != s.end() && *it <= (long) nums[i] + t) return true;
            s.insert((long) nums[i]);
            if (i >= k) s.erase((long) nums[i - k]);
        }
        return false;
    }
};
```

### **Go**

```go
func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	n := len(nums)
	left, right := 0, 0
	rbt := redblacktree.NewWithIntComparator()
	for right < n {
		cur := nums[right]
		right++
		if p, ok := rbt.Floor(cur); ok && cur-p.Key.(int) <= t {
			return true
		}
		if p, ok := rbt.Ceiling(cur); ok && p.Key.(int)-cur <= t {
			return true
		}
		rbt.Put(cur, struct{}{})
		if right-left > k {
			rbt.Remove(nums[left])
			left++
		}
	}
	return false
}
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        //时间复杂度O(n)   空间复杂度均为O(k)
        //改用桶记录（每个桶容量为1，范围t+1）  检查当前及相邻桶

        Map<Integer,Integer> map1 = new HashMap<>();
        int bucketSize = t+1; //超过才算
        for(int ii=0;ii<nums.length;ii++){
            int num = nums[ii];
            int temp_id = getBucketID(num,bucketSize);

            if(map1.containsKey(temp_id)||
            (map1.containsKey(temp_id-1)&&map1.get(temp_id-1)+t>=num)||
            (map1.containsKey(temp_id+1)&&map1.get(temp_id+1)-t<=num)){
                return true;
            }

            //出入
            map1.put(temp_id,num);
            if(ii>=k){
                map1.remove(getBucketID(nums[ii-k],bucketSize));
            }
        }
        return false;
    }

    int getBucketID(int num,int bucketSize){
        if(num>=0){
            return num/bucketSize;
        }
        else{
            return (num+1)/bucketSize - 1;//负数
        }
    }
}
```

### **ywz_1**

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        //O(nlogk)时间复杂度 空间复杂度O(k)
        //数值在超限附近 转为Long
        TreeSet<Long> set1 = new TreeSet<>();

        for(int ii=0;ii<nums.length;ii++){
            Long lower = set1.floor((long)nums[ii]); //最相近的小于等于当前值的值
            if(lower!=null && lower >= (long)nums[ii] - t){
                return true;
            }

            Long upper = set1.ceiling((long)nums[ii]); //最相近的小于等于当前值的值
            if(upper!=null && upper <= (long)nums[ii] + t){
                return true;
            }
            
            set1.add((long)nums[ii]);
            if(ii>=k){
                //出队
                set1.remove((long)nums[ii-k]);
            }

        }
        return false;
    }
}
```

<!-- tabs:end -->
