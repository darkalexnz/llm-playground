"use client";

import { useState, useRef, useEffect, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { cn } from "@/lib/utils";

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
}

const MOCK_RESPONSES = [
  "That's an interesting thought! Let me think about that for a moment.",
  "I appreciate you sharing that. Here's what I think...",
  "Great question! The short answer is that it depends on the context.",
  "I'd be happy to help with that. Could you tell me more about what you're looking for?",
  "That's a really common question. Here's how I'd approach it.",
  "Interesting! I hadn't considered it from that angle before.",
  "Sure thing. Let me break that down for you step by step.",
  "I think there are a few ways to look at this problem.",
];

function getMockResponse(): string {
  return MOCK_RESPONSES[Math.floor(Math.random() * MOCK_RESPONSES.length)];
}

function useDraggable(initialX: number, initialY: number) {
  const [position, setPosition] = useState({ x: initialX, y: initialY });
  const dragState = useRef<{ startX: number; startY: number; origX: number; origY: number } | null>(null);

  const onMouseDown = useCallback((e: React.MouseEvent) => {
    // Only drag from the handle, not from buttons/inputs inside it
    if ((e.target as HTMLElement).closest("button")) return;
    e.preventDefault();
    dragState.current = {
      startX: e.clientX,
      startY: e.clientY,
      origX: position.x,
      origY: position.y,
    };

    const onMouseMove = (ev: MouseEvent) => {
      if (!dragState.current) return;
      const dx = ev.clientX - dragState.current.startX;
      const dy = ev.clientY - dragState.current.startY;
      setPosition({
        x: dragState.current.origX + dx,
        y: dragState.current.origY + dy,
      });
    };

    const onMouseUp = () => {
      dragState.current = null;
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("mouseup", onMouseUp);
    };

    window.addEventListener("mousemove", onMouseMove);
    window.addEventListener("mouseup", onMouseUp);
  }, [position.x, position.y]);

  return { position, onMouseDown };
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [isOpen, setIsOpen] = useState(true);
  const scrollRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Center the modal initially
  const { position, onMouseDown } = useDraggable(
    typeof window !== "undefined" ? Math.round(window.innerWidth / 2 - 200) : 400,
    typeof window !== "undefined" ? Math.round(window.innerHeight / 2 - 250) : 100
  );

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isTyping]);

  const sendMessage = async () => {
    const text = input.trim();
    if (!text) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsTyping(true);

    await new Promise((resolve) => setTimeout(resolve, 800 + Math.random() * 1200));

    const assistantMessage: Message = {
      id: crypto.randomUUID(),
      role: "assistant",
      content: getMockResponse(),
    };

    setIsTyping(false);
    setMessages((prev) => [...prev, assistantMessage]);
    inputRef.current?.focus();
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="h-screen bg-muted/30">
      {/* Floating open button when modal is closed */}
      {!isOpen && (
        <Button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-6 right-6 h-12 w-12 rounded-full shadow-lg"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        </Button>
      )}

      {/* Draggable chat modal */}
      {isOpen && (
        <div
          className="fixed flex flex-col w-[400px] h-[500px] rounded-xl border bg-background shadow-2xl overflow-hidden"
          style={{
            left: position.x,
            top: position.y,
            zIndex: 50,
          }}
        >
          {/* Drag handle / header */}
          <header
            className="flex items-center justify-between border-b px-4 py-2.5 cursor-grab active:cursor-grabbing select-none shrink-0"
            onMouseDown={onMouseDown}
          >
            <div className="flex items-center gap-2">
              <div className="flex gap-1">
                <span className="h-2.5 w-2.5 rounded-full bg-green-500" />
              </div>
              <h1 className="text-sm font-semibold">Chat</h1>
            </div>
            <Button
              variant="ghost"
              size="icon"
              className="h-7 w-7"
              onClick={() => setIsOpen(false)}
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/></svg>
            </Button>
          </header>

          {/* Messages */}
          <ScrollArea className="flex-1" ref={scrollRef}>
            <div className="px-4 py-4 space-y-4">
              {messages.length === 0 && (
                <div className="flex flex-col items-center justify-center pt-20 text-center text-muted-foreground">
                  <p className="text-sm font-medium">No messages yet</p>
                  <p className="text-xs mt-1">Send a message to start.</p>
                </div>
              )}

              {messages.map((message) => (
                <div
                  key={message.id}
                  className={cn(
                    "flex gap-2.5",
                    message.role === "user" && "flex-row-reverse"
                  )}
                >
                  <Avatar className="h-7 w-7 shrink-0">
                    <AvatarFallback
                      className={cn(
                        "text-[10px] font-medium",
                        message.role === "user"
                          ? "bg-primary text-primary-foreground"
                          : "bg-muted"
                      )}
                    >
                      {message.role === "user" ? "U" : "AI"}
                    </AvatarFallback>
                  </Avatar>
                  <div
                    className={cn(
                      "rounded-2xl px-3 py-2 max-w-[75%] text-sm leading-relaxed",
                      message.role === "user"
                        ? "bg-primary text-primary-foreground"
                        : "bg-muted"
                    )}
                  >
                    {message.content}
                  </div>
                </div>
              ))}

              {isTyping && (
                <div className="flex gap-2.5">
                  <Avatar className="h-7 w-7 shrink-0">
                    <AvatarFallback className="bg-muted text-[10px] font-medium">
                      AI
                    </AvatarFallback>
                  </Avatar>
                  <div className="rounded-2xl bg-muted px-3 py-2 text-sm text-muted-foreground">
                    <span className="inline-flex gap-1">
                      <span className="animate-bounce" style={{ animationDelay: "0ms" }}>.</span>
                      <span className="animate-bounce" style={{ animationDelay: "150ms" }}>.</span>
                      <span className="animate-bounce" style={{ animationDelay: "300ms" }}>.</span>
                    </span>
                  </div>
                </div>
              )}
            </div>
          </ScrollArea>

          {/* Input bar */}
          <div className="border-t p-3 shrink-0">
            <div className="flex gap-2">
              <Input
                ref={inputRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Type a message..."
                disabled={isTyping}
                className="flex-1 h-9 text-sm"
                autoFocus
              />
              <Button
                onClick={sendMessage}
                disabled={isTyping || !input.trim()}
                size="sm"
                className="h-9"
              >
                Send
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
