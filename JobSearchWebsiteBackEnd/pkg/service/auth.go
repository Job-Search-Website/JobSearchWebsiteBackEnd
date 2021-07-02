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
	return
}
func Introduction(context *gin.Context){
	email:=context.PostForm("email")
	introduction:=context.PostForm("introduction")
	dao.EditIntroduction(email,introduction)
	context.JSON(http.StatusOK,gin.H{
		"msg":"编辑成功",
	})
	return
}
func GetMyself(context *gin.Context) {
	email := context.PostForm("email")
	user, _ := dao.GetUser(email)
	context.JSON(http.StatusOK, gin.H{
		"email":        user.Email,
		"name":         user.Username,
		"role":         user.Role,
		"introduction": user.Introduction,
	})
	return
}
func GetMyResume(context *gin.Context){
	email:=context.PostForm("email")
	resume:=dao.GetResumeByJobSeeker(email)
	results:=[]map[string]interface{}{}
	for _,temp:=range resume{
		if temp.IsReplied {
			user,_:=dao.GetUser(temp.HrEmail)
			results = append(results, map[string]interface{}{
				"hremail":       temp.HrEmail,
				"resumecontext": temp.ResumeContext,
				"reply":         temp.Reply,
				"releasetime":   temp.ReleseTime,
				"replytime":     temp.ReplyTime,
				"hrname":		 user.Username,
				"hrintroduction":user.Introduction,
			})
		}else{
			user,_:=dao.GetUser(temp.HrEmail)
			results = append(results, map[string]interface{}{
				"hremail":       temp.HrEmail,
				"resumecontext": temp.ResumeContext,
				"releasetime":   temp.ReleseTime,
				"hrname":		 user.Username,
				"hrintroduction":user.Introduction,
			})
		}
	}
	context.JSON(http.StatusOK,gin.H{
		"resume":results,
	})
	return
}
func GetMyJobSeeker(context *gin.Context){
	email:=context.PostForm("email")
	resume:=dao.GetResumeByHr(email)
	results:=[]map[string]interface{}{}
	for _,temp:=range resume{
		if temp.IsReplied {
			user,_:=dao.GetUser(temp.JobSeekerEmail)
			results = append(results, map[string]interface{}{
				"jobseekeremail":temp.JobSeekerEmail,
				"resumecontext": temp.ResumeContext,
				"reply":         temp.Reply,
				"releasetime":   temp.ReleseTime,
				"replytime":     temp.ReplyTime,
				"jobseekername": user.Username,
			})
		}else{
			user,_:=dao.GetUser(temp.HrEmail)
			results = append(results, map[string]interface{}{
				"jobseekeremail":temp.JobSeekerEmail,
				"resumecontext": temp.ResumeContext,
				"releasetime":   temp.ReleseTime,
				"jobseekername": user.Username,
			})
		}
	}
	context.JSON(http.StatusOK,gin.H{
		"resume":results,
	})
	return
}