import type { Document } from "@/data/documents";

interface DocCardProps {
  doc: Document;
}

function PreviewLines({ color }: { color: string }) {
  return (
    <div className="flex flex-col gap-1.5">
      <div
        className="h-2 rounded-full"
        style={{ width: "88%", background: color, opacity: 0.45 }}
      />
      <div
        className="h-2 rounded-full"
        style={{ width: "65%", background: color, opacity: 0.3 }}
      />
      <div
        className="h-2 rounded-full"
        style={{ width: "78%", background: color, opacity: 0.35 }}
      />
      <div
        className="h-2 rounded-full"
        style={{ width: "50%", background: color, opacity: 0.25 }}
      />
    </div>
  );
}

export function DocCard({ doc }: DocCardProps) {
  return (
    <div
      className="w-56 bg-white rounded-xl shadow-md border border-neutral-100 overflow-hidden cursor-default"
      style={{ position: "absolute", left: doc.x, top: doc.y }}
    >
      {/* Color accent bar */}
      <div
        className="h-1.5 w-full"
        style={{ background: doc.previewColor }}
      />

      {/* Abstract preview */}
      <div
        className="px-4 pt-3 pb-3"
        style={{ background: doc.previewColor + "0f" }}
      >
        <PreviewLines color={doc.previewColor} />
      </div>

      {/* Content */}
      <div className="px-4 py-3">
        {/* Tag */}
        <span
          className="inline-block text-xs font-medium px-2 py-0.5 rounded-full mb-2"
          style={{
            background: doc.previewColor + "18",
            color: doc.previewColor,
          }}
        >
          {doc.tag}
        </span>

        {/* Title */}
        <h3 className="text-sm font-semibold text-neutral-900 leading-snug mb-1.5 line-clamp-2">
          {doc.title}
        </h3>

        {/* Summary */}
        <p className="text-xs text-neutral-500 leading-relaxed line-clamp-2">
          {doc.summary}
        </p>

        {/* Date */}
        <p className="mt-2.5 text-xs text-neutral-400">{doc.lastModified}</p>
      </div>
    </div>
  );
}
