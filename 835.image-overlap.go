package leetcode
/*
 * @lc app=leetcode id=835 lang=golang
 *
 * [835] Image Overlap
 */

// @lc code=start
type Translation struct{
	X, Y int
}
func largestOverlap(img1 [][]int, img2 [][]int) int {
	//Compares every pixel with a one in img1 with every pixel with a one in img2
	counter := map[Translation]int{}
	for r1 := range img1{
		for c1 := range img1{
			if img1[r1][c1] == 1{
				//Check this point against every single pixel in img2
				for r2 := range img2{
					for c2 := range img2{
						if img2[r2][c2] == 1{
							counter[Translation{X: c1 - c2, Y: r1- r2}]++
						}
					}
				}
			}
		}
	}
	result := 0
	for _, val:= range counter{
		result = max(result, val)
	}
	return result
}
// @lc code=end

