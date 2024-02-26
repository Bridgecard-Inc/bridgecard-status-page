"use client";

import React, { useEffect, useState } from "react";
import Image from "next/image";
import { CreateDowntimeForm } from "./components/CreateDowntimeForm";
import { LoginModal } from "./components/LoginModal.";

export default function Admin() {
	const [accessToken, setAccessToken] = useState("");
	return (
		<main className="min-h-full max-w-[800px] mx-auto md:py-20 py-20">
			<div className="flex flex-row justify-between items-center mb-10">
				<Image src={"assets/logo.svg"} width={155} height={40} />
				<p className=" font-normal text-base">Upload Downtime</p>
			</div>

			<CreateDowntimeForm accessToken={accessToken} />
			{!accessToken && <LoginModal setAccessToken={setAccessToken} />}
		</main>
	);
}
