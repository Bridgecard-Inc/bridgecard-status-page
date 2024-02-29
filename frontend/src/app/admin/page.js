"use client";

import React, { useEffect, useState } from "react";
import Image from "next/image";
import { CreateDowntimeForm } from "./components/CreateDowntimeForm";
import { AdminForm } from "./components/AdminForm";
import { LoginModal } from "./components/LoginModal.";
import axios from "axios";

import nextConfig from "../../../next.config.mjs";

export default function Admin() {
	const [accessToken, setAccessToken] = useState("");
	const [activeState, toggleActiveState] = useState(1);
	const [admin, setAdmin] = useState({});

	// const { publicRuntimeConfig } = getConfig();

	// // Access the environmental variables
	// const backendHost = publicRuntimeConfig.BACKEND_HOST;
	// const backendPort = publicRuntimeConfig.BACKEND_PORT;

	const navs = [
		{ id: 1, name: "Upload Downtime" },
		{ id: 3, name: "Update Settings" },
	];

	const toggleActive = index => {
		toggleActiveState(index);
	};

	useEffect(() => {
		async function getAdmin() {
			try {
				const res = await axios.get(
					`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/admin/`
				);
				setAdmin(res.data.data.admin);
			} catch (err) {
				console.log("err", err);
			}
		}

		getAdmin();
	}, []);

	return (
		<main className="min-h-full max-w-[800px] mx-auto md:py-20 py-20">
			<div className="flex flex-row justify-between items-center mb-10">
				{admin?.company_logo_url ? (
					<Image src={company_logo_url} width={155} height={40} />
				) : admin?.company_name ? (
					<p className=" font-semibold text-base">{admin?.company_name}</p>
				) : (
					<p className=" font-semibold text-base">Company's Name</p>
				)}
				<p className=" font-normal text-base">Admin Portal</p>
			</div>

			<div className="flex flex-row w-full border-b-2  ">
				{navs.map(nav => {
					return (
						<div
							key={nav.id}
							className={
								activeState === nav.id
									? `mr-5 w-auto text-sm font-semibold cursor-pointer text-teal-500  border-b-2 border-b-teal-500 py-2`
									: `mr-5 w-auto text-sm font-semibold cursor-pointer py-2`
							}
							onClick={() => toggleActive(nav.id)}
						>
							{nav.name}
						</div>
					);
				})}
			</div>

			{activeState === 1 ? (
				<CreateDowntimeForm accessToken={accessToken} admin={admin} />
			) : (
				<AdminForm accessToken={accessToken} admin={admin} />
			)}
			{!accessToken && (
				<LoginModal setAccessToken={setAccessToken} admin={admin} />
			)}
		</main>
	);
}
