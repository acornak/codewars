// A format for expressing an ordered list of integers is to use a comma separated list of either

// individual integers
// or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
// Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

// Example:

// solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
// returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

// https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/go

package codewars

import (
	"fmt"
	"strconv"
	"strings"
)

func minMax(array []int) (int, int) {
	var max int = array[0]
	var min int = array[0]
	for _, value := range array {
		if max < value {
			max = value
		}
		if min > value {
			min = value
		}
	}
	return min, max
}

func intInSlice(a int, list []int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

// func left to right
// func right to left
// func downwards
// func upwards

// TODO
func range_extraction(args []int) string {
	if len(args) < 3 {
		return ""
	}

	res := []string{}
	helper := []int{}

	for i := 0; i < len(args)-1; i += 1 {
		if args[i+1]-args[i] == 1 {
			helper = append(helper, args[i], args[i+1])
		} else {
			if len(helper) > 4 {
				min, max := minMax(helper)
				res = append(res, fmt.Sprintf("%d-%d", min, max))
			} else if len(helper) != 0 {
				for _, v := range helper {
					res = append(res, strconv.Itoa(v))
				}
			}
			if !intInSlice(args[i], helper) {
				res = append(res, strconv.Itoa(args[i]))
			}
			helper = nil
		}
	}

	if len(helper) > 4 {
		min, max := minMax(helper)
		res = append(res, fmt.Sprintf("%d-%d", min, max))
	} else if len(helper) > 0 {
		for _, v := range helper {
			res = append(res, strconv.Itoa(v))
		}
	} else {
		res = append(res, strconv.Itoa(args[len(args)-1]))
	}

	return strings.Join(res[:], ",")
}
