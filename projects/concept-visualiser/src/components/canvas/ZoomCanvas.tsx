"use client";

import { useRef, useState, useEffect, useCallback, type ReactNode } from "react";

interface ZoomCanvasProps {
  children: ReactNode;
  width?: number;
  height?: number;
}

interface Transform {
  zoom: number;
  panX: number;
  panY: number;
}

export function ZoomCanvas({
  children,
  width = 3000,
  height = 2000,
}: ZoomCanvasProps) {
  const [transform, setTransform] = useState<Transform>({
    zoom: 1,
    panX: 0,
    panY: 0,
  });

  const isDragging = useRef(false);
  const lastPos = useRef({ x: 0, y: 0 });
  const containerRef = useRef<HTMLDivElement>(null);

  // Non-passive wheel handler so we can call preventDefault and prevent page scroll
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    const handler = (e: WheelEvent) => {
      e.preventDefault();
      const rect = el.getBoundingClientRect();
      const factor = e.deltaY > 0 ? 0.9 : 1.1;

      setTransform((prev) => {
        const newZoom = Math.min(2.5, Math.max(0.3, prev.zoom * factor));
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;
        // Keep the canvas point under the cursor fixed
        const canvasX = (mx - prev.panX) / prev.zoom;
        const canvasY = (my - prev.panY) / prev.zoom;
        return {
          zoom: newZoom,
          panX: mx - canvasX * newZoom,
          panY: my - canvasY * newZoom,
        };
      });
    };

    el.addEventListener("wheel", handler, { passive: false });
    return () => el.removeEventListener("wheel", handler);
  }, []);

  const handlePointerDown = useCallback(
    (e: React.PointerEvent<HTMLDivElement>) => {
      isDragging.current = true;
      lastPos.current = { x: e.clientX, y: e.clientY };
      e.currentTarget.setPointerCapture(e.pointerId);
    },
    []
  );

  const handlePointerMove = useCallback(
    (e: React.PointerEvent<HTMLDivElement>) => {
      if (!isDragging.current) return;
      const dx = e.clientX - lastPos.current.x;
      const dy = e.clientY - lastPos.current.y;
      lastPos.current = { x: e.clientX, y: e.clientY };
      setTransform((prev) => ({
        ...prev,
        panX: prev.panX + dx,
        panY: prev.panY + dy,
      }));
    },
    []
  );

  const handlePointerUp = useCallback(() => {
    isDragging.current = false;
  }, []);

  const { zoom, panX, panY } = transform;
  const dotSpacing = 28 * zoom;

  return (
    <div
      ref={containerRef}
      className="relative w-full h-screen overflow-hidden bg-neutral-100 cursor-grab active:cursor-grabbing select-none"
      onPointerDown={handlePointerDown}
      onPointerMove={handlePointerMove}
      onPointerUp={handlePointerUp}
    >
      {/* Dot grid background */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          backgroundImage: "radial-gradient(circle, #cbd5e1 1.5px, transparent 1.5px)",
          backgroundSize: `${dotSpacing}px ${dotSpacing}px`,
          backgroundPosition: `${panX % dotSpacing}px ${panY % dotSpacing}px`,
        }}
      />

      {/* Canvas stage */}
      <div
        style={{
          position: "absolute",
          width,
          height,
          transformOrigin: "0 0",
          transform: `translate(${panX}px, ${panY}px) scale(${zoom})`,
        }}
      >
        {children}
      </div>

      {/* Zoom level HUD */}
      <div className="absolute bottom-4 right-4 bg-white/80 backdrop-blur-sm border border-neutral-200 rounded-lg px-3 py-1.5 text-xs text-neutral-400 shadow-sm pointer-events-none select-none"
        style={{ fontFamily: "var(--font-geist-mono), monospace" }}
      >
        {Math.round(zoom * 100)}%
      </div>
    </div>
  );
}
