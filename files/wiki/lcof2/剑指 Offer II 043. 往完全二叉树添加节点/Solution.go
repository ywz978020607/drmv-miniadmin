/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type CBTInserter struct {
	tree []*TreeNode
}

func Constructor(root *TreeNode) CBTInserter {
	var q []*TreeNode
	var tree []*TreeNode
	q = append(q, root)
	for len(q) > 0 {
		node := q[0]
		tree = append(tree, node)
		q = q[1:]
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}
	return CBTInserter{tree}
}

func (this *CBTInserter) Insert(val int) int {
	pidx := (len(this.tree) - 1) >> 1
	node := &TreeNode{Val: val}
	this.tree = append(this.tree, node)
	if this.tree[pidx].Left == nil {
		this.tree[pidx].Left = node
	} else {
		this.tree[pidx].Right = node
	}
	return this.tree[pidx].Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.tree[0]
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(val);
 * param_2 := obj.Get_root();
 */