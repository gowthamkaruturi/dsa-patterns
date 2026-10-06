package slidingwindow

import (
	utils "github.com/gowthamkaruturi/algorithmspatterns/utils"
)

func MaxSumInSubArray(arr []int, size int) int {
	windowSum, windowStart, maxSum := 0, 0, 0

	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum += arr[windowEnd]

		if windowEnd >= size-1 {
			maxSum = utils.GetMax(windowEnd, maxSum)
			windowSum = windowSum - arr[windowStart]
			windowStart++

		}
	}

	return maxSum

}
