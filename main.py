def combine(nums1, nums2):
    p, q, temp_list = 0, 0, list()
    len_left, len_right = len(nums1), len(nums2) 

    while len_left > p and len_right > q:
        if nums1[p] <= nums2[q]:
            temp_list.append(nums1[p])
            p += 1
        else:
            temp_list.append(nums2[q])
            q += 1
    temp_list += nums1[p:]
    temp_list += nums2[q:]

    if len(temp_list) % 2 == 1:
        return temp_list[len(temp_list)//2]
    else:
        return (temp_list[len(temp_list)//2] + temp_list[len(temp_list)//2 - 1])/2

if __name__ == "__main__":
    arr1 = [0,1,2,3,4,5,6,7]
    arr2 = [8,9,10,11,12,13,14]
    print(combine(arr1, arr2))
    