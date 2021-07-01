package util

import (
	"encoding/json"
	"fmt"
	"github.com/Job-Search-Website/models"
	"io/ioutil"
	"log"
	"os"
	"time"
)

func GetTimeStamp() (t int64) {
	loc, _ := time.LoadLocation("Asia/Shanghai")
	t = time.Now().In(loc).Unix()
	return
}
func ReadSettingsFromFile(settingFilePath string) (config models.Config) {
	jsonFile, err := os.Open(settingFilePath)
	if err != nil {
		fmt.Println(err)
	}
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	err = json.Unmarshal(byteValue, &config)
	if err != nil {
		log.Panic(err)
	}
	return config
}