import { useState, useEffect } from "react";

const selectOptions = [
  "Web Application",
  "Mobile Application",
  "UI/UX Design",
  "Branding",
];

function ProjectsFilter({ setSelectOption }) {
  const [options, setOptions] = useState([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API}/projects`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((json) => {
        // Extract unique categories from the projects array
        const uniqueCategories = [
          ...new Set(json.map((project) => project.category)),
        ];

        setOptions(uniqueCategories);
      });
  }, []);
  return (
    <select
      onChange={setSelectOption}
      className="
                px-4
                sm:px-6
                py-2
                border
                dark:border-secondary-dark
                rounded-lg
                text-sm
                sm:text-md
                dark:font-medium
                bg-secondary-light
                dark:bg-ternary-dark
                text-primary-dark
                dark:text-ternary-light
            "
    >
      <option value="" className="text-sm sm:text-md">
        All Projects
      </option>

      {options.map((option) => (
        <option className="text-normal sm:text-md" key={option} value={option}>
          {option}
        </option>
      ))}
    </select>
  );
}

export default ProjectsFilter;
