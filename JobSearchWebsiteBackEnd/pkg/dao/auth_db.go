package dao
import (
	"github.com/Job-Search-Website/models"
	"golang.org/x/crypto/bcrypt"
)

func CreateUser(user models.User) {
	db.Create(&user)
}
func IsEmailandPasswordMatched (email string, psw string) (isEmailandPasswordMatched bool) {
	var user models.User
	db.Where("email = ?", email).Find(&user)
	result := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(psw))
	if result == nil {
		isEmailandPasswordMatched = true
	} else {
		isEmailandPasswordMatched = false
	}
	return
}
