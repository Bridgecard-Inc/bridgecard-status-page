import React from "react";
import { getResources } from "@/utils/fetchData";
import { formatEpoch } from "@/utils/formatDate";

// grey bars for when there's no data available

const Status = async () => {
	const data = await getResources();

	const createEmptyBars = arr => {
		let barArr = [];
		if (arr.length < 80) {
			barArr = [...Array(80 - arr.length).keys()];
		}

		return barArr;
	};

	function last50Elements(array) {
		// Check if the array has fewer than 50 elements
		if (array.length <= 80) {
			return array;
		}

		// Use slice to get the last 50 elements
		return array.slice(-71);
	}

	return (
		<div className="w-ful border  border-gray-300">
			{/* <h3 className="text-base font-semibold mb-5">Mono Connect</h3> */}

			{data.data.resources.map((resource, index) => {
				return (
					<div
						className=" px-6 py-7 pb-0 border-b  last-of-type:border-b-0"
						key={index}
					>
						<div>
							<div className="w-full flex flex-row justify-between items-center mb-1 ">
								<h3 className="text-base font-semibold capitalize">
									{resource.title}
								</h3>
								<p className="text-base font-base text-green-500">
									Operational
								</p>
							</div>
							<div className="flex flex-row justify-between pb-6  ">
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
										<div key={index} className="group relative flex flex-col">
											<div
												className={
													status.monitor_success
														? `bg-green-500 h-[40px] w-[6px] hover:bg-gray-500 mr-1`
														: `bg-red-500 h-[40px] w-[6px] hover:bg-gray-500 mr-1`
												}
											></div>
											<div className=" bg-white border-2 rounded shadow-lg p-3 scale-0 group-hover:scale-100 absolute left-[-40px] bottom-[-82px] w-[300px] z-10">
												{" "}
												<p className="text-sm font-light">
													{formatEpoch(status.monitored_at)}
												</p>
												<p className="text-sm font-light mt-2">
													{status.monitor_success
														? "No downtime recorded"
														: "Downtime was recorded"}
												</p>
											</div>
										</div>
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
