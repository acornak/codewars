package codewars

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountBy(t *testing.T) {
	assert := assert.New(t)
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
		assert.Equal(
			CountBy(testCase.x, testCase.n),
			testCase.res,
			fmt.Sprintf("ERROR: expected %v got instead %v. Args: %v and %v", testCase.res, CountBy(testCase.x, testCase.n), testCase.x, testCase.n),
		)
	}

}

func TestAreTheyTheSame(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   []int
		n   []int
		res bool
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19, 11 * 11},
				res: true,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19},
				res: false,
			},
			{
				x:   nil,
				n:   []int{11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19},
				res: false,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121, 14641, 20736, 361, 25921, 361, 20736, 361},
				res: true,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{231, 14641, 20736, 361, 25921, 361, 20736, 361},
				res: false,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121, 14641, 20736, 36100, 25921, 361, 20736, 361},
				res: false,
			},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Comp(testCase.x, testCase.n),
			fmt.Sprintf("ERROR: expected %v got instead %v. Args: %v and %v", testCase.res, Comp(testCase.x, testCase.n), testCase.x, testCase.n),
		)
	}

}

func TestTribonacci(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   [3]float64
		n   int
		res []float64
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: [3]float64{1, 1, 1}, n: 10, res: []float64{1, 1, 1, 3, 5, 9, 17, 31, 57, 105}},
			{x: [3]float64{0, 0, 1}, n: 10, res: []float64{0, 0, 1, 1, 2, 4, 7, 13, 24, 44}},
			{x: [3]float64{0, 1, 1}, n: 10, res: []float64{0, 1, 1, 2, 4, 7, 13, 24, 44, 81}},
			{x: [3]float64{1, 0, 0}, n: 10, res: []float64{1, 0, 0, 1, 1, 2, 4, 7, 13, 24}},
			{x: [3]float64{0, 0, 0}, n: 10, res: []float64{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}},
			{x: [3]float64{1, 2, 3}, n: 10, res: []float64{1, 2, 3, 6, 11, 20, 37, 68, 125, 230}},
			{x: [3]float64{3, 2, 1}, n: 10, res: []float64{3, 2, 1, 6, 9, 16, 31, 56, 103, 190}},
			{x: [3]float64{1, 1, 1}, n: 1, res: []float64{1}},
			{x: [3]float64{300, 200, 100}, n: 0, res: []float64{}},
			{
				x:   [3]float64{0.5, 0.5, 0.5},
				n:   30,
				res: []float64{0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Tribonacci(testCase.x, testCase.n),
			fmt.Sprintf("ERROR: expected %v got instead %v. Args: %v and %v", testCase.res, Tribonacci(testCase.x, testCase.n), testCase.x, testCase.n),
		)
	}

}
