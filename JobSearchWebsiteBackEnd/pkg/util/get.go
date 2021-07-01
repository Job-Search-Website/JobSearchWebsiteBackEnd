package util

import "time"

func GetTimeStamp() (t int64) {
	loc, _ := time.LoadLocation("Asia/Shanghai")
	t = time.Now().In(loc).Unix()
	return
}
