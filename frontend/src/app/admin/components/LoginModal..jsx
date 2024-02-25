"use client";
import React, { useState } from "react";

export const LoginModal = () => {
	const [formValues, setFormValues] = useState({
		title: "",
		description: "",
		start_at: "",
		end_at: "",
	});

	const handleChange = e => {
		const { name, value } = e.target; // Get the name of the input and its value
		setFormValues({
			...formValues,
			[name]: value, // Update the corresponding field in the state
		});
	};
	return (
		<div className="absolute bg-[rgba(0,0,0,0.8)]  z-10 flex justify-center items-center h-[100vh] w-full top-0 left-0">
			<div className="bg-white  rounded-lg shadow-lg h-[300px] w-[300px] p-5">
				<div className="mb-4">
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						Title
					</label>
					<input
						id="input"
						type="text"
						placeholder="Enter your text here"
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
						name="title"
						value={formValues.title}
						onChange={handleChange}
					/>
				</div>

				<div className="mb-4">
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						Title
					</label>
					<input
						id="input"
						type="text"
						placeholder="Enter your text here"
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
						name="title"
						value={formValues.title}
						onChange={handleChange}
					/>
				</div>
			</div>
		</div>
	);
};
