package domain

type ResponseData struct {
	Resources []Resource `json:"resources"`
}

type FetchAllResourcesApiResponse struct {
	Status  string       `json:"status"`
	Message string       `json:"message"`
	Data    ResponseData `json:"data"`
}
