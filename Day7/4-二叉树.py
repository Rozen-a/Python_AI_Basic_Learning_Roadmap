# 4、完成二叉树层次建树，前序，中序，后序遍历

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def insert_node(self, value):
        """
        插入新结点
        :param value:插入值
        :return:
        """
        new_node = TreeNode(value)
        self.queue.append(new_node)  # 新结点入队
        if self.root is None:
            self.root = new_node  # 树空，作为树根
        else:
            if self.queue[0].left is None:
                self.queue[0].left = new_node  # 首先插入左孩子
            else:
                self.queue[0].right = new_node  # 后插入右孩子
                self.queue.pop(0)  # 已有左右孩子，出队

    def pre_order(self, current_node: TreeNode):
        """
        前序遍历
        :param current_node:
        :return:
        """
        if current_node:
            print(current_node.value, end=' ')
            self.pre_order(current_node.left)
            self.pre_order(current_node.right)

    def mid_order(self, current_node: TreeNode):
        """
        中序遍历
        :param current_node:
        :return:
        """
        if current_node:
            self.mid_order(current_node.left)
            print(current_node.value, end=' ')
            self.mid_order(current_node.right)

    def last_order(self, current_node: TreeNode):
        """
        后序遍历
        :param current_node:
        :return:
        """
        if current_node:
            self.last_order(current_node.left)
            self.last_order(current_node.right)
            print(current_node.value, end=' ')

    def level_order(self):
        queue = deque() # 使用双端队列作为辅助
        queue.append(self.root)  # 根节点入队
        while queue:
            node:TreeNode = queue.popleft()
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()

    for i in range(1, 11):
        tree.insert_node(i)

    print('先序遍历结果：')
    tree.pre_order(tree.root)
    print('\n', '-'*30)

    print('中序遍历结果：')
    tree.mid_order(tree.root)
    print('\n', '-'*30)

    print('后序遍历结果：')
    tree.last_order(tree.root)
    print('\n', '-'*30)

    print('层次遍历结果：')
    tree.level_order()
