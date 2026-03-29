import Link from "next/link";
import { ZoomCanvas } from "@/components/canvas/ZoomCanvas";
import { DocCard } from "@/components/document-map/DocCard";
import { documents } from "@/data/documents";

export default function DocumentMapPage() {
  return (
    <div className="relative w-full h-screen">
      {/* Canvas */}
      <ZoomCanvas>
        {documents.map((doc) => (
          <DocCard key={doc.id} doc={doc} />
        ))}
      </ZoomCanvas>

      {/* Overlay nav */}
      <nav className="absolute top-4 left-4 z-10 flex items-center gap-2 pointer-events-none">
        <Link
          href="/"
          className="pointer-events-auto bg-white/80 backdrop-blur-sm hover:bg-white text-neutral-600 hover:text-neutral-900 text-sm px-3 py-1.5 rounded-lg border border-neutral-200 shadow-sm transition-colors"
        >
          ← Back
        </Link>
        <span className="bg-white/80 backdrop-blur-sm text-sm font-medium text-neutral-700 px-3 py-1.5 rounded-lg border border-neutral-200 shadow-sm">
          Document Map
        </span>
      </nav>
    </div>
  );
}
