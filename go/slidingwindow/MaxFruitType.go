package slidingwindow

import "github.com/gowthamkaruturi/algorithmspatterns/utils"

func MaxFruit(fruits []rune) int {
	if len(fruits) <= 0 {
		return -1
	}
	fruitFrequency := make(map[string]int)

	windowStart, maxlength := 0, 0

	for windowEnd := 0; windowEnd < len(fruits); windowEnd++ {
		fruitFrequency[string(fruits[windowEnd])] = fruitFrequency[string(fruits[windowEnd])] + 1
		for len(fruitFrequency) > 2 {
			fruitFrequency[string(fruits[windowEnd])] = fruitFrequency[string(fruits[windowEnd])] - 1
			if fruitFrequency[string(fruits[windowEnd])] == 0 {
				delete(fruitFrequency, string(fruits[windowStart]))
			}
			windowStart++
		}
		maxlength = utils.GetMax(maxlength, windowEnd-windowStart+1)
	}
	return maxlength
}
