package slidingwindow

import "github.com/gowthamkaruturi/algorithmspatterns/utils"

func NoRepeatSubstring(str string) int {

	windowStart, maxlength := 0, 0
	r := []rune(str)
	m := make(map[string]int)
	for windowEnd := 0; windowEnd < len(str); windowEnd++ {
		c := r[windowEnd]
		if val, ok := m[string(c)]; ok {
			windowStart = utils.GetMax(maxlength, val)
		}
		m[string(c)] = windowEnd
		maxlength = utils.GetMax(maxlength, windowEnd-windowStart+1)
	}

	return maxlength

}
