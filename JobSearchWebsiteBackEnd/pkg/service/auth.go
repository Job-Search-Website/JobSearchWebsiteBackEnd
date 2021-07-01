package service

import (
	"github.com/Job-Search-Website/models"
	"github.com/Job-Search-Website/pkg/dao"
	"github.com/Job-Search-Website/pkg/util"
	"github.com/gin-gonic/gin"
	"net/http"
)

func Signup(context *gin.Context) {
	email := context.PostForm("email")
	password := context.PostForm("password")
	name := context.PostForm("name")
	role := context.PostForm("role")
	passwordhash := util.HashWithSalt(password)
	user := models.User{
		Email: email, Password: passwordhash, Username: name, RegisterTimestamp: util.GetTimeStamp(),
		Role: role}
	dao.CreateUser(user)
	context.JSON(http.StatusOK, gin.H{
		"email": user.Email,
		"msg":   "注册成功",
	})
	return
}

func Login (context *gin.Context) {
	password := context.PostForm("password")
	email := context.PostForm("email")

	if(dao.IsEmailandPasswordMatched(email ,password)) {
		// token
	} else {
		context.JSON(http.StatusBadRequest, gin.H{
			"msg": "用户名密码不匹配",
		})
	}
}
func GetMyself(context *gin.Context){

}
