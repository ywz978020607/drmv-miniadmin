# [剑指 Offer II 007. 数组中和为 0 的三个数](https://leetcode.cn/problems/1fGaJU)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定一个包含 <code>n</code> 个整数的数组&nbsp;<code>nums</code>，判断&nbsp;<code>nums</code>&nbsp;中是否存在三个元素&nbsp;<code>a</code> ，<code>b</code> ，<code>c</code> <em>，</em>使得&nbsp;<code>a + b + c = 0</code> ？请找出所有和为 <code>0</code> 且&nbsp;<strong>不重复&nbsp;</strong>的三元组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,0,1,2,-1,-4]
<strong>输出：</strong>[[-1,-1,2],[-1,0,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 15&nbsp;题相同：<a href="https://leetcode.cn/problems/3sum/">https://leetcode.cn/problems/3sum/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

枚举第一个数，然后用双指针确定另外两个数

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur < 0:
                    left += 1
                elif cur > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1, right = n - 1;
            while (left < right) {
                int cur = nums[i] + nums[left] + nums[right];
                if (cur < 0) {
                    left++;
                } else if (cur > 0) {
                    right--;
                } else {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                }
            }
        }
        return ans;
    }
}
```

### **Go**

```go
func threeSum(nums []int) [][]int {
	n := len(nums)
	ans := make([][]int, 0)
	sort.Ints(nums)
	for i := 0; i < n-2 && nums[i] <= 0; i++ {
		left, right := i+1, n-1
		for left < right {
			cur := nums[i] + nums[left] + nums[right]
			if cur < 0 {
				left++
			} else if cur > 0 {
				right--
			} else {
				ans = append(ans, []int{nums[i], nums[left], nums[right]})
				for left < right && nums[left] == nums[left+1] {
					left++
				}
				for left < right && nums[right] == nums[right-1] {
					right--
				}
				left++
				right--
			}
		}
		for i < n-2 && nums[i] == nums[i+1] {
			i++
		}
	}
	return ans
}
```

### **C++**

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;

        sort(nums.begin(), nums.end());
        for (int k = 0; k < nums.size(); k++) {
            int i = k + 1;
            int j = nums.size() - 1;
            if (k > 0 && nums[k] == nums[k - 1]) continue;

            while(i < j) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    res.push_back(vector<int>{nums[k], nums[i], nums[j]});
                    i++;
                    j--;

                    while(i < j && nums[i] == nums[i - 1]) i++;
                    while(i < j && nums[j] == nums[j + 1]) j--;
                } else if (nums[i] + nums[j] + nums[k] < 0) {
                    i++;
                } else {
                    j--;
                }
            }
        }

        return res;
    }
};
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        // 需要跳过某些 不便用for
        int ii = 0;
        while(ii < nums.length - 2){
            twoSum(nums, ii, res);
            int temp_val = nums[ii];
            while(ii < nums.length - 2 && nums[ii] == temp_val){
                // 跳过相同的数字
                ii++; 
            }
        }

        return res;
    }

    public void twoSum(int[] nums,int ii,List<List<Integer>> res){
        int left = ii + 1;
        int right = nums.length - 1;

        while(left < right){
            if(nums[left] + nums[right] + nums[ii] > 0){
                right--;
            }
            else if(nums[left] + nums[right] + nums[ii] < 0){
                left++;
            }
            else{
                res.add(Arrays.asList(nums[ii], nums[left], nums[right]));
                // res.add(new ArrayList<Integer>(Arrays.asList(nums[ii], nums[left], nums[right])));
                int temp_left_val = nums[left];
                while(left<nums.length - 1 && nums[left] == temp_left_val){
                    // 跳过left
                    left++;
                }
            }
        }
    }
}
```

### **ywz_1**

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        //三数之和
        List<List<Integer>> list1 = new LinkedList<>();

        //先排序
        Arrays.sort(nums);

        for(int ii=0;ii<nums.length-2;ii++){
            if(ii>0 && nums[ii]==nums[ii-1]){
                continue;//去重1
            }

            int left=ii+1;
            int right = nums.length - 1;
            while(left<right){
                //去重
                if(right<nums.length-1&&nums[right]==nums[right+1]){
                    right--;
                    continue;
                }


                if(nums[left]+nums[right]+nums[ii]==0){
                    List<Integer> add = new LinkedList<>();
                    add.add(nums[ii]);
                    add.add(nums[left]);
                    add.add(nums[right]);
                    list1.add(add);
                    
                    right--; //不能用left++原因：去重只考虑了right-- 
                }

                else if(nums[left]+nums[right]+nums[ii]<0){
                    left++;
                }
                else{
                    right--;
                }
            }
            
        }

        return list1;
    }
}
```

<!-- tabs:end -->
