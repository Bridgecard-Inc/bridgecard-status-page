import React from "react";
import { getDowntimes } from "@/utils/fetchData";

const Downtimes = async () => {
	const data = await getDowntimes();

	function last5Elements(array) {
		// Check if the array has fewer than 50 elements
		if (array.length <= 5) {
			return array;
		}

		// Use slice to get the last 50 elements
		return array.slice(-5);
	}

	return (
		<div className="w-full grid grid-cols-1 gap-10 mb-20">
			{last5Elements(data.data.downtimes).map((downtime, index) => {
				return (
					<div className="w-full" key={index}>
						<div className="h-16 flex flex-row items-center justify-between bg-black px-5">
							<h1 className="text-white text-base font-bold capitalize">
								{downtime.title}
							</h1>
						</div>

						<div className="p-5 h-auto border ">{downtime.description}</div>
					</div>
				);
			})}
		</div>
	);
};
export default Downtimes;
