# [剑指 Offer II 002. 二进制加法](https://leetcode.cn/problems/JFETK5)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定两个 01 字符串&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>&nbsp;，请计算它们的和，并以二进制字符串的形式输出。</p>

<p>输入为 <strong>非空 </strong>字符串且只包含数字&nbsp;<code>1</code>&nbsp;和&nbsp;<code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> a = &quot;11&quot;, b = &quot;10&quot;
<strong>输出:</strong> &quot;101&quot;</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> a = &quot;1010&quot;, b = &quot;1011&quot;
<strong>输出:</strong> &quot;10101&quot;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个字符串仅由字符 <code>&#39;0&#39;</code> 或 <code>&#39;1&#39;</code> 组成。</li>
	<li><code>1 &lt;= a.length, b.length &lt;= 10^4</code></li>
	<li>字符串如果不是 <code>&quot;0&quot;</code> ，就都不含前导零。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 67&nbsp;题相同：<a href="https://leetcode.cn/problems/add-binary/">https://leetcode.cn/problems/add-binary/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

模拟笔算加法的过程，注意进位

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = len(a) - 1, len(b) - 1
        arr = []
        carry = 0
        while x >= 0 or y >= 0:
            if x >= 0:
                if a[x] == '1':
                    carry += 1
                x -= 1
            if y >= 0:
                if b[y] == '1':
                    carry += 1
                y -= 1
            arr.append(chr((carry & 1) + ord('0')))
            carry >>= 1
        if carry == 1:
            arr.append('1')
        return ''.join(reversed(arr))
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public String addBinary(String a, String b) {
        int x = a.length() - 1, y = b.length() - 1;
        StringBuilder builder = new StringBuilder();
        int carry = 0;
        while (x >= 0 || y >= 0) {
            if (x >= 0) {
                if (a.charAt(x) == '1') {
                    carry += 1;
                }
                x--;
            }
            if (y >= 0) {
                if (b.charAt(y) == '1') {
                    carry += 1;
                }
                y--;
            }
            builder.append((char) ((carry & 1) + '0'));
            carry >>= 1;
        }
        if (carry == 1) {
            builder.append('1');
        }
        return builder.reverse().toString();
    }
}
```

### **Go**

```go
func addBinary(a string, b string) string {
	x, y := len(a)-1, len(b)-1
	var builder strings.Builder
	carry := 0
	for x >= 0 || y >= 0 {
		if x >= 0 {
			if a[x] == '1' {
				carry += 1
			}
			x--
		}
		if y >= 0 {
			if b[y] == '1' {
				carry += 1
			}
			y--
		}
		builder.WriteRune(rune(carry&1 + '0'))
		carry >>= 1
	}
	if carry == 1 {
		builder.WriteRune('1')
	}
	bytes := []byte(builder.String())
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		bytes[i], bytes[j] = bytes[j], bytes[i]
	}
	return string(bytes)
}
```

### **C++**

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int carry = 0;

        int i = a.size() - 1;
        int j = b.size() - 1;

        while (i >= 0 || j >= 0) {
            int digitA = i >= 0 ? a.at(i--) - '0' : 0;
            int digitB = j >= 0 ? b.at(j--) - '0' : 0;
            int sum = digitA + digitB + carry;
            carry = sum >= 2 ? 1 : 0;
            sum = sum >= 2 ? sum - 2 : sum;
            res += to_string(sum);
        }

        if (carry == 1) res.push_back('1');
        reverse(res.begin(), res.end());
        return res;
    }
};
```

### **...**

```

```

### **ywz_0**

```java
//cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0; //进位
        while (i >= 0 || j >= 0)  // 双指针, 让两个数的末位对齐, 两个指针 i, j均从末尾开始走
        {
            int digitA = i >= 0 ? a[i--] - '0' : 0;
            int digitB = j >= 0 ? b[j--] - '0' : 0;
            int sum = digitA + digitB + carry;
            carry = sum >= 2 ? 1 : 0;
            sum = sum >= 2 ? sum - 2 : sum;
            res.append(to_string(sum));
        }
        if (carry == 1)
            res.append("1");
        reverse(res.begin(), res.end());
        return res;
    }
};

```

### **ywz_1**

```java
class Solution {
    public String addBinary(String a, String b) {

        StringBuffer res = new StringBuffer(0);
        int iter1=a.length()-1;
        int iter2 = b.length()-1;

        int addflag = 0;
        while(iter1>=0||iter2>=0||addflag>0){
            if(iter1>=0){
                addflag += (a.charAt(iter1)=='1')?1:0;
                iter1--;
            }
            if(iter2>=0){
                addflag += (b.charAt(iter2)=='1')?1:0;
                iter2--;
            }

            if(addflag>0|| iter1>=0 || iter2>=0){
                if(addflag%2==0){
                    res.insert(0,'0');
                }
                else{
                    res.insert(0,'1');
                }
                addflag/=2;
            }
        }

        if(res.length()==0){
            res.insert(0,'0');
        }

        return res.toString();
        
    }
}
```

<!-- tabs:end -->
