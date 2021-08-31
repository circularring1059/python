def mergeList(nums1, nums2):
    index = 0
    for i in range(len(nums2)):
        while index < len(nums1):
            if nums2[i] <= nums1[index]:
                nums1.insert(index, nums2[i])
                break
            else:
                index += 1
        else:
            nums1.extend(nums2[i:])
            break
    return nums1

print(mergeList([1,3,3,5], [1,4,4,9]))

def mergeList1(nums1, nums2):
    nums1_pointer, nums2_pointer = 0, 0
    nums3 = []
    while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
        if nums1[nums1_pointer] <= nums2[nums2_pointer]:
            nums3.append(nums1[nums1_pointer])
            nums1_pointer += 1
        else:
            nums3.append(nums2[nums2_pointer])
            nums2_pointer += 1
    if nums1_pointer >= len(nums1):
        nums3.extend(nums2[nums2_pointer::])
    else:
        nums3.extend(nums1[nums1_pointer::])
    return nums3

print(mergeList1([1,2,4],[3,6,6,9]))


class MergeList():
    def merge_list(selfm, array1, array2):
        index = 0
        for i in range(len(array2)):
            while index < len(array1):
              if array2[i] <= array1[index]:
                  array1.insert(index, array2[i])   #insert 费劲
                  break
              else:
                  index += 1
        else:
            array1.extend(array2[i:])
        return array1

merge_list_ins = MergeList()
print(merge_list_ins.merge_list([1,2,6], [4,6,9]))