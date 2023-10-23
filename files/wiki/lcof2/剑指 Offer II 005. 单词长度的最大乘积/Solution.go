func maxProduct(words []string) int {
	n := len(words)
	mask := make([]int32, n)
	for i, word := range words {
		for _, r := range word {
			mask[i] |= 1 << (r - 'a')
		}
	}
	ans := 0
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if mask[i]&mask[j] == 0 {
				ans = max(ans, len(words[i])*len(words[j]))
			}
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
