package bootstrap

import (
	"os"
)

type Env struct {
	BridgecardStatusPageBackendHost string `mapstructure:"BRIDGECARD_STATUS_PAGE_BACKEND_HOST"`
	BridgecardStatusPageBackendPort string `mapstructure:"BRIDGECARD_STATUS_PAGE_BACKEND_PORT"`
}

func NewEnv() *Env {

	env := Env{
		BridgecardStatusPageBackendHost: os.Getenv("BRIDGECARD_STATUS_PAGE_BACKEND_HOST"),
		BridgecardStatusPageBackendPort: os.Getenv("BRIDGECARD_STATUS_PAGE_BACKEND_PORT"),
	}

	return &env
}
