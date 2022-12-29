package codewars

import "fmt"

func revertSlice(s []int) []int {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}

	return s
}

func Snail(snaipMap [][]int) []int {
	// copy the first row
	res := snaipMap[0]
	fmt.Println(res)

	// add last numbers of each row
	for _, v := range snaipMap {
		res = append(res, v[len(v)-1])
	}

	// add last row in reverse order
	res = append(res, revertSlice(snaipMap[len(snaipMap)-1])...)

	fmt.Println(res)
	fmt.Println(snaipMap)

	return res
}
