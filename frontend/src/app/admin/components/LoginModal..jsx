"use client";
import React, { useState } from "react";
import axios from "axios";

export const LoginModal = ({ setAccessToken }) => {
	const [formValues, setFormValues] = useState({
		username: "",
		password: "",
	});
	const [submitting, setSubmitting] = useState(false);

	const handleChange = e => {
		const { name, value } = e.target; // Get the name of the input and its value
		setFormValues({
			...formValues,
			[name]: value, // Update the corresponding field in the state
		});
	};

	const login = async () => {
		setSubmitting(true);
		try {
			const res = await axios.post(
				"http://localhost:8080/v1/admin/login",
				formValues
			);
			setAccessToken(res.data.data.access_token);
		} catch (e) {
			alert(e.data.data.message);
		} finally {
			setSubmitting(false);
		}
	};

	return (
		<div className="absolute bg-[rgba(0,0,0,0.9)]  z-10 flex justify-center items-center h-[100vh] w-full top-0 left-0">
			<div className="bg-white  rounded-lg shadow-lg h-auto w-[400px] p-8">
				<h3 className="text-base font-semibold mb-6">Login as Admin</h3>
				<div className="mb-4">
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						Username
					</label>
					<input
						id="input"
						type="text"
						placeholder="Enter your username"
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
						name="username"
						value={formValues.username}
						onChange={handleChange}
					/>
				</div>

				<div className="mb-4">
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						Password
					</label>
					<input
						id="input"
						type="text"
						placeholder="Enter password"
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
						name="password"
						value={formValues.password}
						onChange={handleChange}
					/>
				</div>

				<button
					className="bg-black mt-6 h-[40px]  text-white font-bold py-2 px-4 rounded w-full"
					onClick={login}
					disabled={submitting}
				>
					{submitting ? "Submitting..." : "Login"}
				</button>
			</div>
		</div>
	);
};
