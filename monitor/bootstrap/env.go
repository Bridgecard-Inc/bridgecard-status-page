package bootstrap

import (
	"log"
	"os"

	"github.com/spf13/viper"
)

type Env struct {
	BridgecardStatusPageBackendHost string `mapstructure:"BRIDGECARD_STATUS_PAGE_BACKEND_HOST"`
	BridgecardStatusPageBackendPort string `mapstructure:"BRIDGECARD_STATUS_PAGE_BACKEND_PORT"`
}

func NewEnv() *Env {

	var env = Env{}

	_, ok := os.LookupEnv("BRIDGECARD_STATUS_PAGE_BACKEND_HOST")
	if !ok {

		viper.SetConfigFile(".env")

		viper.AutomaticEnv()

		err := viper.Unmarshal(&env)
		if err != nil {
			log.Fatal("Environment can't be loaded: ", err)
		}

	} else {
		env = Env{
			BridgecardStatusPageBackendHost: os.Getenv("BRIDGECARD_STATUS_PAGE_BACKEND_HOST"),
			BridgecardStatusPageBackendPort: os.Getenv("BRIDGECARD_STATUS_PAGE_BACKEND_PORT"),
		}
	}

	return &env
}
