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
			comp(testCase.x, testCase.n),
			fmt.Sprintf("ERROR: expected %v got instead %v. Args: %v and %v", testCase.res, comp(testCase.x, testCase.n), testCase.x, testCase.n),
		)
	}

}
