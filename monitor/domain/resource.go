package domain

type Status struct {
	ID             string `json:"_id"`
	ResourceID     string `json:"resource_id"`
	MonitoredAt    int    `json:"monitored_at"`
	MonitorSuccess bool   `json:"monitor_success"`
	DowntimeID     string `json:"downtime_id,omitempty"`
}

type Resource struct {
	ID                         string   `json:"_id"`
	Tag                        string   `json:"tag"`
	Title                      string   `json:"title"`
	URL                        string   `json:"url"`
	APIMethod                  string   `json:"api_method"`
	ExpectedResponseStatusCode int      `json:"expected_response_status_code"`
	Status                     []Status `json:"status"`
}

type ResourceStatusData struct {
	ResourceID     string `json:"resource_id"`
	MonitoredAt    int    `json:"monitored_at"`
	MonitorSuccess bool   `json:"monitor_success"`
}
