package main

import (
	"fmt"
	"slices"
	"sync"
	"time"
)

var counter int
var mu sync.Mutex
var rmu sync.RWMutex

func average(nums []time.Duration) time.Duration {
	var sum time.Duration
	for _, num := range nums {
		sum += num
	}
	return sum / time.Duration(len(nums))
}

func decreament() {
	mu.Lock()
	defer mu.Unlock()

	// rmu.Lock()
	// defer rmu.Unlock()
	counter--
}

func increment() {
	mu.Lock()
	defer mu.Unlock()

	// rmu.Lock()
	// defer rmu.Unlock()
	counter++
}

func main() {
	var wg1 sync.WaitGroup
	var wg2 sync.WaitGroup
	var res1 []time.Duration
	var res2 []time.Duration
	for j := 0; j < 10; j++ {
		startTime1 := time.Now()
		wg1.Add(1)
		go func() {
			for i := 0; i < 10000; i++ {
				wg1.Add(1)
				go func() {
					defer wg1.Done()
					increment()
				}()
			}
			wg1.Done()
		}()
		elapsedTime1 := time.Since(startTime1)

		startTime2 := time.Now()
		wg2.Add(1)
		go func() {
			for i := 0; i < 10000; i++ {
				wg2.Add(1)
				go func() {
					defer wg2.Done()
					decreament()
				}()
			}
			wg2.Done()
		}()
		elapsedTime2 := time.Since(startTime2)

		wg1.Wait()
		wg2.Wait()

		fmt.Println("result1", elapsedTime1)
		fmt.Println("result2", elapsedTime2)

		res1 = append(res1, elapsedTime1)
		res2 = append(res2, elapsedTime2)

	}

	fmt.Println("Total counter:", counter)
	fmt.Printf("Average time: %v\n", average(res1))
	fmt.Printf("Max time %v\n", slices.Max(res1))

	fmt.Printf("Average time: %v\n", average(res2))
	fmt.Printf("Max time %v\n", slices.Max(res2))
}
