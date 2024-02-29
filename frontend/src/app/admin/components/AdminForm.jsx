"use client";

import React, { useEffect, useState } from "react";
import Select from "react-select";
import makeAnimated from "react-select/animated";
import axios from "axios";
import moment from "moment";
// import { getResources } from "@/utils/fetchData";

export const AdminForm = ({ accessToken }) => {
	const [resources, setResources] = useState([]);
	const [resourceIds, setResourceIds] = useState([]);
	const [fetching, setFetching] = useState(true);
	const [submitting, setSubmitting] = useState(false);
	const [message, setMessage] = useState("");
	const [formValues, setFormValues] = useState({
		company_name: "",
		company_accent_color: "",
		company_logo_url: "",
	});

	const handleChange = e => {
		const { name, value } = e.target; // Get the name of the input and its value
		setFormValues({
			...formValues,
			[name]: value, // Update the corresponding field in the state
		});
	};

	const animatedComponents = makeAnimated();

	const constructDropdownOption = arr => {
		const options = arr.map(option => {
			return {
				label: option.title,
				value: option._id,
			};
		});

		return options;
	};

	const uploadDowntime = async () => {
		setSubmitting(true);

		try {
			const res = await axios.patch(
				`http://${process.env.BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/admin/`,
				formValues,
				{
					headers: {
						token: accessToken,
					},
				}
			);

			setMessage(res.data.message);
		} catch (err) {
		} finally {
			setSubmitting(false);

			setTimeout(() => {
				setMessage("");
			}, 3000);
		}
	};

	useEffect(() => {
		const fetchResources = async () => {
			setFetching(true);

			try {
				const res = await axios.get(
					`http://${process.env.BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/admin/`,
					{
						headers: {
							token: accessToken,
						},
					}
				);
				console.log("res", res);
				setFormValues({
					company_name: res.data.data.admin.company_name,
					company_accent_color: res.data.data.admin.company_accent_color,
					company_logo_url: res.data.data.admin.company_logo_url,
				});
			} catch (err) {
			} finally {
			}
		};

		fetchResources();
	}, []);

	return (
		<div className="max-w-[500px] mx-auto mt-20 bg-white border rounded-lg p-5 shadow-xl">
			<h3 className="text-base font-semibold mb-6">Update Admin Settings</h3>
			<div className="mb-4">
				<label htmlFor="input" className="block  text-sm font-semibold mb-1">
					Company Name
				</label>
				<input
					id="input"
					type="text"
					placeholder="Company Name"
					className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
					name="company_name"
					value={formValues.company_name}
					onChange={handleChange}
				/>
			</div>

			<div className="mb-4">
				<label htmlFor="input" className="block  text-sm font-semibold mb-1">
					Company logo url
				</label>

				<input
					id="input"
					type="text"
					placeholder="company logo url"
					className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
					name="company_logo_url"
					value={formValues.company_logo_url}
					onChange={handleChange}
				/>
			</div>

			<div className="mb-4">
				<label htmlFor="input" className="block  text-sm font-semibold mb-1">
					Company color
				</label>

				<input
					id="input"
					type="text"
					placeholder="Company accent color"
					className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
					name="company_accent_color"
					value={formValues.company_accent_color}
					onChange={handleChange}
				/>
			</div>

			{message && (
				<div className="bg-green-50 h-[40px] text-green-500">{message}</div>
			)}
			<button
				className={` ${
					admin.company_accent_color
						? `bg-[${admin.company_accent_color}]`
						: "bg-black"
				} bg-black mt-6 h-[40px]  text-white font-bold py-2 px-4 rounded w-full`}
				disabled={submitting}
				onClick={uploadDowntime}
			>
				{submitting ? "Updating..." : "Update"}
			</button>
		</div>
	);
};
