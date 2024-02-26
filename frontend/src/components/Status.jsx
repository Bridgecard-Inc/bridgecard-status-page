import React from "react";
import { getResources } from "@/utils/fetchData";

// grey bars for when there's no data available

const Status = async () => {
	const data = await getResources();

	console.log("resources", data.data.resources);

	const createEmptyBars = arr => {
		let barArr = [];
		if (arr.length < 70) {
			barArr = [...Array(70 - arr.length).keys()];
		}

		return barArr;
	};

	function last50Elements(array) {
		// Check if the array has fewer than 50 elements
		if (array.length <= 70) {
			return array;
		}

		// Use slice to get the last 50 elements
		return array.slice(-70);
	}

	return (
		<div className="w-full">
			<p className="text-gray-500 text-right mb-1">
				Uptime over the past 30 days
			</p>

			{/* <h3 className="text-base font-semibold mb-5">Mono Connect</h3> */}

			{data.data.resources.map((resource, index) => {
				return (
					<div
						className="border-x border-b border-gray-300 p-6 first-of-type:border-t"
						key={index}
					>
						<div>
							<div className="w-full flex flex-row justify-between items-center mb-1">
								<h3 className="text-base font-semibold capitalize">
									{resource.title}
								</h3>
								<p className="text-base font-base text-green-500">
									Operational
								</p>
							</div>
							<div className="flex flex-row">
								{createEmptyBars(resource.status).map((bar, index) => {
									return (
										<div
											key={index}
											className={`bg-gray-300 h-[40px] w-[8px] mr-1`}
										></div>
									);
								})}
								{last50Elements(resource.status).map((status, index) => {
									return (
										<div
											key={index}
											className={
												status.monitor_success
													? `bg-green-500 h-[40px] w-[8px] hover:bg-gray-500 mr-1`
													: `bg-red-500 h-[40px] w-[8px] hover:bg-gray-500 mr-1`
											}
										></div>
									);
								})}
							</div>
						</div>
					</div>
				);
			})}
		</div>
	);
};

export default Status;
