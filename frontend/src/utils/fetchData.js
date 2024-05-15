export async function getResources() {
	console.log(
		"the url",
		` http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/resource/`
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
		console.log("an error occured");
	}

	return res.json();
}

export async function getDowntimes() {
	console.log(
		"the url2",
		` http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/downtime/`
	);
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
		console.log("an error occured");
	}

	return res.json();
}

export async function getAdmin() {
	console.log(
		"the url3",
		` http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/admin/`
	);
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
		console.log("an error occured");
	}

	return res.json();
}
