package router

import (
	"github.com/Job-Search-Website/pkg/service"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func InitRouter(r *gin.Engine) {
	config := cors.Config{
		AllowMethods:     []string{"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"},
		AllowHeaders:     []string{"Origin", "Content-Length", "Content-Type", "access-control-allow-origin", "token"},
		AllowCredentials: false,
	}
	config.AllowAllOrigins = true
	r.Use(cors.New(config))
	api := r.Group("/api")
	{
		user := api.Group("/auth")
		{
			user.Use(cors.Default())
			user.POST("/signup", service.Signup)
		}
		resume := api.Group("/resume")
		{
			resume.Use(cors.Default())
			resume.GET("",service.GetResume)
			resume.POST("",service.ReleaseResume)
		}
		hr := api.Group("/hr")
		{
			hr.Use(cors.Default())
			hr.GET("hr_list",service.GetHrList)
		}
	}
}
