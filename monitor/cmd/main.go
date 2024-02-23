package main

import (
	"encoding/json"
	"fmt"
	"sync"
	"time"

	"github.com/Bridgecard-Inc/bridgecard-status-page/domain"

	bootstrap "github.com/Bridgecard-Inc/bridgecard-status-page/bootstrap"
	api_client "github.com/Bridgecard-Inc/bridgecard-status-page/utils/api_client"
)

func fetchAllResources(bridgecardStatusPageBackendHost string, bridgecardStatusPageBackendPort int) (*[]domain.Resource, error) {

	client := api_client.NewHTTPClient()

	url := fmt.Sprintf("http://%s:%d/v1/resource/", bridgecardStatusPageBackendHost, bridgecardStatusPageBackendPort)

	_, data, _ := client.Get(url)

	var apiResponse domain.FetchAllResourcesApiResponse

	if err := json.Unmarshal([]byte(data), &apiResponse); err != nil {
		return nil, err
	}

	return &apiResponse.Data.Resources, nil

}

func addResourceStatus(data domain.ResourceStatusData, bridgecardStatusPageBackendHost string, bridgecardStatusPageBackendPort int) error {

	client := api_client.NewHTTPClient()

	jsonData, err := json.Marshal(data)

	if err != nil {
		return err
	}

	url := fmt.Sprintf("http://%s:%d/v1/resource/status/", bridgecardStatusPageBackendHost, bridgecardStatusPageBackendPort)

	_, _, err = client.Post(url, jsonData)
	if err != nil {
		return err
	}

	return nil

}

func pingResource(resource domain.Resource) domain.ResourceStatusData {

	client := api_client.NewHTTPClient()

	var statusCode int

	if resource.APIMethod == "POST" {

		statusCode, _, _ = client.Post(resource.URL, []byte{})

	} else if resource.APIMethod == "GET" {

		statusCode, _, _ = client.Get(resource.URL)

	} else if resource.APIMethod == "PATCH" {

		statusCode, _, _ = client.Patch(resource.URL, []byte{})

	} else if resource.APIMethod == "PUT" {

		statusCode, _, _ = client.Put(resource.URL, []byte{})
	} else if resource.APIMethod == "DELETE" {

		statusCode, _ = client.Delete(resource.URL)
	}

	var monitorSuccess = false

	if statusCode == resource.ExpectedResponseStatusCode {

		monitorSuccess = true

	}

	eventID := time.Now().Unix()

	return domain.ResourceStatusData{
		ResourceID:     resource.ID,
		MonitoredAt:    int(eventID),
		MonitorSuccess: monitorSuccess,
	}

}

func main() {

	env := bootstrap.NewEnv()

	ticker := time.NewTicker(5 * time.Second)
	defer ticker.Stop()

	for {
		<-ticker.C
		resources, err := fetchAllResources(env.BridgecardStatusPageBackendHost, env.BridgecardStatusPageBackendPort)
		if err != nil {
			return
		}

		results := make(chan domain.ResourceStatusData)

		var wg sync.WaitGroup

		for _, resource := range *resources {
			wg.Add(1)
			go func(resource domain.Resource) {
				defer wg.Done()
				result := pingResource(resource)
				results <- result
			}(resource)
		}

		go func() {
			wg.Wait()
			close(results)
		}()

		// Process the results
		for result := range results {
			addResourceStatus(result, env.BridgecardStatusPageBackendHost, env.BridgecardStatusPageBackendPort)
		}
	}
}
