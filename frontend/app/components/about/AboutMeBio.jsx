import Image from 'next/image';
import { useState, useEffect } from 'react';

function AboutMeBio() {

	const [aboutMe, setAboutMe] = useState({});

	useEffect(() => {
		fetch(`${process.env.NEXT_PUBLIC_API}/users/me?username=sammy`, {
		  method: "GET",
		})
		  .then((response) => response.json())
		  .then((json) => {
			setAboutMe(json);
		  });
	  }, []);

	return (
		<div className="block sm:flex sm:gap-10 mt-10 sm:mt-20">
			<div className="w-full sm:w-1/4 mb-7 sm:mb-0">
				<Image
					src="/images/profile.jpeg"
					width={200}
					height={200}
					className="rounded-lg"
					alt="Profile Image"
				/>
			</div>

			<div className="font-general-regular w-full sm:w-3/4 text-left">
				<p className="mb-4 text-ternary-dark dark:text-ternary-light text-lg" >
						{aboutMe.bio}
				</p>
				
			</div>
		</div>
	);
}

export default AboutMeBio;
