// https://www.codewars.com/kata/57a04da9e298a7ee43000111/train/go

package codewars

func swap(sw []int) {
	for a, b := 0, len(sw)-1; a < b; a, b = a+1, b-1 {
		sw[a], sw[b] = sw[b], sw[a]
	}
}

func ReverseList(lst []int) []int {
	if lst != nil {
		swap(lst)
	}
	return lst
}
