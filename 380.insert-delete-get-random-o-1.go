package leetcode	
import "math/rand"
/*
 * @lc app=leetcode id=380 lang=golang
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
type RandomizedSet struct {
	//THe main idea is that we don't actually delete anything when we remove 
	//We only remove the key to find the value
    dict map[int]int//Holds a reference to a values index in data
	data []int//
	size int 
}


func Constructor() RandomizedSet {
    return RandomizedSet{dict: map[int]int{},data:[]int{}, size: 0}
}


func (this *RandomizedSet) Insert(val int) bool {
	_, exists := this.dict[val]
	
	if !exists {//The value was not seen before
		if this.size == len(this.data){//No spare room in data 
			this.data = append(this.data, val)
			this.dict[val] = this.size
		}else{
			//values between size and len(data) have been removed
			//So they are safe to be overwritten
			this.data[this.size] = val
			this.dict[val] = this.size
		}
		this.size++
	}

	return !exists
}


func (this *RandomizedSet) Remove(val int) bool {
	//Swap the last element with the one being removed
	//Reduce the size of the set 
	idx, exists := this.dict[val]
	if !exists{
		return false
	}
	this.size--
	this.dict[this.data[this.size]] = idx //Update position in the map
	this.data[idx], this.data[this.size] = this.data[this.size], this.data[idx]//Swap
	delete(this.dict, this.data[this.size])//Remove reference in dict
	return true    
}


func (this *RandomizedSet) GetRandom() int {
	return this.data[rand.Intn(this.size)]
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
// @lc code=end

