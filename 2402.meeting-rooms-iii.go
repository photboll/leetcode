/*
 * @lc app=leetcode id=2402 lang=golang
 *
 * [2402] Meeting Rooms III
 */

// @lc code=start
import (
	"container/heap"
)

type IntHeap []int
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0:n-1]
	return x
}

type BusyRoom struct {
	end  int
	room int
}
type BusyHeap []BusyRoom
func (h BusyHeap) Len() int { return len(h) }
func (h BusyHeap) Less(i, j int) bool {
	if h[i].end == h[j].end {
		return h[i].room < h[j].room
	}
	return h[i].end < h[j].end
}
func (h BusyHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *BusyHeap) Push(x interface{}) { *h = append(*h, x.(BusyRoom)) }
func (h *BusyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0:n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	free := &IntHeap{}
	heap.Init(free)
	for i := 0; i < n; i++ {
		heap.Push(free, i)
	}

	busy := &BusyHeap{}
	heap.Init(busy)
	count := make([]int, n)

	for _, m := range meetings {
		start, end := m[0], m[1]

		for busy.Len() > 0 && (*busy)[0].end <= start {
			r := heap.Pop(busy).(BusyRoom)
			heap.Push(free, r.room)
		}

		var room, newEnd int
		if free.Len() > 0 {
			room = heap.Pop(free).(int)
			newEnd = end
		} else {
			r := heap.Pop(busy).(BusyRoom)
			room = r.room
			newEnd = r.end + (end - start)
		}
		heap.Push(busy, BusyRoom{newEnd, room})
		count[room]++
	}

	maxRoom := 0
	for i := 1; i < n; i++ {
		if count[i] > count[maxRoom] {
			maxRoom = i
		}
	}
	return maxRoom
}
// @lc code=end

