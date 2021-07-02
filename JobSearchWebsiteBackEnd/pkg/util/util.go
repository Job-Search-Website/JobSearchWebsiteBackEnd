package util

import (
	"fmt"
	"github.com/jinzhu/gorm"
	"log"
	"reflect"
)

func CheckError(err error) bool {
	if err != nil {
		log.Fatal(err.Error())
		return true
	}
	return false
}

func CreateTableIfNotExist(db *gorm.DB, tableModels []interface{}) {
	for _, value := range tableModels {
		if !db.HasTable(value) {
			db.CreateTable(value)
			fmt.Println("Create table ", reflect.TypeOf(value), " successfully")
		}
	}
}
