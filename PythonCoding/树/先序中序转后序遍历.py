class Solution:
    def generatePostOrder(self, inorder, preorder):
        if len(inorder) != len(preorder):
            return []
        res = self.process(inorder,0,len(inorder)-1, preorder, 0, len(preorder) -1)
        return res[::-1]

    def process(self, inorder, l1, r1, preorder, l2, r2):
        if l1 > r1:
            return []
        if l1 == r1:
            return [inorder[l1]]
        res = [preorder[l2]]
        index = inorder.index(preorder[l2])
        leftsize = index - l1
        left = self.process(inorder,l1,index-1, preorder,l2+1, l2+leftsize)
        right = self.process(inorder,index+1,r1, preorder, l2+leftsize+1, r2)
        return res + right + left


so = Solution()
# preorder = [1, 2, 4, 5, 3, 6, 7]
# inorder = [4, 2, 5, 1, 6, 3, 7]

# print(so.generatePostOrder(inorder, preorder))

preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7, 11]
inorder = [8, 4, 9, 2, 10, 5, 1, 6, 3, 11, 7]
print(so.generatePostOrder(inorder, preorder))


class Solution:
    def generatePostOrder(self, inorder, preorder):
        if len(inorder) != len(preorder):
            return []
        postorder = [None for _ in range(len(inorder)) ]
        self.process(inorder,0,len(inorder)-1, preorder, 0, len(preorder) -1, postorder, 0, len(postorder)-1)
        return postorder

    def process(self, inorder, l1, r1, preorder, l2, r2, postorder, l3, r3):
        if l2 > r2:
            return
        if l2 == r2:
            postorder[l3] = preorder[l2]
            return
        postorder[r3] = preorder[l2]
        mid = inorder.index(preorder[l2])
        leftsize = mid - l1
        self.process(inorder,l1,mid-1, preorder,l2+1, l2+leftsize, postorder,l3, l3 +leftsize-1)
        self.process(inorder,mid+1,r1, preorder, l2+leftsize+1, r2, postorder, l3 +leftsize,r3-1)


so = Solution()
# preorder = [1, 2, 4, 5, 3, 6, 7]
# inorder = [4, 2, 5, 1, 6, 3, 7]

# print(so.generatePostOrder(inorder, preorder))

preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7, 11]
inorder = [8, 4, 9, 2, 10, 5, 1, 6, 3, 11, 7]
print(so.generatePostOrder(inorder, preorder))

# map 优化
class Solution:
    def generatePostOrder(self, inorder, preorder):
        if len(inorder) != len(preorder):
            return []
        postorder = [None for _ in range(len(inorder))]
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        self.process(inorder,0,len(inorder)-1, preorder, 0, len(preorder) -1, postorder, 0, len(postorder)-1, inMap)
        return postorder

    def process(self, inorder, l1, r1, preorder, l2, r2, postorder, l3, r3, inMap):
        if l2 > r2:
            return
        if l2 == r2:
            postorder[l3] = preorder[l2]
            return
        postorder[r3] = preorder[l2]
        mid = inMap[preorder[l2]]
        leftsize = mid - l1
        self.process(inorder,l1,mid-1, preorder,l2+1, l2+leftsize, postorder,l3, l3 +leftsize-1, inMap)
        self.process(inorder,mid+1,r1, preorder, l2+leftsize+1, r2, postorder, l3 +leftsize,r3-1, inMap)
