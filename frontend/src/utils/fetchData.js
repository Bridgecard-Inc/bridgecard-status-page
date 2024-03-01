export async function getResources() {
	console.log(
		"utils",
		process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST
	);
	const res = await fetch(
		`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/resource/`,
		{
			cache: "no-store",
		}
	);
	// The return value is *not* serialized
	// You can return Date, Map, Set, etc.

	if (!res.ok) {
		// This will activate the closest `error.js` Error Boundary
		throw new Error("Failed to fetch data");
	}

	return res.json();
}

export async function getDowntimes() {
	const res = await fetch(
		`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/downtime/`,
		{
			cache: "no-store",
		}
	);
	// The return value is *not* serialized
	// You can return Date, Map, Set, etc.

	if (!res.ok) {
		// This will activate the closest `error.js` Error Boundary
		throw new Error("Failed to fetch data");
	}

	return res.json();
}

export async function getAdmin() {
	const res = await fetch(
		`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/admin/`,
		{
			cache: "no-store",
		}
	);
	// The return value is *not* serialized
	// You can return Date, Map, Set, etc.

	if (!res.ok) {
		// This will activate the closest `error.js` Error Boundary
		throw new Error("Failed to fetch data");
	}

	return res.json();
}
