# 作者: 王道 龙哥
# 2026年02月24日11时20分54秒
# xxx@qq.com
def heap_sort(arr):
    """堆排序实现"""
    def heapify(a, n, i):  # a为堆，n为堆大小，i为当前结点下标
        largest = i         # 先假定当前节点为最大值
        l = 2 * i + 1       # 左子结点下标
        r = 2 * i + 2       # 右子结点下标
        if l < n and a[l] > a[largest]:  # 如果左子结点存在且比当前最大值大
            largest = l     # 更新最大值下标为左子结点
        if r < n and a[r] > a[largest]:  # 如果右子结点存在且比当前最大值大
            largest = r     # 更新最大值下标为右子结点
        if largest != i:    # 如果最大值下标不是本节点
            a[i], a[largest] = a[largest], a[i]  # 交换当前节点与最大值节点
            heapify(a, n, largest)               # 递归调整被交换子树

    n = len(arr)
    a = arr[:]  # 复制一份，避免修改原数组
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

# 示例用法
if __name__ == "__main__":
    nums = [3, 6, 8, 10, 1, 2, 1]
    print("排序前:", nums)
    sorted_nums = heap_sort(nums)
    print("排序后:", sorted_nums)
