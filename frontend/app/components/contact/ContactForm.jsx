import { useState } from 'react';
import Button from '../reusable/Button';
import FormInput from '../reusable/FormInput';

function ContactForm() {
	const [name, setName] = useState('')
	const [email, setEmail] = useState('')
	const [subject, setSubject] = useState('')
	const [message, setMessage] = useState('')
	const [response, setResponse] = useState('')
	const [loading, setLoading] = useState(false)

	const handleForm = async (e) => {
		e.preventDefault();
		setLoading(true);
		const res = await fetch(`${process.env.NEXT_PUBLIC_API}/users/email`, {
		  method: "POST",
		  headers: { "Content-Type": "application/json" },
		  body: JSON.stringify({ full_name:name, email: email, subject: subject, message: message, subject: subject }),
		});
	
		if (res.ok) {
		  setLoading(false);
		  setResponse("Message Sent");
		}
	  };


	return (
		<div className="w-full lg:w-1/2">
			<div className="leading-loose">
				{!loading && response && (
				<div className="border border-green-600 w-2/3 p-10 text-center font-thin my-4 text-lg animate-pulse">
					{response}
				</div>
				)}
				<form
					onSubmit={handleForm}
					className="max-w-xl m-4 p-6 sm:p-10 bg-secondary-light dark:bg-secondary-dark rounded-xl shadow-xl text-left"
				>
					<p className="font-general-medium text-primary-dark dark:text-primary-light text-2xl mb-8">
						Contact Form
					</p>

					<FormInput
						inputLabel="Full Name"
						labelFor="name"
						inputType="text"
						inputId="name"
						inputName="name"
						placeholderText="Your Name"
						ariaLabelName="Name"
						setValue={setName}
					/>
					<FormInput
						inputLabel="Email"
						labelFor="email"
						inputType="email"
						inputId="email"
						inputName="email"
						placeholderText="Your email"
						ariaLabelName="Email"
						setValue={setEmail}
					/>
					<FormInput
						inputLabel="Subject"
						labelFor="subject"
						inputType="text"
						inputId="subject"
						inputName="subject"
						placeholderText="Subject"
						ariaLabelName="Subject"
						setValue={setSubject}
					/>

					<div className="mt-6">
						<label
							className="block text-lg text-primary-dark dark:text-primary-light mb-2"
							htmlFor="message"
						>
							Message
						</label>
						<textarea
							className="w-full px-5 py-2 border border-gray-300 dark:border-primary-dark border-opacity-50 text-primary-dark dark:text-secondary-light bg-ternary-light dark:bg-ternary-dark rounded-md shadow-sm text-md"
							id="message"
							name="message"
							cols="14"
							rows="6"
							aria-label="Message"
							onChange={(e) => setMessage(e.target.value)}
						></textarea>
					</div>

					<div className="mt-6">
						<span className="font-general-medium  px-7 py-4 text-white text-center font-medium tracking-wider bg-indigo-500 hover:bg-indigo-600 focus:ring-1 focus:ring-indigo-900 rounded-lg mt-6 duration-500">
							<Button
								title="Send Message"
								type="submit"
								aria-label="Send Message"
							/>
						</span>
					</div>
				</form>
			</div>
		</div>
	);
}

export default ContactForm;
