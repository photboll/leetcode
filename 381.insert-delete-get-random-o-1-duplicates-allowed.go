package leetcode

import "math/rand"

/*
 * @lc app=leetcode id=381 lang=golang
 *
 * [381] Insert Delete GetRandom O(1) - Duplicates allowed
 */

// @lc code=start
type Set map[int]struct{}
func (s Set)Insert(val int){
	s[val] = struct{}{}
}
func (s Set)Delete(val int){
	delete(s, val)
}
//Pops an arbitrary element from the set
func (s Set) Pop() (int, bool){
	for key := range s{
		delete(s, key)
		return key, true
	}
	return 0, false
}
type RandomizedCollection struct {
	//THe main idea is that we don't actually delete anything when we remove 
	//We only remove the key to find the value
    dict map[int]Set//Holds a reference to a values index in data
	data []int//
}


func Constructor() RandomizedCollection {
    return RandomizedCollection{dict: map[int]Set{}, data:[]int{}}
}


func (this *RandomizedCollection) Insert(val int) bool {
	idxs, exists := this.dict[val]//Idxs is a set of idxs
	
	this.data = append(this.data, val)

	if idxs == nil{
		idxs = Set{}
	}
	idxs.Insert(len(this.data)-1)
	this.dict[val] = idxs
	return !exists
}


func (this *RandomizedCollection) Remove(val int) bool {
	//Swap the last element with the one being removed
	//Reduce the size of the set 
	idxs, exists := this.dict[val]
	if !exists {
		return false
	}
	//1. Get the indexes of the elements to be moved and removed
	iRemove, _:= idxs.Pop()//Get an arbitrary index with value val to remove
	iEnd := len(this.data) -1
	lastVal := this.data[iEnd]
	if iRemove != iEnd {
		//2. Update dict
		this.dict[lastVal].Delete(iEnd)//Update reference of moved element in dict
		this.dict[lastVal].Insert(iRemove)//delete old and insert new position
		//3. Swap
		this.data[iRemove], this.data[iEnd] = this.data[iEnd], this.data[iRemove]//Swap
	}

	//4. Delete the final element
	this.data = this.data[:iEnd]//Remove the value from data
	if len(idxs) == 0{
		delete(this.dict, val)
	}

	return true    
}


func (this *RandomizedCollection) GetRandom() int {
	return this.data[rand.Intn(len(this.data))]
}  

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
// @lc code=end

