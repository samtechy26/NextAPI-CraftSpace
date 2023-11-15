import { useState, useEffect } from "react";
import { FiSearch } from "react-icons/fi";
import ProjectSingle from "./ProjectSingle";
import ProjectsFilter from "./ProjectsFilter";

function ProjectsGrid() {
  // const router = useRouter()

  const [category, setCategory] = useState("");
  const [projects, setProjects] = useState([]);
  const [options, setOptions] = useState([]);

  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API}/projects?category=${category}`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((json) => {
        setProjects(json), setOptions(json["category"]);
      });
  }, [category]);

  return (
    <section className="py-5 sm:py-10 mt-5 sm:mt-10">
      <div className="mt-10 sm:mt-16">
        <h3
          className="
                          font-general-regular 
                          text-center text-secondary-dark
                          dark:text-ternary-light
                          text-md
                          sm:text-xl
                          mb-3
                          "
        >
          Search projects by title or filter by category
        </h3>
        <div
          className="
                          flex
                          justify-between
                          border-b border-primary-light
                          dark:border-secondary-dark
                          pb-3
                          gap-3
                          "
        >
          <div className="flex justify-between gap-2">
            <span
              className="
                                  hidden
                                  sm:block
                                  bg-primary-light
                                  dark:bg-ternary-dark
                                  p-2.5
                                  shadow-sm
                                  rounded-xl
                                  cursor-pointer
                                  "
            ></span>
            <input
              className="
                                  ont-general-medium 
                                  pl-3
                                  pr-1
                                  sm:px-4
                                  py-2
                                  border 
                              border-gray-200
                                  dark:border-secondary-dark
                                  rounded-lg
                                  text-sm
                                  sm:text-md
                                  bg-secondary-light
                                  dark:bg-ternary-dark
                                  text-primary-dark
                                  dark:text-ternary-light
                                  "
              id="name"
              name="name"
              type="search"
              required=""
              placeholder="Search Projects"
              aria-label="Name"
            />
          </div>

          <ProjectsFilter setSelectOption={handleCategoryChange} />
        </div>
      </div>

      <div className="text-center">
        <p className="font-general-medium text-2xl sm:text-4xl mb-1 text-ternary-dark dark:text-ternary-light">
          Projects portfolio
        </p>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mt-6 sm:gap-5">
        {projects.map((project) => {
          const { _id, title, category, description, tags, link, image } =
            project;
          return (
            <ProjectSingle
              key={_id}
              id={_id}
              title={title}
              category={category}
              description={description}
              image={image}
            />
          );
        })}
      </div>
    </section>
  );
}

export default ProjectsGrid;
