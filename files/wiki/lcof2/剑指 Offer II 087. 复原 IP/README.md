# [剑指 Offer II 087. 复原 IP](https://leetcode.cn/problems/0on3uN)

## 题目描述

<!-- 这里写题目描述 -->

<p>给定一个只包含数字的字符串 <code>s</code> ，用以表示一个 IP 地址，返回所有可能从&nbsp;<code>s</code> 获得的 <strong>有效 IP 地址 </strong>。你可以按任何顺序返回答案。</p>

<p><strong>有效 IP 地址</strong> 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>&#39;.&#39;</code> 分隔。</p>

<p>例如：&quot;0.1.2.201&quot; 和 &quot;192.168.1.1&quot; 是 <strong>有效</strong> IP 地址，但是 &quot;0.011.255.245&quot;、&quot;192.168.1.312&quot; 和 &quot;192.168@1.1&quot; 是 <strong>无效</strong> IP 地址。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;25525511135&quot;
<strong>输出：</strong>[&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;0000&quot;
<strong>输出：</strong>[&quot;0.0.0.0&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;1111&quot;
<strong>输出：</strong>[&quot;1.1.1.1&quot;]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;010010&quot;
<strong>输出：</strong>[&quot;0.10.0.10&quot;,&quot;0.100.1.0&quot;]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;10203040&quot;
<strong>输出：</strong>[&quot;10.20.30.40&quot;,&quot;102.0.30.40&quot;,&quot;10.203.0.40&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 93&nbsp;题相同：<a href="https://leetcode.cn/problems/restore-ip-addresses/">https://leetcode.cn/problems/restore-ip-addresses/</a>&nbsp;</p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

DFS。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            if not (0 <= int(s) <= 255):
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            return True

        def dfs(s, t):
            if len(t) == 4:
                if not s:
                    ans.append('.'.join(t))
                return
            for i in range(1, min(4, len(s) + 1)):
                if check(s[:i]):
                    t.append(s[:i])
                    dfs(s[i:], t)
                    t.pop()

        ans = []
        dfs(s, [])
        return ans
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    private List<String> ans;

    public List<String> restoreIpAddresses(String s) {
        ans = new ArrayList<>();
        dfs(s, new ArrayList<>());
        return ans;
    }

    private void dfs(String s, List<String> t) {
        if (t.size() == 4) {
            if ("".equals(s)) {
                ans.add(String.join(".", t));
            }
            return;
        }
        for (int i = 1; i < Math.min(4, s.length() + 1); ++i) {
            String c = s.substring(0, i);
            if (check(c)) {
                t.add(c);
                dfs(s.substring(i), t);
                t.remove(t.size() - 1);
            }
        }
    }

    private boolean check(String s) {
        if ("".equals(s)) {
            return false;
        }
        int num = Integer.parseInt(s);
        if (num > 255) {
            return false;
        }
        if (s.charAt(0) == '0' && s.length() > 1) {
            return false;
        }
        return true;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        vector<string> t;
        dfs(s, t, ans);
        return ans;
    }

    void dfs(string s, vector<string>& t, vector<string>& ans) {
        if (t.size() == 4)
        {
            if (s == "")
            {
                string p = "";
                for (auto e : t) p += e + ".";
                p.pop_back();
                ans.push_back(p);
            }
            return;
        }
        for (int i = 1; i < min(4, (int) s.size() + 1); ++i)
        {
            string c = s.substr(0, i);
            if (check(c))
            {
                t.push_back(c);
                dfs(s.substr(i, s.size() - i), t, ans);
                t.pop_back();
            }
        }
    }

    bool check(string s) {
        if (s == "") return false;
        int num = stoi(s);
        if (num > 255) return false;
        if (s[0] == '0' && s.size() > 1) return false;
        return true;
    }
};
```

### **Go**

```go
func restoreIpAddresses(s string) []string {
	check := func(s string) bool {
		if i, _ := strconv.Atoi(s); i > 255 {
			return false
		}
		if s[0] == '0' && len(s) > 1 {
			return false
		}
		return true
	}
	var ans []string
	var dfs func(s string, t []string)
	dfs = func(s string, t []string) {
		if len(t) == 4 {
			if s == "" {
				ans = append(ans, strings.Join(t, "."))
			}
			return
		}
		for i := 1; i < 4 && i < len(s)+1; i++ {
			if check(s[0:i]) {
				t = append(t, s[0:i])
				dfs(s[i:], t)
				t = t[0 : len(t)-1]
			}
		}
	}
	var t []string
	dfs(s, t)
	return ans
}
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    List<String> ans = new ArrayList<>();
    public List<String> restoreIpAddresses(String s) {
        //大于12的时候直接返回
        if (s == null || s.length() < 4 || s.length() > 12) {
            return ans;
        }
        //隔板法
        for (int i = 1; i < s.length() - 2; i++) {
            for (int j = i + 1; j < s.length() - 1; j++) {
                for (int k = j + 1; k < s.length(); k++) {
                    if (checked(s, i, j, k)) {
                        StringBuffer sb = new StringBuffer();
                        sb.append(s.substring(0, i) + ".");
                        sb.append(s.substring(i, j) + ".");
                        sb.append(s.substring(j, k) + ".");
                        sb.append(s.substring(k));
                        ans.add(sb.toString());
                    }
                }
            }
        }
        return ans;
    }

    private boolean checked(String s, int i, int j, int k) {
        String str1 = s.substring(0, i);
        //判断前导0和是否大于255，其实可以抽取一个方法
        if (str1.length() > 1 && str1.charAt(0) == '0' || Integer.parseInt(str1) > 255) {
            return false;
        } 

        String str2 = s.substring(i, j);
        if (str2.length() > 1 && str2.charAt(0) == '0' || Integer.parseInt(str2) > 255) {
            return false;
        } 

        String str3 = s.substring(j, k);
        if (str3.length() > 1 && str3.charAt(0) == '0' || Integer.parseInt(str3) > 255) {
            return false;
        } 

        String str4 = s.substring(k);
        if (str4.length() > 1 && str4.charAt(0) == '0' || Integer.parseInt(str4) > 255) {
            return false;
        }
        return true; 
    }
}

```

### **ywz_1**

```java
class Solution {
    List<String> res;
    public List<String> restoreIpAddresses(String s) {
        res = new ArrayList<>();
        subIp(s,0,0,"","");
        return res;
    }

    public void subIp(String s,int split,int begin,String Segment,String already){ //split 第几段  Segment上一段(未结束)  already 已结束内容
        if(split==3 && begin==s.length()){
            //到达终点null
            res.add(already+Segment);
        }

        else if(split<=3 && begin<s.length()){
            //deal
            char temp = s.charAt(begin);
            //+
            if(isSegment(Segment+temp)){
                //当前段继续加
                subIp(s,split,begin+1,Segment+temp,already);
            }
            
            //next
            if(Segment.length()>0 ){ // && split<3
                subIp(s,split+1,begin+1,""+temp,already+Segment+"."); //""+char -> String
            }
        }

        
    }
    
    boolean isSegment(String s){
        //单一个0应该被允许
        if(Integer.parseInt(s)<=255 && s.charAt(0)!='0' || s.equals("0")){
            return true;
        }
        else{
            return false;
        }
    }
}
```

<!-- tabs:end -->
