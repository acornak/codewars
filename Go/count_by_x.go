// Create a function with two arguments that will return an array of the first (n) multiples of (x).
// Assume both the given number and the number of times to count will be positive numbers greater than 0.
// Return the results as an array (or list in Python, Haskell or Elixir).

// Examples:

// countBy(1,10)  should return  {1,2,3,4,5,6,7,8,9,10}
// countBy(2,5)  should return {2,4,6,8,10}
package main

import (
	"fmt"
	"reflect"
)

func CountBy(x, n int) []int {
	var res []int

	for i := x; i <= n; i++ {
		res = append(res, i)
	}
	return res
}

func main() {
	type TestCase struct {
		x   int
		n   int
		res []int
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 1, n: 2, res: []int{1, 2}},
			{x: 1, n: 10, res: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}},
			{x: 2, n: 5, res: []int{2, 3, 4, 5}},
		},
	}

	for _, testCase := range testCases.sliceTestCases {
		if reflect.DeepEqual(CountBy(testCase.x, testCase.n), testCase.res) {
			fmt.Println("OK")
		} else {
			fmt.Printf("ERROR\nexpected %v got instead %v", testCase.res, CountBy(testCase.x, testCase.n))
		}
	}

}
