/** @type {import('next').NextConfig} */
const nextConfig = {
	publicRuntimeConfig: {
		// Define your environment variables here
		BACKEND_HOST: process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST,
		BACKEND_PORT: process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT,
		// Add more variables as needed
	},
};

export default nextConfig;
