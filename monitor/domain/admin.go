package domain

type Admin struct {
	CompanyName        string `json:"company_name"`
	CompanyAccentColor string `json:"company_accent_color"`
	CompannyLogoUrl    string `json:"company_logo_url"`
	WebhookUrl         string `json:"webhook_url"`
}
