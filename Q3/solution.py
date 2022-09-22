class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
            # get the length of both lists
            size1, size2 = len(nums1), len(nums2)

            # we switch lst 1 with nums2 in case lst 1 has more elements
            # this is done to make nums1 the shorter one for faster calculation

            if size1 > size2:
                nums1, size1, nums2, size2 = nums2, size2, nums1, size1

            # set the starting and ending indexes to decide the cut for median
            low = 0
            high = size1

            # we do a binary seach from here
            while low <= high:

                # a cut divides the lists into left and right part
                # if cut_1 is 0 it means nothing is there on left side of list 1
                # if cut_1 is length of list then there is nothing on right side
                # likewise, for cut_2
                cut_1 = (low + high) // 2
                cut_2 = (size1 + size2 + 1) // 2 - cut_1

                # values to the left of the median are always smaller than right
                # if there are no values to the left of the cut,
                # set the left values  to be minus infinity
                # in case there are no values to the right of the cut,
                # we set the right values to be infinity
                # since cut_1 gives us the number of elements,
                # to get the index we subtract 1

                max_left1 = float('-inf') if cut_1 == 0 else nums1[cut_1 - 1]
                min_right1 = float('inf') if cut_1 == size1 else nums1[cut_1]

                max_left2 = float('-inf') if cut_2 == 0 else nums2[cut_2 - 1]
                min_right2 = float('inf') if cut_2 == size2 else nums2[cut_2]

                # implies all the correct elements found for median calculation
                if (max_left1 <= min_right2) and (max_left2 <= min_right1):

                    # in case total number of elements are even
                    if ((size1 + size2) % 2 == 0):
                        return ((max(max_left1, max_left2) + min(min_right1, min_right2)) / 2)
                    # in case total number of elements are odd
                    else:
                        return max(max_left1, max_left2)

                # if values in left are greater, implies too ahead in the list
                # so we need to decrease the index to get back to smaller values

                elif (max_left1 > min_right2):
                    high = cut_1 - 1

                # else keep on increasing the index
                else:
                    low = cut_1 + 1

        # example to test the median program
if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    sol=Solution()
    print('Median:', sol.findMedianSortedArrays(nums1, nums2))