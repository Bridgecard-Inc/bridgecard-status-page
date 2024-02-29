package domain

type FetchAllResourcesApiResponseData struct {
	Resources []Resource `json:"resources"`
}

type FetchAllResourcesApiResponse struct {
	Status  string                           `json:"status"`
	Message string                           `json:"message"`
	Data    FetchAllResourcesApiResponseData `json:"data"`
}

type FetchAllAdminDetailsApiResponseData struct {
	Admin Admin `json:"admin"`
}

type FetchAdminDetailsApiResponse struct {
	Status  string                              `json:"status"`
	Message string                              `json:"message"`
	Data    FetchAllAdminDetailsApiResponseData `json:"data"`
}
