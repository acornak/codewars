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

	for i := 1; i <= n; i++ {
		res = append(res, i*x)
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
			{x: 1, n: 1, res: []int{1}},
			{x: 1, n: 2, res: []int{1, 2}},
			{x: 1, n: 10, res: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}},
			{x: 2, n: 5, res: []int{2, 4, 6, 8, 10}},
			{x: 3, n: 5, res: []int{3, 6, 9, 12, 15}},
			{x: 50, n: 5, res: []int{50, 100, 150, 200, 250}},
			{x: 100, n: 5, res: []int{100, 200, 300, 400, 500}},
		},
	}

	for _, testCase := range testCases.sliceTestCases {
		if reflect.DeepEqual(CountBy(testCase.x, testCase.n), testCase.res) {
			fmt.Println("OK")
		} else {
			fmt.Printf("ERROR: expected %v got instead %v\n", testCase.res, CountBy(testCase.x, testCase.n))
		}
	}

}
