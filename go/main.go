package main

import (
	"fmt"

	"github.com/gowthamkaruturi/algorithmspatterns/slidingwindow"
)

func main() {
	// response := 0
	// arr := []int{2, 3, 4, 5, 8, 17}
	// response = slidingwindow.MaxSumInSubArray(arr, 3)
	// fmt.Printf("max sum from the subarray %v is	%d \n ", arr, response)
	// arr2 := []int{2, 1, 5, 2, 8}

	// response = slidingwindow.MinSumInSubArray(arr2, 7)
	// fmt.Printf("max sum from the subarray %v is	%d \n", arr2, response)
	// fmt.Println(slidingwindow.MinSumInSubArray([]int{3, 4, 1, 1, 6}, 8))

	// k := slidingwindow.LongestSlidingWindowKDistinct("araaci", 1)
	// fmt.Print(k)
	// fmt.Println()
	// k = slidingwindow.LongestSlidingWindowKDistinct("cbbebi", 3)
	// fmt.Print(k)
	// fmt.Println()
	// k = slidingwindow.MaxFruit([]rune("gowtham"))
	// fmt.Println(k)
	k := slidingwindow.NoRepeatSubstring("gowtham")
	fmt.Println(k)
	k = slidingwindow.NoRepeatSubstring("kavyammmm")
	fmt.Println(k)
}
