package dao

import "github.com/Job-Search-Website/models"

func CreateUser(user models.User) {
	db.Create(&user)
}
