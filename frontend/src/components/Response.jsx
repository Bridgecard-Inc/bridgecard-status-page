import React from "react";
import Image from "next/image";
import Status from "./Status";
import Downtimes from "./Downtimes";
import { getAdmin } from "@/utils/fetchData";

const Response = async () => {
	const data = await getAdmin();
	const admin = data.data.admin;

	return (
		<main className="min-h-full max-w-[800px] mx-auto md:py-20 py-20">
			<div className="flex flex-row justify-between items-center mb-10">
				{admin?.company_logo_url ? (
					<p>test</p>
				) : admin?.company_name ? (
					<p className=" font-semibold text-base">{admin?.company_name}</p>
				) : (
					<p className=" font-semibold text-base">Company's Name</p>
				)}

				<p className=" font-normal text-base">Api Status Page</p>
			</div>
			<Downtimes />
			<Status />
		</main>
	);
};

export default Response;
