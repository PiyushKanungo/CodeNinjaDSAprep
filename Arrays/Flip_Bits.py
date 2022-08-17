def FlipBits(arr, n):
    max_diff = 0
    org_one_count = 0

    for i in range(n):

        if arr[1] == 1:
            org_one_count += 1

        count1, count0 = 0, 0

        for j in range(i, n):
            if arr[j] ==1:
                count1 += 1

            else:
                count0 += 1
            max_diff = max(max_diff,count1 - count0)

    return org_one_count + max_diff


