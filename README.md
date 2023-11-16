# NextAPI CraftSpace

Welcome to the Portfolio Web Application project! This full-stack web application is designed to showcase your skills, projects, and bio in a visually appealing and interactive manner. Built using Next.js, React, Tailwind CSS for the frontend, and FastAPI for the backend, this project provides a seamless and efficient experience.

## Technologies Used

- **Frontend:**
  - Next.js: A React framework for building efficient and scalable web applications.
  - React: A JavaScript library for building user interfaces.
  - Tailwind CSS: A utility-first CSS framework for rapid UI development.

- **Backend:**
  - FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
  - MongoDB: A NoSQL database for storing and retrieving data efficiently.

## Features

- **Project Management:**
  - Add, list, update, and delete projects with ease.
  - View detailed information about each project.

- **Bio Editing:**
  - Edit your personal bio to keep it up-to-date.

- **Resume Download:**
  - Allow visitors to download your resume directly from the website.

- **Contact Form:**
  - Provide a beautifully styled web form for visitors to reach out to you.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/samtechy26/NextAPI-CraftSpace.git`
2. Navigate to the project directory: `cd NextAPI-CraftSpace`
3. Install dependencies:
   ```bash
   cd frontend
   npm install
   cd ../backend
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   - Create a MongoDB database and update the connection string in the `backend/.env` file.

5. Run the application:
   ```bash
   cd frontend
   npm run dev
   cd ../backend
   uvicorn app.main:app --reload
   ```

6. Access the application at `http://localhost:3000` in your browser.

## Customize Your Portfolio

1. Update the frontend components in the `frontend/app` directory to reflect your personal style and preferences.
2. Modify the backend API routes in the `backend/app` directory to handle portfolio data according to your needs.

## Contributions

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
