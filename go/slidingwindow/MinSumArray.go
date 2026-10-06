package slidingwindow

import (
	"math"

	utils "github.com/gowthamkaruturi/algorithmspatterns/utils"
)

func MinSumInSubArray(arr []int, Sum int) int {
	windowSum, windowStart, minLength := 0, 0, math.MaxInt

	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum += arr[windowEnd]

		for windowSum >= Sum {
			minLength = utils.GetMin(minLength, windowEnd-windowStart+1)
			windowSum = windowSum - arr[windowStart]
			windowStart++

		}
	}

	return minLength

}
