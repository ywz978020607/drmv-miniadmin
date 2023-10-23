# [剑指 Offer II 063. 替换单词](https://leetcode.cn/problems/UhWRSj)

## 题目描述

<!-- 这里写题目描述 -->

<p>在英语中，有一个叫做&nbsp;<code>词根(root)</code> 的概念，它可以跟着其他一些词组成另一个较长的单词&mdash;&mdash;我们称这个词为&nbsp;<code>继承词(successor)</code>。例如，词根<code>an</code>，跟随着单词&nbsp;<code>other</code>(其他)，可以形成新的单词&nbsp;<code>another</code>(另一个)。</p>

<p>现在，给定一个由许多词根组成的词典和一个句子，需要将句子中的所有<code>继承词</code>用<code>词根</code>替换掉。如果<code>继承词</code>有许多可以形成它的<code>词根</code>，则用最短的词根替换它。</p>

<p>需要输出替换之后的句子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;cat&quot;,&quot;bat&quot;,&quot;rat&quot;], sentence = &quot;the cattle was rattled by the battery&quot;
<strong>输出：</strong>&quot;the cat was rat by the bat&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], sentence = &quot;aadsfasf absbs bbab cadsfafs&quot;
<strong>输出：</strong>&quot;a a b c&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;a&quot;, &quot;aa&quot;, &quot;aaa&quot;, &quot;aaaa&quot;], sentence = &quot;a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa&quot;
<strong>输出：</strong>&quot;a a a a a a a a bbb baba a&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;catt&quot;,&quot;cat&quot;,&quot;bat&quot;,&quot;rat&quot;], sentence = &quot;the cattle was rattled by the battery&quot;
<strong>输出：</strong>&quot;the cat was rat by the bat&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;ac&quot;,&quot;ab&quot;], sentence = &quot;it is abnormal that this solution is accepted&quot;
<strong>输出：</strong>&quot;it is ab that this solution is ac&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= dictionary.length&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code>&nbsp;仅由小写字母组成。</li>
	<li><code>1 &lt;= sentence.length &lt;= 10^6</code></li>
	<li><code>sentence</code>&nbsp;仅由小写字母和空格组成。</li>
	<li><code>sentence</code> 中单词的总量在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中每个单词的长度在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中单词之间由一个空格隔开。</li>
	<li><code>sentence</code>&nbsp;没有前导或尾随空格。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 648&nbsp;题相同：&nbsp;<a href="https://leetcode.cn/problems/replace-words/">https://leetcode.cn/problems/replace-words/</a></p>

## 解法

<!-- 这里可写通用的实现逻辑 -->

前缀树实现。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Trie:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.root = None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            cur = trie
            for c in root:
                idx = ord(c) - ord('a')
                if cur.children[idx] is None:
                    cur.children[idx] = Trie()
                cur = cur.children[idx]
            cur.root = root

        ans = []
        for word in sentence.split():
            cur = trie
            for c in word:
                idx = ord(c) - ord('a')
                if cur.children[idx] is None or cur.root is not None:
                    break
                cur = cur.children[idx]
            ans.append(word if cur.root is None else cur.root)
        return ' '.join(ans)
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Trie {
    Trie[] children = new Trie[26];
    String root;
}

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Trie trie = new Trie();
        for (String root : dictionary) {
            Trie cur = trie;
            for (char c : root.toCharArray()) {
                if (cur.children[c - 'a'] == null) {
                    cur.children[c - 'a'] = new Trie();
                }
                cur = cur.children[c - 'a'];
            }
            cur.root = root;
        }
        List<String> ans = new ArrayList<>();
        for (String word : sentence.split("\\s+")) {
            Trie cur = trie;
            for (char c : word.toCharArray()) {
                if (cur.children[c - 'a'] == null || cur.root != null) {
                    break;
                }
                cur = cur.children[c - 'a'];
            }
            ans.add(cur.root == null ? word : cur.root);
        }
        return String.join(" ", ans);
    }
}
```

### **C++**

```cpp
class Trie {
public:
    string root;
    vector<Trie*> children;

