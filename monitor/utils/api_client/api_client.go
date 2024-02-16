package api_client

import (
	"bytes"
	"net/http"
)

type APIClient interface {
	Get(url string) (int, []byte, error)
	Post(url string, data []byte) (int, []byte, error)
	Put(url string, data []byte) (int, []byte, error)
	Patch(url string, data []byte) (int, []byte, error)
	Delete(url string) (int, error)
}

type HTTPClient struct {
	client *http.Client
}

func NewHTTPClient() *HTTPClient {
	return &HTTPClient{
		client: &http.Client{},
	}
}

func (c *HTTPClient) Get(url string) (int, []byte, error) {
	resp, err := c.client.Get(url)
	if err != nil {
		return 500, nil, err
	}
	defer resp.Body.Close()

	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	return resp.StatusCode, buf.Bytes(), nil
}

func (c *HTTPClient) Post(url string, data []byte) (int, []byte, error) {
	resp, err := c.client.Post(url, "application/json", bytes.NewBuffer(data))
	if err != nil {
		return 500, nil, err
	}
	defer resp.Body.Close()

	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	return resp.StatusCode, buf.Bytes(), nil
}

func (c *HTTPClient) Put(url string, data []byte) (int, []byte, error) {
	req, err := http.NewRequest("PUT", url, bytes.NewBuffer(data))
	if err != nil {
		return 500, nil, err
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.client.Do(req)
	if err != nil {
		return 500, nil, err
	}
	defer resp.Body.Close()

	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	return resp.StatusCode, buf.Bytes(), nil
}

func (c *HTTPClient) Delete(url string) (int, error) {
	req, err := http.NewRequest("DELETE", url, nil)
	if err != nil {
		return 500, err
	}

	resp, err := c.client.Do(req)
	if err != nil {
		return 500, err
	}
	defer resp.Body.Close()

	return resp.StatusCode, nil
}

func (c *HTTPClient) Patch(url string, data []byte) (int, []byte, error) {
	req, err := http.NewRequest("PATCH", url, bytes.NewBuffer(data))
	if err != nil {
		return 500, nil, err
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.client.Do(req)
	if err != nil {
		return 500, nil, err
	}
	defer resp.Body.Close()

	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	return resp.StatusCode, buf.Bytes(), nil
}
