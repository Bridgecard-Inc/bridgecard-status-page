"use client";

import React, { useEffect, useState } from "react";
import Select from "react-select";
import makeAnimated from "react-select/animated";
import axios from "axios";
import moment from "moment";
import nextConfig from "../../../../next.config.mjs";
// import { getResources } from "@/utils/fetchData";

export const CreateDowntimeForm = ({ accessToken, admin }) => {
	const [resources, setResources] = useState([]);
	const [resourceIds, setResourceIds] = useState([]);
	const [fetching, setFetching] = useState(true);
	const [submitting, setSubmitting] = useState(false);
	const [message, setMessage] = useState("");
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

	const modifyList = arr => {
		let newArr = [];
		for (let i = 0; i < arr.length; i++) {
			newArr.push(arr[i].value);
		}

		return newArr;
	};

	const customStyles1 = {
		placeholder: () => ({
			fontSize: "14px",
			color: "#797979;",
			marginTop: "-35px",
		}),

		control: (base, state) => ({
			...base,
			border: state.isFocused ? "1px solid #ecc337" : "1px solid #ebebeb",
			// This line disable the blue border
			boxShadow: "none",
			borderRadius: "8px",
			minHeight: "40px",
		}),

		singleValue: (provided, state) => ({
			...provided,
			color: "#141416",
			fontSize: "16px",
		}),

		option: (provided, state) => ({
			...provided,
			color: state.isSelected ? "white" : "black",
			background: state.isSelected ? "#ecc337" : "white",
			fontSize: "16px",
		}),

		valueContainer: (provided, state) => ({
			...provided,
			minHeight: "40px",
			display: "flex",
			alignItems: "center",
			paddingLeft: "20px",
		}),
	};

	const uploadDowntime = async () => {
		setSubmitting(true);
		const values = {
			resource_ids: resourceIds,
			title: formValues.title,
			description: formValues.description,
			start_at: moment(formValues.start_at).unix(),
			end_at: moment(formValues.end_at).unix(),
		};
		try {
			const res = await axios.post(
				`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/downtime/`,
				values,
				{
					headers: {
						token: accessToken,
					},
				}
			);

			setMessage(res.data.message);
			setFormValues({
				title: "",
				description: "",
				start_at: "",
				end_at: "",
			});
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
					`http://${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT}/v1/resource/`
				);

				setResources(res.data.data.resources);
			} catch (err) {
			} finally {
			}
		};

		fetchResources();
	}, []);

	return (
		<div className="max-w-[500px] mx-auto mt-20 bg-white border rounded-lg p-5 shadow-xl">
			<h3 className="text-base font-semibold mb-6">Upload Downtime</h3>
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
					Description
				</label>

				<textarea
					rows={4}
					id="input"
					type="text"
					placeholder="Enter your text here"
					name="description"
					value={formValues.description}
					onChange={handleChange}
					className="shadow appearance-none border rounded-lg  h-[80px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
				/>
			</div>

			<div className="mb-4 grid grid-cols-2 gap-4">
				<div>
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						Start At
					</label>

					<input
						id="input"
						type="date"
						name="start_at"
						value={formValues.start_at}
						onChange={handleChange}
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
					/>
				</div>

				<div>
					<label htmlFor="input" className="block  text-sm font-semibold mb-1">
						End At
					</label>

					<input
						id="input"
						type="date"
						name="end_at"
						value={formValues.end_at}
						onChange={handleChange}
						className="shadow appearance-none border rounded-lg  h-[40px]  w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline placeholder:text-sm"
					/>
				</div>
			</div>
			<div className="mb-4 w-full">
				<label htmlFor="input" className="block  text-sm font-semibold mb-1">
					Resources
				</label>

				<Select
					styles={customStyles1}
					closeMenuOnSelect={false}
					components={animatedComponents}
					placeholder=" Select resources"
					isMulti
					options={constructDropdownOption(resources)}
					isSearchable={false}
					instanceId={1}
					onChange={e => setResourceIds(modifyList(e))}
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
				{submitting ? "Uploading..." : "Upload"}
			</button>
		</div>
	);
};
