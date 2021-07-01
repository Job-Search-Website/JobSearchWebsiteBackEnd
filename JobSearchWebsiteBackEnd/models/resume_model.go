package models

import "time"

type Resume struct {
	ID		string	`gorm:"primary_key"`
	HrEmail string
	JobSeekerEmail string
	IsReplied	bool
	ReleseTime	time.Time
	ReplyTime	time.Time
	ResumeContext string
	Reply	string
}
