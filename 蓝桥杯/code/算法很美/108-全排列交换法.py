def permute(arr):
    #结果数组
    res = []
    size = len(arr)
    #递归逻辑，操作同一个数组，k表示第k层，即第k个位置
    def getPermutation(arr , k):
        #终止条件为所有元素排完
        if k == size:
            #拷贝此时的数组
            arr_copy = [i for i in arr]
            #加入结果数组
            res.append(arr_copy)
        #遍历每一个可与当前k这个位置元素交换的元素
        for i in range(k , size):
            #与k位置元素交换
            arr[k] , arr[i] = arr[i] , arr[k]
            #处理下一层
            getPermutation(arr , k+1)
            #回溯，交换回去
            arr[k] , arr[i] = arr[i] , arr[k]

    getPermutation(arr,0)
            
    return res
