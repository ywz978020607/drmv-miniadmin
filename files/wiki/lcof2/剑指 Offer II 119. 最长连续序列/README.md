# [剑指 Offer II 119. 最长连续序列](https://leetcode.cn/problems/WhsWhI)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定一个未排序的整数数组 <code>nums</code> ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [100,4,200,1,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>最长数字连续序列是 <code>[1, 2, 3, 4]。它的长度为 4。</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,3,7,2,5,8,4,6,0,1]
<strong>输出：</strong>9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>可以设计并实现时间复杂度为&nbsp;<code>O(n)</code><em> </em>的解决方案吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 128&nbsp;题相同：&nbsp;<a href="https://leetcode.cn/problems/longest-consecutive-sequence/">https://leetcode.cn/problems/longest-consecutive-sequence/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

**方法 1：排序**

设 res 表示连续序列的最大长度，t 表示当前合法连续序列的长度，初始时 `res = t = 1`。

先排序数组，然后从下标 1 开始遍历数组，判断 `nums[i]` 与前一个数 `nums[i - 1]` 的大小关系：

-   若 `nums[i] == nums[i - 1]`，直接跳过；
-   若 `nums[i] - nums[i - 1] == 1`，说明是连续序列，t 自增，利用 `res = max(res, t)` 更新最大长度；
-   否则 t 重置为 1，继续往下遍历。

此方法时间复杂度 `O(nlogn)`，空间复杂度 `O(1)`。

**方法 2：哈希表**

设 res 表示连续序列的最大长度，初始为 0。哈希表 s 存放数组出现的每个元素。

遍历数组，以当前遍历到的元素 `nums[i]` 做为起点，循环判断 `nums[i] + 1`，`nums[i] + 2` ... 是否存在 s 中，并不断更新连续序列的最大长度。

在这个过程中，如果 `nums[i]`, `nums[i] + 1`, `nums[i + 2]`, ... 是一个连续序列，遍历下个元素 `nums[i] + 1` 时，其实无需再重复循环。因此，只需要判断 `nums[i] - 1` 是否在 s 中，是则直接跳过。

此方法时间复杂度 `O(n)`，空间复杂度 `O(n)`。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        nums.sort()
        res = t = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] - nums[i - 1] == 1:
                t += 1
                res = max(res, t)
            else:
                t = 1
        return res
```

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        for num in nums:
            if num - 1 not in s:
                t = 1
                next = num + 1
                while next in s:
                    t += 1
                    next += 1
                res = max(res, t)
        return res
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        if (n < 1) {
            return n;
        }
        Arrays.sort(nums);
        int res = 1, t = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] == nums[i - 1]) {
                continue;
            }
            if (nums[i] - nums[i - 1] == 1) {
                t += 1;
                res = Math.max(res, t);
            } else {
                t = 1;
            }
        }
        return res;
    }
}
```

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        int res = 0;
        for (int num : nums) {
            if (!s.contains(num - 1)) {
                int t = 1, next = num + 1;
                while (s.contains(next++)) {
                    ++t;
                }
                res = Math.max(res, t);
            }
        }
        return res;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    int longestConsecutive(vector<int> &nums) {
        int n = nums.size();
        if (n < 2)
            return n;
        sort(nums.begin(), nums.end());
        int res = 1, t = 1;
        for (int i = 1; i < n; ++i)
        {
            if (nums[i] == nums[i - 1])
                continue;
            if (nums[i] - nums[i - 1] == 1)
            {
                ++t;
                res = max(res, t);
            }
            else
            {
                t = 1;
            }
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    int longestConsecutive(vector<int> &nums) {
        unordered_set<int> s;
        for (int num : nums)
            s.insert(num);
        int res = 0;
        for (int num : nums)
        {
            if (!s.count(num - 1))
            {
                int t = 1, next = num + 1;
                while (s.count(next++))
                    ++t;
                res = max(res, t);
            }
        }
        return res;
    }
};
```

### **Go**

```go
func longestConsecutive(nums []int) int {
	n := len(nums)
	if n < 2 {
		return n
	}
	sort.Ints(nums)
	res, t := 1, 1
	for i := 1; i < n; i++ {
		if nums[i] == nums[i-1] {
			continue
		}
		if nums[i]-nums[i-1] == 1 {
			t++
			res = max(res, t)
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

```go
func longestConsecutive(nums []int) int {
	s := make(map[int]bool)
	for _, num := range nums {
		s[num] = true
	}
	res := 0
	for _, num := range nums {
		if !s[num-1] {
			t, next := 1, num+1
			for s[next] {
				next++
				t++
			}
			res = max(res, t)
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        // 并查集版-带数量版本，并使用Map防止重复元素加入
        Map<Integer, Integer> map1 = new HashMap<>();
        graph = new int[nums.length];
        size = new int[nums.length];
        for(int ii=0;ii<nums.length;ii++){
            graph[ii] = ii;
            size[ii] = 1;
            if(!map1.containsKey(nums[ii])){
                map1.put(nums[ii], ii); //去重
            }
        }

        for(int ii:map1.values()){
            if(map1.containsKey(nums[ii]-1) || map1.containsKey(nums[ii]+1)){
                int jj = 0;
                if(map1.containsKey(nums[ii]-1)){
                    jj = map1.get(nums[ii] - 1);
                }
                if(map1.containsKey(nums[ii]+1)){
                    jj = map1.get(nums[ii] + 1);
                }
                if(findpath(ii) != findpath(jj)){
                    // ii 并入 jj
                    size[findpath(jj)] += size[findpath(ii)];
                    graph[findpath(ii)] = findpath(jj);
                }
            }
        }
        int res=0;
        for(int ii=0;ii<size.length;ii++){
            res = Math.max(res, size[ii]);
        }
        return res;
    }
    private int[] graph;
    private int[] size;
    public int findpath(int x){
        if(graph[x] != x){
            graph[x] = findpath(graph[x]);
        }
        return graph[x];
    }
}

```

### **ywz_1**

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        //时间复杂度O(n)
        //bfs版
        Set<Integer> set1 = new HashSet<>();
        for(int num:nums){
            set1.add(num);
        }

        int res = 0;
        //每次取Set内的一个元素作为起点--会动态删改set1
        while(!set1.isEmpty()){
            Iterator<Integer> iter = set1.iterator();
            int len = bfs(set1,iter.next());
            res = Math.max(res,len);
        }
        return res;
    }

    public int bfs(Set<Integer>set1,int num){
        Deque<Integer> del = new ArrayDeque<>();
        int len = 0;
        del.addLast(num);
        set1.remove(num);//立即移除防止重复添加--队列好习惯
        while(!del.isEmpty()){
            int node = del.pollFirst();
            len++;

            if(set1.contains(node-1)){
                del.addLast(node-1);
                set1.remove(node-1);
            }
            if(set1.contains(node+1)){
                del.addLast(node+1);
                set1.remove(node+1);
            }
        }
        return len;
    }

}
```

<!-- tabs:end -->
