# [剑指 Offer II 066. 单词之和](https://leetcode.cn/problems/z1R5dt)

## 题目描述

<!-- 这里写题目描述 -->

<p>实现一个 <code>MapSum</code> 类，支持两个方法，<code>insert</code>&nbsp;和&nbsp;<code>sum</code>：</p>

<ul>
	<li><code>MapSum()</code> 初始化 <code>MapSum</code> 对象</li>
	<li><code>void insert(String key, int val)</code> 插入 <code>key-val</code> 键值对，字符串表示键 <code>key</code> ，整数表示值 <code>val</code> 。如果键 <code>key</code> 已经存在，那么原来的键值对将被替代成新的键值对。</li>
	<li><code>int sum(string prefix)</code> 返回所有以该前缀 <code>prefix</code> 开头的键 <code>key</code> 的值的总和。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
inputs = [&quot;MapSum&quot;, &quot;insert&quot;, &quot;sum&quot;, &quot;insert&quot;, &quot;sum&quot;]
inputs = [[], [&quot;apple&quot;, 3], [&quot;ap&quot;], [&quot;app&quot;, 2], [&quot;ap&quot;]]
<strong>输出：</strong>
[null, null, 3, null, 5]

<strong>解释：</strong>
MapSum mapSum = new MapSum();
mapSum.insert(&quot;apple&quot;, 3);  
mapSum.sum(&quot;ap&quot;);           // return 3 (<u>ap</u>ple = 3)
mapSum.insert(&quot;app&quot;, 2);    
mapSum.sum(&quot;ap&quot;);           // return 5 (<u>ap</u>ple + <u>ap</u>p = 3 + 2 = 5)
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= key.length, prefix.length &lt;= 50</code></li>
	<li><code>key</code> 和 <code>prefix</code> 仅由小写英文字母组成</li>
	<li><code>1 &lt;= val &lt;= 1000</code></li>
	<li>最多调用 <code>50</code> 次 <code>insert</code> 和 <code>sum</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 677&nbsp;题相同：&nbsp;<a href="https://leetcode.cn/problems/map-sum-pairs/">https://leetcode.cn/problems/map-sum-pairs/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

利用哈希表存储每个键的所有前缀子串。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(int)
        self.t = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        old = self.t[key]
        self.t[key] = val
        for i in range(1, len(key) + 1):
            self.data[key[:i]] += val - old

    def sum(self, prefix: str) -> int:
        return self.data[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class MapSum {
    private Map<String, Integer> data;
    private Map<String, Integer> t;

    /** Initialize your data structure here. */
    public MapSum() {
        data = new HashMap<>();
        t = new HashMap<>();
    }

    public void insert(String key, int val) {
        int old = t.getOrDefault(key, 0);
        t.put(key, val);
        for (int i = 1; i < key.length() + 1; ++i) {
            String k = key.substring(0, i);
            data.put(k, data.getOrDefault(k, 0) + (val - old));
        }
    }

    public int sum(String prefix) {
        return data.getOrDefault(prefix, 0);
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```

### **C++**

```cpp
class MapSum {
public:
    unordered_map<string, int> data;
    unordered_map<string, int> t;

    /** Initialize your data structure here. */
    MapSum() {

    }

    void insert(string key, int val) {
        int old = t[key];
        t[key] = val;
        for (int i = 1; i < key.size() + 1; ++i)
        {
            string k = key.substr(0, i);
            data[k] += (val - old);
        }
    }

    int sum(string prefix) {
        return data[prefix];
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```

### **Go**

```go
type MapSum struct {
	data map[string]int
	t    map[string]int
}

/** Initialize your data structure here. */
func Constructor() MapSum {
	return MapSum{
		data: make(map[string]int),
		t:    make(map[string]int),
	}
}

func (this *MapSum) Insert(key string, val int) {
	old := this.t[key]
	this.t[key] = val
	for i := 1; i < len(key)+1; i++ {
		k := key[:i]
		this.data[k] += (val - old)
	}
}

func (this *MapSum) Sum(prefix string) int {
	return this.data[prefix]
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
```

### **...**

```

```

<!-- tabs:end -->
