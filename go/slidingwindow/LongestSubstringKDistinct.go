package slidingwindow

import (
	"fmt"

	"github.com/gowthamkaruturi/algorithmspatterns/utils"
)

func LongestSlidingWindowKDistinct(str string, k int) int {

	if len(str) == 0 {
		return -1
	}

	windowStart, maxLength := 0, 0
	r := []rune(str)
	charFrequencyMap := make(map[string]int)
	for windowEnd := 0; windowEnd < len(r); windowEnd++ {
		c := r[windowEnd]
		charFrequencyMap[string(c)] = charFrequencyMap[string(c)] + 1

		for len(charFrequencyMap) > k {
			s := r[windowStart]
			charFrequencyMap[string(s)] = charFrequencyMap[string(s)] - 1
			if charFrequencyMap[string(s)] == 0 {
				delete(charFrequencyMap, string(s))
			}
			windowStart++
		}
		maxLength = utils.GetMax(maxLength, windowEnd-windowStart+1)

	}
	fmt.Print(string(r[windowStart:len(r)]) + "-->")
	return maxLength

}
