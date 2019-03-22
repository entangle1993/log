#!usr/bin/env python
# encoding:utf-8

'''
ref:
https://blog.csdn.net/together_cz/article/details/77493916
'''


class Node(object):
    '''
    节点类
    '''

    def __init__(self, data):
        self.num = data
        self.next = None


class Solution:
    '''
    实现删除指定节点功能
    '''

    def delete_node(self, node):
        node.num = node.next.num
        node.next = node.next.next
    '''
    输出该链表中倒数第k个结点。
    '''
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head!=None:
            l.append(head)
            head=head.next
        if k>len(l) or k<1:
            return
        return l[-k]


class PrintNode():
    '''
    输出指定节点为起始节点的链表
    '''

    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.num))
            node = node.next
        print '->'.join(res_list)



if __name__ == '__main__':
    node1 = Node(90)
    node2 = Node(34)
    node3 = Node(89)
    node4 = Node(77)
    node5 = Node(23)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print 'init single linknode is:'
    printnode = PrintNode()
    printnode.print_node(node1)
    s = Solution()
    s.delete_node(node4)
    print 'after delete node,the single linknode is:'
    printnode.print_node(node1)
    a = s.FindKthToTail(node1,2)
    print a.num