    Trie() {
        root = "";
        children.resize(26);
    }
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie* trie = new Trie();
        for (auto root : dictionary)
        {
            Trie* cur = trie;
            for (char c : root)
            {
                if (!cur->children[c - 'a']) cur->children[c - 'a'] = new Trie();
                cur = cur->children[c - 'a'];
            }
            cur->root = root;
        }

        string ans = "";
        istringstream is(sentence);
        vector<string> ss;
        string s;
        while (is >> s) ss.push_back(s);
        for (auto word : ss)
        {
            Trie* cur = trie;
            for (char c : word)
            {
                if (!cur->children[c - 'a'] || cur->root != "") break;
                cur = cur->children[c - 'a'];
            }
            ans += cur->root == "" ? word : cur->root;
            ans += " ";
        }
        ans.pop_back();
        return ans;
    }
};
```

### **Go**

```go
func replaceWords(dictionary []string, sentence string) string {
	trie := &Trie{}
	for _, root := range dictionary {
		cur := trie
		for _, c := range root {
			c -= 'a'
			if cur.children[c] == nil {
				cur.children[c] = &Trie{}
			}
			cur = cur.children[c]
		}
		cur.root = root
	}

	var ans []string
	for _, word := range strings.Split(sentence, " ") {
		cur := trie
		for _, c := range word {
			c -= 'a'
			if cur.children[c] == nil || cur.root != "" {
				break
			}
			cur = cur.children[c]
		}
		if cur.root == "" {
			ans = append(ans, word)
		} else {
			ans = append(ans, cur.root)
		}
	}
	return strings.Join(ans, " ")
}

type Trie struct {
	children [26]*Trie
	root     string
}
```

### **...**

```

```

### **ywz_0**

```java
class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        //创建字典树
        Trie myTrie = new Trie();
        for(String s:dictionary){
            myTrie.insert(s);
        }
        //切割
        String[] list1 = sentence.split(" ");

        for(int ii=0;ii<list1.length;ii++){
            String find = findPrefix(myTrie,list1[ii]);
            if(find!=null){
                list1[ii] = find;
            }
        }

        //注意合并
        return String.join(" ",list1); //相邻补空格
    }

    //寻找词根，没有返回null
    String findPrefix(Trie root,String word){
        Trie temp = root;
        StringBuffer buffer1 = new StringBuffer(0);
        for(char c:word.toCharArray()){
            if(temp.next[(int)c-'a']!=null){
                temp = temp.next[(int)c-'a'];
                buffer1.append(c);
                //判断最短退出
                if(temp.isEnd){
                    break;
                }
            }
            else{
                //没走到字典里的isEnd  但内容对不上了 说明不是词根-- 返回null
                return null;
            }
        }
        return buffer1.toString();
    }
}

class Trie {
    Trie[] next;
    boolean isEnd;
    /** Initialize your data structure here. */
    public Trie() {
        next = new Trie[26]; //链起来
        isEnd = false;
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Trie temp = this;
        for(char c:word.toCharArray()){
            if(temp.next[(int)c-'a']==null){
                temp.next[(int)c-'a'] = new Trie();
            }
            temp = temp.next[(int)c - 'a'];
        }
        temp.isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Trie temp = this;
        for(char c:word.toCharArray()){
            if(temp.next[(int)c-'a']==null){
                return false;
            }
            temp = temp.next[(int)c - 'a'];
        }
        if(temp.isEnd){
            return true;
        }
        else{
            return false;
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Trie temp = this;
        for(char c:prefix.toCharArray()){
            if(temp.next[(int)c-'a']==null){
                return false;
            }
            temp = temp.next[(int)c - 'a'];
        }
        return true;
    }
}
```

<!-- tabs:end -->
