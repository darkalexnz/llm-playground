import Link from "next/link";
import { Map } from "lucide-react";

const visualizations = [
  {
    href: "/document-map",
    Icon: Map,
    name: "Document Map",
    description:
      "A zoomable, pannable canvas of documents with titles, summaries, and content previews.",
  },
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-neutral-50">
      <div className="max-w-3xl mx-auto px-6 py-16">
        {/* Header */}
        <div className="mb-12">
          <h1 className="text-2xl font-bold text-neutral-900 mb-1.5 tracking-tight">
            Concept Visualiser
          </h1>
          <p className="text-neutral-500 text-sm">
            Interactive visual representations of data, documents, and systems.
          </p>
        </div>

        {/* Visualization gallery */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {visualizations.map(({ href, Icon, name, description }) => (
            <Link
              key={href}
              href={href}
              className="group block bg-white border border-neutral-200 rounded-xl p-5 hover:border-neutral-300 hover:shadow-md transition-all"
            >
              <div className="w-9 h-9 rounded-lg bg-neutral-100 group-hover:bg-neutral-200 flex items-center justify-center mb-4 transition-colors">
                <Icon className="w-4.5 h-4.5 text-neutral-600" strokeWidth={1.75} />
              </div>
              <h2 className="text-sm font-semibold text-neutral-900 mb-1">{name}</h2>
              <p className="text-xs text-neutral-500 leading-relaxed">{description}</p>
            </Link>
          ))}
        </div>
      </div>
    </main>
  );
}
