import PagesMetaHead from "../../components/PagesMetaHead";
import ProjectSingle from "../../components/projects/ProjectSingle";

export const getServerSideProps = async () => {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API}/projects`);
  const projects = await res.json();

  return {
    props: {
      projects,
      revalidate: 10,
    },
  };
};

function Projects({ projects }) {
  return (
    <div className="container mx-auto">
      <section className="py-5 sm:py-10 mt-5 sm:mt-10">
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
    </div>
  );
}

export default Projects;
